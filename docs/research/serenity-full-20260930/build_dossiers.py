import csv,json,datetime,hashlib,collections
from pathlib import Path
from compile_review import P,read,dump,scope,snap,models,prices
notes={}
for l in (P/'analyst_notes.psv').read_text().splitlines():
    t,thesis,risk,invalid,method,priority=l.split('|');notes[t]=dict(thesis=thesis,risk=risk,invalidation=invalid,method_comment=method,priority=priority)
dec=read('final_decisions.json');over=read('review_overrides.json');cor=read('latest_material_corrections.json')
baseline={r['ticker']:r for r in read('baseline_public.json')}
sources=collections.defaultdict(list)
for n in ['supplement_status.json','primary_status.json']:
    for r in read(n):
        if not r.get('ok'):continue
        if r['ticker']=='CCXI' and ('amgen' in r['url'].lower() or 'chemocentryx' in r['url'].lower()):continue
        sources[r['ticker']].append({k:r.get(k) for k in ['url','path','title','retrieved_utc']})
for t,r in cor.items():
    for url in r['urls']:sources[t].append({'url':url,'title':'本轮重大事项追加核验','path':'latest_material_corrections.json'})
for t,r in over.items():
    if r.get('event_url'):sources[t].append({'url':r['event_url'],'title':'IR事项补核','path':'review_overrides.json'})
def f(x):return 'UNKNOWN' if x is None else f'{x:.2f}'
def pct(x):return 'UNKNOWN' if x is None else f'{x*100:+.2f}%'
rows=[];dossiers=['# 74家公司逐股底稿 · 2026-09-30\n\n这是全池研究底稿。状态以本文件和REVIEW_TABLE为准；原始采集文件不代表已验收。行情统一为9月29日已结束的常规交易日，不混入9月30日盘中价格。所有未来数字均为作者情景，不是公司承诺。\n']
for t in scope['universe']:
    n=notes[t];q=prices.get(t,{});m=models.get(t);o=over.get(t,{})
    cap=None;gaps=[];deadline='';path='';margin=None
    if t in dec['pass']:
        d=dec['pass'][t];status='研究门通过，账户门待确认';reason=d['reason'];cap=d['cap'];margin=d['margin_price'];event=d['event'];url=d['event_url']
    elif t in dec['conditional']:
        d=dec['conditional'][t];status='条件观察';reason=d['gap'];gaps=[d['gap']];cap=d['cap'];deadline=d['deadline'];path=d['path'];event=d['event'];url=d['event_url']
    elif t in dec['valuation_exclude']:
        status='排除';cap=round(m['values'][1]*1.05,2)
        reason=f"当前价{f(q.get('close'))}高于本轮作者基准价值{f(m['values'][1])}及合理参与上限{cap:.2f}，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。"
        event=o.get('event','已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。');url=o.get('event_url','')
    elif t in dec['hard_exclude']:
        status='排除';reason=dec['hard_exclude'][t];event=o.get('event',reason);url=o.get('event_url','')
    else:
        status='研究未完成';gaps=dec['incomplete'][t];reason='；'.join(gaps);event=o.get('event','SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。');url=o.get('event_url','');path='继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。'
    if url:sources[t].append({'url':url,'title':'公司事件核查路径','path':'final_decisions.json'})
    ss=[];seen=set()
    for s in sources[t]:
        if s['url'] not in seen:ss.append(s);seen.add(s['url'])
    sources[t]=ss
    sec=snap['sec'].get(t,{})
    sector=baseline[t].get('sector','')
    peer='XLV' if t in ['TEM','RXRX','SCTX'] else 'SOXX' if sector in ['packaging_test','semiconductor','memory'] or t in ['TSM','NVDA','AVGO','CRDO','ALAB','AEHR','AXTI','AMAT','KLAC','LRCX','FORM','CAMT','ONTO','ACMR','RMBS','TER'] else 'QQQ'
    foreign=t in ['SIVE','SOI','IQE','ESMT','ASMPT','Lenovo']
    relative=(q.get('return_20')-prices[peer]['return_20']) if q.get('return_20') is not None and not foreign else None
    cur=m['currency'] if m else {'SIVE':'SEK','SOI':'EUR','IQE':'GBX','ESMT':'TWD','ASMPT':'HKD','Lenovo':'HKD'}.get(t,'USD')
    values=m['values'] if m else [None]*3
    row=dict(ticker=t,sector=sector,status=status,reason=reason,independent_gaps=len(gaps),gaps='；'.join(gaps),price_date=q.get('last_date'),currency=cur,close=q.get('close'),stress=values[0],base=values[1],bull=values[2],participation_cap=cap if status in ['研究门通过，账户门待确认','条件观察'] else None,valuation_reentry_ceiling=cap if status=='排除' else None,margin_of_safety_reference=margin,return_1=q.get('return_1'),return_5=q.get('return_5'),return_20=q.get('return_20'),return_60=q.get('return_60'),peer=peer if not foreign else '本币收益，不与美元ETF直接比',relative_20=relative,volume_ratio=q.get('volume_ratio'),bars=q.get('bars'),event=event,economic_invalidation=n['invalidation'],owner='current_thread_direct',deadline=deadline,path=path,account_gate='未验证；未读取账户，不计算个性化股数',source_urls='\n'.join(s['url'] for s in ss),price_source=q.get('source'))
    rows.append(row)
    trend=f"{q.get('last_date')}收盘 {f(q.get('close'))} {cur}；当日{pct(q.get('return_1'))}，5/20/60交易日{pct(q.get('return_5'))}/{pct(q.get('return_20'))}/{pct(q.get('return_60'))}。20日均价{f(q.get('sma_20'))}，50日均价{f(q.get('sma_50'))}；20日高/低{f(q.get('high20'))}/{f(q.get('low20'))}；末日量/20日均量{f(q.get('volume_ratio'))}倍，共{q.get('bars')}根日线。"
    trend+=f" 20日相对{peer}为{pct(relative)}个百分点差（非超额收益率比值）。" if relative is not None else ' 本币数据不直接减美元ETF收益；不足60根时不编造60日指标。'
    if t=='SOI':trend+=' 使用stockanalysis的155.50欧元；曾有另一二手源154.95的差异，未把该报价差当否决理由。'
    if t=='KLAC':trend+=' 6月10比1拆股已识别；本20/60日窗口均在拆股后，EPS也使用拆股后口径。'
    docs=[f"\n## {t} — {status}\n",f"**业务与瓶颈。** {n['thesis']}\n",f"**反证、现金与稀释。** {n['risk']} {o.get('fundamental_addendum','')} {cor.get(t,{}).get('text','')}\n",f"**完整交易日价格与量价。** {trend} [行情来源]({q.get('source')})\n"]
    if m:
        docs.append(f"**估值。** 压力/基准/强情景现值：{f(values[0])} / {f(values[1])} / {f(values[2])} {cur}。{n['method_comment']} {m['basis']}\n")
        params={k:v for k,v in m.items() if k not in ['basis','values']}
        docs.append('```json\n'+json.dumps(params,ensure_ascii=False,indent=2)+'\n```\n')
    else:docs.append('**估值。** UNKNOWN，未用统一市销率补空。'+n['method_comment']+'\n')
    if margin:docs.append(f"**价格地图。** 高安全边际研究参考≤{margin}；合理参与研究上限{cap} {cur}。两者都不是损失保证。超过上限须重新评估，不自动追涨。\n")
    docs.append(f"**公司事件。** {event}"+(f" [核查入口]({url})" if url else '')+'\n')
    docs.append(f"**经济失效。** {n['invalidation']} 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。\n")
    docs.append(f"**处置。** {reason}\n")
    if gaps:docs.append(f"**未闭合项（{len(gaps)}项）。** "+'；'.join(gaps)+f"。Owner=current_thread_direct。{path} "+(f"复核到期：{deadline}。" if deadline else '')+'\n')
    if status=='研究门通过，账户门待确认':docs.append('**触发与组合。** 估值日无新反证且价格不超过上限，可进入账户门计算；不要求完美回踩。若选择盘中执行路径，使用常规盘开盘30分钟后的承接/第二次上破，本报告未核9月30日分钟触发。不因一家公司通过而同时推荐多只高度相关AI股。账户资金、整数1股比例及计划损失未验证；不构成当前股数或订单指令。\n')
    docs.append('**一手与本地证据。**\n\n'+'\n'.join(f"- [{s.get('title') or '原文'}]({s['url']})"+(f"；[保存文本]({P/s['path']})" if s.get('path') else '') for s in ss[:8])+'\n')
    if sec.get('source'):docs.append(f"- [SEC披露索引]({sec['source']})；采集时间{sec.get('retrieved_utc','见public_snapshot')}，索引存在不等于全部正文已审核。\n")
    dossiers.extend(docs)
dump('review_table.json',rows)
with (P/'REVIEW_TABLE.csv').open('w') as f0:
    w=csv.DictWriter(f0,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(P/'DOSSIERS.md').write_text('\n'.join(dossiers))
dump('source_index.json',dict(sources))
counts=collections.Counter(r['status'] for r in rows)
assert len(rows)==len(set(r['ticker'] for r in rows))==74
assert set(scope['universe'])==set(notes)==set(r['ticker'] for r in rows)
assert all(r['independent_gaps']==1 for r in rows if r['status']=='条件观察')
assert all(r['independent_gaps']==0 and r['participation_cap']>=r['close'] for r in rows if r['status']=='研究门通过，账户门待确认')
assert all(len(a['values'])==3 and all(mathv>=0 for mathv in a['values']) for a in models.values())
verify={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':74,'unique':74,'scenario_models':len(models),'price_rows':sum(t in prices for t in scope['universe']),'counts':dict(counts),'overall':'筛选未完成','fixed_nine':{t:next(r['status'] for r in rows if r['ticker']==t) for t in ['FORM','AEHR','AXTI','SOI','IQE','ESMT','SIVE','GEV','HWM']},'validation':'结构、数量、日期与公式检查；不声称代码验证能证明研究判断正确','tradingagents_completed_outputs_this_run':0,'sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['REVIEW_TABLE.csv','DOSSIERS.md','valuation_results.json']}}
dump('VERIFY.json',verify)
print(json.dumps(verify,ensure_ascii=False,indent=2))
