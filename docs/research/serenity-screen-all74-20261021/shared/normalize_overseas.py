"""Normalize public local-market bars; omit the unfinished European session."""
import json,csv,datetime
from pathlib import Path
from zoneinfo import ZoneInfo
P=Path(__file__).resolve().parent
base=json.loads((P/'TECHNICALS.json').read_text())['metrics']
out={};quote_refs={}
for t in ['SOI','IQE','SIVE','ASMPT','Lenovo','ESMT']:
    f=P/'public'/('OVER_HISTORY_'+t+'.json');r=json.loads(f.read_text())['chart']['result'][0];meta=r['meta'];zone=ZoneInfo(meta['exchangeTimezoneName'])
    q=r['indicators']['quote'][0];adj=r['indicators'].get('adjclose',[{}])[0].get('adjclose',[])
    bars=[];cutoff='2026-10-20' if t in ['SOI','IQE','SIVE'] else '2026-10-21'
    for i,stamp in enumerate(r['timestamp']):
        date=datetime.datetime.fromtimestamp(stamp,zone).strftime('%Y-%m-%d')
        if date>cutoff or q['close'][i] is None:continue
        bars.append({'date':date,**{k:q[k][i] for k in ['open','high','low','close','volume']},'adjusted_close':adj[i] if i<len(adj) else None})
    c=[x['close'] for x in bars];n=len(c);v=[x['volume'] or 0 for x in bars]
    ret=lambda k:(c[-1]/c[-k-1]-1)*100 if n>k else None
    m={'symbol':t,'provider_symbol':meta['symbol'],'issuer_name':meta.get('longName'),'currency':meta['currency'],'market':meta.get('fullExchangeName'),
       'asof_complete_local':bars[-1]['date'],'bars':n,'close':c[-1],'return5_pct':ret(5),'return20_pct':ret(20),'return60_pct':ret(60),
       'SMA20':sum(c[-20:])/20,'SMA50':sum(c[-50:])/50,'low20':min(x['low'] for x in bars[-20:]),'high20':max(x['high'] for x in bars[-20:]),
       'close_drawdown60_pct':(c[-1]/max(c[-60:])-1)*100,'volume_last':v[-1],'avg_volume20':sum(v[-20:])/20,
       'volume_last_vs_avg20':v[-1]/(sum(v[-20:])/20) if sum(v[-20:]) else None,
       'RS20_vs_SOXX_pp':ret(20)-base['SOXX']['return20_pct'],'RS20_vs_QQQ_pp':ret(20)-base['QQQ']['return20_pct'],
       'benchmark_asof':'2026-10-20 US regular close; not synchronous local snapshot','price_return_basis':'raw local price, dividends excluded; adjusted-close supplied separately; no FX hedging',
       'corporate_events':r.get('events',{}),'source':str(f.relative_to(P))}
    out[t]={'metrics':m,'complete_bars':bars}
    quote_refs[t]={'symbol':meta['symbol'],'issuer_name':meta.get('longName'),'currency':meta['currency'],'price':meta['regularMarketPrice'],
       'last_market_time_local':datetime.datetime.fromtimestamp(meta['regularMarketTime'],zone).isoformat(),
       'session':'intraday' if t in ['SOI','IQE','SIVE'] else 'local closed; not US regular trading','source':str(f.relative_to(P)),
       'not_exchange_original':True}
(P/'OVERSEAS_TECHNICALS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(P/'OVERSEAS_QUOTES.json').write_text(json.dumps(quote_refs,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'quotes':quote_refs,'complete_bar_counts':{t:len(d['complete_bars']) for t,d in out.items()}},ensure_ascii=False))
