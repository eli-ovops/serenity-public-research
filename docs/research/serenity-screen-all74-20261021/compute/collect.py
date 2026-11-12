import json, urllib.request, hashlib, concurrent.futures, datetime
from pathlib import Path
from html.parser import HTMLParser
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[3]
class Text(HTMLParser):
 def __init__(self): super().__init__();self.text=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'): self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'): self.skip=max(0,self.skip-1)
  if t in ('p','div','tr','h1','h2','h3'): self.text.append('\n')
 def handle_data(self,d):
  if not self.skip:self.text.append(d.strip()+' ')
def one(j):
 ident,url=j;rec={'id':ident,'url':url,'asof':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'SerenityResearch/1.1 public-market review','Accept':'application/json,text/html,*/*'})
  with urllib.request.urlopen(req,timeout=20) as r: data=r.read(12000000);rec['http']=r.status
  (BASE/'sources').mkdir(exist_ok=True);p=BASE/'sources'/(ident+'.raw');p.write_bytes(data);rec.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  if data[:1] in (b'{',b'['):
   d=json.loads(data)
   if 'facts' in d:
    selected={}
    wanted=['Revenue','SalesRevenue','NetIncome','ProfitLoss','CashAndCash','ShortTermInvest','LongTermDebt','DebtCurrent','StockBasedCompensation','ShareBasedCompensation','CommonStockSharesOutstanding','WeightedAverageNumberOfDilutedShares','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','Assets','Liabilities']
    for ns, facts in d['facts'].items():
     for k,v in facts.items():
      if any(w in k for w in wanted):
       units={u:[x for x in vals if x.get('filed','')>='2026-07-01' and x.get('end','')>='2026-01-01'][-8:] for u,vals in v.get('units',{}).items()}
       if any(units.values()): selected[ns+':'+k]=units
    (BASE/'sources'/(ident+'.selected.json')).write_text(json.dumps(selected,ensure_ascii=False,indent=2))
  else:
   parser=Text();parser.feed(data.decode(errors='replace'));(BASE/'sources'/(ident+'.txt')).write_text(''.join(parser.text))
 except Exception as e:rec['error']=str(e)
 return rec
if __name__=='__main__':
 jobs=json.loads((BASE/'jobs.json').read_text())
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:results=list(ex.map(one,jobs))
 (BASE/'receipts.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(json.dumps(results))
