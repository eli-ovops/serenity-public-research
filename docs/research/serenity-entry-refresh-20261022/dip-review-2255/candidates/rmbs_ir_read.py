import urllib.request,pathlib,datetime,json,hashlib,concurrent.futures,re,html
P=pathlib.Path('docs/research/serenity-entry-refresh-20261022/dip-review-2255/candidates')
def get(z):
 k,u=z;v={'url':u,'started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(u,timeout=15) as r:b=r.read();v['status']=r.status
  (P/(k+'.html')).write_bytes(b);v['sha256']=hashlib.sha256(b).hexdigest();v['bytes']=len(b);t=html.unescape(re.sub('<[^>]+>',' ',b.decode(errors='replace')));t=re.sub(r'\s+',' ',t);(P/(k+'.txt')).write_text(t);print(k,t[-17000:])
 except Exception as e:v['error']=str(e);v['status']=getattr(e,'code',None);print(k,v)
 v['finished']=datetime.datetime.now(datetime.timezone.utc).isoformat();(P/(k+'.receipt.json')).write_text(json.dumps(v,indent=2))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:list(e.map(get,[('RMBS_IR_NEWS','https://investor.rambus.com/press-releases/default.aspx'),('RMBS_IR_EVENTS','https://investor.rambus.com/events-and-presentations/default.aspx')]))

