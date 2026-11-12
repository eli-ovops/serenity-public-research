"""Reproducible preliminary eight-condition audit; unknowns retained explicitly."""
import json, csv, statistics
from pathlib import Path
from datetime import date, timedelta
P=Path(__file__).resolve().parent
POOL=json.loads((P/'SCOPE.json').read_text())['universe']
INLINE=json.loads((P/'inline_facts.json').read_text()) if (P/'inline_facts.json').exists() else {}
MANUAL=json.loads((P/'manual_financial.json').read_text()) if (P/'manual_financial.json').exists() else {}
OVERSEAS=json.loads((P/'overseas_metrics.json').read_text()) if (P/'overseas_metrics.json').exists() else {}

def day(s):return date.fromisoformat(s)
def series(d,candidates,instant=False):
 allp=[]
 for ns,k in candidates:
  fact=d.get('facts',{}).get(ns,{}).get(k)
  if not fact:continue
  units=fact['units']; currency=next((u for u in ['USD','TWD','KRW','EUR','GBP','CNY','SEK','HKD'] if u in units),None)
  if not currency:continue
  points=[{**x,'tag':ns+':'+k,'currency':currency} for x in units[currency] if x.get('filed','')<='2026-10-06' and x.get('end','')<='2026-10-06' and (instant or x.get('start'))]
  allp.extend(points)
 # Preferred tag wins only when available for that same period; latest filing within that tag wins.
 rank={ns+':'+k:i for i,(ns,k) in enumerate(candidates)}
 unique={}
 for x in sorted(allp,key=lambda x:(-rank[x['tag']],x.get('filed',''))):unique[(x.get('start'),x['end'])]=x
 return list(unique.values())

def durations(points,lo,hi):return sorted([x for x in points if lo<=(day(x['end'])-day(x['start'])).days+1<=hi],key=lambda x:x['end'])
def quarter_series(points):
 out=durations(points,70,110)
 for x in durations(points,160,380):
  n=(day(x['end'])-day(x['start'])).days+1
  if n<220:target=90
  elif n<310:target=180
  else:target=270
  prior=[p for p in points if p['start']==x['start'] and abs((day(p['end'])-day(p['start'])).days+1-target)<20 and p['end']<x['end']]
  if not prior:continue
  prev=max(prior,key=lambda z:z['end']);start=(day(prev['end'])+timedelta(days=1)).isoformat()
  if not 70<=(day(x['end'])-day(start)).days+1<=110:continue
  if not any(abs((day(p['end'])-day(x['end'])).days)<5 for p in out):out.append({**x,'start':start,'val':x['val']-prev['val'],'derived':'YTD/annual minus prior cumulative','components':[x,prev]})
 return sorted(out,key=lambda x:x['end'])

REV=[('us-gaap','RevenueFromContractWithCustomerExcludingAssessedTax'),('us-gaap','RevenueFromContractWithCustomerIncludingAssessedTax'),('us-gaap','Revenues'),('us-gaap','SalesRevenueNet'),('us-gaap','SalesRevenueGoodsNet'),('ifrs-full','Revenue'),('ifrs-full','RevenueFromContractsWithCustomers')]
NI=[('us-gaap','NetIncomeLoss'),('ifrs-full','ProfitLossAttributableToOwnersOfParent'),('us-gaap','NetIncomeLossAvailableToCommonStockholdersBasic'),('us-gaap','ProfitLoss'),('ifrs-full','ProfitLoss')]
EQ=[('us-gaap','StockholdersEquity'),('ifrs-full','EquityAttributableToOwnersOfParent'),('us-gaap','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'),('ifrs-full','Equity')]

def match(points,end,days,tolerance):
 a=[x for x in points if abs((day(end)-day(x['end'])).days-days)<=tolerance]
 return min(a,key=lambda x:abs((day(end)-day(x['end'])).days-days)) if a else None
def growth(a,b):return a/b-1 if b>0 else None
def state(x,threshold):return 'UNKNOWN' if x is None else ('PASS' if x>threshold else 'FAIL')

def financial(t):
 f=P/'facts'/(t+'.json')
 if not f.exists():return {'financial_status':'no current SEC facts; manual review needed'}
 d=json.loads(f.read_text())
 for ns,ff in INLINE.get(t,{}).get('facts',{}).items():
  for k,fact in ff.items():
   target=d['facts'].setdefault(ns,{}).setdefault(k,{'units':{}})
   for u,points in fact['units'].items():target['units'].setdefault(u,[]).extend(points)
 rev=series(d,REV);ni=series(d,NI);eq=series(d,EQ,True)
 minority=series(d,[('us-gaap','MinorityInterest'),('ifrs-full','NoncontrollingInterests')],True)
 for e in eq:
  if e['tag'].endswith('IncludingPortionAttributableToNoncontrollingInterest') or e['tag']=='ifrs-full:Equity':
   m=match(minority,e['end'],0,0)
   if m:e['val']-=m['val'];e['minority_subtraction']=m['val']
 rq=quarter_series(rev);nq=quarter_series(ni)
 ans={'entity':d.get('entityName'),'revenue_quarters':rq[-9:],'net_income_quarters':nq[-9:],'annual_net_income':durations(ni,350,380)[-6:]}
 if rq:
  r=rq[-1];p=match(rq,r['end'],365,18);ans.update(revenue_period=r['end'],revenue=r['val'],revenue_yoy=growth(r['val'],p['val']) if p else None,revenue_prior_year=p)
 if nq:
  n=nq[-1];py=match(nq,n['end'],365,18);pq=match(nq,n['end'],91,20)
  ans.update(ni_period=n['end'],net_income=n['val'],ni_yoy=growth(n['val'],py['val']) if py else None,ni_qoq=growth(n['val'],pq['val']) if pq else None,ni_qoq_amount=n['val']-pq['val'] if pq else None,ni_prior_year=py,ni_prior_quarter=pq)
  # 4 adjacent quarters; do not sum overlapping annual/YTD values.
  qs=[n];cursor=n
  for _ in range(3):
   q=match(nq,cursor['end'],91,20)
   if q is None:break
   qs.append(q);cursor=q
  if len(qs)==4 and 330<=(day(n['end'])-day(qs[-1]['start'])).days+1<=390:
   ttm=sum(q['val'] for q in qs);e=match(eq,n['end'],0,7);e0=match(eq,n['end'],365,18)
   ans.update(ttm_net_income=ttm,roe_end_equity=e,roe_start_equity=e0,roe=ttm/((e['val']+e0['val'])/2) if e and e0 and min(e['val'],e0['val'])>0 else None)
 annual=durations(ni,350,380)
 if annual:
  a=annual[-1];old=match(annual,a['end'],1095,25)
  ans.update(cagr_latest=a,cagr_base=old,cagr=(a['val']/old['val'])**(1/3)-1 if old and min(a['val'],old['val'])>0 else None)
 # Quarterly foreign filings often not tagged. An annual observation is not current quarter.
 if not rq or not nq or min(ans.get('revenue_period','0000'),ans.get('ni_period','0000'))<'2026-04-01':ans['financial_status']='latest quarter requires primary report supplementation'
 return ans

def main():
 coll={x['ticker']:x for x in json.loads((P/'collection.json').read_text())};out=[]
 for t in POOL:
  f=financial(t);m=MANUAL.get(t,{})
  if m.get('ni_period') and m['ni_period']!=f.get('ni_period'):
   f['roe']=None;f['ttm_net_income']=None
  f.update(m)
  r={'ticker':t,'financial':f,'tests':{},'gaps':[]};tests=r['tests'];h=OVERSEAS.get(t,coll.get(t,{}).get('history',{}))
  tests['1_listing_age']='UNKNOWN';tests['1_ST']='N/A_NON_A_SHARE';tests['8_code']='N/A_NON_A_SHARE'
  if h.get('bars',0)>=250:tests['1_listing_age']='PASS_HISTORY_OLDER_THAN_YEAR'
  if t in OVERSEAS:tests['1_listing_age']='PASS_LONG_ESTABLISHED_LISTING'
  if t in ['DPC','SCTX','SKHY']:tests['1_listing_age']='FAIL_LISTED_SERIES_UNDER_YEAR'
  tests['2_revenue_yoy']=state(f.get('revenue_yoy'),.25)
  tests['3_ni_yoy']=state(f.get('ni_yoy'),.30)
  if (f.get('ni_prior_year') or {}).get('val',1)<=0 and (f.get('net_income') or 0)>0:tests['3_ni_yoy']='UNDEFINED_NONPOSITIVE_BASE'
  tests['3_ni_qoq']='UNKNOWN' if f.get('ni_qoq') is None else ('PASS' if f['ni_qoq']>0 and f.get('net_income',0)>0 else 'FAIL')
  tests['6_ROE']=state(f.get('roe'),.15);tests['7_CAGR']=state(f.get('cagr'),.20)
  if f.get('cagr_base') and f['cagr_base']['val']<=0:tests['7_CAGR']='UNDEFINED_NONPOSITIVE_BASE'
  if (f.get('cagr_latest') or {}).get('val',1)<=0:tests['7_CAGR']='FAIL_NONPOSITIVE_LATEST_YEAR'
  if t=='IQE':tests['7_CAGR']='FAIL_NONPOSITIVE_LATEST_YEAR'
  if f.get('net_income') is not None and f['net_income']<=0:tests['3_ni_yoy']='FAIL_LOSS';tests['3_ni_qoq']='FAIL_LOSS'
  if h.get('sma50') is not None and h.get('sma150') is not None:tests['4_MA']='PASS' if h['close']>max(h['sma50'],h['sma150']) else 'FAIL'
  else:tests['4_MA']='UNKNOWN'
  if h.get('vol10') is not None and h.get('vol120') is not None:tests['5_volume']='PASS' if h['vol10']>h['vol120'] else 'FAIL'
  else:tests['5_volume']='UNKNOWN'
  r['technical']={k:v for k,v in h.items() if k!='rows'}
  r['failed']=[k for k,v in tests.items() if v.startswith('FAIL') or v.startswith('UNDEFINED')]
  r['unknown']=[k for k,v in tests.items() if v=='UNKNOWN']
  r['status']='STRICT_FAIL' if r['failed'] else ('UNFINISHED' if r['unknown'] else 'STRICT_PASS')
  out.append(r)
 (P/'audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
 with (P/'AUDIT.csv').open('w') as fp:
  fields=['ticker','status','revenue_period','ni_period','revenue_yoy','ni_yoy','ni_qoq','roe','cagr','close','sma50','sma150','vol10','vol120','failed','unknown'];w=csv.DictWriter(fp,fieldnames=fields);w.writeheader()
  for r in out:w.writerow({'ticker':r['ticker'],'status':r['status'],**{k:r['financial'].get(k) for k in fields[2:9]},**{k:r['technical'].get(k) for k in fields[9:14]},'failed':';'.join(r['failed']),'unknown':';'.join(r['unknown'])})
 for r in out:
  f=r['financial'];h=r['technical'];print(r['ticker'],'period',f.get('revenue_period'),f.get('ni_period'),'growth',*[round(f[k]*100,2) if f.get(k) is not None else None for k in ['revenue_yoy','ni_yoy','ni_qoq','roe','cagr']],'MA',r['tests']['4_MA'],'VOL',r['tests']['5_volume'],'FAIL',','.join(r['failed']))
 print('NO KNOWN FAIL',[r['ticker'] for r in out if not r['failed']])
if __name__=='__main__':main()
