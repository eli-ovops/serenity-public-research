"""Bounded public research snapshot. No account endpoints or background jobs."""
import csv, json, statistics, urllib.request, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
BASE=[r['ticker'].replace('SIVE/SIVEF','SIVE') for r in csv.DictReader((ROOT/'SERENITY_GTC_MERGED_CANDIDATE_MATRIX.csv').open())]
EXTRA='WDC STX FN AMKR ASX TER KLAC LRCX AMAT ASML ACMR ENTG RMBS INTC SKHY ON GFS CCXI AEHR AXTI SOI IQE ESMT HWM TSLA RXRX CLS DPC SCTX AMZN AIP ASMPT Lenovo LASR TEM NBIS ALAB GNRC'.split()
UNIVERSE=list(dict.fromkeys(BASE+EXTRA))
NON_US={'SIVE','SOI','IQE','ESMT','ASMPT','Lenovo'}

def fetch(url):
    headers={'User-Agent':'Mozilla/5.0 public research'} if 'api.nasdaq.com' in url else {'User-Agent':'Serenity public financial research [REDACTED_EMAIL]','Accept':'application/json'}
    req=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req,timeout=25) as r: return json.load(r)

def number(x): return float(str(x).replace('$','').replace(',',''))

def history(t):
    kind='etf' if t in ['QQQ','SOXX','RSP','XLV'] else 'stocks'
    url=f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass={kind}&fromdate=2026-05-01&todate=2026-09-17&limit=5000'
    data=fetch(url)
    rows=((data.get('data') or {}).get('tradesTable') or {}).get('rows') or []
    rows=[dict(date=datetime.strptime(x['date'],'%m/%d/%Y').date().isoformat(),**{k:number(x[k]) for k in ['open','high','low','close','volume']}) for x in rows]
    rows=sorted([x for x in rows if x['date']<='2026-09-17'],key=lambda x:x['date'])
    if not rows: raise ValueError('No completed-session rows')
    m={'last_date':rows[-1]['date'],'close':rows[-1]['close'],'bars':len(rows),'price_basis':'unadjusted OHLC; corporate actions must be reviewed'}
    for n in [5,20,60]:
        m['return_'+str(n)]=rows[-1]['close']/rows[-n-1]['close']-1 if len(rows)>n else None
    for n in [20,50]:
        m['sma_'+str(n)]=statistics.mean(x['close'] for x in rows[-n:]) if len(rows)>=n else None
    m['low20']=min(x['low'] for x in rows[-20:]); m['high20']=max(x['high'] for x in rows[-20:])
    m['volume_ratio']=statistics.mean(x['volume'] for x in rows[-20:])/statistics.mean(x['volume'] for x in rows[-40:-20]) if len(rows)>=40 else None
    m['drawdown_from_high20']=rows[-1]['close']/m['high20']-1
    return {'source':url,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'metrics':m,'rows':rows}

def submissions(t,cik):
    url=f'https://data.sec.gov/submissions/CIK{cik:010d}.json'
    d=fetch(url); r=d['filings']['recent']; out=[]
    for i,day in enumerate(r['filingDate']):
        if day<'2026-07-01': continue
        if r['form'][i] in ['4','3','144','4/A','3/A']: continue
        acc=r['accessionNumber'][i]
        out.append({'date':day,'form':r['form'][i],'url':f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{r['primaryDocument'][i]}"})
    return {'source':url,'name':d['name'],'cik':cik,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'filings':out[:20]}

def main():
    registry={'scope_frozen_utc':datetime.now(timezone.utc).isoformat(),'universe':UNIVERSE,'owner':'current thread direct research','completion':'primary fundamentals + reproducible valuation + completed-session trend + company events + economic invalidation; quote alone never counts','prices':{},'sec':{}}
    with ThreadPoolExecutor(max_workers=5) as p:
        jobs={p.submit(history,t):t for t in UNIVERSE+['QQQ','SOXX','RSP','XLV'] if t not in NON_US}
        for f in as_completed(jobs):
            t=jobs[f]
            try: registry['prices'][t]=f.result()
            except Exception as e: registry['prices'][t]={'error':str(e),'status':'unverified, not excluded'}
    (OUT/'public_snapshot.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2))
    print('prices',len(registry['prices']),'errors',sum('error' in r for r in registry['prices'].values()),flush=True)
    try:
        mapping=fetch('https://www.sec.gov/files/company_tickers.json')
        by={v['ticker']:int(v['cik_str']) for v in mapping.values()}
        with ThreadPoolExecutor(max_workers=4) as p:
            jobs={p.submit(submissions,t,by[t]):t for t in UNIVERSE if t in by and t not in NON_US}
            for f in as_completed(jobs):
                t=jobs[f]
                try: registry['sec'][t]=f.result()
                except Exception as e: registry['sec'][t]={'error':str(e)}
    except Exception as e: registry['sec_mapping_error']=str(e)
    (OUT/'public_snapshot.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2))
    print('sec',len(registry['sec']),flush=True)
    with (OUT/'trend_metrics.csv').open('w') as f:
        fields=['ticker','last_date','close','return_5','return_20','return_60','sma_20','sma_50','low20','high20','drawdown_from_high20','volume_ratio','bars','price_basis']
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for t,r in registry['prices'].items():
            if 'metrics' in r:w.writerow({'ticker':t,**r['metrics']})

if __name__=='__main__':main()
