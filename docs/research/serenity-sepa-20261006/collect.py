"""Finite public financial-data collection for the frozen 74-name criteria audit."""
import json, subprocess, statistics, csv
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

OUT=Path(__file__).resolve().parent
BASE=OUT.parent/'serenity-full-20260930'
B=json.loads((BASE/'public_snapshot.json').read_text())
POOL=B['universe']; NOW=datetime.now(timezone.utc).isoformat()
ALIASES={'SOI':'SOI.PA','IQE':'IQE.L','SIVE':'SIVE.ST','ESMT':'3006.TW','ASMPT':'0522.HK','Lenovo':'0992.HK'}
for folder in ['facts','submissions','history','reports']:(OUT/folder).mkdir(exist_ok=True)
(OUT/'SCOPE.json').write_text(json.dumps({'universe':POOL,'count':len(POOL),'frozen_utc':NOW,'owner':'current_thread_direct','cutoff_date':'2026-10-06','history_completed_through':'2026-10-05','completion':'all 8 original conditions per company; primary financial statements, trailing annual history, 150 trading-day prices and 120 volumes; UNKNOWN never counts as pass','ROE':'TTM attributable net income / average attributable equity at TTM start and end; positive equity required','CAGR':'latest completed fiscal year versus three fiscal years earlier; positive endpoints required','NI':'GAAP/IFRS attributable net income; adjusted income shown separately; quarterly not YTD','A_share_rules':'ST and 30/00 code exclusions only apply to actual A-share listing, not arbitrary foreign ticker prefixes','vcp':'not established by these 8 conditions; separate unperformed pattern test'},ensure_ascii=False,indent=2))

def fetch(url,path,ua='Serenity public financial research [REDACTED_EMAIL]',timeout=18):
 p=subprocess.run(['curl','--silent','--show-error','--fail','--max-time',str(timeout),'-A',ua,url],capture_output=True,timeout=timeout+3)
 if p.returncode:raise RuntimeError(p.stderr.decode()[:180])
 d=json.loads(p.stdout);path.write_bytes(p.stdout);return d

def company(t):
 r={'ticker':t,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'errors':[]}
 sec=B['sec'].get(t,{})
 if sec.get('cik'):
  cik=sec['cik'];r['cik']=cik
  for k,url in [('facts',f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json'),('submissions',f'https://data.sec.gov/submissions/CIK{cik:010d}.json')]:
   try:
    d=fetch(url,OUT/k/(t+'.json'));r[k]={'ok':True,'source':url}
    if k=='submissions':
     r['name']=d.get('name');recent=d['filings']['recent'];r['financial_filings']=[];r['new_material_filings']=[]
     for i,form in enumerate(recent['form']):
      date=recent['filingDate'][i]
      if date>'2026-10-06':continue
      item={'date':date,'form':form,'report_date':recent.get('reportDate',['']*len(recent['form']))[i],'url':f"https://www.sec.gov/Archives/edgar/data/{cik}/{recent['accessionNumber'][i].replace('-','')}/{recent['primaryDocument'][i]}"}
      if form in ['10-Q','10-K','20-F','40-F','6-K'] and len(r['financial_filings'])<8:r['financial_filings'].append(item)
      if date>='2026-09-30' and form in ['8-K','6-K','10-Q','10-K','20-F','S-1','F-1']:r['new_material_filings'].append(item)
   except Exception as e:r['errors'].append(k+': '+str(e))
 else:r['facts']={'ok':False,'reason':'non SEC issuer'}
 # Known Nasdaq path supplies a completed-session full daily history.
 if t not in ALIASES:
  url=f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate=2025-01-01&todate=2026-10-05&limit=5000'
  try:
   d=fetch(url,OUT/'history'/(t+'.json'),'Mozilla/5.0',18)
   rows=((d.get('data') or {}).get('tradesTable') or {}).get('rows') or []
   def num(x):return float(str(x).replace('$','').replace(',',''))
   rows=[{'date':datetime.strptime(x['date'],'%m/%d/%Y').date().isoformat(),**{k:num(x[k]) for k in ['open','high','low','close','volume']}} for x in rows]
   rows=sorted([x for x in rows if x['date']<='2026-10-05'],key=lambda x:x['date'])
   if not rows:raise ValueError('no completed rows')
   m={'source':url,'last_date':rows[-1]['date'],'close':rows[-1]['close'],'bars':len(rows),'rows':rows,'basis':'unadjusted Nasdaq; splits must be checked before pass'}
   for n in [50,150,200]:m['sma'+str(n)]=statistics.mean(x['close'] for x in rows[-n:]) if len(rows)>=n else None
   for n in [10,120]:m['vol'+str(n)]=statistics.mean(x['volume'] for x in rows[-n:]) if len(rows)>=n else None
   r['history']=m
  except Exception as e:r['errors'].append('history: '+str(e))
 else:r['history']={'status':'overseas manual source pending','symbol':ALIASES[t]}
 return r

if __name__=='__main__':
 results=[]
 with ThreadPoolExecutor(max_workers=4) as pool:
  for f in as_completed([pool.submit(company,t) for t in POOL]):
   r=f.result();results.append(r);(OUT/'collection.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
   print(r['ticker'], 'facts='+str(r.get('facts',{}).get('ok')), 'bars='+str(r.get('history',{}).get('bars',0)), 'errors='+str(len(r['errors'])),flush=True)
 print('FINISHED',len(results),flush=True)
