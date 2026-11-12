import json,subprocess,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
baseline=json.load(open(P.parent/'serenity-full-20260930/public_snapshot.json'))['sec']
def get(x):
 t,b=x;u=f"https://data.sec.gov/submissions/CIK{b['cik']:010d}.json";r=subprocess.run(['curl','-sS','--fail','--max-time','12','-A','Serenity public research [REDACTED_EMAIL]',u],capture_output=True,timeout=14);z={'ticker':t,'source':u,'window':'Oct8 after prior intraday cutoff; date-level conservatively includes wholeOct8','retrieved_utc':datetime.now(timezone.utc).isoformat(),'ok':False}
 if not r.returncode:
  d=json.loads(r.stdout);f=d['filings']['recent'];z.update(ok=True,new_filings=[{'date':dt,'form':f['form'][i],'url':f"https://www.sec.gov/Archives/edgar/data/{int(d['cik'])}/{f['accessionNumber'][i].replace('-','')}/{f['primaryDocument'][i]}"} for i,dt in enumerate(f['filingDate']) if dt=='2026-10-08'])
 else:z['error']=r.stderr.decode()[:90]
 (P/('sec_bridge_'+t+'.json')).write_text(json.dumps(z,indent=2));return z
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:out=list(e.map(get,[(t,b) for t,b in baseline.items() if b.get('cik')]))
print(json.dumps([{'ticker':z['ticker'],'material':[f for f in z.get('new_filings',[]) if f['form'] not in ['4','3','5','144']]} for z in out if any(f['form'] not in ['4','3','5','144'] for f in z.get('new_filings',[]))]))
