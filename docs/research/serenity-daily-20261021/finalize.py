"""Finite local consolidation and evidence checks; no network or accounts."""
import csv, json, hashlib, datetime, re
from pathlib import Path
P=Path(__file__).resolve().parent
S=json.loads((P/'SCOPE.json').read_text())
def dump(name,obj):
    (P/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def read(name): return json.loads((P/name).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
quotes={}
for t in list(S['positions'])+['QQQ','SOXX','SPY','RSP','XLV','XBI']:
    f=P/'public'/('FINAL_'+t+'.json')
    if not f.exists(): f=P/'public'/('QUOTE_'+t+'.json')
    d=json.loads(f.read_text())['data']; v=d.get('primaryData') or d
    quotes[t]={'price':float(v['lastSalePrice'].replace('$','').replace(',','')),
        'change_percent':v.get('percentageChange'),
        'asof':v.get('lastTradeTimestamp') or d.get('timeAsOf'),
        'session':'regular','source':str(f.relative_to(P)),
        'trade_time_independently_confirmed':bool(d.get('primaryData'))}
dump('FINAL_QUOTES.json',quotes)
targets={**S['positions'],'CAMT':0,'DPC':1,'TEM':0,'AIP':0}
rules={
 'NVDA':{'downside':'REGULAR close<214: final target1','profit_protection':'228–230 with SOXX<538: same first batch to1; mutually exclusive','new_fact':'1.1bn capacity reservation advance; payment timing and profit unknown'},
 'TSM':{'economic_exit':'Q4 revenue<52.3bn AND gross margin<65% with structural demand/yield/cost deterioration: target0','retired':'419','review':'Nov10 monthly sales and new earnings'},
 'CLS':{'economic_exit':'major AI projects cancelled/delayed with earnings cut, or normalized operating margin persistently below7%: target0','retired':'317 automatic exit','review':'Oct26 after-market Q3/Oct27 investor day'},
 'TEM':{'current_action':'exit3','new_fact':'S4/A new meeting and exchange terms; no per-share earnings/cash improvement','model':'MODEL_EVENT_BRIDGE.md'},
 'AIP':{'current_action':'exit10','new_fact':'Nov5 earnings date only; base11.60/strong24.24 unchanged','model':'MODEL_EVENT_BRIDGE.md'},
 'CAMT':{'already_triggered':'Oct20 regular close127.90<128.50 AND SOXX500.01<538','current_action':'exit1; today rebound does not reset; operating growth/right-tail retained as counterevidence'},
 'FORM':{'downside':'valid regular-session trade<=100: target0','profit_protection':'120 warning;130–131 without stronger new earnings/cash: target0','new_fact':'same300m Teradyne transaction; counted once','current_action':'hold1, no add'},
 'RXRX':{'temporary_hold':True,'gaps':['full rNPV','current IR event coverage/closing cash confirmation'],'review':'Oct30 before Nov2 clinical event; earlier material facts','economic_exit':'efficacy/tolerability or viable registration path invalidated: target0','retired':'3.6/4.0 automatic batches'},
 'DPC':{'already_triggered':'Oct20 regular close29.12<30.15: final target1','same_threshold_not_repeated_on_remaining':True,'temporary_remaining_one':True,'gaps':['dynamic IR/event timeliness','disposal consideration/current cash bridge'],'review':'Oct22 before regular session, request based','economic_exit':'IGT order/capacity setbacks impair normalized cash return or debt/capex erodes per-share payoff: target0'},
 'POET':{'economic_exit':'qualification/production cancelled or persistently delayed, or materially worsened cash bridge and inadequate per-share return: target0','retired':'5.70 automatic all-exit','review':'Nov16 Q3 or new material facts; weak relative strength plus other risks reviewed earlier'},
 'INOD':{'temporary_hold':True,'gaps':['IR event timeliness'],'review':'Oct22 before regular session, request based','downside':'REGULAR close<52: target0','profit_protection':'61–65 with no improved operating earnings evidence AND QQQ<743: same remaining1 exits'},
 'SCTX':{'downside':'REGULAR close<16.7 AND XBI<145: target1','profit_protection':'25–26 absent new human evidence: target1, same first batch mutually exclusive','economic_exit':'serious safety/registration failure or materially reduced runway triggers immediate remaining-size reunderwriting','review':'2027H1 data goal; earlier facts and current technical review'}
}
dec=[]
for t,n in S['positions'].items():
    k=targets[t]; a='EXIT' if k==0 else 'REDUCE' if k<n else 'HOLD'
    dec.append({'symbol':t,'user_confirmed_qty':n,'research_target_qty':k,'action':a,
        'not_a_fill':True,'price':quotes[t], 'conditions':rules[t],
        'full_new_buy_research_passed':False})
dump('DECISIONS.json',{'date':'2026-10-21','owner':'root','user_reaffirmation':'latest screenshots12; no repeated question',
    'capital_current':'UNKNOWN;2829.66 is Oct20 historical NAV','prior_technical_review':'Oct21 04:00 Beijing expired; individually reassessed today',
    'new_technical_review':'Oct22 04:00 Beijing or material new facts earlier; specific evidence gaps separately dated',
    'decisions':dec,'automation':'none; request based'})
rows=[]
for t in S['universe']:
    if t=='FORM': status='条件观察';gap='唯一研究缺口：回到原109参与锚；接近边界非硬FAIL。已有1股不自动加第二股；账户/加仓独立未知。'
    elif t in ['TEM','AIP']: status='排除';gap='当前价估值与现金/稀释风险，事件桥已核；新财报/每股兑现改变后重审。'
    else: status='未完成';gap='本轮未完成全项新买基本面/估值/事件/经济失效；索引或报价不等于研究完成。'
    q=None
    for name in ['FINAL_'+t,'QUOTE_'+t,'FALLBACK_CHART_'+t]:
        f=P/'public'/(name+'.json')
        if not f.exists(): continue
        j=json.loads(f.read_text());d=j.get('data') or {}; v=d.get('primaryData') or d
        if v.get('lastSalePrice'):
            q=(v['lastSalePrice'],v.get('lastTradeTimestamp') or d.get('timeAsOf'),str(f.relative_to(P)));break
    if t=='ESMT': q=('246 TWD','2026-10-21 TWSE close','public/TWSE_ESMT.json')
    sec=P/'public_company'/('SEC_'+t+'.json')
    if not sec.exists(): sec=P/'public'/('SEC_'+t+'.json')
    rows.append({'symbol':t,'user_qty':S['positions'].get(t,0),'new_buy_status':status,
       'price_reference':q[0] if q else 'UNKNOWN','price_asof':q[1] if q else 'UNKNOWN',
       'price_source':q[2] if q else 'current overseas path unverified',
       'sec_index':'read index only; body scope in COMPANY_UPDATE/NONHOLDING_INCREMENT' if sec.exists() else 'overseas local disclosure not fully checked',
       'holding_risk_review':'REPORT.md' if t in S['positions'] else 'not a current holding',
       'gap_or_disposition':gap,'owner':'root','condition_expiry':'2026-10-22 04:00 Beijing or new material fact' if t=='FORM' else ''})
with (P/'COVERAGE.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
checks={}
checks['actual12_unique']=len(dec)==12 and len(set(d['symbol'] for d in dec))==12
checks['targets_in_user_bounds']=all(0<=d['research_target_qty']<=d['user_confirmed_qty'] for d in dec)
checks['three_exit_one_reduce_eight_hold']={a:sum(d['action']==a for d in dec) for a in ['EXIT','REDUCE','HOLD']}=={'EXIT':3,'REDUCE':1,'HOLD':8}
trigger=read('OCT20_CLOSE_TRIGGERS.json')
checks['CAMT_trigger']=trigger['closes']['CAMT']<128.5 and trigger['closes']['SOXX']<538
checks['DPC_trigger']=trigger['closes']['DPC']<30.15
checks['NVDA_INOD_not_triggered']=trigger['closes']['NVDA']>=214 and trigger['closes']['INOD']>=52
checks['all74_frozen']=len(rows)==74 and len(set(r['symbol'] for r in rows))==74
counts={a:sum(r['new_buy_status']==a for r in rows) for a in ['研究门通过','条件观察','排除','未完成']}
checks['counts_0_1_2_71']=list(counts.values())==[0,1,2,71]
checks['numeric_refs69']=sum(r['price_reference']!='UNKNOWN' for r in rows)==69
raw=[];bad=[]
for f in list((P/'public').glob('*.receipt.json'))+list((P/'public_company').glob('*.receipt.json')):
    j=json.loads(f.read_text())
    if j.get('http_status')!=200: continue
    path=j.get('raw_path')
    candidates=[P/path,P/f.parent.name/path] if path else []
    candidates.extend([f.with_name(f.name.replace('.receipt.json','.raw')),f.with_name(f.name.replace('.receipt.json','.html'))])
    target=next((x for x in candidates if x.exists()),None)
    h=j.get('sha256')
    if target and h:
        ok=sha(target)==h;raw.append(str(target.relative_to(P)))
        if not ok: bad.append(str(f.relative_to(P)))
checks['current_available_raw_hashes_match']=not bad
prior=P.parent/'serenity-user-execution-20261020-2254'
pm=json.loads((prior/'MANIFEST.json').read_text()); priorbad=[]
for e in pm['files']:
    f=prior/e['path']
    if not f.exists() or sha(f)!=e['sha256']:priorbad.append(e['path'])
checks['prior69_files_unchanged']=not priorbad and len(pm['files'])==69
sec_current={f.stem.replace('SEC_','') for loc in ['public','public_company'] for f in (P/loc).glob('SEC_*.json') if not f.name.endswith('.receipt.json')}
checks['sec68_indices']=len(sec_current)==68
pol=P.parent.parent/'交易研究执行准则.md'
dump('POLICY_READ_RECEIPT.json',{'file':str(pol),'sha256':sha(pol),'version':'SERENITY-DECISION-2026-10-20-v1.1',
   'full_read_tool_receipt':'functions exec after compaction at2026-10-21T14:19:57Z; complete141line output inspected',
   'not_software_enforcement':True})
report=(P/'REPORT.md').read_text()
missing=[]
for link in re.findall(r'\]\(([^)]+)\)',report):
    if link.startswith(('https://','http://')):continue
    if link in ['VALIDATION.json']:continue
    if not (P/link.split('#')[0]).exists():missing.append(link)
checks['report_local_links']=not missing
dump('VALIDATION.json',{'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'new_buy_counts':counts,
   'raw_hash_verified_count':len(raw),'raw_hash_mismatches':bad,'prior_manifest_files':len(pm['files']),
   'prior_manifest_mismatch':priorbad,'missing_links':missing,
   'limits':['No full74 screen completion','RXRX rNPV and IR gap','DPC/INOD IR event gaps','VIX delayed/timezone unmarked','TSM/CLS final refresh timeout;10:07 current-turn data retained','AIP/SERV chart timestamps not independent trade times','No continuous monitoring or real investment performance validation']})
files=[{'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(P.rglob('*')) if f.is_file() and f.name!='MANIFEST.json']
dump('MANIFEST.json',{'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files})
print(json.dumps({'checks':checks,'counts':counts,'raw':len(raw),'manifest_files':len(files)},ensure_ascii=False))
