import json,subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parent
urls={'SIVE':'https://stockanalysis.com/quote/sto/SIVE/history/','SOI':'https://stockanalysis.com/quote/epa/SOI/history/','IQE':'https://stockanalysis.com/quote/aim/IQE/history/','ESMT':'https://stockanalysis.com/quote/tpe/3006/history/','ASMPT':'https://stockanalysis.com/quote/hkg/0522/history/','Lenovo':'https://stockanalysis.com/quote/hkg/0992/history/','CCXI':'https://stockanalysis.com/stocks/ccxi/history/'}
def one(t,u):
 r={'ticker':t,'source':u}
 try:
  c=subprocess.run(['curl','--fail','--silent','--show-error','--max-time','15',u],capture_output=True,timeout=18)
  if c.returncode:raise ValueError(c.stderr.decode()[:200])
  soup=BeautifulSoup(c.stdout,'html.parser');rows=[]
  for tr in soup.select('table tr'):
   cols=[a.get_text(' ',strip=True) for a in tr.select('td')]
   if cols:rows.append(cols)
  r['rows']=rows
  if not rows:r['error']='no readable history table'
 except Exception as e:r['error']=str(e)
 return r
with ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(lambda kv:one(*kv),urls.items()))
(P/'overseas_history.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
for x in out:print(x['ticker'],len(x.get('rows',[])),x.get('rows',[None])[:2],x.get('error'))
