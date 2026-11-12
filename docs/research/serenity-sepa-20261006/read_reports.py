"""Retrieve full latest SEC statements and index existing issuer source texts."""
import json,subprocess,re
from pathlib import Path
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
P=Path(__file__).resolve().parent;BASE=P.parent/'serenity-full-20260930'
class Reader(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
  if t in ['p','div','tr','table','h1','h2','h3','li']:self.text.append('\n')
  elif t in ['td','th']:self.text.append(' | ')
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip:self.text.append(s)
def one(r):
 t=r['ticker'];out={'ticker':t,'sources':[],'retrieved_utc':datetime.now(timezone.utc).isoformat()}
 idx=json.load(open(BASE/'source_index.json')).get(t,[])
 for s in idx:
  path=BASE/s.get('path','')
  if s.get('path','').startswith('primary/') and path.is_file():out['sources'].append({**s,'path':str(path.resolve()),'characters':len(path.read_text())})
 filings=list(r.get('financial_filings',[]))
 sf=P/'submissions'/(t+'.json')
 if sf.exists():
  full=json.loads(sf.read_text());recent=full['filings']['recent'];cik=int(full['cik'])
  for i,form in enumerate(recent['form']):
   if form in ['10-K','20-F','40-F']:
    u=f"https://www.sec.gov/Archives/edgar/data/{cik}/{recent['accessionNumber'][i].replace('-','')}/{recent['primaryDocument'][i]}"
    if not any(x['url']==u for x in filings):filings.append({'date':recent['filingDate'][i],'report_date':recent['reportDate'][i],'form':form,'url':u})
    break
  ann=[i for i,f in enumerate(recent['form']) if f in ['10-K','20-F','40-F'] and recent['reportDate'][i]]
  if ann:
   year=int(recent['reportDate'][ann[0]][:4])-3
   base=next((i for i in ann if int(recent['reportDate'][i][:4])==year),None)
   if base is not None:
    u=f"https://www.sec.gov/Archives/edgar/data/{cik}/{recent['accessionNumber'][base].replace('-','')}/{recent['primaryDocument'][base]}"
    filings.append({'date':recent['filingDate'][base],'report_date':recent['reportDate'][base],'form':recent['form'][base]+'_BASE','url':u})
 # Read current quarter and latest annual, each original full document.
 chosen=[]
 for forms in [('10-Q',),('10-K','20-F','40-F')]:
  f=next((f for f in filings if f['form'] in forms),None)
  if f and f not in chosen:chosen.append(f)
 chosen.extend(f for f in filings if f['form'].endswith('_BASE'))
 for f in chosen:
  path=P/'reports'/(t+'_'+f['form']+'.html')
  if not path.exists():
   z=subprocess.run(['curl','--silent','--show-error','--fail','--max-time','18','-A','Serenity public financial research [REDACTED_EMAIL]',f['url']],capture_output=True,timeout=21)
   if z.returncode:out['sources'].append({**f,'error':z.stderr.decode()[:120]});continue
   path.write_bytes(z.stdout)
  reader=Reader();reader.feed(path.read_text(errors='replace'));txt=''.join(reader.text);txt=re.sub(r'[ \t]+',' ',txt);txt=re.sub(r'\n\s*\n','\n',txt)
  dest=path.with_suffix('.txt');dest.write_text(txt);out['sources'].append({**f,'path':str(dest.resolve()),'characters':len(txt),'complete_download':True})
  # Financial statements and discussion retained, including all text; compact snippets for review.
 out['complete_text_sources']=sum(1 for s in out['sources'] if s.get('characters',0)>1000)
 return out
if __name__=='__main__':
 out=[];rows=json.load(open(P/'collection.json'))
 with ThreadPoolExecutor(max_workers=4) as pool:
  for f in as_completed([pool.submit(one,r) for r in rows]):
   r=f.result();out.append(r);(P/'report_index.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(r['ticker'],r['complete_text_sources'],flush=True)
 print('DONE',len(out),flush=True)
