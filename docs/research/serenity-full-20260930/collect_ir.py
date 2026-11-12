"""Bounded public issuer news/event discovery, no credentials or automatic retries."""
import json,subprocess,re
from pathlib import Path
from urllib.parse import urlsplit,urljoin
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parent
s=json.loads((P/'primary_manifest.json').read_text())
roots={}
for x in s:
 h=urlsplit(x['url']).netloc
 if 'sec.gov' not in h and 'amgen' not in h: roots.setdefault(x['ticker'],'https://'+h+'/')
roots.update({'CCXI':'https://churchillcapital-11.com/','INOD':'https://investor.innodata.com/events-and-presentations/','RMBS':'https://investor.rambus.com/','DPC':'https://ir.doncasters.com/','SKHY':'https://news.skhynix.com/','ESMT':'https://www.esmt.com.tw/tw/press-room','SOI':'https://www.soitec.com/home/group/corporate/newsroom/press-releases','SIVE':'https://www.sivers-semiconductors.com/press/','IQE':'https://www.iqep.com/media/press-releases/','ASMPT':'https://www.asmpt.com/en/investor-relations/announcements-circulars/','Lenovo':'https://investor.lenovo.com/en/ir/announcements.php'})
(P/'ir').mkdir(exist_ok=True)
def read(u):
 c=subprocess.run(['curl','--fail','--silent','--show-error','--max-time','12','--max-filesize','4000000','-A','Serenity public research',u],capture_output=True,timeout=15)
 if c.returncode:raise ValueError(c.stderr.decode(errors='replace')[:180])
 soup=BeautifulSoup(c.stdout,'html.parser')
 links=[{'title':a.get_text(' ',strip=True),'url':urljoin(u,a.get('href',''))} for a in soup.find_all('a',href=True) if re.search('event|calendar|press|news|2026',a.get_text(' ',strip=True),re.I)]
 for a in soup(['script','style','nav','footer']):a.decompose()
 text=soup.get_text(' ',strip=True)
 if len(text)<250:raise ValueError('content shell; not readable event evidence')
 return text,links

def one(t,u):
 row={'ticker':t,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'documents':[],'review_status':'UNREVIEWED_not_event_pass'}
 try:
  txt,links=read(u);(P/'ir'/f'{t}_root.txt').write_text(txt)
  row['documents'].append({'source':u,'path':f'ir/{t}_root.txt','links':links,'characters':len(txt)})
  event=next((a['url'] for a in links if re.search('events|calendar',a['title'],re.I) and a['url']!=u and urlsplit(a['url']).netloc==urlsplit(u).netloc),None)
  if event:
   try:
    txt,ll=read(event);(P/'ir'/f'{t}_events.txt').write_text(txt);row['documents'].append({'source':event,'path':f'ir/{t}_events.txt','links':ll,'characters':len(txt)})
   except Exception as e:row['event_error']=str(e)
 except Exception as e:row['error']=str(e)
 return row
out=[]
with ThreadPoolExecutor(max_workers=4) as pool:
 for f in as_completed([pool.submit(one,t,u) for t,u in roots.items()]):
  out.append(f.result());(P/'ir_status.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
  if len(out)%16==0:print('IR',len(out),sum(bool(x['documents']) for x in out),flush=True)
print('DONE',len(out),sum(bool(x['documents']) for x in out),flush=True)
