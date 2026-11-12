"""Closed-session public facts and preexisting trigger audit; no account access."""
import json
from pathlib import Path
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parent
OLD=BASE.parent/'serenity-rmbs-complete-20261023'
P=BASE/'public'
def read(path):return json.loads(path.read_text())
def num(x):return float(str(x).replace('$','').replace(',','').replace('%',''))
hist={}
for t in ['NVDA','TSM','CLS','RMBS','RXRX','DPC','POET','SCTX','QQQ','SOXX','XBI','XLI']:
    path=OLD/'public'/('HISTORY_FULL_'+t+'.json') if t in ['RMBS','QQQ','SOXX'] else P/('HISTORY_'+t+'.json')
    data=read(path)['data'];rows=data['tradesTable']['rows']
    bars=sorted([{'date':datetime.strptime(r['date'],'%m/%d/%Y').date().isoformat(),**{k:num(r[k]) for k in ['open','high','low','close','volume']}} for r in rows],key=lambda x:x['date'])
    assert bars[-1]['date']=='2026-10-22',t
    hist[t]={'bars':bars,'source':str(path)}
stats={}
for t,h in hist.items():
 b=h['bars'];c=[r['close'] for r in b];r=b[-1]
 s={'latest_completed_regular_bar':r,'source':h['source'],'rows':len(b),
 'returns_pct':{str(n):(c[-1]/c[-1-n]-1)*100 if len(b)>n else None for n in [1,5,20,60]},
 'SMA20':sum(c[-20:])/20 if len(c)>=20 else None,'SMA50':sum(c[-50:])/50 if len(c)>=50 else None,
 'prior20_high':max(x['high'] for x in b[-21:-1]),'prior20_low':min(x['low'] for x in b[-21:-1]),
 'volume_vs_prior20':r['volume']/(sum(x['volume'] for x in b[-21:-1])/len(b[-21:-1]))}
 if t in ['NVDA','TSM','CLS','RMBS','POET','DPC','RXRX','SCTX']:
  bench='SOXX' if t in ['NVDA','TSM','CLS','RMBS','POET'] else 'XBI' if t in ['RXRX','SCTX'] else 'XLI'
  s['benchmark']=bench
  refdate=b[-21]['date'] if len(b)>20 else None
  ref={x['date']:x for x in hist[bench]['bars']}
  s['RS20_pp']=s['returns_pct']['20']-((ref['2026-10-22']['close']/ref[refdate]['close']-1)*100) if refdate in ref else None
 stats[t]=s
quotes={t:read(P/('INFO_'+t+'.json'))['data'] for t in ['NVDA','TSM','CLS','RMBS','RXRX','DPC','POET','SCTX','QQQ','SPY','RSP','SOXX','XBI','XLV','XLI']}
nv=stats['NVDA']['latest_completed_regular_bar'];sx=stats['SCTX']['latest_completed_regular_bar'];xb=stats['XBI']['latest_completed_regular_bar']
triggers={'NVDA':{'old_close_lt214':nv['close']<214,'old_rebound228to230_and_SOXXlt538':nv['high']>=228 and stats['SOXX']['latest_completed_regular_bar']['close']<538,
 'exact_intraday_composite_timestamp':'UNKNOWN; need aligned minute data if day high228 reached; close214 independently decidable','target_after_same_first_batch':1,'user_fill_confirmed':False},
 'RMBS':{'old_regular_price_lte85_seen':stats['RMBS']['latest_completed_regular_bar']['low']<=85,'actual_first_tick':'UNKNOWN'},
 'SCTX':{'old_close_lt16_7':sx['close']<16.7,'XBI_close_lt145':xb['close']<145,'combined_close_trigger':sx['close']<16.7 and xb['close']<145,
 'price25to26_seen':sx['high']>=25,'first_intraday_tick':'UNKNOWN'}}
out={'retrieved_for_this_run':datetime.now(timezone.utc).isoformat(),'latest_regular_session':'2026-10-22','session_now':'US closed; Beijing10/23 morning; tonight21:30 regular open',
 'stats':stats,'quotes':quotes,'VIX':read(P/'VIX.json'),'VIX_time_warning':'Provider timestamp and last_trade_time lack timezone; delayed reference not synchronized Nasdaq tick',
 'preexisting_triggers':triggers,'reuse':'RMBS/QQQ/SOXX142-day histories read earlier this same US-closed session, unchanged data explicitly reused; new current info independently confirms same closes',
 'no_current_NAV_assumed':True}
(BASE/'shared').mkdir(exist_ok=True)
(BASE/'shared/MARKET.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'stats':{k:{'bar':v['latest_completed_regular_bar'],'return20':v['returns_pct']['20'],'RS20_pp':v.get('RS20_pp'),'low20':v['prior20_low'],'high20':v['prior20_high']} for k,v in stats.items()},'old_triggers':triggers},ensure_ascii=False,indent=2))
