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
domains={'FORM':'formfactor','CAMT':'camtek','ONTO':'ontoinnovation','AMKR':'amkor','ASX':'aseglobal','AEHR':'aehr','ASMPT':'asmpt','TSEM':'towersemi|towerjazz','CRDO':'credosemi','AAOI':'ao-inc|appliedoptoelectronics','CIEN':'ciena','POET':'poet-technologies','SIVE':'sivers-semiconductors','LWLG':'lightwavelogic','NOK':'nokia','COHR':'coherent','LITE':'lumentum','FN':'fabrinet','AXTI':'axt.com','SOI':'soitec','IQE':'iqep','LASR':'nlight','MOD':'modine','AAON':'aaon','NVT':'nvent','SMCI':'supermicro','VRT':'vertiv','DELL':'dell','HPE':'hpe','CLS':'celestica','Lenovo':'lenovo','ANET':'arista','AMZN':'aboutamazon','NBIS':'nebius','PWR':'quantaservices','FLNC':'fluenceenergy','ETN':'eaton','GEV':'gevernova','HWM':'howmet','DPC':'doncasters','GNRC':'generac','NVDA':'nvidia','AVGO':'broadcom','MRVL':'marvell','AIP':'arteris','ALAB':'asteralabs','TSM':'tsmc','KLAC':'kla.com','LRCX':'lamresearch','AMAT':'appliedmaterials','ASML':'asml','ACMR':'acmr','ENTG':'entegris','INTC':'intel|intc.com','ON':'onsemi','GFS':'gf.com','MU':'micron','WDC':'wdc','STX':'seagate','RMBS':'rambus','SKHY':'skhynix','ESMT':'esmt','TER':'teradyne','CCXI':'amgen','TSLA':'tesla','RXRX':'recursion','SCTX':'scribetx','TEM':'tempus','OUST':'ouster','HSAI':'hesaitech','INOD':'innodata','VPG':'vpgsensors|vpg|vishaypg','RR':'richtechrobotics','SERV':'serverobotics'}
ciks={str(v['cik']):k for k,v in snap['sec'].items() if 'cik' in v}
items=[]
for f in P.glob('search_*.txt'):
 for b in f.read_text().split('--------------------------------------------------------------------------------'):
  m=re.search(r'\((https://[^\s]+)\)',b)
  if not m:continue
  u=m.group(1);host=urlparse(u).netloc
  if any(x in host for x in ['reddit','youtube','wikipedia','proxy','financialfilings']):continue
  ticker=None
  for t,d in domains.items():
   if re.search(d,host,re.I):ticker=t;break
  sm=re.search(r'sec.gov/Archives/edgar/data/(\d+)/',u)
  if sm:ticker=ciks.get(sm.group(1))
  if not ticker:continue
  title=b.strip().splitlines()[0]
  score=0
  if re.search('2026|2027',title):score+=2
  if re.search('reports|announces|results|interim|10q',title,re.I):score+=2
  if re.search('to report|to release|announce.*date|conference call|first quarter|2025',title,re.I):score-=4
  items.append({'ticker':ticker,'url':u,'title':title,'score':score,'discovery':f.name})
extra={
'FORM':'https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2026-second-quarter-results',
'CAMT':'https://www.camtek.com/news-and-events/camtek-announces-results-for-the-second-quarter-of-2026/',
'ONTO':'https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Reports-2026-Second-Quarter-Results/default.aspx',
'AMKR':'https://amkortech.gcs-web.com/news-releases/news-release-details/amkor-technology-reports-financial-results-second-quarter-2026',
'AEHR':'https://www.sec.gov/Archives/edgar/data/1040470/000165495426006655/aehr_ex991.htm',
'ASMPT':'https://www.asmpt.com/en/investor-relations/financial-information/',
'AIP':'https://ir.arteris.com/news-releases/news-release-details/arteris-announces-financial-results-second-quarter-and-0'}
for t,u in extra.items():items.append({'ticker':t,'url':u,'title':'Known current IR financial source','score':9,'discovery':'live_web_this_turn'})
jobs=[]
for t in json.loads((P/'SCOPE.json').read_text())['universe']:
 chosen=sorted([x for x in items if x['ticker']==t],key=lambda x:-x['score'])
 seen=set()
 for x in chosen:
  if x['url'] not in seen:
   jobs.append(x);seen.add(x['url'])
  if len(seen)>=2:break
 for x in snap['sec'].get(t,{}).get('filings',[]):
  if x['date']>='2026-09-24' and x['form'] in ['8-K','6-K','8-A12B'] and x['url'] not in seen:jobs.append({'ticker':t,'url':x['url'],'title':x['form']+' '+x['date'],'discovery':'current_SEC_index','score':10})
(P/'primary_manifest.json').write_text(json.dumps(jobs,ensure_ascii=False,indent=2))
(P/'primary').mkdir(exist_ok=True)
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
with ThreadPoolExecutor(max_workers=5) as pool:
 for f in as_completed([pool.submit(fetch,i,x) for i,x in enumerate(jobs)]):
  out.append(f.result())
  (P/'primary_status.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
  if len(out)%20==0:print('documents',len(out),'success',sum(x['ok'] for x in out),flush=True)
print('DONE',len(out),'success',sum(x['ok'] for x in out),flush=True)
