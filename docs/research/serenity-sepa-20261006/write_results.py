"""Publish the 74-name logical screen with explicit field and reading limitations."""
import json,csv,collections
from pathlib import Path
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
rows=json.loads((P/'audit.json').read_text());pool=json.loads((P/'SCOPE.json').read_text())['universe']
assert len(rows)==len(pool)==74 and {r['ticker'] for r in rows}==set(pool)
assert all(r['failed'] for r in rows), 'Never publish zero matches without an independent counterexample per company.'
codes={'1_listing_age':'上市时间','2_revenue_yoy':'营收同比','3_ni_yoy':'净利润同比','3_ni_qoq':'净利润环比','4_MA':'50/150日均线','5_volume':'10/120日均量','6_ROE':'ROE','7_CAGR':'三年利润CAGR'}
def fmt(v):return 'UNKNOWN' if v is None else f'{v*100:.2f}%'
def ratio(h):return 'UNKNOWN' if not h.get('vol120') else f"{h['vol10']/h['vol120']:.4f}"
def mark(s):
 if s.startswith('PASS'):return '满足'
 if s.startswith('FAIL'):return '不满足'
 if s.startswith('UNDEFINED'):return '不可正常计算'
 if s.startswith('N/A'):return '不适用'
 return 'UNKNOWN'
def counter(r):
 t=r['ticker'];f=r['financial'];h=r['technical'];tests=r['tests']
 if t in ['DPC','SCTX','SKHY']:return '对应上市股票序列不足一年；详见上市口径说明'
 if tests['5_volume']=='FAIL':return f"10日均量/120日均量={ratio(h)}，不大于1"
 if tests['2_revenue_yoy']=='FAIL':return f"营收同比{fmt(f.get('revenue_yoy'))}，未超过25%"
 if tests['3_ni_yoy'].startswith('FAIL_LOSS'):return '最新季度法定净利润为亏损，未通过盈利增长条件'
 if tests['3_ni_qoq']=='FAIL':return f"净利润环比{fmt(f.get('ni_qoq'))}，不为正"
 if tests['6_ROE']=='FAIL':return f"TTM ROE={fmt(f.get('roe'))}，未超过15%"
 if tests['7_CAGR'].startswith('UNDEFINED'):return '三年前年度净利润非正，不能按正利润CAGR>20%判通过'
 if tests['7_CAGR'].startswith('FAIL_NONPOSITIVE'):return '最新完整年度净利润非正，不满足正利润复合增长要求'
 if tests['7_CAGR']=='FAIL':return f"三年净利润CAGR={fmt(f.get('cagr'))}，未超过20%"
 if tests['4_MA']=='FAIL':return '收盘价未同时高于50日和150日均线'
 if tests['3_ni_yoy']=='FAIL':return f"净利润同比{fmt(f.get('ni_yoy'))}，未超过30%"
 raise AssertionError(t)

now=datetime.now(timezone.utc).isoformat()
details=['# 74家公司逐项核验表','',f'生成UTC：{now}。正式池74只全部保留，Owner为本线程。行情统一截至2026-10-05已完成交易日；不把10月6日亚洲盘中混入完整日线。',
'','本表是用户给定条件的逻辑筛选，不是Serenity估值/事件/账户研究门通过表。一个明确不满足项即足以证明该股票不能同时满足全部条件；其余未知分项仍列UNKNOWN，不伪装成全部分项验证完成。',
'','|公司|最近收入季度|营收同比|最近利润季度|利润同比|利润环比|TTM ROE|年度三年CAGR|均线条件|10/120均量比|上市一年|至少一项独立反证|未闭合分项|',
'|---|---|---:|---|---:|---:|---:|---:|---|---:|---|---|---|']
for r in rows:
 f=r['financial'];h=r['technical'];ts=r['tests']
 details.append('|'+ '|'.join([r['ticker'],f.get('revenue_period') or 'UNKNOWN',fmt(f.get('revenue_yoy')),f.get('ni_period') or 'UNKNOWN',fmt(f.get('ni_yoy')),fmt(f.get('ni_qoq')),fmt(f.get('roe')),fmt(f.get('cagr')),mark(ts['4_MA']),ratio(h),mark(ts['1_listing_age']),counter(r),'、'.join(codes.get(k,k) for k in r['unknown']) or '无UNKNOWN测试项'])+'|')
details+=['','## 每家公司来源与计算说明','']
index={r['ticker']:r for r in json.loads((P/'report_index.json').read_text())}
for r in rows:
 t=r['ticker'];f=r['financial'];h=r['technical'];details+=['### '+t,'',f"结论：原条件不全满足。独立反证：{counter(r)}。",'']
 if f.get('note'):details+=[f['note'],'']
 if h.get('source'):details += ['行情来源：'+h['source'],'']
 if f.get('source'):details+=['补充财务来源：'+f['source'],'']
 for s in index.get(t,{}).get('sources',[]):
  if s.get('characters',0)>1000:details.append(f"- {s.get('title') or s.get('form') or '一手正文'}：{s['url']}；保存正文：{s['path']}")
 details+=['']
(P/'ALL74.md').write_text('\n'.join(details))

core=[r for r in rows if all(r['tests'][k]=='PASS' for k in ['2_revenue_yoy','3_ni_yoy','3_ni_qoq','6_ROE','7_CAGR'])]
partial=[r['ticker'] for r in rows if r['unknown']]
counts=collections.Counter(r['tests']['5_volume'] for r in rows)
report=['# 2026-10-06 原八条条件全池判定','',
'结论：固定74家公司中，当前没有一家同时满足全部适用条件。74只均已有至少一项独立不达标证据；不是用数据失败、没有账户资金或未完成估值解释为没有匹配。','',
'本轮统计仅指这套规则的匹配结果：全部满足0 / 单缺口待判断0 / 已确认至少一项不满足74 / 是否匹配仍无法判断0。它不替代Serenity正式研究通过/排除数量，不代表市场无机会，也不构成持仓卖出指令。','',
f'分项完整性边界：{len(partial)}家公司仍有UNKNOWN分项（名单见下）。因此不能声称74家公司每个指标均已完整核实，更不能声称全部年报、季报、附注和历史事项都已逐字审读。已经完成的是全池“是否同时满足”判定，以及所需财报表格、原始披露与行情的读取/计算。','',
'## 原条件口径冻结','',
'- 最新季度法定GAAP/IFRS归母净利润为主要口径，非GAAP利润另看；不得拿半年累计当第二季度。盈利同比要求正基期，扭亏标不可正常计算，不杜撰增长率。',
'- ROE固定为TTM归母利润/期初期末平均归母权益，负权益不伪装成高ROE。原提示未明确ROE年度还是TTM，因此同时披露本次定义；其他定义需要另行对照。',
'- 三年CAGR固定为最近完整财政年度与三年前完整财政年度，公式(NI最近/NI基期)^(1/3)-1，正利润端点才适用。没有用季度利润年化代替。',
'- 价格必须同时高于50/150交易日简单均线，均量10交易日必须严格大于120交易日。',
'- ST及30/00代码为A股市场条件，本池没有A股上市序列，标市场不适用。ESMT台湾3006不可误认为A股创业板；按跨市场字面代码过滤则会另被排除，不改变本次零匹配结果。',
'- DPC、SCTX与SKHY的当前美国上市序列不足一年。SKHY是老公司新ADS；韩国普通股上市年龄不等于新美国ADS序列年龄。即使放开这三只上市年龄门，它们也无法用现有美国交易史验证150日和120日指标。','',
'## 财务条件较强但被其他原条件挡住的公司','',
'以下8家在本次法定盈利/TTM定义下满足营收同比、净利润同比和环比、ROE及三年CAGR五个财务测试；仍须现金流与非经常项目分析，不能把机械通过当作利润质量验证。','',
'|公司|营收同比|利润同比|利润环比|TTM ROE|三年利润CAGR|均线|10/120日均量比|','|---|---:|---:|---:|---:|---:|---|---:|']
for r in core:
 f=r['financial'];report.append('|'+ '|'.join([r['ticker']]+[fmt(f.get(k)) for k in ['revenue_yoy','ni_yoy','ni_qoq','roe','cagr']]+[mark(r['tests']['4_MA']),ratio(r['technical'])])+'|')
report+=['',f"成交量条件在70只具备120交易日可比历史的股票中：{counts['PASS']}满足、{counts['FAIL']}不满足；另4只未能计算（3个新上市序列及CCXI行情身份/来源问题）。12只通过量能条件者均有另外的明确财务或均线反证。",'',
'CLS均量比约0.9955，仅比1低约0.45%，属于临界结果。按原规则字面不满足，但跨行情供应商、成交量修订可能改变标签；不能把这一微小差距说成公司突然不可投资。','',
'## 原文核对发现的修正','',
'- INOD：季度收入/利润同比增长，但最近季度净利润14.412m低于前季14.898m，环比约-3.26%；三年前年度亏损，不能当正常正利润CAGR。',
'- CAMT：最新季度收入同比仅约8%，GAAP净利润同比下降约31%；不能用旧2021季度事实替代当前季度，也不能拿后半年订单预期当已实现增长。',
'- MU：更新到9月30日发布的FY2026第四季度及全年，不延用第三季度；FY2023亏损使正常三年利润CAGR不可用。',
'- ESMT：读取2026Q2、2025Q2、2025年度、2022年度完整合并报表。2026Q2扭亏，2025年度245.125m对2022年度1042.193m，使年度三年CAGR为负；同时量能门不满足。',
'- Lenovo：最近季度法定归母亏损609m，调整后利润1075m不能直接替换法定口径。',
'- 原始结构化年报字段个别存在金额scale不一致，已用原始inline-XBRL的scale与合并口径context校正，包含ANET；年度与季度数字未直接拼接成假利润。','',
'## 对策略的评估','',
'可以作为已经盈利的成长股的辅助测试，现阶段不适合直接替换Serenity全部右尾池。利润环比会受季节性和非经常项影响；三年利润条件排除刚扭亏企业；持续放量要求会挡住整理缩量的强势公司。一次零匹配只证明此日按此组阈值的结果，不能证明策略有/无超额收益。VCP识别、回测、事件与估值买入研究均未由本轮条件筛选替代。','',
'## 证据、局限与运行收尾','',
'- 74家公司均有一手来源索引；68个SEC主体取全量companyfacts及submissions，原始JSON保存在facts/和submissions/。',
'- 下载最新季度/年度及三年前基期申报正文并解析完整inline-XBRL；67个主体有可解析的原始申报，SKHY另用完整ADS招股书及公司披露。原文路径见report_index.json；下载/解析不是所有段落语义审核完成。',
'- 67只美国上市序列取得Nasdaq完整日线。6只海外序列通过公开浏览器页面1Year、100Rows分页读取200行，排除10月6日未完成行；指标在overseas_metrics.json。海外原始200行尚未导出为本地独立数据集，复算可回到公开页面。',
'- CCXI对应Churchill Capital Corp XI，不使用旧ChemoCentryx历史行情。季度法定净利润反证来自正确CIK2074973；行情与长期ROE字段仍UNKNOWN。',
'- 未闭合分项公司：'+', '.join(partial)+'。每只至少一个独立已证实的不满足项，所以不影响“不能全部同时满足”的逻辑结论；但不能称逐项全验证。',
'- 未做逐只拆股/公司行动专项审计，因此均线通过标签不能单独升级为可交易判断；原始报价口径与单位留在数据内。',
'- 当前市场仅作背景：10月5日QQQ收756.20、+0.88%，开749.35、高756.92、低749.08；VIX取得当日16:14EDT15.52、+1.372%，该源当日日线尚未入表，最新完整OHLC仍10月2日16.15/16.24/15.30/15.31。不将旧日内结构冒充10月5日。来源 https://stockanalysis.com/etf/qqq/history/ 和 https://chartexchange.com/symbol/index-vix/historical/ 。这不影响规则的静态财务/量价匹配判定。',
'- 本轮Owner为本线程；规则ROUTING-2026-09-30-v3已核，实际model/effort/速度UNKNOWN。使用agent-reach公开读取路由和PDF读取技能；匿名Jina及Yahoo直接路径失败后用已可用公开网页/浏览器，不创建登录、不读取秘密、不安装依赖。',
'- 全部一次性前台采集脚本已退出；无账户访问、交易、调度器或后台监控。本目录全部数据、源码、原文用于审计/复算保留。临时初始验证文件/tmp/serenity-sepa-nvda-facts.json与/tmp/serenity-sepa-nvda-nasdaq.json作为来源验证证据保留，无清理。','',
'[74只逐项表](ALL74.md)；[可计算字段CSV](AUDIT.csv)；[完整测试JSON](audit.json)；[原文索引](report_index.json)。']
(P/'REPORT.md').write_text('\n'.join(report))
(P/'VERIFY.json').write_text(json.dumps({'generated_utc':now,'frozen_count':74,'unique_count':len({r['ticker'] for r in rows}),'all_have_independent_counterexample':all(r['failed'] for r in rows),'matches':0,'known_fail':74,'undecided_match':0,'companies_with_unknown_fields':partial,'all_financial_fields_complete':False,'all_filing_paragraphs_semantically_read':False,'all_corporate_actions_audited':False,'trading_recommendations':False},ensure_ascii=False,indent=2))
print('74 distinct rows; 74 independent failures; 0 matches; unknown subfields',len(partial))
