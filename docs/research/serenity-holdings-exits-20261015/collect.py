import json,subprocess,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
base=json.load(open(P.parent/'serenity-full-20260930/public_snapshot.json'))
pos={'TSLA':1,'NVDA':2,'TSM':1,'RXRX':30,'CLS':1,'NVT':2,'CAMT':1,'DPC':3,'SCTX':2,'POET':20,'INOD':1}
(P/'SCOPE.json').write_text(json.dumps({'holdings_user_confirmed':pos,'frozen_utc':datetime.now(timezone.utc).isoformat(),'owner':'current_thread','scope':'all remaining holdings, forward exit rules, no brokerage access'},indent=2))
jobs=[]
for t in list(pos)+['QQQ','RSP','SOXX','XBI']:
 typ='etf' if t in ['QQQ','RSP','SOXX','XBI'] else 'stocks'
 jobs.extend([('quote',t,f'https://api.nasdaq.com/api/quote/{t}/info?assetclass={typ}'),('history',t,f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass={typ}&fromdate=2026-05-01&todate=2026-10-14&limit=5000')])
for t in pos:
 cik=base['sec'][t]['cik'];jobs.append(('sec',t,f'https://data.sec.gov/submissions/CIK{cik:010d}.json'))
def f(job):
 k,t,u=job;z={'source':u,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'ok':False}
 r=subprocess.run(['curl','-sS','--fail','--max-time','18','-A','Mozilla/5.0' if k!='sec' else 'Serenity public financial research [REDACTED_EMAIL]',u],capture_output=True)
 if r.returncode:z['error']=r.stderr.decode()[:140]
 else:
  try:
   d=json.loads(r.stdout);z.update(ok=True,data=d)
   if k=='sec':
    a=d['filings']['recent'];z['filings']=[{'date':dt,'form':a['form'][i],'url':f"https://www.sec.gov/Archives/edgar/data/{int(d['cik'])}/{a['accessionNumber'][i].replace('-','')}/{a['primaryDocument'][i]}"} for i,dt in enumerate(a['filingDate']) if dt>='2026-10-14']
  except Exception as e:z['error']=str(e)
 (P/(k+'_'+t+'.json')).write_text(json.dumps(z,indent=2));return {'kind':k,'ticker':t,'ok':z['ok']}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:out=list(e.map(f,jobs))
(P/'manifest.json').write_text(json.dumps(out,indent=2));print(out)
