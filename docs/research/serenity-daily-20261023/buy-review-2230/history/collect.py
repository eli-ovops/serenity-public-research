from pathlib import Path
import urllib.request,json,hashlib,datetime,concurrent.futures
p=Path(__file__).resolve().parent
jobs=[('HPE','https://stockanalysis.com/stocks/hpe/history/'),('QQQ','https://stockanalysis.com/etf/qqq/history/'),('SOXX','https://stockanalysis.com/etf/soxx/history/')]
def one(j):
 s,url=j;r={'symbol':s,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=16)as x:data=x.read(8*1024*1024);r.update(http=x.status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest());(p/(s+'.html')).write_bytes(data)
 except Exception as e:r['error']=str(e)
 (p/(s+'.receipt.json')).write_text(json.dumps(r,indent=2));return r
with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:print(json.dumps(list(pool.map(one,jobs))))
