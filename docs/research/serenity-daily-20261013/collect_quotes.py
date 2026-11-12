import json,subprocess,concurrent.futures,re
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
pool=json.load(open(P.parent/'serenity-full-20260930/public_snapshot.json'))['universe']
over={'SOI':'quote/epa/SOI','IQE':'quote/aim/IQE','SIVE':'quote/sto/SIVE','ESMT':'quote/tpe/3006','ASMPT':'quote/hkg/0522','Lenovo':'quote/hkg/0992'}
def get(t):
 u='https://stockanalysis.com/'+(over.get(t,'etf/'+t.lower() if t in ['QQQ','RSP','SOXX','XBI'] else 'stocks/'+t.lower()))+'/'
 z={'ticker':t,'source':u,'retrieved_utc':datetime.now(timezone.utc).isoformat()}
 r=subprocess.run(['curl','-sS','--fail','--max-time','15','-A','Mozilla/5.0',u],capture_output=True,timeout=17)
 if r.returncode:z.update(ok=False,error=r.stderr.decode()[:100])
 else:
  b=BeautifulSoup(r.stdout,'html.parser')
  for x in b(['script','style','nav','footer']):x.decompose()
  txt=b.get_text(' ',strip=True);z.update(ok=True,text=txt)
 (P/('quote_'+t+'.json')).write_text(json.dumps(z,indent=2))
 return {'ticker':t,'ok':z['ok'],'snippet':z.get('text','')[max(0,z.get('text','').find('Real-Time Price')-80):max(0,z.get('text','').find('Real-Time Price')-80)+450]}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:
 out=list(e.map(get,pool+['QQQ','RSP','SOXX','XBI']))
(P/'quote_manifest.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
