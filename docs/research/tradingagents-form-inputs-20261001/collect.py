import json,urllib.request,csv,io
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parent
urls={'sec':'https://data.sec.gov/submissions/CIK0001039399.json','ir_news':'https://investors.formfactor.com/press-releases','ir_events':'https://investors.formfactor.com/events-and-presentations','earnings':'https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2026-second-quarter-results','vix':'https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv'}
for t in ['FORM','QQQ','SOXX','RSP']:
 urls[t]=f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass={"stocks" if t=="FORM" else "etf"}&fromdate=2026-05-01&todate=2026-09-30&limit=5000'
def fetch(pair):
 name,url=pair;row={'source':url,'retrieved_utc':datetime.now(timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 Serenity public research [REDACTED_EMAIL]'})
  with urllib.request.urlopen(req,timeout=20) as res:data=res.read().decode()
  if name in ['ir_news','ir_events','earnings']:
   soup=BeautifulSoup(data,'html.parser')
   for e in soup(['script','style']):e.decompose()
   row['text']=soup.get_text(' ',strip=True)
  elif name=='vix':row['rows']=list(csv.DictReader(io.StringIO(data)))[-110:]
  elif name=='sec':
   d=json.loads(data);f=d['filings']['recent'];row['name']=d['name'];row['filings']=[{k:f[k][i] for k in ['filingDate','form','accessionNumber','primaryDocument']} for i in range(len(f['filingDate'])) if f['filingDate'][i]>='2026-09-01']
  else:row['data']=json.loads(data)
  row['ok']=True
 except Exception as e:row.update(ok=False,error_type=type(e).__name__)
 (R/(name+'.json')).write_text(json.dumps(row,ensure_ascii=False,indent=2))
 return name,row['ok']
with ThreadPoolExecutor(max_workers=4) as ex:
 for result in ex.map(fetch,urls.items()):print(result,flush=True)
