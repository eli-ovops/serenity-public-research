"""Bounded, public-only document capture; no credential/cookie store or retries."""
from pathlib import Path
import json,re,io,urllib.request
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from bs4 import BeautifulSoup
from pypdf import PdfReader
P=Path(__file__).resolve().parent
snap=json.loads((P/'public_snapshot.json').read_text())
base=json.loads((P/'baseline_public.json').read_text())
existing={x['url'] for x in json.loads((P/'primary_status.json').read_text())}
jobs=[]
for t in snap['universe']:
 fs=[x for x in snap['sec'].get(t,{}).get('filings',[]) if x['form'] in ['10-Q','10-K']]
 if fs and fs[0]['url'] not in existing:jobs.append(dict(ticker=t,url=fs[0]['url'],title=fs[0]['form']+' '+fs[0]['date']))
for x in base:
 u=x.get('primary_source','')
 if '/Archives/' in u and u not in existing and not any(z['url']==u for z in jobs):jobs.append(dict(ticker=x['ticker'],url=u,title='prior located primary, verify period'))
extra={
'SIVE':'https://www.sivers-semiconductors.com/wp-content/uploads/2026/08/Sivers-Interim-report-Q226.pdf',
'RR':'https://ir.richtechrobotics.com/node/7606/html',
'TSEM':'https://ir.towersemi.com/static-files/da25365d-20d1-4c75-83d9-93b39badcb42',
'NOK':'https://www.nokia.com/newsroom/nokia-corporation-report-for-q2-and-half-year-2026/',
'CCXI':'https://www.sec.gov/Archives/edgar/data/2074973/000121390026097764/ea0297114-04.htm'}
for t,u in extra.items():jobs.append(dict(ticker=t,url=u,title='current discovered source'))
(P/'supplement_manifest.json').write_text(json.dumps(jobs,indent=2))
def fetch(i,x):
 r=dict(x,index=i,retrieved_utc=datetime.now(timezone.utc).isoformat())
 try:
  req=urllib.request.Request(x['url'],headers={'User-Agent':'Serenity public research [REDACTED_EMAIL]'})
  with urllib.request.urlopen(req,timeout=12) as res:
   raw=res.read(8000000);ctype=res.headers.get('Content-Type','')
  if raw.startswith(b'%PDF'):text='\n'.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(raw)).pages)
  else:
   soup=BeautifulSoup(raw,'html.parser')
   for q in soup(['script','style','nav','footer']):q.decompose()
   text=soup.get_text(' ',strip=True)
  filename=f"primary/{i:03d}_{x['ticker']}.txt"
  (P/filename).write_text(text);r.update(ok=True,path=filename,characters=len(text))
 except Exception as e:r.update(ok=False,error=str(e))
 return r
out=[]
with ThreadPoolExecutor(max_workers=4) as pool:
 for f in as_completed([pool.submit(fetch,200+i,x) for i,x in enumerate(jobs)]):
  out.append(f.result()); (P/'supplement_status.json').write_text(json.dumps(out,indent=2))
  if len(out)%10==0:print(len(out),sum(x['ok'] for x in out),flush=True)
print('DONE',len(out),sum(x['ok'] for x in out),flush=True)
