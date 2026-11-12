"""One bounded public SEC companyfacts request per known issuer; no retries."""
from pathlib import Path
import json,urllib.request,subprocess
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor,as_completed
P=Path(__file__).resolve().parent
D=json.loads((P/'public_snapshot.json').read_text())
KEYS=['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet','NetIncomeLoss','NetIncomeLossAvailableToCommonStockholdersBasic','OperatingIncomeLoss','GrossProfit','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','CashAndCashEquivalentsAtCarryingValue','ShortTermInvestments','LongTermDebtCurrent','LongTermDebtNoncurrent','LongTermDebt','StockBasedCompensation','WeightedAverageNumberOfDilutedSharesOutstanding','EarningsPerShareDiluted','CommonStockSharesOutstanding','EntityCommonStockSharesOutstanding','ProfitLoss','Revenue','CashFlowsFromUsedInOperatingActivities']
def one(t,x):
 u=f"https://data.sec.gov/api/xbrl/companyfacts/CIK{x['cik']:010d}.json";r={'ticker':t,'source':u,'at':datetime.now(timezone.utc).isoformat()}
 try:
  z=subprocess.run(['curl','--silent','--show-error','--fail','--max-time','18','-A','Serenity public research [REDACTED_EMAIL]',u],capture_output=True,timeout=21)
  if z.returncode:raise RuntimeError('curl '+str(z.returncode)+' '+z.stderr.decode()[:180])
  d=json.loads(z.stdout);r['facts']={}
  for ns,ff in d['facts'].items():
   for k,f in ff.items():
    if k not in KEYS:continue
    units={}
    for un,vs in f['units'].items():
     a=[v for v in vs if v.get('end','')>='2025-07-01' and v.get('filed','')<='2026-09-30']
     uniq={}
     for v in sorted(a,key=lambda v:v.get('filed','')):uniq[(v.get('start'),v['end'])]=v
     units[un]=list(uniq.values())[-8:]
    r['facts'][ns+':'+k]=units
  r['ok']=True
 except Exception as e:r.update(ok=False,error=str(e))
 return r
out=[]
with ThreadPoolExecutor(max_workers=4) as pool:
 for f in as_completed([pool.submit(one,t,x) for t,x in D['sec'].items() if 'cik' in x]):
  out.append(f.result());(P/'companyfacts.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
  if len(out)%16==0:print(len(out),sum(x['ok'] for x in out),flush=True)
print('DONE',len(out),sum(x['ok'] for x in out),flush=True)
