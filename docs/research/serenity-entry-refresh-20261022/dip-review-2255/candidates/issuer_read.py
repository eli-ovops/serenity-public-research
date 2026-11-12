import urllib.request,pathlib,datetime,json,concurrent.futures,re,html
P=pathlib.Path('docs/research/serenity-entry-refresh-20261022/dip-review-2255/candidates')
jobs=[('RMBS_NEWS','https://www.rambus.com/newsroom/'),('RMBS_EVENT','https://investor.rambus.com/press-releases/press-release-details/2026/Rambus-to-Announce-Third-Quarter-Fiscal-Year-2026-Results/default.aspx'),('ANET_HOME','https://investors.arista.com/Home/default.aspx')]
def get(j):
 k,u=j;v={'url':u,'started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(u,timeout=15) as r:b=r.read();v['status']=r.status
  (P/(k+'.html')).write_bytes(b);t=html.unescape(re.sub('<[^>]+>',' ',b.decode(errors='replace')));t=re.sub(r'\s+',' ',t);(P/(k+'.txt')).write_text(t);v['bytes']=len(b);print(k,t[-18000:])
 except Exception as e:v['error']=str(e);v['status']=getattr(e,'code',None);print(k,v)
 v['finished']=datetime.datetime.now(datetime.timezone.utc).isoformat();(P/(k+'.receipt.json')).write_text(json.dumps(v,indent=2))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:list(e.map(get,jobs))

