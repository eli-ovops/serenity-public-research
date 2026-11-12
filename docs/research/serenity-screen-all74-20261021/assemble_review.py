"""Root acceptance/consolidation. Reads frozen child outputs; no network or trading."""
import json,csv,math,datetime,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text())
def dump(name,data):(P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
scope=read(P/'SCOPE.json'); latest=read(P/'USER_EXECUTION_UPDATE.json'); positions=latest['positions_after']
quotes=read(P/'shared/QUOTE_SNAPSHOT.json')['quotes']; over=read(P/'shared/OVERSEAS_QUOTES.json')
cards={};checks=[];arithmetic=[]
for group,expected in scope['groups'].items():
    rows=read(P/group/'CARDS.json')
    checks.append({'check':group+'_ownership_complete','pass':len(rows)==len(expected) and {c['symbol'] for c in rows}==set(expected)})
    for c in rows:
        t=c['symbol']; assert t not in cards
        v=c['valuation'];m=v.get('model',v);values=m['values']; pm=c['price_map']
        q=quotes.get(t) or over[t];currency=over[t]['currency'] if t in over else 'USD'
        if currency=='GBp':currency='GBX'
        cap=pm.get('reasonable_participation_upper',pm.get('reasonable_participation_ceiling'))
        if cap is None:cap=pm['reasonable_participation_zone'][-1]
        gap=c.get('gaps',[]); status=c['status']; event=c.get('event_gate',{})
        condition_ok=True
        if status=='条件观察':condition_ok=len(gap)==1 and bool(c.get('conditional_deadline') or (isinstance(gap[0],dict) and gap[0].get('deadline')))
        checks.append({'check':t+'_core_card','pass':len(values)==3 and len(c.get('primary_sources',[]))>0 and bool(c.get('financial_facts')) and bool(c.get('invalidation')) and bool(event) and condition_ok})
        if '通过' in status:checks.append({'check':t+'_pass_has_no_research_gaps','pass':len(gap)==0 and q['price']<=cap*1.0001 and 'FAIL' not in event.get('status','') and 'partial' not in event.get('status','')})
        calc=None
        # Independent arithmetic from documented input families, not invoking owner code.
        if 'eps' in m and 'pe' in m and 'earnout_shares_m' not in m:
            calc=[m['eps'][i]*m['pe'][i]*m.get('fx',1)/(1+m['rate'])**m['years'] for i in range(3)]
        elif 'revenue_m' in m and 'net_margin' in m and 'pe' in m:
            calc=[(m['revenue_m'][i]*m['net_margin'][i]*m['pe'][i]+m['net_cash_m'][i])/m['shares_m'][i]/(1+m['rate'])**m['years']*m.get('quote_multiplier',1) for i in range(3)]
        elif all(k in m for k in ['revenue','net_margin','pe','net_cash','shares','years']):
            calc=[(m['revenue'][i]*m['net_margin'][i]*m['pe'][i]+m['net_cash'][i])/m['shares'][i]/(1+m.get('rate',.15))**m['years'] for i in range(3)]
        elif t=='INOD':
            calc=[m['revenue'][i]*m['net_margin'][i]/m['shares'][i]*m['pe'][i] for i in range(3)]
        elif 'ebitda_m' in m:
            calc=[(m['ebitda_m'][i]*m['multiple'][i]+m['net_cash_m'][i])/m['shares_m'][i]/(1+m['rate'])**m['years'] for i in range(3)]
        if calc is not None:
            # FLNC disclosed model caps negative operating equity at zero (limited liability),
            # not a traded-price floor or evidence that insolvency is impossible.
            if t=='FLNC': calc=[max(0,x) for x in calc]
            delta=max(abs(a-b) for a,b in zip(calc,values));arithmetic.append({'symbol':t,'recomputed':calc,'submitted':values,'max_abs_difference':delta,'pass':delta<.02})
        plan=c.get('research_limit_plan')
        if not plan and group=='power_other' and pm.get('fixed_protection_price') is not None:
            plan={'time_in_force':'DAY','limit':q['price'],'valid_until':'2026-10-21T20:00:00Z','price_guard':pm['fixed_protection_price'],
                  'guard_trigger_session':pm['protection_trigger'],'guard_basis':pm['protection_basis'],
                  'per_share_planned_price_risk':max(0,q['price']-pm['fixed_protection_price']),
                  'fundamental_invalidation':c['invalidation'],'valuation_ceiling':cap}
        if t in ['ONTO','FN']:
            limit=225 if t=='ONTO' else 358; guard=c['invalidation']['fixed_risk']
            plan={'time_in_force':'DAY','limit':limit,'valid_until':'2026-10-21T20:00:00Z','price_guard':guard['price'],
                'guard_trigger_session':guard['definition'],'guard_basis':guard['basis'],'per_share_planned_price_risk':limit-guard['price'],
                'fundamental_invalidation':c['invalidation']['economic'],'valuation_ceiling':cap}
        if plan:
            if t in ['AAON','HPE','ONTO']:
                review={'AAON':[83.80,84],'HPE':[59.88,62],'ONTO':[232.48,244.10]}[t]
                plan={**plan,'root_priority':{'AAON':1,'HPE':2,'ONTO':3}[t],
                    'profit_review_price':review[0],
                    'profit_exit_without_stronger_per_share_evidence':review[1],
                    'new_material_fact':'research plan expires, user must withdraw/not execute unfilled actual orders; assistant cannot cancel orders',
                    'personal_quantity':'not set; hypothetical one-share calculations only; select one alternative'}
            risk=plan['limit']-plan['price_guard']; cmin=max(10*plan['limit'],200*risk)
            plan={**plan,'root_recomputed_price_risk':risk,'root_minimum_NAV_one_share_before_fees':cmin,
                  'capital_current':'UNKNOWN','quantity_personal':'not set','current_holdings_not_overwritten':True}
            checks.append({'check':t+'_plan_positive_and_within_value_cap','pass':risk>0 and plan['limit']<=cap})
        cards[t]={'symbol':t,'group':group,'identity':c['identity'],'currency':currency,'quote':q,'valuation':v,'values':values,
           'participation_cap':cap,'price_map':pm,'event_gate':event,'event_asof':c.get('event_asof') or c.get('asof'),
           'invalidation':c['invalidation'],'status':status,'research_gaps':gap,'reason':c['reason'],
           'conditional_owner':c.get('conditional_owner'),'conditional_deadline':c.get('conditional_deadline'),'conditional_path':c.get('conditional_path'),
           'source_card':str((P/group/'CARDS.json').resolve()),'source_report':str((P/group/'REPORT.md').resolve()),
           'primary_sources':c['primary_sources'],'user_confirmed_qty':positions.get(t,0),'research_limit_plan':plan,
           'account_gate':'current NAV/cash/fees unverified; no account access'}
ordered=[cards[t] for t in scope['universe']]
counts={s:sum(c['status']==s for c in ordered) for s in ['研究门通过，账户门待确认','条件观察','排除','研究未完成']}
checks.extend([{'check':'all74_unique','pass':len(ordered)==74 and len(set(c['symbol'] for c in ordered))==74},
 {'check':'latest9_and_four_sells_reconciled','pass':len(positions)==9 and all(positions.get(t,0)==0 for t in ['CAMT','TEM','AIP','TSLA','NVT']) and positions['DPC']==1},
 {'check':'all_recomputed_arithmetic','pass':all(x['pass'] for x in arithmetic)}])
dump('ALL74_CARDS.json',{'screen_date':'2026-10-21','owner':'root','status_counts':counts,'current_positions':positions,'cards':ordered})
with (P/'ALL74.csv').open('w',newline='') as f:
    fields=['symbol','currency','reference_price','price_asof','stress','base','strong','participation_cap','status','known_qty','event_status','gap','reason','source_report']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for c in ordered:
        w.writerow(dict(zip(fields,[c['symbol'],c['currency'],c['quote']['price'],c['quote'].get('asof') or c['quote'].get('last_market_time_local'),*c['values'],c['participation_cap'],c['status'],c['user_confirmed_qty'],c['event_gate'].get('status'),json.dumps(c['research_gaps'],ensure_ascii=False),c['reason'],c['source_report']])))
dump('ROOT_ARITHMETIC_AUDIT.json',{'independent_formula_checks':arithmetic,'bespoke_models':'owner source inputs/receipts plus clinical independent review and CLINICAL_VALIDATION; not asserting all models are standard EPS'})
dump('ROOT_ACCEPTANCE.json',{'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if all(x['pass'] for x in checks) else 'NEEDS_FIX',
    'counts':counts,'checks':checks,'source_limits':['ASX official event calendar refused; current exclusion independently valuation based','AEHR latest annual-vote8K body not first-party read; investment not excluded by tool fault',
    'CCXI final capital table not fully read; independent denominator sensitivity and economic bound retained','ETN/FLNC/SERV selected new filing body limits do not erase independent financial counterevidence',
    'clinical PoS and future capital availability not calibrated; scenario figures not exact fairvalues','overseas market/odd-lot availability separate from research; quotes/FX/local closes not simultaneous'],
    'what_complete_means':'all74 have a finite research disposition with valuation/evidence/event status/invalidations; not all possible documents read or all74 buy gates passed',
    'holdings_decision':'retain latest confirmed9, no extra clinical half reduction from uncalibrated model; existing protections and review dates persist'})
table=['# 74家逐股筛选总表 · 2026-10-21','', '数值为作者三情景现值，不是公司目标价或已知概率；币种逐行列出。报价主要10:58–11:00ET，欧洲/港台当地时段见列。研究状态与账户/现仓动作分开。', '',
    '|公司|币种|本轮参考价|压力／基准／强|合理参与上限|研究处置|依据／唯一缺口|','|---|---|---:|---:|---:|---|---|']
for c in ordered:
    reason=c['reason'].replace('|','／').replace('\n',' ')
    if c['status']=='条件观察':reason=str(c['research_gaps']).replace('|','／').replace('\n',' ')
    status='通过；账户待核' if '通过' in c['status'] else c['status']
    table.append(f"|[{c['symbol']}]({c['source_report']})|{c['currency']}|{c['quote']['price']:.3f}|{' / '.join(f'{x:.2f}' for x in c['values'])}|{c['participation_cap']:.2f}|{status}|{reason}|")
table+=['','计数：'+json.dumps(counts,ensure_ascii=False),'','非零持仓仍为用户确认9只；CAMT/TEM/AIP清仓、DPC剩1均已记录。研究通过不等于建议买回刚卖股票，也不等于所有通过者一起买。', '',
    '完整模型、事件、反证、来源和阅读限制见[ALL74_CARDS.json](ALL74_CARDS.json)与三个分组原报告。ASX等独立估值排除的次要事件原文缺口明列于[ROOT_ACCEPTANCE.json](ROOT_ACCEPTANCE.json)，不声称所有财报全文/新闻均已读完。']
(P/'ALL74.md').write_text('\n'.join(table)+'\n')
print(json.dumps({'counts':counts,'arithmetic_checked':len(arithmetic),'failures':[x for x in checks if not x['pass']]},ensure_ascii=False))
