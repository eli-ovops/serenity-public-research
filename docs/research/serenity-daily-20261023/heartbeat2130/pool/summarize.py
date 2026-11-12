from pathlib import Path
import json,hashlib,datetime
p=Path(__file__).resolve().parent; root=p.parent; base=Path('docs/research/serenity-entry-refresh-20261022');cards=json.loads(Path('docs/research/serenity-screen-all74-20261021/ALL74_CARDS.json').read_text())['cards']
rows=[];delta=[]
for c in cards:
 s=c['symbol'];r={'symbol':s,'old_cap_comparison_only':c['participation_cap'],'old_status_not_revalidated':c['status'],'new_research_status':'not_revalidated'}
 f=next((f for f in [root/'public'/f'INFO_{s}.json',p/'public'/f'INFO_{s}.json',p/'public'/f'OVER_{s}.json'] if f.exists()),None)
 if f:
  d=json.loads(f.read_text());r['price_source']=str(f);r['sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
  if 'chart' in d:
   m=d['chart']['result'][0]['meta'];r.update(price=m['regularMarketPrice'],currency=m['currency'],asof_utc=datetime.datetime.fromtimestamp(m['regularMarketTime'],datetime.timezone.utc).isoformat(),timezone=m['exchangeTimezoneName'],price_change_percent=m.get('regularMarketChangePercent'),identity=m.get('longName'),session='overseas market; source timestamp controls')
   if s == 'ESMT':r['freshness']='prior-session/stale; not Oct23 fresh confirmation'
  else:
   d=d.get('data')
   if d and d.get('primaryData'):
    m=d['primaryData'];r.update(price=float(m['lastSalePrice'].replace('$','').replace(',','')),currency='USD',asof=m.get('lastTradeTimestamp'),price_change_percent=m.get('percentageChange'),identity=d.get('companyName'),session=d.get('marketStatus'))
   else:r['quote_error']='HTTP200 no usable data'
 else:r['quote_error']='missing'
 f=p/'public'/f'SEC_{s}.json'
 if f.exists():
  n=json.loads(f.read_text())['filings']['recent'];old=next((q for q in [base/'dip-review-2255/public'/f.name,base/'request-adjust-2200/public'/f.name,base/'heartbeat2130/public'/f.name] if q.exists()),None)
  r['sec_source']=str(f);r['sec_baseline']=str(old);r['sec_latest_date']=n['filingDate'][0]
  oldn=json.loads(old.read_text())['filings']['recent'] if old else {'accessionNumber':[]};seen=set(oldn['accessionNumber']);new=[]
  for i,a in enumerate(n['accessionNumber']):
   if a not in seen:new.append({k:n[k][i] for k in ['filingDate','form','accessionNumber','primaryDocument']})
  r['new_accessions']=new
  for n in new:delta.append(dict(symbol=s,**n,baseline=str(old),body_read=False,meaning='new relative to saved baseline, not necessarily new today'))
 else:r['sec_status']='non-US six overseas; no SEC job, local exchange announcements not comprehensively rechecked'
 rows.append(r)
held=['NVDA','TSM','CLS','RMBS','RXRX','DPC','POET','SCTX'];good=[r for r in rows if 'price'in r]
o={'owner':'/root/heartbeat_pool','asof_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'public finite incremental collection; no full74 underwriting or buy decision','frozen_symbols':[c['symbol'] for c in cards],'price_count':len(good),'price_missing':[r['symbol'] for r in rows if 'price'not in r],'sec_index_count':sum('sec_source'in r for r in rows),'new_accession_count':len(delta),'new_accession_issuer_count':len(set(r['symbol'] for r in delta)),'new_accessions':delta,'current_held_symbols':held,'held_new_accessions':[r for r in delta if r['symbol']in held],'deep_review_candidate':{'symbol':'HPE','owner':'root','reason':'54.6433 quote vs old62 comparison coordinate; Mzansi release unread prerequisite; no old-plan revival'},'rows':rows,'limits':['All12 increment accession bodies unread by pool; root may independently read','Six overseas local exchange/currentIR event gates not all closed','All74 valuation/technical/economic invalidation not refreshed','No investment status counts revalidated; incremental coverage only']}
(p/'INCREMENT.json').write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
print('prices',len(good),'missing',o['price_missing'],'SEC',o['sec_index_count'],'delta',len(delta));print([(r['symbol'],r.get('price'),r.get('asof_utc'))for r in rows if r['symbol']in ['SOI','IQE','SIVE','ESMT','ASMPT','Lenovo']])
lines=['# 10/23 21:30全池公开增量','',f'冻结74家，取得{len(good)}个可用价格快照、68份SEC索引。采集与完整研究分开；不新增任何研究通过/排除结论。当前现仓 NVDA/TSM/CLS/RMBS/RXRX/DPC/POET/SCTX 均无相对指定昨夜原件的新accession。','',f'相对每卡记录的10/22基线，共{len(delta)}条首次发现accession，涉及10家；其中10/22提交9条、10/23提交3条。索引新增不等于当天新事件。全部正文在pool未读。','', '|代码|提交日期|表格|accession|','|---|---|---|---|']
lines += [f"|{x['symbol']}|{x['filingDate']}|{x['form']}|{x['accessionNumber']}|"for x in delta]
lines += ['', '仅建议root优先深核HPE，原cap仅供坐标比较，不能复活旧单。FORM/INOD本轮为非现仓池报价，持仓以root当前SCOPE为准。','', '固定九家均含在价格池。有限IR线索：FORM10/22新厂公告索引；AEHR11/2财报日历、10/7后续Sonoma订单；AXTI10/29财报日历；SOI官网财报索引最新Q1；IQE官方IR仅列9/7中报及融资入口，未完成完整RNS；SIVE10/22临时股东大会公告索引及10/20LiDAR生产订单；ESMT官网确认3006身份，未完成当轮MOPS；HWM10/14财报日历索引；GEV10/20Songon燃机订单索引。索引/搜索线索不冒充正文核验或24h事件门。','', '热端链：DPC/GEV/HWM68SEC路径含本轮索引。Siemens Energy官方Press Hub实际只见Loading，未取得完整增量；MHI官方新闻索引已读，不冒充全热端公告读完；PCC/BRK.B本轮未查。OEM不等于独立叶片铸造商，未据这些线索调整估值。','', '海外：IQE.L为GBp/GBX（35.3便士=0.353GBP），ESMT=3006.TW/TWD；各价UTC原时间与当地时区逐卡保存，ESMT为前交易日源时间；ASMPT/Lenovo为10/23香港收盘后时点，不能冒充10/23新价。海外6家当地公告门仍未全闭合。','', '原始HTTP数据及SHA在public/*.receipt.json，全部本agent136次请求无HTTP错误；报价复用root时保存对应路径。PRIMARY_NATIVE/EXTRA_NATIVE/SUPPLEMENT_NATIVE保存有限官方索引工具回执。未读正文、74估值更新、走势完整性与事件门是明确未完成项。']
(p/'REPORT.md').write_text('\n'.join(lines)+'\n')
manifest={str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest()for f in p.rglob('*')if f.is_file() and f.name!='SHA256.json'};(p/'SHA256.json').write_text(json.dumps(manifest,indent=2)+'\n')
