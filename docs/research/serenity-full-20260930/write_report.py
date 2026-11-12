import json,datetime,collections
from pathlib import Path
P=Path(__file__).resolve().parent
r=lambda n:json.loads((P/n).read_text())
a=r('review_table.json');ix={x['ticker']:x for x in a};d=r('final_decisions.json');v=r('VERIFY.json');s=r('SCOPE.json')
notes={}
for line in (P/'analyst_notes.psv').read_text().splitlines():
 t,thesis,risk,inv,method,priority=line.split('|');notes[t]=dict(thesis=thesis,risk=risk,inv=inv,method=method)
fmt=lambda x:'—' if x is None else f'{x:,.2f}'
link=lambda n:f'[{n}]({P/n})'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
text=f'''# 74家公司全池研究记录 · 2026年9月30日

**实际结果：7家研究门通过、6家条件观察、47家当期排除、14家研究未完成。整体仍为“筛选未完成”。** 74家均有逐股底稿和完整交易日日线，66家有可复算的三情景数值模型；这不意味着74家都完成了全部决策门。14家未完成项没有被当成市场没有机会，也没有被偷偷从名单删除。

本轮直接执行Owner：current_thread_direct。候选池于北京时间9月30日15:44冻结，信息检索覆盖本轮至17:31左右，各源实际截点见原始记录。**价格统一使用9月29日已结束的常规交易日，不是9月30日盘中报价。** 美股尚未核验9月30日常规盘触发；海外股票使用各自当地交易日和本币。没有访问账户、订单或持仓数据，没有给个性化股数。

阅读入口：{link('REVIEW_TABLE.csv')} 为74家横向总表；{link('DOSSIERS.md')} 为逐股来源、现金、稀释、走势、三情景参数、事件与经济失效；{link('valuation_results.csv')} 为数值模型；{link('VERIFY.json')} 为数量与计算检查。表格中的“排除”指本轮新资金研究处置，不是已有持仓必须卖出。

## 先看哪些

结合你偏好的中小公司和右尾空间，我把 **INOD、FORM、AAON** 放在研究门已通过的优先组。优先是证据、兑现路径与价格共同判断，不代表已证明谁的收益率最高。三家的基准估值与现价接近，右尾主要来自强情景，不能把强情景当最可能结果。

|公司|9月29日收盘 USD|压力 / 基准 / 强情景现值 USD|本轮合理参与上限 USD|核心判断与最主要风险|
|---|---:|---:|---:|---|
'''
comments={'INOD':'训练数据已盈利；大客户集中、ATM稀释及预付款会影响每股现金。','FORM':'HBM与先进封装提高测试内容；2028 EPS5.8要求增长和利润率持续兑现。','AAON':'BASX冷却订单与产能释放；交付、授信和营运资本比故事更关键。','NVDA':'经营盈利与现金支撑较强；不是小公司，客户资本回报、自研芯片与资本配置是风险。','TSM':'制造、先进封装与良率能力；海外厂成本及地缘跳空需承受。','AVGO':'定制AI与软件现金；客户集中、债务、SBC及项目节奏。','HPE':'Juniper/网络改善；不是纯网络公司，今晚投资者日可能改变假设。'}
for t in d['pass']:
 x=ix[t];text+=f"|{t}|{fmt(x['close'])}|{fmt(x['stress'])} / {fmt(x['base'])} / {fmt(x['bull'])}|{fmt(x['participation_cap'])}|{comments[t]}|\n"
text+='''
研究门通过的含义是：以本轮已核证据和作者估值假设，可进入账户层计算；**不是七只一起买，也不是按旧收盘价现在即可成交。** 新建仓与已有持仓的加仓分开判断。你的当轮总资金、合并AI敞口和计划账户损失没有核实，不能据此给出“再买一股”。

参与条件固定为：公司论点没有新反证，最新价格不超过上限，事件窗口重新核对；中国时区长期研究可使用估值锚，不强制等待完美回踩。若采用盘中路径，需常规盘开盘30分钟后出现承接或第二次上破。本轮没有生成订单方案，表中上限也不是止损价。基本面失效条件逐股写在底稿，新的财报、指引、融资或并购会使旧价格图过期。

这些估值没有给出情景概率，因此不能据此声称期望收益或胜率提高。压力情景也不是最大亏损；事件跳空可能更差。数字保留小数是为了复算，实际参与区不按几美分作伪精确否决。

## 单项缺口的六家公司

|公司|9月29日收盘|研究上限|唯一未闭合项|复核期限（北京时间）|
|---|---:|---:|---|---|
'''
for t,z in d['conditional'].items():
 x=ix[t];text+=f"|{t}|{fmt(x['close'])} {x['currency']}|{fmt(z['cap'])} {x['currency']}|{z['gap']}|{z['deadline'].replace('T',' ').replace('+08:00','')}|\n"
text+='''
每项的Owner均为当前线程，补证路径见逐股底稿。CLS已重算新发股份和未来EPS，仍差扩产与SBC现金结算后的现金回报桥；因此暂不把它写成可以加仓。NVT已计算融资利息，但动态IR列表的事件交叉核查未闭合。ASMPT已核财报和月报，不能把未完成的本地市场比较伪装成完整相对强度。期限是待办复核点，不是已经运行的后台监控。

## 大盘和行业环境

|指标|9月29日常规收盘|当日|结构|
|---|---:|---:|---|
|QQQ|737.93|+0.19%|高于20/50日均线722.94/714.32；当日735.34–740.58，5日−1.27%、20日+2.95%。|
|VIX|16.04|−0.19%|开16.17、高16.44、低15.73；未与指数共同显示全面压力升级。|
|SOXX|567.44|+1.19%|20日约+11.04%，半导体强于广泛市场。|
|RSP|209.50|−0.11%|20日约−4.51%，低于20/50日均线，广度偏弱。|
|XLV|170.73|−0.31%|医疗数据与临床公司使用医疗行业参照，不套半导体纯度。|

判断是科技/半导体强、广度弱，尚不能由这些证据认定大盘全面失控；也不能由QQQ小涨推断所有板块安全。VIX使用[Cboe历史数据](https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv)，其余历史路径和完整日线保存于`public_snapshot.json`、`closed_session_prices.json`。这些是9月29日结构，不能继承成9月30日盘中确认。

事件上，[Micron已排期9月30日16:30美东财报](https://investors.micron.com/news/press-release/2026/Micron-Technology-to-Report-Fiscal-Fourth-Quarter-Results-on-September-30-2026/default.aspx)，即10月1日04:30北京，当前新建仓事件门不通过。HPE的[Networking Investor Day](https://www.hpe.com/us/en/newsroom/press-release/2026/09/hpe-to-webcast-networking-investor-day-event.html)在9月30日23:30北京；普通投资者日不自动等于重大二元事件，但新材料若改变盈利假设必须立即重算。

## 全部74家处置表

下表按冻结名单保留全部公司。未来24小时事件若未完全闭合，底稿明确标示；估值排除只表示当前已有独立的价格判断，**不代表排除者一旦降价就自动通过其他门**。通过者和条件观察者也不是不变排名。

“基准”是作者情景现值，不是分析师一致预期或公司目标价。大部分成熟企业为2028规范化EPS×退出PE折现；转盈型企业为收入×净利率÷未来稀释股数，DPC另作EBITDA/净利润交叉检查。全部假设可复算，没有拿同一市销率套74家公司。

|公司|币种|收盘|基准现值|本轮状态|处置依据 / 未闭合项|
|---|---|---:|---:|---|---|
'''
for x in a:
 t=x['ticker'];status={'研究门通过，账户门待确认':'研究通过，账户待核','条件观察':'条件观察','排除':'排除','研究未完成':'未完成'}[x['status']]
 if t in d['pass']:why=comments[t]
 elif t in d['conditional']:why=d['conditional'][t]['gap']
 elif t in d['valuation_exclude']:why=f"价格高于本轮基准参与区；重入参考≤{fmt(x['valuation_reentry_ceiling'])}，再核其他门。"
 elif t=='GNRC':why='住宅与数据中心分开估值；高于195研究上限。'
 elif t=='MU':why='24小时内财报；财报后旧模型过期。'
 elif t=='FLNC':why='收入指引下修、预计亏损扩大，交付爬坡反证。'
 else:why='；'.join(d['incomplete'][t])
 text+=f"|{t}|{x['currency']}|{fmt(x['close'])}|{fmt(x['base'])}|{status}|{why}|\n"
text+='''
固定九家完整保留：FORM通过；AEHR、AXTI、SOI、IQE、SIVE、GEV、HWM当期排除；ESMT未完成。这里不存在把ESMT缺证改成“没有价值”，也没有遗漏燃机热端。

## 这轮改变判断的事实

- **现金不能直接当盈利。** INOD客户预付及相关待付款已剔出压力现金口径；CLS的SBC现金结算在融资现金流，必须从股东角度再看；FN扩产后的FCF很薄。对应完整表及来源均在各自底稿。
- **融资改变每股分母。** CLS8月新发约1113万股；Lenovo旧可转债已转换且仍有其他可转证券/权证；Sivers股本已更新。未把回购授权提前当成实际减股。
- **净利润可以包含很大的非经营项目。** NVDA、AMZN、SKHY、INTC、WDC等没有机械年化最新净利；INTC政府托管股重估与经营亏损分开，SKHY模型舍弃投资重估、回到中周期经营假设。
- **已发生的经营反证优先于新故事。** FLNC9月16日下修FY26收入至24亿美元、调整EBITDA亏损约2亿美元；之后供应商合作不能直接消除这个反证。[公司修订指引](https://ir.fluenceenergy.com/news-releases/news-release-details/fluence-energy-announces-revised-guidance-fiscal-year-2026)
- **证券身份先于价格。** CCXI按Churchill Capital Corp XI / Agility Robotics拟并购研究，旧ChemoCentryx/Amgen资料已从有效引用排除；IQE为GBX，ESMT为台湾3006，SKHY为0.1普通股对应1 ADS，TSM为5普通股对应1 ADS，KLAC为拆股后口径。

## 电力与燃气轮机热端：单独看利益落点

需求链覆盖接网（PWR）、配电/机柜（ETN/NVT）、发电设备（GEV/GNRC）、热端精密铸造（HWM/DPC）、材料/涂层/检测及长期资格壁垒。HWM航空敞口较大，DPC更接近独立铸造供应商；两者本轮均因价格与规范化利润要求不匹配排除，不是没有需求。

GEV、Siemens Energy、Mitsubishi Heavy Industries是OEM；不能由OEM集中度推断“只有三家叶片铸造商”。Precision Castparts是Berkshire旗下，不能伪装成独立可买的小盘股。Siemens Energy、MHI、PCC仅为产业比较，不计入74家通过数。MHI及PCC最新来源分别为[MHI季度结果](https://www.mhi.com/news/26080401.html)和[Berkshire Q2报告](https://www.berkshirehathaway.com/qtrly/2ndqtr26.pdf)；Siemens Energy的当前定量分拆尚未闭合，不给它单独价格判断。

客户自制叶片可能同时表明供应紧张和后向整合风险。本轮没有核验到足以证明某个SpaceX/Tesla内制产线已经替代供应商的原始材料，因此不把该传闻当确定利好或利空。供应商要跟踪的是资格、良率、扩产回报及客户采购份额。

## 14家未完成：还不能交付买入排名

'''
for t,gaps in d['incomplete'].items():
 text+=f"- **{t}**："+'；'.join(gaps)+'。\n'
text+='''
这些不是14个已证实的坏公司。POET/LWLG及服务机器人、SPAC和临床公司需要可校准的商业化/概率/稀释路径；AMZN、NBIS等需要把AI增长与持续资本开支相连；ESMT还存在一手Q2现金表的取得缺口。没有把未知的成功概率随便填成50%，也没有把“未读完或未建模”写成排除。若要称本轮74家正式筛选全部完成，这14家仍须继续补证；条件观察的6家则须按单一缺口迁移状态。

## TradingAgents本轮贡献与限制

本轮尝试了已安装TradingAgents与现有Codex桥接：一次原生bull研究调用在180秒内没有完成输出；缩小输入后的一次bear调用在120秒内同样未完成。**本轮完成的TradingAgents分析输出为0。** 已停止继续重复调用，没有为此新增密钥、安装或后台任务。

所以这份资料是本线程直接查一手披露、读取报表并建模的成果，不能宣传成TradingAgents提升了选股准确率。它在本轮的实际限制是不能稳定交付结果；后续即使能输出，也要用可追溯的新事实、纠错和决策改变来证明价值，报告更长不算提升。本轮没有对照收益实验，也没有胜率改善证据。

## 数据与方法审计

- 74/74唯一证券、价格行及底稿已核；66套三情景算式可复算；8家数值模型UNKNOWN。结构检查不证明预测正确。
- 通过7、条件6、排除47、未完成14之和为74。47个排除中，45个为作者估值判断，MU为已排期财报事件，FLNC为已发生的指引/执行反证。
- 估值使用不同年份、不同币种及不同风险假设；默认12%只是作者折现输入，不是市场规律。INOD使用2027前瞻PE定价，不能把它与其他公司的2028退出PE不加区分地比较。
- 港股/欧股/台股约49根本币历史，不编造缺失的60日或50日均线；美股多数取得104根。SOI某二手源155.50与另一源154.95的差异保留披露，不用这0.35%的差异当否决理由。
- 原始抓取里有失败页、旧数据、菜单页和错误证券线索；有效结论看修订后底稿及来源表，不能把下载成功数当研究完成数。

'''
(P/'REPORT.md').write_text(text)
s['research_status']='partial_review_delivered_not_complete';s['last_review_utc']=now;s['counts']=v['counts'];w=lambda n,x:(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2));w('SCOPE.json',s)
(P/'README.md').write_text('''# 资料使用说明

REPORT.md是用户可读的当前结果，DOSSIERS.md和REVIEW_TABLE.csv是逐股状态。原始抓取、搜索、旧假设及追加纠正保留作研究证据，不代表全部内容有效。请勿把primary_status的ok解释成正文已验收，或把companyfacts最近一条当最新季度。

当前模型66家，未建立数值模型8家；当前全池仍未完成。final_decisions.json是状态决策输入。compile_review.py、build_dossiers.py可重新生成算式与底稿；closure_updates.py、final_bridge_updates.py、last_financial_review.py为一次性追加操作记录，不应重复运行，以免重复追加文字。write_report.py生成用户报告。

重要纠正：CCXI的旧Amgen链接无效；FPI/XBRL可能滞后且部分股数单位异常；行情用9月29日完整交易日；HKD/SEK/EUR/GBX/TWD与ADS不得混算。ASMPT中文月报文本有字体乱码，其股数已通过公开PDF第2页渲染人工核对。所有未来EPS、利润率、股数、折现率及汇率均为作者假设，不是公司承诺。

TradingAgents本轮未获得完成输出；两个目录是失败调用证据，不能当多agent研究报告。研究不访问任何账户、持仓、密钥或交易系统。
''')
print(P/'REPORT.md',len(text),v['counts'])
