import urllib.request,json,datetime,pathlib,hashlib,concurrent.futures,re
BASE=pathlib.Path(__file__).parent

def get(j):
 p=BASE/'public'/j['id'];r=dict(j,asof=datetime.datetime.now(datetime.timezone.utc).isoformat())
 if p.with_suffix('.receipt.json').exists():return json.loads(p.with_suffix('.receipt.json').read_text())
 try:
  with urllib.request.urlopen(urllib.request.Request(j['url'],headers={'User-Agent':'SerenityResearch/1.1 public-market review'}),timeout=18) as x:
   b=x.read(6*1024*1024);p.with_suffix('.raw').write_bytes(b);r.update(http=x.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
   try:
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(b,'html.parser')
    for z in soup(['script','style']):z.decompose()
    p.with_suffix('.txt').write_text(soup.get_text(' ',strip=True))
   except ImportError:pass
 except Exception as e:r['error']=str(e)
 p.with_suffix('.receipt.json').write_text(json.dumps(r,indent=2));return r
if __name__=='__main__':
 jobs=json.loads((BASE/'jobs.json').read_text())
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
  for r in ex.map(get,jobs):print(r['id'],r.get('http',r.get('error')),r.get('bytes'))
