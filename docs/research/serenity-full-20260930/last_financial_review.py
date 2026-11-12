import json
from pathlib import Path
P=Path(__file__).resolve().parent
r=lambda n:json.loads((P/n).read_text())
def w(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2))
d=r('final_decisions.json');c=r('latest_material_corrections.json');m=r('complex_models.json')
def add(t,txt,urls):
 a=c.get(t,{'text':'','urls':[]});a['text']+=' '+txt;a['urls']=list(dict.fromkeys(a['urls']+urls));c[t]=a
add('INTC','完整Q2 10-Q已补核：Products季度经营利润4.817十亿美元，Foundry亏2.089十亿美元，Corporate未分配亏1.416十亿美元；Foundry收入大多集团内部，不能按57.65亿美元全作外部销售。Q2净亏主要受政府托管股份重估约125亿美元影响，不等于现金经营亏损。政府未释放托管股7100万及有条件Foundry控制权权证2.41亿股须另计；未来股数5.5–6.0十亿足以容纳已知部分及SBC压力情景，并不承诺未来不再融资。估值交叉桥（作者2028假设）：Products EBIT22/28/38十亿，Foundry -8/-4/+2十亿，企业成本4/3/3十亿，净利息1.5十亿、税20%、股数5.5/5.7/6.0十亿，EPS约1.24/2.74/4.73。原EPS1/3/6情景已更宽松，仍不支持当前115.93处于合理基准区。现金短投29.727十亿低于债务50.537十亿；不得给现金和资产重复加值。',['https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm'])
d['incomplete'].pop('INTC',None)
if 'INTC' not in d['valuation_exclude']:d['valuation_exclude'].append('INTC')
add('SKHY','ADS招股书已核：发行后728,865,500普通股，1ADS=0.1普通股；不能直接使用韩股EPS除美元ADS股价。采用未来740/750/770百万普通股，不把回购授权当已注销股。最新Q2净利高于收入，模型完全舍弃该非经营收益，改用中周期收入、税后经营净利率和未来净现金；压力/基准/强景不将76%季度营业利润率永续化。汇率假设1450KRW/USD，不是实时报价。资产重估明细仍未拆成逐项当期利润桥，但不进入估值分子；该缺项不会增加估值，不能据此掩盖当前价格相对中周期基准偏高。',['https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm','https://news.skhynix.com/en/q2-2026-business-results/'])
m['SKHY']={'method':'net_profit','year':2028,'rate':.12,'years':2.25,'revenue_m':[360000000,480000000,620000000],'net_margin':[.22,.28,.32],'pe':[10,14,18],'net_cash_m':[50000000,80000000,110000000],'shares_m':[740,750,770],'currency':'USD','input_currency':'KRW','quote_multiplier':.1/1450,'basis':'金额为百万KRW，股数为百万普通股；乘0.1转换ADS，再除1450汇率假设。2028中周期收入360/480/620万亿KRW、税后经营净利率22/28/32%，未来净现金50/80/110万亿扣扩产预算后的情景。剔除全部投资重估，不用Q2净利年化；IPO后728.8655百万普通股为股本起点。强景并非最大可能收益。'}
d['incomplete'].pop('SKHY',None)
if 'SKHY' not in d['valuation_exclude']:d['valuation_exclude'].append('SKHY')
add('AMKR','完整6月30日10-Q已补核：H1 CFO381.573百万，支付PPE688.425百万，出售资产与补贴36.992百万，FCF负269.860百万。0% 2031可转债10亿美元及最多1.5亿美元期权须计转股；转股价106.37美元、cap call不保证消除一切稀释。9月8日第二阶段将Arizona总投资升至120亿美元，是多年项目，不能视为2026一次性支付，也不能忽略对后续资本回报的影响。当前唯一核心缺口是多年资金来源/折旧及订单利润的闭合预算。',['https://www.sec.gov/Archives/edgar/data/1047127/000104712726000046/amkr-20260630.htm','https://ir.amkor.com/press-releases','https://ir.amkor.com/news-releases/news-release-details/amkor-technology-announces-phase-2-arizona-advanced-packaging'])
# AMKR仍保留未完成：资金回报模型与后续事件核对未同时完成，不能只因取得完整10-Q改为单缺口。
d['incomplete']['AMKR']=['Arizona 120亿美元多年项目的资金/折旧/订单利润预算','9月新项目之后IR未来事件交叉核查']
add('ON','9月16日SEC 425 Investor Day材料已读：公司2030目标为2026E起收入CAGR12–14%、AI数据中心收入逾25亿美元、非GAAP毛利53%、FCF30–35%。这些是公司目标不是已实现利润。Synaptics全股票收购的200百万协同及约18个月EPS增厚目标须和1.350换股比例、新股及SBC一起计算；原EPS5基准仅单体敏感性，未作并表价格推荐。',['https://www.sec.gov/Archives/edgar/data/1097864/000114036126036771/ef20081954_425.htm'])
d['incomplete']['ON']=['Synaptics交易后经营利润/持续SBC/换股稀释的并表估值','交易后IR/股东投票及未来24小时事件交叉核查']
add('AMZN','完整Q2 10-Q已补入：TTM CFO161.403十亿美元，净资本开支169.007十亿，FCF负7.604十亿；再扣融资租赁本金1.599及其他融资义务.308十亿，股东现金口径约负9.511十亿，且CFO还加回SBC，不能视为SBC无成本。Q2 AWS营业利润16.6十亿、北美9.1、国际1.7；投资重估不进入未来EPS。规范化EPS模型虽有敏感性，但AI资产更新周期、持续资本开支与分部股东现金DCF尚未闭合，不能仅看增长宣布通过。',['https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm'])
add('ESMT','已尝试公司财务入口、Q2董事会结果、公告及定向检索；官网本轮可定位完整现金流PDF仍是115Q1，不能冒充115Q2。二手数据展示H1 CFO105.85892亿台币，仅作待核线索，不升级一手结论。可转债308台币转换价已核；累计期末库存/应收、可转债股本和当地事件仍须MOPS/公司Q2原表补证，保持未完成。',['https://www.esmt.com.tw/tw/investor/financial','https://www.esmt.com.tw/tw/press-room/2026073001','https://www.esmt.com.tw/tw/press-room/2026091001?category=investor-Info'])
add('SMCI','年报确认FY26融资现金流入94.788亿美元，超过经营流出68.099亿美元；现金增加不是靠经营自然产生。2028可转价61.06美元、2030可转价55.20、2029修订转换价约83.44；价格超过各触发区时EPS稀释会变化，低现价PE不能完全反映强景股本。年报仍讨论正在整改的财务报告内控缺陷。现金回收与完全稀释未来EPS尚未同时闭合，不能因为Q4单季转正或看似便宜直接通过。',['https://www.sec.gov/Archives/edgar/data/1375365/000137536526000022/smci-20260630.htm'])
w('final_decisions.json',d);w('latest_material_corrections.json',c);w('complex_models.json',m)
print(len(d['pass']),len(d['conditional']),len(d['valuation_exclude'])+len(d['hard_exclude']),len(d['incomplete']))
