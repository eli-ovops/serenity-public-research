import json,urllib.request,statistics,re
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,urljoin
R=Path(__file__).resolve().parent;P=R.parent/'serenity-full-20260930'
old=json.loads((P/'public_snapshot.json').read_text());universe=json.loads((P/'SCOPE.json').read_text())['universe']
now=lambda:datetime.now(timezone.utc).isoformat()
(R/'SCOPE.json').write_text(json.dumps({'universe':universe,'frozen_utc':now(),'owner':'current thread','scope':'all-pool incremental daily check; not full fundamental re-underwrite','required':'price/trend, company disclosure and financial changes separately counted; deep review priority holdings/candidates/material events'},indent=2))
symbols={'SOI':'SOI.PA','IQE':'IQE.L','ESMT':'3006.TW','SIVE':'SIVE.ST','ASMPT':'0522.HK','Lenovo':'0992.HK'}
roots={}
for x in json.loads((P/'ir_status.json').read_text()):
 if x.get('documents'):roots[x['ticker']]=x['documents'][0]['source']
for x in json.loads((P/'primary_manifest.json').read_text()):
 h=urlsplit(x['url']).netloc
 if h and 'sec.gov' not in h and 'amgen' not in h:roots.setdefault(x['ticker'],'https://'+h+'/')
roots.update({'INOD':'https://investor.innodata.com/news-releases/','FORM':'https://investors.formfactor.com/press-releases','NVDA':'https://nvidianews.nvidia.com/news','CLS':'https://corporate.celestica.com/news-releases','POET':'https://poet-technologies.com/news.html','AAON':'https://investors.aaon.com/news-events/press-releases','MU':'https://investors.micron.com/news/default.aspx','HPE':'https://investors.hpe.com/news-and-events','CCXI':'https://churchillcapital-11.com/','SIVE':'https://www.sivers-semiconductors.com/press/','IQE':'https://www.iqep.com/media/press-releases/','ESMT':'https://www.esmt.com.tw/tw/press-room','SOI':'https://www.soitec.com/home/group/corporate/newsroom/press-releases','Lenovo':'https://investor.lenovo.com/en/ir/announcements.php'})
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 public financial research [REDACTED_EMAIL]'})
 with urllib.request.urlopen(req,timeout=12) as z:return z.read().decode()
def one(kind,t,url):
 row={'ticker':t,'kind':kind,'source':url,'retrieved_utc':now()}
 try:
  raw=get(url)
  if kind=='price':
   z=json.loads(raw)['chart']['result'][0];row['meta']=z['meta'];q=z['indicators']['quote'][0];rows=[]
   for i,ts in enumerate(z['timestamp']):
    if any(q[k][i] is None for k in ['close','open','high','low','volume']):continue
    rows.append({'date':datetime.fromtimestamp(ts,timezone.utc).date().isoformat(),**{k:q[k][i] for k in ['close','open','high','low','volume']}})
   row['rows']=rows;closed=[x for x in rows if x['date']<='2026-10-01'];c=[x['close'] for x in closed]
   row['completed_metrics']={'last_date':closed[-1]['date'],'close':c[-1],'sma20':statistics.mean(c[-20:]),'sma50':statistics.mean(c[-50:]) if len(c)>=50 else None,**{f'return_{n}':c[-1]/c[-n-1]-1 if len(c)>n else None for n in [1,5,20,60]},'volume_over_prior20':closed[-1]['volume']/statistics.mean(x['volume'] for x in closed[-21:-1]) if len(closed)>20 and statistics.mean(x['volume'] for x in closed[-21:-1]) else None}
  elif kind=='sec':
   z=json.loads(raw);f=z['filings']['recent'];cik=int(z['cik']);row['name']=z['name'];row['new_filings']=[{'date':f['filingDate'][i],'form':f['form'][i],'url':f"https://www.sec.gov/Archives/edgar/data/{cik}/{f['accessionNumber'][i].replace('-','')}/{f['primaryDocument'][i]}"} for i in range(len(f['filingDate'])) if f['filingDate'][i]>='2026-09-30']
  else:
   soup=BeautifulSoup(raw,'html.parser');row['links']=[{'title':a.get_text(' ',strip=True),'url':urljoin(url,a['href'])} for a in soup.find_all('a',href=True) if re.search(r'2026|results|earnings|guidance|financ|announc|conference|quarter|investor|acquis|order|contract',a.get_text(' ',strip=True),re.I)]
   for e in soup(['script','style','nav','footer']):e.decompose()
   row['text']=soup.get_text(' ',strip=True);row['semantic_review']='not yet reviewed; fetch does not mean current events verified'
  row['ok']=True
 except Exception as e:row.update(ok=False,error_type=type(e).__name__)
 (R/f'{kind}_{t}.json').write_text(json.dumps(row,ensure_ascii=False,indent=2));return row
jobs=[]
for t in universe+['QQQ','SOXX','RSP','^VIX']:
 jobs.append(('price',t,f'https://query1.finance.yahoo.com/v8/finance/chart/{symbols.get(t,t)}?range=6mo&interval=1d'))
for t in universe:
 if old['sec'].get(t,{}).get('cik'):jobs.append(('sec',t,old['sec'][t]['source']))
 if roots.get(t):jobs.append(('ir',t,roots[t]))
out=[]
with ThreadPoolExecutor(max_workers=6) as ex:
 for f in as_completed([ex.submit(one,*j) for j in jobs]):
  x=f.result();out.append({k:v for k,v in x.items() if k in ['ticker','kind','ok','error_type','source']})
  if len(out)%30==0:print('collected',len(out),'of',len(jobs),'ok',sum(x['ok'] for x in out),flush=True)
(R/'manifest.json').write_text(json.dumps(out,indent=2));print('DONE',len(out),flush=True)
