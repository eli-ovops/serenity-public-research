import subprocess,json,concurrent.futures
from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parent
jobs={'DPC_disposal':'https://ir.doncasters.com/news-and-events/news/news-details/2026/DPC-Holdings-Agrees-to-Dispose-of-Ivostud-to-DUBAG-Group/default.aspx','FORM_ex99':'https://www.sec.gov/Archives/edgar/data/1039399/000103939926000037/ex-991.htm'}
def get(x):
 t,u=x;r=subprocess.run(['curl','-sS','--fail','--max-time','15','-A','Serenity public research [REDACTED_EMAIL]',u],capture_output=True,timeout=17);z={'source':u,'ok':not r.returncode}
 if r.returncode:z['error']=r.stderr.decode()[:120]
 else:z['text']=BeautifulSoup(r.stdout,'html.parser').get_text(' ',strip=True)
 (P/(t+'.json')).write_text(json.dumps(z,indent=2));return t,z
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:print(json.dumps(dict(e.map(get,jobs.items()))))
