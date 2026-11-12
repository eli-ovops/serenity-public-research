"""Deterministic diagnostics from complete public daily bars; not a buy model."""
import json,csv,datetime,math
from pathlib import Path
P=Path(__file__).resolve().parent
sources=json.loads((P/'HISTORY_SOURCES.json').read_text())
def number(v):
    return float(str(v).replace('$','').replace(',','').replace('%',''))
allrows={};missing=[]
for t,s in sources.items():
    f=Path(s)
    if not f.exists():missing.append(t);continue
    j=json.loads(f.read_text());data=j.get('data') or {};table=data.get('tradesTable') or {};rows=table.get('rows') or []
    bars=[]
    for r in rows:
        try:bars.append({'date':datetime.datetime.strptime(r['date'],'%m/%d/%Y').strftime('%Y-%m-%d'),**{k:number(r[k]) for k in ['open','high','low','close','volume']}})
        except (KeyError,ValueError,TypeError):continue
    bars=sorted(bars,key=lambda x:x['date'])
    if not bars:missing.append(t);continue
    allrows[t]=bars
metrics={}
for t,bars in allrows.items():
    c=[x['close'] for x in bars];vol=[x['volume'] for x in bars];n=len(c)
    ret=lambda k:(c[-1]/c[-1-k]-1)*100 if n>k and c[-1-k] else None
    m={'symbol':t,'asof':bars[-1]['date'],'bars':n,'close':c[-1],
       'return5_pct':ret(5),'return20_pct':ret(20),'return60_pct':ret(60),
       'SMA20':sum(c[-20:])/20 if n>=20 else None,'SMA50':sum(c[-50:])/50 if n>=50 else None,
       'low20':min(x['low'] for x in bars[-20:]),'high20':max(x['high'] for x in bars[-20:]),
       'close_drawdown60_pct':(c[-1]/max(c[-60:])-1)*100,
       'volume_last':vol[-1],'avg_volume10':sum(vol[-10:])/min(10,n),'avg_volume20':sum(vol[-20:])/min(20,n),
       'volume_last_vs_avg20':vol[-1]/(sum(vol[-20:])/min(20,n)) if sum(vol[-20:]) else None,
       'down_volume_share20':sum(bars[i]['volume'] for i in range(max(1,n-20),n) if c[i]<c[i-1])/sum(vol[-20:]) if sum(vol[-20:]) else None,
       'jump_warning_dates':[bars[i]['date'] for i in range(1,n) if c[i-1] and (c[i]/c[i-1]>1.8 or c[i]/c[i-1]<0.55)],
       'source_path':sources[t],'split_status':'not independently adjusted; corporate-action review required where jump warnings or disclosed split'}
    metrics[t]=m
for t,m in metrics.items():
    for bench in ['QQQ','SOXX','XLI','XLV','XBI','SPY']:
        br=metrics.get(bench,{}).get('return20_pct')
        m['RS20_vs_'+bench+'_pp']=m['return20_pct']-br if m['return20_pct'] is not None and br is not None else None
(P/'TECHNICALS.json').write_text(json.dumps({'asof':'2026-10-20 regular close','metrics':metrics,'missing':missing,'not_live_quotes':True},ensure_ascii=False,indent=2)+'\n')
with (P/'TECHNICALS.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(next(iter(metrics.values()))));w.writeheader();w.writerows(metrics.values())
print(json.dumps({'series':len(metrics),'missing':missing,'notOct20':[t for t,m in metrics.items() if m['asof']!='2026-10-20'],'jump_warnings':{t:m['jump_warning_dates'] for t,m in metrics.items() if m['jump_warning_dates']}},ensure_ascii=False))
