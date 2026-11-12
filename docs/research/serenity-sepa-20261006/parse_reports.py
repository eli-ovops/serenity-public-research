"""Read every downloaded inline-XBRL filing, preserving scales and consolidated contexts."""
import json,re,warnings
from pathlib import Path
from bs4 import BeautifulSoup,XMLParsedAsHTMLWarning
warnings.filterwarnings('ignore',category=XMLParsedAsHTMLWarning)
P=Path(__file__).resolve().parent
F={}
for path in sorted((P/'reports').glob('*.html')):
 t=path.name.split('_')[0];s=BeautifulSoup(path.read_text(errors='replace'),'lxml');contexts={};units={}
 for c in s.find_all('xbrli:context'):
  if c.find(['xbrldi:explicitmember','xbrldi:typedmember']):continue
  def v(k):
   z=c.find('xbrli:'+k);return z.get_text() if z else None
  end=v('enddate') or v('instant')
  if end:contexts[c.get('id')]={'start':v('startdate'),'end':end}
 for u in s.find_all('xbrli:unit'):
  z=u.find('xbrli:measure')
  if z:units[u.get('id')]=z.get_text().split(':')[-1]
 d=F.setdefault(t,{'facts':{},'files':[]});count=0
 for f in s.find_all('ix:nonfraction'):
  c=contexts.get(f.get('contextref'));unit=units.get(f.get('unitref'));name=f.get('name','');parts=name.split(':',1)
  if not c or not unit or len(parts)!=2:continue
  text=f.get_text().strip().replace(',','').replace('\xa0','').replace('−','-').replace('–','-')
  try:val=float(text.strip('()'))*(10**int(f.get('scale','0')))
  except (ValueError,TypeError):continue
  if f.get('sign')=='-' or text.startswith('('):val=-abs(val)
  item={**c,'val':val,'form':path.name.split('_')[1].split('.')[0],'filed':'2026-10-06','primary_path':str(path.resolve()),'context':f.get('contextref'),'scale':f.get('scale','0'),'display':f.get_text().strip()}
  if not item['start']:item.pop('start')
  d['facts'].setdefault(parts[0],{}).setdefault(parts[1],{'units':{}})['units'].setdefault(unit,[]).append(item);count+=1
 d['files'].append({'path':str(path.resolve()),'consolidated_numeric_facts':count,'characters':len(path.read_text(errors='replace'))})
 print(t,path.name,count,flush=True)
(P/'inline_facts.json').write_text(json.dumps(F,ensure_ascii=False,indent=2))
print('DONE',len(F),flush=True)
