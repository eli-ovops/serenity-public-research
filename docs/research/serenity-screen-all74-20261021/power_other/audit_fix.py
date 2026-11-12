import json, math, hashlib
from pathlib import Path
P=Path(__file__).parent
cards=json.load(open(P/'CARDS.json'))
models=json.load(open(P/'MODELS.json'))
for c in cards:
    s=c['symbol']
    c['event_asof']='2026-10-21T15:07:19Z'
    c['event_gate']['next24h_end']='2026-10-22T15:07:19Z'
    c['event_gate']['asof_meaning']='Actual clock receipt after finite source review; sources collected at individual earlier timestamps, not continuously monitored.'
    c['financial_facts']['tag_warning'] += ' IMPORTANT: source_tag_receipts filed=2026-10-06 is inherited extraction/acquisition label, NOT verified SEC filing date. Actual filing dates must use SEC submissions accession. Raw receipts kept unchanged for provenance.'
    if s=='TEM':
        c['valuation'].update(revenue_m=[2050,2700,3250],EVsales=[3,5,8],factorization_provenance='docs/research/serenity-alternatives-20261020-2230/TEM_MODEL.json; factorization verified by original input, not inferred. Position boundary in old file is obsolete.')
        c['price_map']['high_safety_margin']=round(c['price_map']['base']*.7,2)
    if s=='INOD':
        p=c['price_map'];p['fixed_protection_price']=52
        p['protection_basis']='Existing user position frozen regular-close52 protection takes precedence; no lowering to newly computed50.17. Existing profit recovery61-65 with QQQ<743 and no improved earnings triggers exit of the same1share; no automatic add.'
        p['one_share_planned_loss_usd']=round(p['quote']['price']-52,4)
        p['minimum_NAV_one_share_usd']=round(max(10*p['quote']['price'],200*(p['quote']['price']-52)),2)
    if s=='CCXI':
        m=c['valuation'];m['capital_bound_test']={'base_enterprise_plus_cash_m':4600,'discount_factor':1.18**m['years'],'old_max_redemption_shares_m':235.273423,'value_with_no_further_dilution':4600/235.273423/1.18**m['years'],'agility_merger_shares_alone_m':200.870923,'value_ignoring_all_SPAC_PIPE_options_and_warrants':4600/200.870923/1.18**m['years'],'note':'Favorable lower-denominator bound ignores all sponsor/public/PIPE equity, future financing and dilution while retaining100m cash. It still fails reasonable upper valuation at currentquote. Strong operating scenario can exceedquote; this is valuation discipline, not proof robotics fails.'}
        c['gaps']=[{'item':'Final Oct13 definitive proforma captable body not read (403).','decision_effect':'Nonblocking for present independent base-valuation exclusion only: even target-only200.871m denominator is below market under same base operating assumptions. Blocking before any future new-buy pass.','owner':'screen_power_other','path':'Issuer Agility/Churchill final prospectus independent hosted copy','deadline':'2026-11-02 before vote/new recommendation'}]
        c['reason']+=' Conservative capital bound: base value8.27 at235.273m,9.69 with ONLY200.871m Agility shares and zero SPAC/PIPE/options; current greater than both. Exact capital rights remain specifically unverified, not erased.'
    if s=='RXRX':
        c['holding_decision']={'confirmed_shares':20,'research_target_remaining':10,'action':'Reduce10 now in regular session; retain10 as explicitly limited clinical right-tail position, not add. Not a trade receipt.','why_now':'New finite rNPV now closes the previously missing cash/dilution bridge. At3.665 versus base~0.82,20shares carry~56.9USD modeled base-value shortfall;10 carries~28.45. June/September cash and offering improve survival but addshares and do not establish clinical-commercial value. This changes prior temporaryhold20 rationale.','why_not_zero':'REC4881 phase1b/2 efficacy durability and planned registration path, Sanofi option and financing support a real upside path. Clinical probabilities/peak prices are not empirically calibrated; approval/penetration upside can exceed the modeled strongcase. Retaining10 preserves some exposure while reducing estimated loss.','deadline':'2026-10-30 regular close / next user-request before11/2 data; no background promise. At that review require a specific event-exposure choice, not indefinite temporaryhold.','exit_remaining':'Severe safety/efficacy failure, FDA denies viable registration path, or available funding no longer covers milestone and new dilutive terms materially worsen per-share map: remaining10→0 without waiting rebound. No old$3.6/$4 automatic batch restored.','fees_NAV':'UNKNOWN; target within confirmed20, does not assert portfolio risk-budget compliance or realized P&L.'}
    if s=='SCTX':
        c['holding_decision']={'confirmed_shares':2,'research_target_remaining':1,'action':'Reduce1 now in regular session; retain1 for2027H1 first human-data option; noadd. Not completedtrade.','why_now':'New rNPV explicitly includes later clinical funding and conversion-adjusted IPO shares. Current~20 versusbase4.82 andstrong16.22 leaves little conservative margin before human efficacy evidence. Two shares roughlydouble permanent clinical/funding risk; reducing1 now replaces waiting25–26 with a valuation-grounded decision.','why_not_zero':'No disclosed clinical failure; firsthumanstudy has started and IPO cashfunding targets1H2029. Large eligible cardiovascular market and durable silencing could exceed authorpenetration/success assumptions. One retainedshare acknowledges this right tail and avoids treating uncalibrated rNPV as certainty.','deadline':'Next material trial/safety/financing update; formal event pre-review before2027H1 firstdata, or earlier userrequest. No scheduledmonitor.','exit_remaining':'Severe human safety issue, lack of durable target effect, or trial delay/funding cuts impair thefirstdata path →1→0. Oldfirstbatch conditions25–26 or close<16.7 AND XBI<145 are superseded for firstbatch by current2→1; do not repeat them to auto-sell remaining1.','fees_NAV':'UNKNOWN; sharetarget within latestconfirmed2; no budgetpercentage invented.'}
    if s=='DPC':c['holding_decision']={'confirmed_shares':1,'research_target_remaining':1,'action':'Hold1, noautomaticadd. Alreadyexecutedsale1 not repeated.','reason':'Price28.62near28.12base, explicit cash/IPO/interest bridge and independent OEM demand retain right-tail46.59; normal operatingcash weakness remains.','protection':'New regular-close27.57 capital-protection review forremaining1; fundamental cancellations/qualification/yield/cash obligations deterioration can exit immediately. Old30.15 secondbatch not reapplied.'}
    if s=='INOD':c['holding_decision']={'confirmed_shares':1,'research_target_remaining':1,'action':'Hold1, noadd.','reason':'IR Nov5date now closed, normalizedcash stress stillpositive, current57.43 below66.24base. Existingprotect52 and recovery61–65+QQQ<743 unchanged; economiccustomerloss/normalizedmargin<12% exits.','protection':'Existing regularclose52; no relaxation to50.17 despite new20daylow.'}
    models[s]=c['valuation']
(P/'CARDS.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2))
(P/'MODELS.json').write_text(json.dumps(models,ensure_ascii=False,indent=2))
r=(P/'REPORT.md').read_text().replace('14:20–15:10 UTC','约14:20 UTC起逐源采集，实际工具时钟15:07:19 UTC完成汇总').replace('10月22日15:10 UTC','10月22日15:07:19 UTC')
r=r.replace('|50.17|','|52|').replace('L=50.17','L=52.00')
r+='\n\n## 验收修订：现仓与资本缺口\n\n事件截点采用真实clock回执2026-10-21 15:07:19 UTC，不预填未来15:10。source_tag_receipts的filed=Oct6为继承采集标签，不当SEC真实申报日；SEC_DELTA/submissions才是申报时序。TEM已核旧模型2050×3、2700×5、3250×8，来自serenity-alternatives-20261020-2230/TEM_MODEL.json；随当前68.03静态换股更新，既非固定报价也非已完成并购。\n\nINOD原持仓52收盘保护优先，不下移50.17；原反弹61–65、QQQ<743且无新盈利改善退出同一1股条件保留。上文通用结构说明只适用于新建图；个别数值以CARDS修订为准。\n\nCCXI最新最终资本表正文仍未读；特意列非阻塞现价估值排除的缺口。基准2031年收入1bn、净利15%、30倍与末期现金100m，甚至不计未来稀释且分母仅235.273m，现值8.27；再极端删除全部SPAC/PIPE/激励，仅保留Agility200.871m份额，现值9.69，仍不足现价合理参与。强经营情景可以更高，不能称机器人注定失败；任何重新推荐须先补最终权利表。\n'
for c in cards:
    if 'holding_decision'in c:r+='\n### '+c['symbol']+' 最新确认现仓判断\n\n'+json.dumps(c['holding_decision'],ensure_ascii=False,indent=2)+'\n'
(P/'REPORT.md').write_text(r)
manifest=[]
for f in P.rglob('*'):
    if f.is_file() and f.name!='MANIFEST.json':manifest.append({'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(P/'MANIFEST.json').write_text(json.dumps(manifest,indent=2))
print('audit fixes saved',len(cards))
