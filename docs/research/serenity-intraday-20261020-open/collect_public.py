"""One finite public read per listed job. No auth, retries, background process or trades."""
import json, urllib.request, hashlib, concurrent.futures, datetime, sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
def one(job):
    out={'id':job['id'],'url':job['url'],'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(job['url'],headers={'User-Agent':'SerenityResearch/1.1 public-market review','Accept':'application/json,text/html,*/*'})
        with urllib.request.urlopen(req,timeout=16) as response:
            data=response.read(8*1024*1024)
            out.update(http_status=response.status,final_url=response.url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
            path=BASE/'public'/(job['id']+'.raw');path.parent.mkdir(exist_ok=True)
            path.write_bytes(data);out['raw_path']=str(path.relative_to(BASE))
            try:
                parsed=json.loads(data);(path.parent/(job['id']+'.json')).write_text(json.dumps(parsed,ensure_ascii=False,indent=2))
            except (ValueError,UnicodeError): pass
    except Exception as e:
        out['error']=str(e);out['http_status']=getattr(e,'code',None)
    out['finished_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (BASE/'public').mkdir(exist_ok=True)
    (BASE/'public'/(job['id']+'.receipt.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    return out
if __name__=='__main__':
    jobs=json.loads((BASE/sys.argv[1]).read_text())
    jobs=[j for j in jobs if not (BASE/'public'/(j['id']+'.receipt.json')).exists()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(one,jobs))
    print(json.dumps([{k:v for k,v in r.items() if k in ['id','http_status','error','bytes']} for r in results],ensure_ascii=False))
