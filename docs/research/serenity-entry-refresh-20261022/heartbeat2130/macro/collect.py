import urllib.request,json,pathlib,datetime,concurrent.futures,urllib.parse
P=pathlib.Path('docs/research/serenity-entry-refresh-20261022/heartbeat2130/macro')
def get(s):
 u='https://query1.finance.yahoo.com/v8/finance/chart/'+urllib.parse.quote(s,safe='')+'?range=5d&interval=1m&includePrePost=false';a=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(u,timeout=15) as r:b=r.read();status=r.status
  name=s.replace('^','');(P/(name+'.json')).write_bytes(b);d=json.loads(b)['chart']['result'][0];m=d['meta'];ts=d.get('timestamp',[]);q=d['indicators']['quote'][0];today=[i for i,t in enumerate(ts) if datetime.datetime.fromtimestamp(t,datetime.timezone.utc).date().isoformat()=='2026-10-22'];rows=[{'utc':datetime.datetime.fromtimestamp(ts[i],datetime.timezone.utc).isoformat(),'open':q['open'][i],'high':q['high'][i],'low':q['low'][i],'close':q['close'][i]} for i in today if q['close'][i] is not None];v={'symbol':s,'url':u,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'http':status,'meta':m,'today_samples':rows};(P/(name+'_SUMMARY.json')).write_text(json.dumps(v,indent=2));return {'s':s,'price':m.get('regularMarketPrice'),'time':m.get('regularMarketTime'),'prev':m.get('chartPreviousClose'),'last':rows[-1:]}
 except Exception as e:
  v={'symbol':s,'url':u,'started_at':a,'error':str(e)};(P/(s.replace('^','')+'_ERROR.json')).write_text(json.dumps(v));return v
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 for r in ex.map(get,['QQQ','SPY','RSP','SOXX','XBI','XLV','^VIX']):print(json.dumps(r))

