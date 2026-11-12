"""Finite daily public disclosure check; a fetched page is not a completed research decision."""
import json,subprocess,re
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor,as_completed
from urllib.parse import urlsplit,urljoin
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parent;BASE=P.parent/'serenity-full-20260930'
B=json.load(open(BASE/'public_snapshot.json'));POOL=B['universe']
P.mkdir(exist_ok=True)
(P/'SCOPE.json').write_text(json.dumps({'universe':POOL,'count':74,'frozen_utc':datetime.now(timezone.utc).isoformat(),'owner':'current_thread_direct','scope':'daily all-pool incremental prices, filings and issuer pages; deeper review holdings, FORM and AAON. Not full74 valuation completion.'},ensure_ascii=False,indent=2))
manifest=json.load(open(BASE/'primary_manifest.json'));roots={}
for r in manifest:
 u=r['url'];host=urlsplit(u).netloc
 if host and 'sec.gov' not in host:roots.setdefault(r['ticker'],'https://'+host+'/')
roots.update({'AAON':'https://investors.aaon.com/investor-news','NVDA':'https://investor.nvidia.com/news-and-events/press-releases/default.aspx','CLS':'https://corporate.celestica.com/news-releases','TSLA':'https://ir.tesla.com/press','TSM':'https://investor.tsmc.com/english/financial-calendar','RXRX':'https://ir.recursion.com/news-events/press-releases','NVT':'https://investors.nvent.com/press-releases/default.aspx','CAMT':'https://www.camtek.com/investors/','DPC':'https://ir.doncasters.com/news-and-events/news/default.aspx','SCTX':'https://www.scribetx.com/newsroom','POET':'https://www.poet-technologies.com/news-media','SOI':'https://www.soitec.com/home/group/corporate/newsroom/press-releases','IQE':'https://www.iqep.com/media/press-releases/','SIVE':'https://www.sivers-semiconductors.com/press/','ESMT':'https://www.esmt.com.tw/tw/press-room','ASMPT':'https://www.asmpt.com/en/investor-relations/news-events/','Lenovo':'https://investor.lenovo.com/en/publications/announcements.php'})
def one(kind,t,u):
 r={'kind':kind,'ticker':t,'source':u,'retrieved_utc':datetime.now(timezone.utc).isoformat()}
 try:
  p=subprocess.run(['curl','--silent','--show-error','--fail','--max-time','14','-A','Serenity public financial research [REDACTED_EMAIL]',u],capture_output=True,timeout=17)
  if p.returncode:raise RuntimeError(p.stderr.decode()[:140])
  if kind=='sec':
   d=json.loads(p.stdout);f=d['filings']['recent'];cik=int(d['cik']);r['name']=d['name'];r['new_filings']=[]
   for i,dt in enumerate(f['filingDate']):
    if dt<'2026-10-13' or dt>'2026-10-14':continue
    r['new_filings'].append({'date':dt,'form':f['form'][i],'url':f"https://www.sec.gov/Archives/edgar/data/{cik}/{f['accessionNumber'][i].replace('-','')}/{f['primaryDocument'][i]}"})
  else:
   s=BeautifulSoup(p.stdout,'html.parser');r['links']=[{'title':a.get_text(' ',strip=True),'url':urljoin(u,a['href'])} for a in s.find_all('a',href=True) if re.search('2026|results|earnings|guidance|announc|press|news|quarter|investor|acquis|contract|order',a.get_text(' ',strip=True),re.I)]
   for e in s(['script','style','nav','footer']):e.decompose()
   r['text']=s.get_text(' ',strip=True);r['status']='retrieved, semantic review pending';r['short_page']=len(r['text'])<300
  r['ok']=True
 except Exception as e:r.update(ok=False,error=str(e))
 (P/(kind+'_'+t+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2));return {k:v for k,v in r.items() if k in ['kind','ticker','source','ok','error','short_page']}
jobs=[('sec',t,f"https://data.sec.gov/submissions/CIK{r['cik']:010d}.json") for t,r in B['sec'].items() if r.get('cik')]+[('ir',t,roots[t]) for t in POOL if t in roots]
out=[]
with ThreadPoolExecutor(max_workers=5) as pool:
 for f in as_completed([pool.submit(one,*j) for j in jobs]):
  out.append(f.result());(P/'manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
  if len(out)%30==0:print('collected',len(out),'of',len(jobs),'ok',sum(x['ok'] for x in out),flush=True)
print('DONE',len(out),sum(x['ok'] for x in out),flush=True)
