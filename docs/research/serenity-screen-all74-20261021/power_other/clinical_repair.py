import json, copy, re, hashlib
from pathlib import Path
P=Path(__file__).parent
cards=json.load(open(P/'CARDS.json')); models=json.load(open(P/'MODELS.json'))
untouched={c['symbol']:json.dumps(c,sort_keys=True) for c in cards if c['symbol'] not in ['RXRX','SCTX']}
RAMP=[.1,.25,.5,.75,1,1,1,1,1,.8,.5,.2]
def pv_program(p,prob=None):
    return sum(p['peak']*p['margin']*(p['prob'] if prob is None else prob)*r/1.15**(p['launch']-2026+i) for i,r in enumerate(RAMP))
def funded_path(cash,shares,x,cut_after2=1,issue_factor=1):
    # Monthly liquidity buckets. Raise before a month's expense when the reserve would be breached.
    # Fractional t=months/12 from valuation; no claim these hypothetical financings are available.
    rows=[];newcapital=0;newpv=0;costpv=0;issued=0;balance=cash
    for month in range(1,x['funding_years']*12+1):
        opening=balance;spend=x['annual_burn']/12*(cut_after2 if month>24 else 1)
        need=max(0,x['reserve']+spend-balance)
        balance+=need;newcapital+=need;issued+=need/(x['financing_price']*issue_factor)
        newpv+=need/1.15**((month-1)/12)
        costpv+=spend/1.15**(month/12);balance-=spend
        rows.append({'month':month,'fund_at_t_years':(month-1)/12,'opening_cash_m':opening,'new_financing_m':need,'cash_spend_m':spend,'ending_cash_m':balance})
    diluted=shares+x['SBC_shares']+issued
    residual=cash+newpv-costpv
    riskpv=sum(pv_program(p) for p in x['programs']); allpv=sum(pv_program(p,1) for p in x['programs'])
    return {'cash_path':rows,'financing_required_m':newcapital,'newcapital_pv_m':newpv,'cost_pv_m':costpv,'future_diluted_shares_m':diluted,'pipeline_pv_m':riskpv,'all_success_pipeline_pv_m':allpv,'cash_residual_pv_m':residual,'equity_pv_m':max(0,residual+riskpv),'value':max(0,residual+riskpv)/diluted,'all_success_value':max(0,residual+allpv)/diluted,'first_financing_month':next((r['month'] for r in rows if r['new_financing_m']>1e-8),None),'minimum_cash_m':min(r['ending_cash_m'] for r in rows),'ending_cash_m':balance}
out={};report=[]
for c in cards:
    s=c['symbol']
    if s not in ['RXRX','SCTX']:continue
    m=c['valuation'];price=c['price_map']['quote']['price']
    if 'pre_repair_model' not in m:m['pre_repair_model']=copy.deepcopy(m)
    old=m['pre_repair_model']; new=[]
    for x in old['scenarios']:
        y=copy.deepcopy(x);calc=funded_path(old['current_cash_m'],old['current_shares_m'],x);y.update(calc)
        y.pop('financing_year',None)
        y['required_common_PoS_at_current_price']=(price*y['future_diluted_shares_m']-y['cash_residual_pv_m'])/y['all_success_pipeline_pv_m']
        y['required_peak_sales_scale_at_original_PoS']=(price*y['future_diluted_shares_m']-y['cash_residual_pv_m'])/y['pipeline_pv_m'] if y['pipeline_pv_m'] else None
        y['common_PoS_peak_sales_grid']=[{'all_programs_PoS':p,'peak_sales_multiplier':k,'per_share':max(0,y['cash_residual_pv_m']+y['all_success_pipeline_pv_m']*p*k)/y['future_diluted_shares_m']} for p in [.05,.1,.2,.3,.5,1] for k in [.5,1,2]]
        # Cost truncation alone is not a fair scenario: also extinguish all affected pipeline value.
        cut=funded_path(old['current_cash_m'],old['current_shares_m'],x,.5)
        y['early_termination_cost_sensitivity']={'interpretation':'50% lower burn after year2 with ALL modeled programs failing; reduced funding and shares, ZERO pipeline PV. Illustrates retained cash, not a favorable operating forecast. Full-budget model overstates costs for paths stopped after failure. No branch probabilities assigned.','funding_m':cut['financing_required_m'],'diluted_shares_m':cut['future_diluted_shares_m'],'cash_only_value':max(0,cut['cash_residual_pv_m'])/cut['future_diluted_shares_m']}
        cheap=funded_path(old['current_cash_m'],old['current_shares_m'],x,1,.5)
        y['half_issue_price_sensitivity']={'price':x['financing_price']*.5,'shares_m':cheap['future_diluted_shares_m'],'risk_adjusted_value':cheap['value'],'all_success_value':cheap['all_success_value']}
        new.append(y)
    m['scenarios']=new;m['values']=[x['value']for x in new]
    m['all_success_values']=[x['all_success_value']for x in new]
    m['method']='Author rNPV: finite12year postlaunch FCF ramp, no terminal. Monthly cash spend with pre-month financing whenever projected cash falls below reserve; newcapital discounted at monthstart, spend at monthend. EquityPV=max(0,currentcash+PVnewcapital-PVspend+rNPV); divide future dilutedshares including financedshares andSBC. All probabilities, peak sales, financingprices and timing are assumptions, not observed/company probabilities.'
    m['funding_caveat']='Conditional fully funded paths only. External financing price can exceed author rNPV and is NOT asserted achievable. Without financing the forecast cannot continue when cash depletes; options include early termination, licensing, sale or insolvency. No arbitrary continuation with negative cash. Initial cash includes estimated post-offering balances and restricted/intervening-burn uncertainty, so cash runway is scenario not bank proof.'
    m['cost_bias']='Precommercial full-program budgets are paid on every probability-weighted revenue path; this is a conservative expected-cost approximation, not a calibrated decision tree. Failure can stop trials earlier and reduce subsequent burn/dilution. The paired early-termination sensitivity drops pipeline PV to zero while halving spending after2years; no benefit from saved cost while silently keeping failed drug sales.'
    m['right_tail_note']='risk-adjusted strong is NOT a success ceiling. All-program PoS=1 at same strong commercial assumptions is an explicit conditional right-tail illustration, not a probability forecast nor an upper bound on success. Commercial peaks can also exceed/fall short of scenarios.'
    m['inverse_note']='Necessary common PoS holds every program at same probability with its scenario commercial peaks; values>1 mean impossible under that combination. Alternatively required peak multiplier holds original program probabilities fixed. These invert the price equation, do not estimate true probabilities; joint dependence between programs not calibrated.'
    c['valuation']=m;models[s]=m
    p=c['price_map'];p['stress'],p['base'],p['strong']=m['values'];p['risk_adjusted_strong_label']='Author probability-weighted strong, not clinical success ceiling';p['conditional_all_success_strong']=m['all_success_values'][2]
    p['reasonable_participation_upper']=round(p['base']*1.05,2);p['expensive_above']=p['reasonable_participation_upper'];p['high_safety_margin']=round(p['base']*.7,2);p['at_current_price']=price/p['base']-1;p['one_share_stress_loss_usd']=max(0,price-p['stress'])
    c['reason']='New-buy excluded under this author conservative risk-adjusted valuation, not an empirical fair-value estimate or hard clinical failure. Required success/peak-sales combinations and explicit all-success right tail are now shown. Probability and financing uncertainty do not justify mechanical immediate sale of the existing clinical-option position.'
    c.setdefault('holding_decision_history',[])
    if not any(z.get('status')=='REJECTED_BY_ROOT'for z in c['holding_decision_history']):c['holding_decision_history'].append({'status':'REJECTED_BY_ROOT','proposal':copy.deepcopy(c['holding_decision']),'reason':'Independent review found financing timing and incomplete right-tail presentation; root did not adopt immediate half-reduction solely from subjective rNPV. No trade took place based on this proposal.'})
    n=20 if s=='RXRX'else 2
    c['holding_decision']={'status':'ROOT_DECISION_RECORDED_FOR_FINAL_ACCEPTANCE','confirmed_shares':n,'research_target_remaining':n,'action':'Hold existing position, no add; root retained current9-position facts. Prior half-reduction proposal not adopted and not execution.','reason':'No newly verified clinical/regulatory/financing deterioration during this model-only review and original protection not triggered at the source snapshot. Existing funding supports the next milestone; RXRX has real preliminary efficacy and a registration-development path, SCTX remains early human study with IPO runway. Clinical and commercial upside can exceed risk-adjusted strong. This supports retaining finite existing option exposure while declining new exposure; not proof marketprice is cheap. Prior RXRX reduction already recognized.','limitations':'Current NAV, fees and exact new cash unknown; no budget compliance claim, no continuous monitoring. Clinical data remain early; total loss and future dilution possible.'}
    if s=='RXRX':c['holding_decision'].update(deadline='2026-10-30 before11/2 clinical-data event; at next requested review decide event exposure using updated evidence, not indefinite temporaryhold.',exit='Material efficacy/safety failure or viable registration path denied ->20to0. Cash/financing worsens enough to threaten milestone -> reunderwrite and reduce quantified exposure. Old3.6/4automatic batches remain retired.')
    else:c['holding_decision'].update(deadline='Next material safety/financing update and before2027H1firsthuman data; requested-review only.',protection='Original mutually exclusive FIRST reduction remains: rebound25-26 without new human evidence ->2to1; OR regularclose<16.7 AND XBI<145 ->2to1. Neither inferred triggered by this model revision. Serious safety/registration/funding failure triggers earlier reassessment including exit; no new lower threshold.')
    out[s]={'price':price,'risk_adjusted_values':m['values'],'all_success_values':m['all_success_values'],'first_financing_month':[x['first_financing_month']for x in new],'minimum_cash':[x['minimum_cash_m']for x in new],'necessary_common_probability':[x['required_common_PoS_at_current_price']for x in new],'necessary_peak_multiplier_original_PoS':[x['required_peak_sales_scale_at_original_PoS']for x in new]}
    report+=['## '+s,'',json.dumps(out[s],ensure_ascii=False,indent=2),'',m['funding_caveat'],'',m['cost_bias'],'',m['inverse_note'],'',m['right_tail_note'],'',json.dumps(c['holding_decision'],ensure_ascii=False,indent=2),'']
for c in cards:
    if c['symbol']in untouched:assert json.dumps(c,sort_keys=True)==untouched[c['symbol']]
(P/'CARDS.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2));(P/'MODELS.json').write_text(json.dumps(models,ensure_ascii=False,indent=2))
(P/'CLINICAL_REVISION.md').write_text('# Clinical model correction / root decision\n\nOnly RXRX and SCTX revised. Prior immediate half-reduction is rejected history, not an order or trade. Run clinical_repair.py after audit_fix.py for full reproduction.\n\n'+'\n'.join(report))
r=(P/'REPORT.md').read_text()
for c in cards:
    s=c['symbol']
    if s not in out:continue
    p=c['price_map'];newrow=f"|{s}|{p['quote']['price']:.3f}|{' / '.join(f'{v:.2f}'for v in c['valuation']['values'])}|{p['reasonable_participation_upper']:.2f}|-|{c['status']}|"
    r=re.sub(r'^\|'+s+r'\|.*$',lambda _:newrow,r,flags=re.M)
    pat=r'(## '+s+r' — .*?)(?=\n## |\Z)'
    def secfix(match):
        b=match.group(1)
        b=re.sub(r'\*\*估值。\*\*.*?(?=\n\n)',lambda _: '**估值（已修订）。** 月度融资现金不为负的压力/基准/概率加权强景为 '+ '/'.join(f'{v:.2f}'for v in c['valuation']['values'])+'；同强商业假设、全部PoS=1的条件成功情景为'+f"{c['valuation']['all_success_values'][2]:.2f}"+'，不是成功上限。融资与反推成功率见CLINICAL_REVISION.md；参数未经实证校准。',b,flags=re.S)
        b=re.sub(r'\*\*决定。\*\*.*?(?=\n\n)',lambda _:'**决定。** 作者审慎估值框架排除新买；总控决定现仓保留'+str(c['holding_decision']['confirmed_shares'])+'股，不因本次模型更正立即减半。原提议已不采纳，见holding_decision_history。',b,flags=re.S)
        return b
    r=re.sub(pat,secfix,r,flags=re.S)
    hp=r'### '+s+r' 最新确认现仓判断\n.*?(?=\n### |\n\n复算顺序|\Z)'
    r=re.sub(hp,lambda _: '### '+s+' 最新确认现仓判断\n\n'+json.dumps(c['holding_decision'],ensure_ascii=False,indent=2)+'\n',r,flags=re.S)
r+='\n\n## 临床模型独审修订（优先于此前草稿）\n\n只更新RXRX/SCTX。原RXRX20→10、SCTX2→1为未采纳提议，已移入两卡holding_decision_history，未有成交。总控维持RXRX20/SCTX2；融资支持下一里程碑、真实初步疗效/研发路径和可超过概率加权强景的右尾支持保留现有期权敞口，旧保护未因模型修订触发或取消。当前概率/净价未校准，不能把模型差额直接认定确定损失。\n\n统一2028融资已改为现金储备不足前的月初分段融资，假设资金能获得时所有月末现金非负；无法融资则必须停止/缩减研发或寻找合作，不能负现金继续经营。融资价为外生假设，即使高于rNPV亦不意味着确定融到。全预算消耗计入失败路径会高估费用，已增加失败后缩减成本且归零管线价值的配对敏感性。成功率=1条件价值、市场价反推必要成功率/峰销组合、半价融资稀释详见 [CLINICAL_REVISION.md](CLINICAL_REVISION.md) 与两卡模型。复现最后追加 `python3 clinical_repair.py`。\n'
(P/'REPORT.md').write_text(r)
checks=[]
for c in cards:
    if c['symbol']not in out:continue
    for i,x in enumerate(c['valuation']['scenarios']):
        assert x['minimum_cash_m']>=-1e-8
        assert all(z['opening_cash_m']+z['new_financing_m']-z['cash_spend_m']>=-1e-8 for z in x['cash_path'])
        assert abs(x['value']-x['equity_pv_m']/x['future_diluted_shares_m'])<1e-10
        p=x['required_common_PoS_at_current_price'];implied=(x['cash_residual_pv_m']+p*x['all_success_pipeline_pv_m'])/x['future_diluted_shares_m']
        assert abs(implied-c['price_map']['quote']['price'])<1e-8
        checks.append({'symbol':c['symbol'],'scenario':i,'nonnegative_cash':True,'value_recomputed':True,'price_inverse_recomputed':True})
(P/'CLINICAL_VALIDATION.json').write_text(json.dumps({'other21_unchanged':True,'checks':checks,'outputs':out,'scope':'Arithmetic and liquidity consistency, not proof probabilities or financing availability.'},indent=2))
manifest=[{'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}for f in P.rglob('*')if f.is_file()and f.name!='MANIFEST.json'];(P/'MANIFEST.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(out,indent=2))
