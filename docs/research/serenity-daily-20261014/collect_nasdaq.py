import json,subprocess,concurrent.futures
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
pool=json.load(open(P.parent/'serenity-full-20260930/public_snapshot.json'))['universe']; overseas={'SOI','IQE','SIVE','ESMT','ASMPT','Lenovo'}
def fetch(job):
 kind,t,u=job; z={'ticker':t,'source':u,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'ok':False}
 r=subprocess.run(['curl','-sS','--fail','--max-time','15','-A','Mozilla/5.0' if kind in ['nasdaq','history'] else 'Serenity public research [REDACTED_EMAIL]',u],capture_output=True,timeout=17)
 if r.returncode:z['error']=r.stderr.decode()[:140]
 else:
  try:
   if kind in ['nasdaq','history']:z.update(data=json.loads(r.stdout),ok=True)
   else:
    s=BeautifulSoup(r.stdout,'html.parser');z.update(ok=True,text=s.get_text(' ',strip=True),links=[{'title':a.get_text(' ',strip=True),'url':a.get('href')} for a in s.find_all('a',href=True)])
  except Exception as e:z['error']=str(e)
 (P/(kind+'_'+t+'.json')).write_text(json.dumps(z,ensure_ascii=False,indent=2));return {'kind':kind,'ticker':t,'ok':z['ok']}
jobs=[('nasdaq',t,f'https://api.nasdaq.com/api/quote/{t}/info?assetclass={"etf" if t in ["QQQ","RSP","SOXX","XBI"] else "stocks"}') for t in pool+['QQQ','RSP','SOXX','XBI'] if t not in overseas]
jobs += [('history',t,f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass={"etf" if t in ["QQQ","RSP","SOXX","XBI"] else "stocks"}&fromdate=2026-07-01&todate=2026-10-13&limit=5000') for t in ['FORM','AAON','INOD','RXRX','SOXX','XBI','QQQ','RSP']]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:out=list(e.map(fetch,jobs))
(P/'nasdaq_primary_manifest.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
