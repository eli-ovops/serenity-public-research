> 2026-10-01口径更正：本报告部分美股“末日量/20日均量”误用了两段20日平均成交量之比。FORM的9月29日正确值为1.0934倍（含当日的20日均量），不是1.0368倍。详见[更正表](../tradingagents-form-inputs-20261001/historical_volume_corrections.csv)。历史原始数据保留；不要沿用旧量比推断放量或买卖结论。

# 74家公司逐股底稿 · 2026-09-30

这是全池研究底稿。状态以本文件和REVIEW_TABLE为准；原始采集文件不代表已验收。行情统一为9月29日已结束的常规交易日，不混入9月30日盘中价格。所有未来数字均为作者情景，不是公司承诺。


## FORM — 研究门通过，账户门待确认

**业务与瓶颈。** HBM高并行探针卡、先进封装与硅光测试增加测试内容；Q2收入2.582亿美元，Q3收入指引2.70亿±0.10亿。

**反证、现金与稀释。** 客户集中、测试方案替代、产能爬坡；H1经营现金流1.068亿减资本开支0.248亿，须区分合资安排与经常收益。 Q2 GAAP EPS0.71、调整0.82；GAAP毛利50.7%，Q3 GAAP EPS0.75±0.09。H1 CFO106.764百万减Capex24.791百万=81.973百万；持续SBC计入2028规范化EPS。 

**完整交易日价格与量价。** 2026-09-29收盘 136.25 USD；当日+4.03%，5/20/60交易日+8.13%/+35.42%/+14.81%。20日均价114.28，50日均价113.14；20日高/低136.69/92.05；末日量/20日均量1.04倍，共104根日线。 20日相对SOXX为+24.39%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/FORM/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：47.74 / 134.84 / 209.23 USD。Q3非GAAP EPS中值0.86只是起点；2028盈利情景要求测试内容和产能持续兑现，SBC不能免费加回。 Q3调整EPS0.86中值对应年化3.44的规模参照，非全年预测。基准2028 EPS5.8要求HBM增长和经营杠杆，须保留SBC；强景不假设无限提高利润率。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.8,
    5.8,
    7.5
  ],
  "pe": [
    22.0,
    30.0,
    36.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**价格地图。** 高安全边际研究参考≤95；合理参与研究上限140 USD。两者都不是损失保证。超过上限须重新评估，不自动追涨。

**公司事件。** SEC近期披露、Q2原文与IR新闻/日历核对；最近会议9月10日，未发现未来24小时已知重大公司事件。 [核查入口](https://investors.formfactor.com/events-and-presentations)

**经济失效。** 连续两季HBM相关订单/收入低于同口径计划且毛利率跌破45%，或核心客户转移探针方案。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 探针卡测试内容和HBM需求已有收入/毛利及现金支撑；基准134.84美元，140为约4%的合理参与误差带。强情景需要持续放量，并非当前已实现价值。

**触发与组合。** 估值日无新反证且价格不超过上限，可进入账户门计算；不要求完美回踩。若选择盘中执行路径，使用常规盘开盘30分钟后的承接/第二次上破，本报告未核9月30日分钟触发。不因一家公司通过而同时推荐多只高度相关AI股。账户资金、整数1股比例及计划损失未验证；不构成当前股数或订单指令。

**一手与本地证据。**

- [10-Q 2026-08-04](https://www.sec.gov/Archives/edgar/data/1039399/000103939926000033/form-20260627.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/200_FORM.txt)
- [IR事项补核](https://investors.formfactor.com/events-and-presentations)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001039399.json)；采集时间2026-09-30T07:47:28.190496+00:00，索引存在不等于全部正文已审核。


## TSEM — 排除

**业务与瓶颈。** 硅光代工、SiGe及模拟特色工艺；Q2收入4.60亿、净利0.91亿，客户多年供货需求支持扩产。

**反证、现金与稀释。** H1含2.90亿客户预付款，不能当经常FCF；13亿美元2027合同需审查取消/产能约束。  

**完整交易日价格与量价。** 2026-09-29收盘 234.43 USD；当日+3.71%，5/20/60交易日-0.92%/+14.33%/+7.07%。20日均价216.54，50日均价225.38；20日高/低240.00/190.55；末日量/20日均量1.09倍，共104根日线。 20日相对QQQ为+11.37%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/TSEM/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：51.15 / 162.73 / 334.77 USD。利润捕获取决于良率、折旧和预付款履约成本，不将2028管理层目标直接当现值。 Q2净利0.91亿美元、收入4.60亿美元；基准2028 EPS7需要硅光产能与高附加值工艺扩大，不能把客户预付款当利润。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    3.0,
    7.0,
    12.0
  ],
  "pe": [
    22.0,
    30.0,
    36.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 硅光扩产认证延后两个季度或合同需求下修，同时预付款不能覆盖履约资本开支。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价234.43高于本轮作者基准价值162.73及合理参与上限170.87，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [Financial Model (https://towersemi.com/wp-content/uploads/2026/05/TSEM_Q12026_IRCALL_SLIDES_FF.pdf)](https://towersemi.com/wp-content/uploads/2026/05/TSEM_Q12026_IRCALL_SLIDES_FF.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/002_TSEM.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000928876.json)；采集时间2026-09-30T07:47:29.870954+00:00，索引存在不等于全部正文已审核。


## CRDO — 排除

**业务与瓶颈。** AEC与高速互连芯片缓解机柜内部带宽/功耗瓶颈；FY27Q1收入4.790亿、经营利润1.207亿。

**反证、现金与稀释。** 客户集中、SBC、光互连方案替代及大客户自研；营收增长不等于每股现金增长。  

**完整交易日价格与量价。** 2026-09-29收盘 192.35 USD；当日-0.17%，5/20/60交易日-0.11%/-14.96%/-27.57%。20日均价176.86，50日均价209.36；20日高/低221.74/149.14；末日量/20日均量2.41倍，共104根日线。 20日相对SOXX为-26.00%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/CRDO/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：34.10 / 123.99 / 278.97 USD。经营利润而非高调整EPS作锚；明确持续SBC和未来稀释。 FY27Q1 GAAP EPS0.67、收入4.79亿美元；基准要求2028盈利接近现季度规模的1.9倍且持续计SBC，强景需新产品/客户量产。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.0,
    5.0,
    9.0
  ],
  "pe": [
    22.0,
    32.0,
    40.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 主要客户AEC部署放缓并出现毛利/份额同步下滑，或新客户不能补足集中订单。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价192.35高于本轮作者基准价值123.99及合理参与上限130.19，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-09-02](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/crdo-20260801.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/201_CRDO.txt)
- [prior located primary, verify period](https://www.sec.gov/Archives/edgar/data/1807794/000162828026059795/credoq12027ex-991.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/240_CRDO.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001807794.json)；采集时间2026-09-30T07:47:28.547182+00:00，索引存在不等于全部正文已审核。


## CAMT — 排除

**业务与瓶颈。** 先进封装、HBM及高端晶圆检测/量测；Q2收入1.332亿，Q3指引1.58–1.60亿，H2增长有订单支撑。

**反证、现金与稀释。** GAAP EPS0.46显著低于调整后0.78；收购、可转债、扩产和客户集中；现金投资余额不是净现金。   Q2调整净利39.448百万减持续SBC4.873百万为34.575百万；保留收购摊销时更低，不能直接使用0.78 EPS。H1/Q2稀释股数为51.433/51.520百万而不是5万股。未来2028基准EPS5.6对应约54百万股、302.4百万归母净利；按30%净利率须约10.08亿美元收入，比2026 H1的254.9百万显著提高，是有风险的作者增长假设。当前价即使对该假设仍高于估值上限，故按价格排除；可转债不把总现金直接加回。

**完整交易日价格与量价。** 2026-09-29收盘 152.82 USD；当日+7.16%，5/20/60交易日+0.96%/+14.04%/+7.74%。20日均价143.43，50日均价147.44；20日高/低154.46/126.09；末日量/20日均量0.84倍，共104根日线。 20日相对SOXX为+3.01%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/CAMT/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：42.62 / 138.87 / 250.30 USD。2028EPS增长须对应先进封装产能和毛利兑现，不能用调整利润替代所有者收益。 Q2 GAAP EPS0.46、调整0.78；2028基准5.6依赖H2放量和后续两年增长，风险是SBC/收购摊销差额长期不收敛。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.5,
    5.6,
    8.5
  ],
  "pe": [
    22.0,
    32.0,
    38.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** H2收入无法实现较H1增长30%以上且后续订单下修，或先进封装份额实质下降。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价152.82高于本轮作者基准价值138.87及合理参与上限145.81，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/1109138/000117891326003975/zk2635905.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.camtek.com/investors/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001109138.json)；采集时间2026-09-30T07:47:28.357945+00:00，索引存在不等于全部正文已审核。


## MOD — 排除

**业务与瓶颈。** 数据中心热管理与冷却设备，扩产与业务组合变化提供增长。

**反证、现金与稀释。** Q1FY27经营现金流4140万低于资本开支4640万；冷却产能爬坡、传统业务周期。   财报原文链接已经补入有效来源索引，来源为公司原文/SEC，非二手转述。

**完整交易日价格与量价。** 2026-09-29收盘 183.72 USD；当日+4.96%，5/20/60交易日-6.25%/+2.96%/-21.88%。20日均价187.24，50日均价196.67；20日高/低203.22/172.84；末日量/20日均量1.06倍，共104根日线。 20日相对QQQ为+0.01%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/MOD/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：55.79 / 154.98 / 278.97 USD。以冷却增长和传统业务合理利润分开核算，须纳入增量资本开支回报。 Q1FY27 EPS1.37；基准8依赖冷却增量与现有业务现金转换，交易导致业务范围变化时本模型失效。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    4.0,
    8.0,
    12.0
  ],
  "pe": [
    18.0,
    25.0,
    30.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 数据中心订单增速低于新增产能增速且经营利润率持续下降。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价183.72高于本轮作者基准价值154.98及合理参与上限162.73，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [本轮重大事项追加核验](https://investors.modine.com/news/news-details/2026/Modine-Reports-First-Quarter-Fiscal-2027-Results/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/67347/000110465926088569/mod-20260630x10q.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000067347.json)；采集时间2026-09-30T07:49:07.359282+00:00，索引存在不等于全部正文已审核。


## ONTO — 排除

**业务与瓶颈。** 先进封装检测、光刻与先进节点量测；Q2收入3.431亿，Q3指引3.80–4.00亿，披露积压超过10亿。

**反证、现金与稀释。** Q2 GAAP EPS1.21对比调整后1.93；积压兑现周期、Rigaku投资与并购资本配置。  

**完整交易日价格与量价。** 2026-09-29收盘 304.69 USD；当日+5.52%，5/20/60交易日+7.36%/+14.03%/+0.27%。20日均价269.77，50日均价281.35；20日高/低304.78/240.01；末日量/20日均量0.77倍，共104根日线。 20日相对SOXX为+2.99%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ONTO/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：85.24 / 232.48 / 390.56 USD。增长质量较强；估值必须扣除持续SBC并审阅投资/收购会计，不只看账面现金。 Q2 GAAP EPS1.21，Q3收入3.8–4.0亿美元；基准10要求订单交付与产能利用率持续提升，投资重估不计持续盈利。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    5.0,
    10.0,
    14.0
  ],
  "pe": [
    22.0,
    30.0,
    36.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 连续两季先进封装出货递延且毛利率下降，或积压取消取代正常交付。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价304.69高于本轮作者基准价值232.48及合理参与上限244.10，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-06](https://www.sec.gov/Archives/edgar/data/704532/000119312526338401/onto-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/202_ONTO.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000704532.json)；采集时间2026-09-30T07:49:07.833089+00:00，索引存在不等于全部正文已审核。


## AAON — 研究门通过，账户门待确认

**业务与瓶颈。** 定制HVAC、BASX数据中心冷却；新产能吞吐和订单兑现是核心。

**反证、现金与稀释。** H1经营现金流5497万、期末现金字段仅1.3万美元，须同时核对授信/负债而非单独宣判缺钱。 已核对6月末循环借款435百万、未使用授信163.692百万，杠杆1.46低于契约上限3.0；全年资本开支约190百万。低账面现金余额不能单独证明流动性危机。扩产投入与现金回收是盈利敏感性的重要风险。 8月28日品牌/投资者材料和8月13日常规股息已核。BASX Q2末积压14.304亿美元，现有工厂空间的公司收入产能估计至少20亿美元；产能不是销售。2028 EPS4需BASX出货/利润兑现，不能把潜在产能直接放入已实现盈利。

**完整交易日价格与量价。** 2026-09-29收盘 85.11 USD；当日-0.28%，5/20/60交易日+7.36%/+12.02%/-22.17%。20日均价79.03，50日均价84.71；20日高/低91.52/73.50；末日量/20日均量1.00倍，共104根日线。 20日相对QQQ为+9.07%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AAON/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：34.10 / 92.99 / 167.38 USD。产能释放后的正常化EPS模型可算，融资与资本开支已补核；现金仅1.3万美元不能脱离授信余额解读。 Q2 EPS0.68；基准4依赖BASX与新工厂吞吐，不假设融资免费。已核对借款4.35亿美元和可用授信1.637亿美元。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.0,
    4.0,
    6.0
  ],
  "pe": [
    22.0,
    30.0,
    36.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**价格地图。** 高安全边际研究参考≤65；合理参与研究上限95 USD。两者都不是损失保证。超过上限须重新评估，不自动追涨。

**公司事件。** 8月13日8-K为已支付常规股息，8月28日为品牌及投资者材料更新；SEC+IR未发现未来24小时已知重大公司事件。 [核查入口](https://investors.aaon.com/events)

**经济失效。** 积压不能转化为出货，资本开支持续超过融资可承受范围且毛利下滑。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** BASX订单与扩产对应真实冷却瓶颈；借款与未用授信已核，基准92.99美元。95为合理参与上限，执行/资金占用风险高于成熟设备龙头。

**触发与组合。** 估值日无新反证且价格不超过上限，可进入账户门计算；不要求完美回踩。若选择盘中执行路径，使用常规盘开盘30分钟后的承接/第二次上破，本报告未核9月30日分钟触发。不因一家公司通过而同时推荐多只高度相关AI股。账户资金、整数1股比例及计划损失未验证；不构成当前股数或订单指令。

**一手与本地证据。**

- [10-Q 2026-08-10](https://www.sec.gov/Archives/edgar/data/824142/000082414226000055/aaon-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/203_AAON.txt)
- [Investor News (https://investors.aaon.com/investor-news)](https://investors.aaon.com/investor-news)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/010_AAON.txt)
- [AAON Investor Relations (https://investors.aaon.com/)](https://investors.aaon.com/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/009_AAON.txt)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/824142/000082414226000059/irpresentationaugust26ta.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/824142/000082414226000057/aaon-20260812.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [IR事项补核](https://investors.aaon.com/events)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000824142.json)；采集时间2026-09-30T07:49:08.288410+00:00，索引存在不等于全部正文已审核。


## NVT — 条件观察

**业务与瓶颈。** 电气连接、机柜与数据中心基础设施，Maverick Power扩充电力布局。

**反证、现金与稀释。** 9月29日8亿美元债券已完成；17.5亿美元收购资金含6亿定期贷款和循环授信，旧净债务已过期。   Maverick2026收入估计700百万美元，17.5亿对11.5倍调整EBITDA隐含约152.17百万EBITDA；另有最高550百万现金或有对价。作者按800百万票息6.15%+600百万贷款6%+250百万循环6%测利息100.2百万，再减D&A20百万和25%税，增量利润约23.98百万，约0.15美元/股（160百万股假设），不能把全部EBITDA当EPS。正式归母模型及或有对价仍需对照交割披露。 收购利息桥为作者预算：Maverick 2026收入700百万，1750/11.5约152.2百万调整EBITDA；800百万债券×6.15%+600百万定贷×假设6%+250百万循环借款×假设6%=100.2百万年息。再扣20百万D&A、25%税后约24百万新增利润，按160百万股约0.15 EPS，不能把全部EBITDA当增厚。2028 EPS8需原业务增长及收购后运营改善；最高550百万earnout另作未来资本负担，基准不假定新增回购。当前新增利率并非所有余额已实借，计算是全额融资压力预算。

**完整交易日价格与量价。** 2026-09-29收盘 161.68 USD；当日+0.74%，5/20/60交易日-0.60%/+7.25%/+3.05%。20日均价156.35，50日均价157.07；20日高/低166.19/143.87；末日量/20日均量0.85倍，共104根日线。 20日相对QQQ为+4.30%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/NVT/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：69.74 / 154.98 / 255.73 USD。须做收购后利润与利息/股数桥接，不能用Q2资产负债表当9月底净债务。 Q2 EPS1.32；基准8是收购后总盈利假设，新增利息桥已核为压力预算，2028增长是假设；IR事件交叉核验未完成，不可直接作买价。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    5.0,
    8.0,
    11.0
  ],
  "pe": [
    18.0,
    25.0,
    30.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 9月29日债券完成，6.15%票息；Maverick交易仍须交割，outside date为11月20日可延至2027年2月19日。不是9月30日已知排期交割。IR列表动态框架未完整显示，保留唯一事件缺口。 [核查入口](https://investors.nvent.com/press-releases/default.aspx)

**经济失效。** 收购协同不能覆盖融资成本或整合令自由现金流/债务比恶化。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 近期IR活动/新闻的当前完整列表无法从动态页面直接读出，未来24小时事件有限核查尚差这一条交叉证据。

**未闭合项（1项）。** 近期IR活动/新闻的当前完整列表无法从动态页面直接读出，未来24小时事件有限核查尚差这一条交叉证据。。Owner=current_thread_direct。SEC重大融资及Maverick公告已读；用公司可读活动列表或发行人新闻联合核对，无新增重大二元事件即可闭合，不把动态页面故障当公司有风险。若仍受阻，明确证据管线受阻并降为未完成。 复核到期：2026-10-01T09:00:00+08:00。

**一手与本地证据。**

- [8-K 2026-09-29](https://www.sec.gov/Archives/edgar/data/1720635/000110465926111938/tm2626249d1_8k.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/013_NVT.txt)
- [本轮重大事项追加核验](https://investors.nvent.com/press-releases/press-release-details/2026/nVent-to-Acquire-Maverick-Power/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [公司事件核查路径](https://investors.nvent.com/press-releases/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/final_decisions.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001720635.json)；采集时间2026-09-30T07:49:07.909331+00:00，索引存在不等于全部正文已审核。


## ANET — 条件观察

**业务与瓶颈。** AI以太网交换和软件生态；Q2收入30.36亿、经营利润13.78亿，现金生成较强。

**反证、现金与稀释。** 超大客户集中、白盒与自研ASIC、NVIDIA端到端竞争；持续SBC应计成本。  活动页只有动态框架，没有把空表当成确认无事件；通过可读官方主页新闻及SEC最新披露替代核对。财报增长和现金质量支持研究论点，唯一等待条件为既定合理价格。

**完整交易日价格与量价。** 2026-09-29收盘 202.86 USD；当日-1.01%，5/20/60交易日-1.14%/+3.66%/+17.07%。20日均价197.41，50日均价191.63；20日高/低212.00/181.27；末日量/20日均量0.65倍，共104根日线。 20日相对QQQ为+0.71%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ANET/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：77.49 / 189.86 / 325.47 USD。在高利润率基础上给质量溢价，但未来增长与股本不能无限外推。 Q2 GAAP EPS0.95；基准2028 EPS7要求AI以太网份额与高利润率延续，SBC计入利润、股数不因回购授权自动减少。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    4.0,
    7.0,
    10.0
  ],
  "pe": [
    25.0,
    35.0,
    42.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 事件页只有动态框架，已改用可读官方新闻主页及SEC最新披露；未发现未来24小时已知重大公司事件，保留未披露事件残余风险。 [核查入口](https://investors.arista.com/Home/default.aspx?LanguageId=1)

**经济失效。** 云客户支出转向其他网络架构并伴份额/毛利下降，而非仅短期交付波动。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 价格尚高于合理参与上限200美元；本轮唯一未满足项为估值价格，不以轻微指数涨跌加设门槛。

**未闭合项（1项）。** 价格尚高于合理参与上限200美元；本轮唯一未满足项为估值价格，不以轻微指数涨跌加设门槛。。Owner=current_thread_direct。本次已核Q2/SEC与IR新闻页；到期按最新常规盘收盘和是否出现新公司事实复核，价格≤200且无新反证即升级，仍高于则转当期价格排除。 复核到期：2026-10-01T09:00:00+08:00。

**一手与本地证据。**

- [10-Q 2026-08-05](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000175/anet-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/204_ANET.txt)
- [(https://www.sec.gov/Archives/edgar/data/1596532/000159653226000174/ex991q226-earningsrelease.htm)](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000174/ex991q226-earningsrelease.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/014_ANET.txt)
- [本轮重大事项追加核验](https://investors.arista.com/Home/default.aspx?LanguageId=1)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001596532.json)；采集时间2026-09-30T07:49:08.639892+00:00，索引存在不等于全部正文已审核。


## AAOI — 排除

**业务与瓶颈。** 800G/1.6T光模块量产及垂直制造；Q2收入1.919亿，Q3指引2.55–2.90亿。

**反证、现金与稀释。** Q2仍GAAP亏损；H1经营现金流负0.738亿，扩产及稀释要求高；Q3指引使用约9280万稀释股。  

**完整交易日价格与量价。** 2026-09-29收盘 100.67 USD；当日+3.98%，5/20/60交易日-5.92%/-6.52%/-18.39%。20日均价102.41，50日均价111.54；20日高/低116.90/93.62；末日量/20日均量0.56倍，共104根日线。 20日相对QQQ为-9.47%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AAOI/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：2.94 / 20.70 / 52.75 USD。按未来归母净利润而非市销率单独估值；未来股本须高于基本股。 Q3收入指引255–290百万、稀释股数92.8百万。基准需毛利和规模杠杆，未来扩产后不假定剩余净现金。

```json
{
  "revenue": [
    900,
    1500,
    2400
  ],
  "net_margin": [
    0.03,
    0.1,
    0.15
  ],
  "shares": [
    105,
    115,
    130
  ],
  "pe": [
    18,
    25,
    30
  ],
  "net_cash": [
    0,
    0,
    0
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** Q3收入低于2.55亿并且毛利率无法接近29%，或扩产再次依赖明显折价融资。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价100.67高于本轮作者基准价值20.70及合理参与上限21.74，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-06](https://www.sec.gov/Archives/edgar/data/1158114/000143774926026278/aaoi20260630_10q.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/205_AAOI.txt)
- [prior located primary, verify period](https://www.sec.gov/Archives/edgar/data/1158114/000168316826006055/aaoi_ex9901.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/241_AAOI.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001158114.json)；采集时间2026-09-30T07:49:09.224395+00:00，索引存在不等于全部正文已审核。


## CIEN — 排除

**业务与瓶颈。** 数据中心互联、相干光和跨园区容量升级；Q3收入16.71亿、Q4中值17.5亿。

**反证、现金与稀释。** 两大客户约41.7%；应收账期和存货上升；债务与投资并存。  

**完整交易日价格与量价。** 2026-09-29收盘 354.92 USD；当日+3.12%，5/20/60交易日-3.70%/-7.28%/-18.19%。20日均价345.44，50日均价375.79；20日高/低381.60/311.60；末日量/20日均量1.49倍，共104根日线。 20日相对QQQ为-10.24%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/CIEN/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：69.74 / 193.73 / 396.76 USD。将Q3 EPS1.83与调整2.11差额正常化；9月投资者论坛新目标需逐项对照。 Q3 GAAP EPS1.83、Q4收入中值17.5亿美元；2028基准EPS10包括相干光增长，不将两大客户集中度降低当既定事实。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    5.0,
    10.0,
    16.0
  ],
  "pe": [
    18.0,
    25.0,
    32.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 云客户订单缩减并伴DSO持续恶化、毛利率失去改善。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价354.92高于本轮作者基准价值193.73及合理参与上限203.42，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-09-03](https://www.sec.gov/Archives/edgar/data/936395/000162828026060361/cien-20260801.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/206_CIEN.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000936395.json)；采集时间2026-09-30T07:49:09.068706+00:00，索引存在不等于全部正文已审核。


## PWR — 排除

**业务与瓶颈。** 输配电接网与工程能力是AI供电落地瓶颈；Q2收入95.57亿、积压534亿。

**反证、现金与稀释。** 工程执行、并购、劳动力与许可；积压不是净利润，营运资本现金流可逆。  

**完整交易日价格与量价。** 2026-09-29收盘 651.79 USD；当日+1.15%，5/20/60交易日+1.43%/+7.36%/-3.30%。20日均价630.94，50日均价642.13；20日高/低659.85/593.70；末日量/20日均量0.76倍，共104根日线。 20日相对QQQ为+4.41%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/PWR/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：185.98 / 433.96 / 737.73 USD。正常化EPS为主、FCF转换作交叉检验，不能把季度9亿FCF直接年化。 Q2 EPS2.96，积压534亿美元；基准20依赖工程交付/利润率和适度并购，不把积压当利润，不将单季FCF年化。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    12.0,
    20.0,
    28.0
  ],
  "pe": [
    20.0,
    28.0,
    34.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 接网项目连续取消/推迟且利润率下降，或并购ROIC不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价651.79高于本轮作者基准价值433.96及合理参与上限455.66，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [QUANTA SERVICES REPORTS SECOND QUARTER 2026 RESULTS :: Quanta Services, Inc. (PWR) (https://investors.quantaservices.com/news-events/press-releases/detail/402/quanta-services-reports-second-quarter-2026-results)](https://investors.quantaservices.com/news-events/press-releases/detail/402/quanta-services-reports-second-quarter-2026-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/021_PWR.txt)
- [PWR 06-30-2026 Earnings Release (https://investors.quantaservices.com/_assets/_fc69198b082640a1f770638c0383eb48/quantaservices/news/2026-07-30_QUANTA_SERVICES_REPORTS_SECOND_QUARTER_2026_402.pdf)](https://investors.quantaservices.com/_assets/_fc69198b082640a1f770638c0383eb48/quantaservices/news/2026-07-30_QUANTA_SERVICES_REPORTS_SECOND_QUARTER_2026_402.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/020_PWR.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001050915.json)；采集时间2026-09-30T07:49:11.335084+00:00，索引存在不等于全部正文已审核。


## POET — 研究未完成

**业务与瓶颈。** 光引擎光互连集成具工程潜力，但目前商业规模与成熟光模块商不同。

**反证、现金与稀释。** 小基数收入增长、合作公告、演示与付费量产订单不能互换；融资和产能验证风险。  

**完整交易日价格与量价。** 2026-09-29收盘 7.67 USD；当日+3.51%，5/20/60交易日-6.12%/+2.82%/-14.30%。20日均价7.69，50日均价7.89；20日高/低8.75/7.02；末日量/20日均量0.72倍，共104根日线。 20日相对QQQ为-0.14%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/POET/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** UNKNOWN，未用统一市销率补空。用里程碑与融资稀释情景；当前订单规模/毛利不足，不凑市销率目标价。

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 已宣布客户无法进入可重复付费量产，或现金消耗使量产前需大规模折价融资。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 可重复付费量产订单/毛利证据；融资后每股现金与概率估值

**未闭合项（2项）。** 可重复付费量产订单/毛利证据；融资后每股现金与概率估值。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [News & Media | POET Technologies (https://www.poet-technologies.com/news-media)](https://www.poet-technologies.com/news-media)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/022_POET.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001437424.json)；采集时间2026-09-30T07:49:10.450727+00:00，索引存在不等于全部正文已审核。


## SIVE — 排除

**业务与瓶颈。** InP激光器与无线业务；Jabil项目目标为2027订单与量产，格拉斯哥扩产服务长期需求。

**反证、现金与稀释。** Q2收入5380万SEK同比降12%、经营现金流负7000万；12亿美元机会管道不是订单；融资扩大股本。   8月13日官方公告：权证行权新增1,659,015股，合计356,740,332股。2029模型390/430/480百万股包含未来融资，不是假称当前股数。即使强情景改为完全不新增股、仅使用356.740百万股，强价值约20.74SEK，仍低于31.86；有新量产订单/利润证据才能上修，12亿美元管道不能代替已签订单。

**完整交易日价格与量价。** 2026-09-29收盘 31.86 SEK；当日+1.21%，5/20/60交易日-10.96%/+29.41%/UNKNOWN。20日均价30.00，50日均价UNKNOWN；20日高/低35.96/22.10；末日量/20日均量0.62倍，共49根日线。 本币数据不直接减美元ETF收益；不足60根时不编造60日指标。 [行情来源](https://stockanalysis.com/quote/sto/SIVE/history/)

**估值。** 压力/基准/强情景现值：0.15 / 4.18 / 15.41 SEK。采用分阶段收入、利润与稀释；不把销售pipeline折扣后直接当积压。 Q2收入53.8百万SEK，强景需Jabil和其他量产项目大幅兑现；8月13日公告已发行356.740332百万股；390–480百万为未来融资稀释情景，不是当前已发行事实。不能把12亿美元pipeline当订单。

```json
{
  "method": "net_profit",
  "year": 2029,
  "rate": 0.18,
  "years": 3.25,
  "revenue_m": [
    350,
    800,
    1600
  ],
  "net_margin": [
    0,
    0.12,
    0.22
  ],
  "pe": [
    20,
    30,
    35
  ],
  "net_cash_m": [
    100,
    200,
    350
  ],
  "shares_m": [
    390,
    430,
    480
  ],
  "currency": "SEK"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** Jabil资格认证/首批生产订单延后至2027下半年后，或融资后现金仍不足以支持扩产。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价31.86高于本轮作者基准价值4.18及合理参与上限4.39，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [current discovered source](https://www.sivers-semiconductors.com/wp-content/uploads/2026/08/Sivers-Interim-report-Q226.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/245_SIVE.txt)
- [Sivers Semiconductors AB (publ), Publishes Interim Report Q1, January – March 2026 - Sivers Semiconductors (https://www.sivers-semiconductors.com/press/sivers-semiconductors-ab-publ-publishes-interim-report-q1-january-march-2026/)](https://www.sivers-semiconductors.com/press/sivers-semiconductors-ab-publ-publishes-interim-report-q1-january-march-2026/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/024_SIVE.txt)
- [Interim Report Q1 (https://www.sivers-semiconductors.com/wp-content/uploads/2026/05/Sivers-Interim-report-Q126_FINAL_ENG.pdf)](https://www.sivers-semiconductors.com/wp-content/uploads/2026/05/Sivers-Interim-report-Q126_FINAL_ENG.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/023_SIVE.txt)
- [本轮重大事项追加核验](https://www.sivers-semiconductors.com/press/bootstrap-exercises-warrants-in-sivers-semiconductors/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)


## FLNC — 排除

**业务与瓶颈。** 电网储能集成、软件和电力调节；AI用电相关性间接。

**反证、现金与稀释。** 9个月经营现金流负3.665亿、现金3.393亿；项目验收、关税、保函与融资约束。 9月16日最新修订：FY26收入约24亿美元，原中值30亿；调整EBITDA亏损约2亿美元，原亏损1000万。美国代工爬坡/供应链执行已实际失效，不能继续用旧订单故事推买入。 

**完整交易日价格与量价。** 2026-09-29收盘 7.82 USD；当日+4.27%，5/20/60交易日+7.57%/-27.66%/-56.12%。20日均价8.90，50日均价11.26；20日高/低11.37/7.01；末日量/20日均量1.13倍，共104根日线。 20日相对QQQ为-30.61%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/FLNC/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：0.00 / 7.20 / 20.95 USD。按项目毛利→净利润→现金转换建立情景，不能仅按订单金额定价。 储能集成低毛利模式，基准3.5%净利需项目验收及现金回款改善；使用总经济权益股数情景而非只取Class A平均股数，融资路径仍需验证。负利润情景取零经营股权价值，并非断言会破产。

```json
{
  "method": "net_profit",
  "year": 2029,
  "rate": 0.18,
  "years": 3.25,
  "revenue_m": [
    3000,
    4500,
    6500
  ],
  "net_margin": [
    -0.01,
    0.035,
    0.06
  ],
  "pe": [
    12,
    18,
    23
  ],
  "net_cash_m": [
    0,
    0,
    0
  ],
  "shares_m": [
    220,
    230,
    250
  ],
  "currency": "USD"
}
```

**公司事件。** 9月16日指引下修已经发生；9月24日供应协议不抵消亏损与执行反证。 [核查入口](https://ir.fluenceenergy.com/news-releases/news-release-details/fluence-energy-announces-revised-guidance-fiscal-year-2026)

**经济失效。** 现金和可用授信不足履约，或主要项目毛利/回款持续低于合同预算。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 9月16日实际下修FY26收入约20%、调整EBITDA亏损扩大至2亿美元，代工爬坡执行反证已出现；重新入池须公司新披露证明交付/项目利润恢复，并给出可核资金保障。

**一手与本地证据。**

- [10-Q 2026-08-05](https://www.sec.gov/Archives/edgar/data/1868941/000186894126000029/flnc-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/207_FLNC.txt)
- [IR事项补核](https://ir.fluenceenergy.com/news-releases/news-release-details/fluence-energy-announces-revised-guidance-fiscal-year-2026)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001868941.json)；采集时间2026-09-30T07:49:10.201294+00:00，索引存在不等于全部正文已审核。


## SMCI — 研究未完成

**业务与瓶颈。** AI服务器集成和液冷交付，Q4收入约111亿、毛利率17.5%，规模增长显著。

**反证、现金与稀释。** 全年经营现金流负68.10亿而Q4转正；库存/应收融资、可转债和内控风险，不能只取最好单季。   年报确认FY26融资现金流入94.788亿美元，超过经营流出68.099亿美元；现金增加不是靠经营自然产生。2028可转价61.06美元、2030可转价55.20、2029修订转换价约83.44；价格超过各触发区时EPS稀释会变化，低现价PE不能完全反映强景股本。年报仍讨论正在整改的财务报告内控缺陷。现金回收与完全稀释未来EPS尚未同时闭合，不能因为Q4单季转正或看似便宜直接通过。

**完整交易日价格与量价。** 2026-09-29收盘 41.02 USD；当日-1.82%，5/20/60交易日-1.25%/+10.03%/+50.86%。20日均价39.41，50日均价35.73；20日高/低43.76/35.36；末日量/20日均量0.69倍，共104根日线。 20日相对QQQ为+7.08%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/SMCI/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：15.50 / 61.99 / 153.44 USD。低表观PE必须同时通过营运资本和资产质量；正常化盈利估值不能替代现金检验。 FY26 EPS3.26；基准5仍须全年回款正常化，财务/内控不确定性用低倍数不能完全消除。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.0,
    5.0,
    9.0
  ],
  "pe": [
    10.0,
    16.0,
    22.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 现金回款持续落后收入、主要客户坏账/退货，或财报/内控出现新实质反证。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 全年营运资本/回款恢复桥；可转债与内控风险对未来每股盈利的影响

**未闭合项（2项）。** 全年营运资本/回款恢复桥；可转债与内控风险对未来每股盈利的影响。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [10-K 2026-08-31](https://www.sec.gov/Archives/edgar/data/1375365/000137536526000022/smci-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/208_SMCI.txt)
- [prior located primary, verify period](https://www.sec.gov/Archives/edgar/data/1375365/000137536526000021/exhibit991_20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/242_SMCI.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001375365.json)；采集时间2026-09-30T07:49:10.398234+00:00，索引存在不等于全部正文已审核。


## LWLG — 研究未完成

**业务与瓶颈。** 电光聚合物材料可能改善调制功耗和带宽；需付费授权/量产验证。

**反证、现金与稀释。** Q2收入仅3.28万美元、经营亏损727万；董事任命和展会不能证明商业收入拐点。  

**完整交易日价格与量价。** 2026-09-29收盘 5.17 USD；当日+3.40%，5/20/60交易日-6.34%/-4.79%/-30.14%。20日均价5.17，50日均价6.04；20日高/低5.70/4.62；末日量/20日均量0.96倍，共104根日线。 20日相对QQQ为-7.74%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/LWLG/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** UNKNOWN，未用统一市销率补空。现有收入不足支撑盈利倍数；商业授权规模、成功概率和稀释缺乏可校准基础，估值UNKNOWN。

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 到下一轮公司指引复核仍无可核对的付费量产授权，并持续靠发行股份覆盖现金消耗。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 付费量产授权规模；商业成功率及融资稀释估值

**未闭合项（2项）。** 付费量产授权规模；商业成功率及融资稀释估值。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [(https://www.sec.gov/Archives/edgar/data/1325964/000107997326001097/lwlg_10q-063026.htm)](https://www.sec.gov/Archives/edgar/data/1325964/000107997326001097/lwlg_10q-063026.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/029_LWLG.txt)
- [10-Q (https://www.sec.gov/Archives/edgar/data/1325964/000155335026000087/lwlg_10q-033126.htm)](https://www.sec.gov/Archives/edgar/data/1325964/000155335026000087/lwlg_10q-033126.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/030_LWLG.txt)
- [8-K 2026-09-29](https://www.sec.gov/Archives/edgar/data/1325964/000107997326001303/lwlg_8k.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/031_LWLG.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001325964.json)；采集时间2026-09-30T07:49:11.289577+00:00，索引存在不等于全部正文已审核。


## NOK — 排除

**业务与瓶颈。** 光网络与数据中心连接，合并Infinera后需检验真正云客户增量。

**反证、现金与稀释。** 传统移动网络占比、重组成本与收购协同稀释AI纯度；不能只因低股价判断便宜。   完整Q2报告现已读取：H1 CFO162百万欧元、资本开支266百万，FCF负104百万；Q2 FCF负732百万，2026重组现金流出700–800百万。净现金2776百万不等于所有者当期盈利；Network Infrastructure Q2收入2037百万、经营利润166百万，传统Mobile仍为2680百万收入。2025年报核实1 ADS=1普通股。基准EPS0.45欧元×18倍经折现及1.10汇率假设约6.90美元；即把净现金按约58亿股粗略全加回，仍不足当前10.36。业务可能增长不等于当前价安全。

**完整交易日价格与量价。** 2026-09-29收盘 10.36 USD；当日+2.37%，5/20/60交易日-4.25%/+2.17%/-17.19%。20日均价10.37，50日均价10.06；20日高/低11.17/9.54；末日量/20日均量1.25倍，共104根日线。 20日相对QQQ为-0.78%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/NOK/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：2.56 / 6.90 / 14.32 USD。按网络基础设施与传统业务分部利润，最新Q2全文及ADS比例已核，重组现金与光网络增量分开。 Q2可比EPS0.07、报告EPS0；2028基准0.45要求光/IP增长覆盖重组与传统业务。USD/EUR=1.10是假设，已核1ADS=1普通股。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    0.25,
    0.45,
    0.7
  ],
  "pe": [
    12.0,
    18.0,
    24.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1.1,
  "currency": "USD",
  "input_currency": "EUR"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 光网络订单/利润不能补偿传统业务收缩且协同连续落后。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价10.36高于本轮作者基准价值6.90及合理参与上限7.25，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [追加完整财务报表](https://ml-eu.globenewswire.com/Resource/Download/3f0c9c33-04b4-4498-b6d8-f6705ef358a8)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/301_NOK.txt)
- [本轮重大事项追加核验](https://www.nokia.com/newsroom/nokia-corporation-report-for-q2-and-half-year-2026/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.nokia.com/system/files/2026-03/nokia-annual-report-2025.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000924613.json)；采集时间2026-09-30T07:49:11.687911+00:00，索引存在不等于全部正文已审核。


## NVDA — 研究门通过，账户门待确认

**业务与瓶颈。** 算力平台、网络及软件生态的收入与高利润兑现；FY27Q2收入962.21亿、GAAP经营利润637.34亿。

**反证、现金与稀释。** 出口限制、超大客户自研ASIC、资本开支周期；投资收益不能作为经常净利润。 H1 CFO74.421十亿美元，物业/设备及无形资产付款4.434十亿美元；该现金生成不是可全分配现金，另有42.404十亿美元股权投资购买和24.896十亿美元净债务发行。投资收益从盈利估值剔除，关注客户融资/循环资本风险；回购授权不当已回购。 9月3日8-K披露拟119亿美元收购Hugging Face，并有最高10亿美元员工股权留任计划；预计2027H1交割且须监管批准。估值不预先计协同，现金不得全部视作可分配，保留稀释及监管风险。

**完整交易日价格与量价。** 2026-09-29收盘 227.21 USD；当日-0.72%，5/20/60交易日-0.73%/+2.91%/+16.19%。20日均价222.64，50日均价216.98；20日高/低234.76/208.93；末日量/20日均量0.88倍，共104根日线。 20日相对SOXX为-8.12%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/NVDA/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：136.39 / 325.47 / 559.50 USD。规范化每股盈利与FCF并看；回购授权不是已执行回购，不提前减少股数。 FY27Q2调整EPS2.22；2028基准14较现季度规模参照8.88仍需增长，去投资收益、保留SBC，不提前计1500亿美元新增授权的回购减股。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    8.0,
    14.0,
    19.0
  ],
  "pe": [
    22.0,
    30.0,
    38.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**价格地图。** 高安全边际研究参考≤225；合理参与研究上限320 USD。两者都不是损失保证。超过上限须重新评估，不自动追涨。

**公司事件。** 9月3日8-K为拟收购Hugging Face，预计2027H1并须审批；9月28日回购是授权。SEC+IR未发现未来24小时已知重大公司事件。 [核查入口](https://investor.nvidia.com/home/default.aspx)

**经济失效。** 数据中心增长和毛利同时实质下修、客户投资回报恶化引发持续取消订单。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 经营现金与盈利规模支持基准325.47美元；资本配置、客户融资及拟收购Hugging Face的119亿美元价款另列风险，不靠授权回购减少预测股数。320为估值上限，不是建议等上涨后才买。

**触发与组合。** 估值日无新反证且价格不超过上限，可进入账户门计算；不要求完美回踩。若选择盘中执行路径，使用常规盘开盘30分钟后的承接/第二次上破，本报告未核9月30日分钟触发。不因一家公司通过而同时推荐多只高度相关AI股。账户资金、整数1股比例及计划损失未验证；不构成当前股数或订单指令。

**一手与本地证据。**

- [10-Q 2026-08-26](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/209_NVDA.txt)
- [NVDA 2027 Q2 10-Q-2026-08-27-08-33 (https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf)](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/035_NVDA.txt)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [IR事项补核](https://investor.nvidia.com/home/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001045810.json)；采集时间2026-09-30T07:49:11.618703+00:00，索引存在不等于全部正文已审核。


## TSM — 研究门通过，账户门待确认

**业务与瓶颈。** 先进制程和先进封装的制造及良率瓶颈；Q2营收1.270万亿台币、ADS EPS4.31美元。

**反证、现金与稀释。** 海外厂成本、资本开支、客户集中和地缘事件；股价单位为5股普通股对应的ADS。  H1 CFO469.14亿美元、物业设备支出267.99亿美元，粗差201.15亿美元，未扣另列融资现金流利息3.13亿美元。净利含非经营收益，2028模型不年化Q2。9月24日6-K披露已批准资本拨款而非当期全部现金支出。

**完整交易日价格与量价。** 2026-09-29收盘 456.94 USD；当日+0.90%，5/20/60交易日+1.09%/+10.02%/+1.14%。20日均价434.04，50日均价422.36；20日高/低459.43/407.81；末日量/20日均量1.01倍，共104根日线。 20日相对SOXX为-1.02%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/TSM/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：167.38 / 464.95 / 813.67 USD。规范化ADS盈利与资本开支/现金流交叉校准，不用台湾普通股EPS直接比美股。 按美国ADS，每ADS=5普通股；Q2 ADS EPS4.31。2028基准24反映先进制程增长及海外成本，压力12检验周期/资本开支。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    12.0,
    24.0,
    35.0
  ],
  "pe": [
    18.0,
    25.0,
    30.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**价格地图。** 高安全边际研究参考≤325；合理参与研究上限470 USD。两者都不是损失保证。超过上限须重新评估，不自动追涨。

**公司事件。** 9月24日6-K为8月资本拨款等月报；下一次月营收10月8日、财报10月15日，窗口外。SEC+IR未发现未来24小时已知重大事件。 [核查入口](https://investor.tsmc.com/english/financial-calendar)

**经济失效。** 先进制程领先或定价能力实质丧失，海外扩产长时间稀释利润与现金回报。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 先进制程/封装经营盈利与现金生成可核，2028 ADS EPS24、25倍退出PE得到464.95美元；仅留约1%误差带。海外厂成本和地缘跳空属于不能靠止损保证控制的残余风险。

**触发与组合。** 估值日无新反证且价格不超过上限，可进入账户门计算；不要求完美回踩。若选择盘中执行路径，使用常规盘开盘30分钟后的承接/第二次上破，本报告未核9月30日分钟触发。不因一家公司通过而同时推荐多只高度相关AI股。账户资金、整数1股比例及计划损失未验证；不构成当前股数或订单指令。

**一手与本地证据。**

- [6-K 2026-09-24](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000660/tsm-monthend6kx20260924.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/038_TSM.txt)
- [本轮重大事项追加核验](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/114aaca0fea2050e96b91fffbab9ed04ba09cd92/FS.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [公司事件核查路径](https://investor.tsmc.com/english/financial-calendar)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/final_decisions.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001046179.json)；采集时间2026-09-30T07:49:12.399818+00:00，索引存在不等于全部正文已审核。


## AVGO — 研究门通过，账户门待确认

**业务与瓶颈。** 定制AI芯片、交换与软件现金流；FY26Q3收入295.91亿，AI收入167亿、FCF137亿。

**反证、现金与稀释。** 超大客户集中、持续SBC、软件收购债务；定制芯片项目节奏可使增速跳变。  9个月CFO329.50亿美元、资本支出10.13亿美元，SBC62.87亿美元须作为持续成本考虑；现金239.75亿美元、账面债务594.19亿美元。9月10日S-4仅等本金交换6.54004亿美元2037债券，不是股票并购或新增负债。

**完整交易日价格与量价。** 2026-09-29收盘 355.10 USD；当日+1.58%，5/20/60交易日-2.59%/-4.12%/-5.03%。20日均价356.31，50日均价375.74；20日高/低372.70/335.81；末日量/20日均量1.40倍，共104根日线。 20日相对SOXX为-15.15%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AVGO/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：139.49 / 390.56 / 759.43 USD。优先规范化EPS和实际FCF，不能忽略SBC与未来客户融资安排。 FY26Q3 GAAP EPS2.68、FCF137亿美元；基准2028 EPS18需定制AI兑现和软件现金，保留持续SBC并审查客户融资。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    9.0,
    18.0,
    28.0
  ],
  "pe": [
    20.0,
    28.0,
    35.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**价格地图。** 高安全边际研究参考≤275；合理参与研究上限395 USD。两者都不是损失保证。超过上限须重新评估，不自动追涨。

**公司事件。** 9月2日8-K为已发布财报及9月30日常规派息；9月10日S-4仅登记同本金旧债交换，不新增负债或募集现金。SEC、IR新闻及活动页未发现未来24小时重大二元事件。 [核查入口](https://investors.broadcom.com/company-information/past-events)

**经济失效。** 主要定制项目失去份额且网络/软件现金流不能覆盖资本和偿债需求。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 定制AI与软件盈利、现金流支持基准390.56美元；SBC保留为成本，负债及客户集中保留风险。395为约1%估值误差带。

**触发与组合。** 估值日无新反证且价格不超过上限，可进入账户门计算；不要求完美回踩。若选择盘中执行路径，使用常规盘开盘30分钟后的承接/第二次上破，本报告未核9月30日分钟触发。不因一家公司通过而同时推荐多只高度相关AI股。账户资金、整数1股比例及计划损失未验证；不构成当前股数或订单指令。

**一手与本地证据。**

- [10-Q 2026-09-10](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/210_AVGO.txt)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/1730168/000119312526387881/d154803ds4.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [公司事件核查路径](https://investors.broadcom.com/company-information/past-events)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/final_decisions.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001730168.json)；采集时间2026-09-30T07:49:12.624126+00:00，索引存在不等于全部正文已审核。


## MU — 排除

**业务与瓶颈。** HBM与DRAM供需带来显著盈利，最新已报告为FY26Q3。

**反证、现金与稀释。** 9月30日盘后财报是24小时内重大二元事件；Q3高利润含景气峰值风险。  

**完整交易日价格与量价。** 2026-09-29收盘 1065.08 USD；当日+1.05%，5/20/60交易日-2.84%/+11.09%/+8.16%。20日均价1005.52，50日均价949.71；20日高/低1108.72/902.60；末日量/20日均量0.84倍，共104根日线。 20日相对QQQ为+8.14%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/MU/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：185.98 / 604.44 / 1239.88 USD。跨周期正常化EPS；本轮事件窗口不新建仓，财报后旧模型自动失效需刷新。 中周期而非当季EPS24.67乘四；2028三景检验ASP回落和HBM延续，9月30日财报后旧模型失效。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    30.0,
    65.0,
    100.0
  ],
  "pe": [
    8.0,
    12.0,
    16.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 9月30日16:30 EDT（北京时间10月1日04:30）Q4财报电话会；本截点未来24小时内重大公司二元事件，新建仓事件门失败，现有持仓不因此自动全卖。 [核查入口](https://investors.micron.com/news/press-release/2026/Micron-Technology-to-Report-Fiscal-Fourth-Quarter-Results-on-September-30-2026/default.aspx)

**经济失效。** 财报显示库存/供给反转或HBM认证、毛利和产能计划实质下修。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 未来24小时内有9月30日盘后财报，当前研究不做事件下注；财报发布后重算指引、存储周期及价格图。不是已有持仓全卖结论。

**一手与本地证据。**

- [IR事项补核](https://investors.micron.com/news/press-release/2026/Micron-Technology-to-Report-Fiscal-Fourth-Quarter-Results-on-September-30-2026/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000723125.json)；采集时间2026-09-30T07:49:12.868706+00:00，索引存在不等于全部正文已审核。


## ETN — 排除

**业务与瓶颈。** 配电设备与电气系统；Q2销售增长21%，美洲电气订单及积压强。

**反证、现金与稀释。** 订单不能代替现金、收购和Mobility交易仍有完成条件；融资后债务增加。   财报原文链接已经补入有效来源索引，来源为公司原文/SEC，非二手转述。

**完整交易日价格与量价。** 2026-09-29收盘 433.27 USD；当日+0.43%，5/20/60交易日-2.08%/+7.81%/+4.80%。20日均价417.02，50日均价420.37；20日高/低447.33/384.77；末日量/20日均量1.16倍，共104根日线。 20日相对QQQ为+4.86%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ETN/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：154.98 / 334.77 / 545.55 USD。规范化EPS估值；剥离/交易尚未完成，不提前将所有协同计入。 Q2 EPS2.11；2028基准16要求电气利润增长与交易整合，调整项不能无限加回，强景不能由订单增速直接替代。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    10.0,
    16.0,
    22.0
  ],
  "pe": [
    20.0,
    27.0,
    32.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 电气订单下降叠加交期缩短/提价回吐，导致增量利润不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价433.27高于本轮作者基准价值334.77及合理参与上限351.51，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [本轮重大事项追加核验](https://www.eaton.com/us/en-us/company/news-insights/news-releases/2026/eaton-reports-record-second-quarter-2026-results.html)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001551182.json)；采集时间2026-09-30T07:49:12.854664+00:00，索引存在不等于全部正文已审核。


## VRT — 排除

**业务与瓶颈。** 数据中心电力和热管理；Q2收入32.74亿、利润与订单规模提升。

**反证、现金与稀释。** 客户预付和积压质量、扩产成本、收购整合；9月24日宣布拟购King Environmental，预计Q4交割。  

**完整交易日价格与量价。** 2026-09-29收盘 248.34 USD；当日+1.76%，5/20/60交易日-2.02%/-4.01%/-22.02%。20日均价253.36，50日均价264.17；20日高/低295.34/226.94；末日量/20日均量1.25倍，共104根日线。 20日相对QQQ为-6.97%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/VRT/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：93.77 / 209.23 / 362.66 USD。以去除预付款波动后的现金流交叉检验EPS，收购未交割不计协同。 Q2 EPS1.27；2028基准9依赖订单兑现和利润率，不计未交割收购协同；预付款不能永久充当FCF。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    5.5,
    9.0,
    13.0
  ],
  "pe": [
    22.0,
    30.0,
    36.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 订单增长转负同时利润率和回款下降，或新液冷架构令现有系统份额受损。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价248.34高于本轮作者基准价值209.23及合理参与上限219.69，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [(https://www.sec.gov/Archives/edgar/data/1674101/000162828026050323/q22026exhibit991vrt07292026.htm)](https://www.sec.gov/Archives/edgar/data/1674101/000162828026050323/q22026exhibit991vrt07292026.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/045_VRT.txt)
- [8-K 2026-09-24](https://www.sec.gov/Archives/edgar/data/1674101/000162828026063311/vrt-20260924.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/047_VRT.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001674101.json)；采集时间2026-09-30T07:49:13.329222+00:00，索引存在不等于全部正文已审核。


## GEV — 排除

**业务与瓶颈。** 燃气轮机OEM、电网与服务，AI供电需求与长期交付能力有直接联系。

**反证、现金与稀释。** 116GW包含产能预留，不全是不可撤销订单；高FCF含预付款，风电拖累和交付成本。  

**完整交易日价格与量价。** 2026-09-29收盘 962.49 USD；当日+1.34%，5/20/60交易日+1.28%/+7.12%/-16.45%。20日均价936.45，50日均价968.41；20日高/低983.34/868.25；末日量/20日均量1.05倍，共104根日线。 20日相对QQQ为+4.16%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/GEV/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：136.39 / 511.45 / 1115.89 USD。使用扣预付款波动的中周期利润；不能把季度51亿FCF当永续现金流。 Q2 EPS2.47；基准2028 EPS22已含较大燃机/电网经营杠杆，剔除预付款FCF并给风电损失，116GW不全是固定订单。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    8.0,
    22.0,
    40.0
  ],
  "pe": [
    22.0,
    30.0,
    36.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 预留转单率下降或取消增加，燃机/电网订单不能带动可持续利润率。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价962.49高于本轮作者基准价值511.45及合理参与上限537.02，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [Six months ended June 30, 2026 (https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev2q2026form10-q.pdf)](https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev2q2026form10-q.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/049_GEV.txt)
- [GE Vernova 2nd Quarter 2026 Earnings Report Webcast | GE Vernova (https://www.gevernova.com/investors/events/2nd-quarter-2026-earnings-webcast)](https://www.gevernova.com/investors/events/2nd-quarter-2026-earnings-webcast)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/048_GEV.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001996810.json)；采集时间2026-09-30T07:49:14.068758+00:00，索引存在不等于全部正文已审核。


## COHR — 排除

**业务与瓶颈。** 光器件、激光与光模块垂直制造；Q4收入20.46亿、非GAAP EPS1.74，毛利改善。

**反证、现金与稀释。** 全年经营现金流0.795亿对资本开支11.029亿；优先股、债务、营运资本及持续SBC影响股东收益。   年报EPS附注已核：FY26稀释股数195.387百万，含Series B转换影响12.419百万；6月末Series B已发行股为0，不能继续说全部优先股未核。FY26 CFO79.514百万、资本支出1102.909百万，增长现金消耗仍是风险。按已含转换的EPS做2028基准10、PE28的现值216.98，当前292.21需要超出基准的兑现；不靠把全部融资现金加值证明便宜。

**完整交易日价格与量价。** 2026-09-29收盘 292.21 USD；当日+3.46%，5/20/60交易日-5.86%/+5.18%/-12.96%。20日均价291.27，50日均价297.00；20日高/低332.86/255.25；末日量/20日均量0.84倍，共104根日线。 20日相对QQQ为+2.22%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/COHR/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：61.99 / 216.98 / 461.08 USD。以正常化现金生成和完全稀释EPS交叉估值；不把收入增长直接变为股东FCF。 FY26 EPS4.12；基准2028 EPS10依赖光模块/激光器产能释放，FY26末Series B已为零，稀释股与新融资已核；经营现金弱，增长仍是敏感性。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    4.0,
    10.0,
    17.0
  ],
  "pe": [
    20.0,
    28.0,
    35.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 扩产不能转化为可收回现金，库存/应收持续吞噬利润或光模块价格竞争侵蚀毛利。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价292.21高于本轮作者基准价值216.98及合理参与上限227.83，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-K 2026-08-14](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/iivi-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/211_COHR.txt)
- [(https://www.sec.gov/Archives/edgar/data/820318/000119312526346860/d128030dex991.htm)](https://www.sec.gov/Archives/edgar/data/820318/000119312526346860/d128030dex991.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/051_COHR.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000820318.json)；采集时间2026-09-30T07:49:14.640266+00:00，索引存在不等于全部正文已审核。


## LITE — 排除

**业务与瓶颈。** 高速激光器、云光模块与CPO相关产能；AI光连接需求有业务基础。

**反证、现金与稀释。** FY26巨额债务转换/清偿会计损失，不能视作经营崩溃；同样不能忽略转换稀释、优先股和客户预付款。   年报已核8月14日普通股89.7百万，另有约2.9百万NVIDIA优先股一对一转换及FY26反稀释的转换/激励证券。以106百万未来股数作压力桥，相对于89.7百万约增加18%；原EPS20不能当保守基准。CFO751.4百万减Capex451.3百万为300.1百万，不能支持当前价格已隐含的利润而不依赖后续大幅成长。原三景仅敏感性，当前价相对基准过高。

**完整交易日价格与量价。** 2026-09-29收盘 973.49 USD；当日+5.66%，5/20/60交易日+2.94%/+6.42%/+33.13%。20日均价915.95，50日均价866.99；20日高/低1026.76/818.89；末日量/20日均量0.93倍，共104根日线。 20日相对QQQ为+3.47%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/LITE/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：123.99 / 464.95 / 1239.88 USD。必须重建转换后完全稀释股数与规范化利润；净亏损EPS−92.96不可直接套PE。 FY26经营利润5.248亿美元、转换后基本股约89.7百万；2028基准EPS20已要求大幅放量，不用巨额清偿损失EPS作锚。稀释来源已核：基本89.7百万股之外仍有优先股、转换及RSU，未来股数压力约106百万。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    8.0,
    20.0,
    40.0
  ],
  "pe": [
    20.0,
    30.0,
    40.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 产能增加后单位毛利仍恶化，或下一代激光器认证/主要客户份额落后。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价973.49高于本轮作者基准价值464.95及合理参与上限488.20，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-K 2026-08-17](https://www.sec.gov/Archives/edgar/data/1633978/000162828026057358/lite-20260627.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/212_LITE.txt)
- [Lumentum - Quarterly Results (https://investor.lumentum.com/quarterly-results/default.aspx/1000/default.aspx)](https://investor.lumentum.com/quarterly-results/default.aspx/1000/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/052_LITE.txt)
- [Lumentum - Investor Relations (https://investor.lumentum.com/overview/default.aspx)](https://investor.lumentum.com/overview/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/053_LITE.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001633978.json)；采集时间2026-09-30T07:49:14.645261+00:00，索引存在不等于全部正文已审核。


## MRVL — 排除

**业务与瓶颈。** 定制芯片、DSP与光互连硅片；FY27Q2收入27.393亿、数据中心增长46%。

**反证、现金与稀释。** GAAP EPS0.33与调整0.94差距大；客户定制项目集中、收购、SBC及NVIDIA竞争。  

**完整交易日价格与量价。** 2026-09-29收盘 263.27 USD；当日+4.51%，5/20/60交易日+0.35%/+24.38%/+5.62%。20日均价237.23，50日均价223.20；20日高/低267.48/200.62；末日量/20日均量0.73倍，共104根日线。 20日相对QQQ为+21.43%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/MRVL/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：42.62 / 139.49 / 323.92 USD。以持续SBC为成本；10月6日Investor Day是下一次假设复核点。 Q2 GAAP EPS0.33、调整0.94；基准6依赖项目放量和真实利润杠杆，不能把调整差额全当非经常；10月6日后刷新。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.5,
    6.0,
    11.0
  ],
  "pe": [
    22.0,
    30.0,
    38.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 项目量产延期或主客户转单，收入增长无法形成GAAP及每股现金利润。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价263.27高于本轮作者基准价值139.49及合理参与上限146.46，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-28](https://www.sec.gov/Archives/edgar/data/1835632/000183563226000025/mrvl-20260801.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/213_MRVL.txt)
- [8-K 2026-09-25](https://www.sec.gov/Archives/edgar/data/1835632/000162828026063592/mrvl-20260925.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/056_MRVL.txt)
- [Financial Results | Marvell Technology, Inc. (MRVL) (https://investor.marvell.com/financial-information/financial-results)](https://investor.marvell.com/financial-information/financial-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/055_MRVL.txt)
- [August 27, 2026 - EXHIBIT 99.1 - 8-K: Current report | Marvell Technology, Inc. (MRVL) (https://investor.marvell.com/sec-filings/all-sec-filings/content/0001835632-26-000022/q227_8kx812026ex-991.htm)](https://investor.marvell.com/sec-filings/all-sec-filings/content/0001835632-26-000022/q227_8kx812026ex-991.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/054_MRVL.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001835632.json)；采集时间2026-09-30T07:49:14.852722+00:00，索引存在不等于全部正文已审核。


## DELL — 排除

**业务与瓶颈。** AI服务器与企业基础设施的规模交付；FY27Q2收入469.7亿、调整EPS7.04。

**反证、现金与稀释。** 低毛利硬件、客户集中、营运资本和融资业务债务；不可给收入统一软件倍数。  

**完整交易日价格与量价。** 2026-09-29收盘 539.59 USD；当日-0.71%，5/20/60交易日-1.70%/+18.33%/+31.03%。20日均价537.72，50日均价481.82；20日高/低595.51/421.89；末日量/20日均量2.10倍，共104根日线。 20日相对QQQ为+15.37%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/DELL/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：195.28 / 418.46 / 748.58 USD。全年调整EPS25.50为公司指引，需扣持续SBC；用规范化EPS与现金流校准。 FY27调整EPS指引25.50，2028基准30保留持续SBC和硬件利润约束；不按服务器收入给予软件倍数。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    18.0,
    30.0,
    42.0
  ],
  "pe": [
    14.0,
    18.0,
    23.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** AI服务器毛利率/回款恶化抵消出货增长，或全年EPS指引实质下修。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价539.59高于本轮作者基准价值418.46及合理参与上限439.38，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-09-08](https://www.sec.gov/Archives/edgar/data/1571996/000157199626000046/dell-20260731.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/214_DELL.txt)
- [Dell Technologies Delivers Second Quarter Fiscal 2027 Financial Results | Dell USA (https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~09~dell-technologies-delivers-second-quarter-fiscal-2027-financial-results.htm)](https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~09~dell-technologies-delivers-second-quarter-fiscal-2027-financial-results.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/057_DELL.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001571996.json)；采集时间2026-09-30T07:49:15.082595+00:00，索引存在不等于全部正文已审核。


## HPE — 研究门通过，账户门待确认

**业务与瓶颈。** Juniper并入后网络业务、AI服务器和服务组合改善；Q3收入122亿、非GAAP EPS1.11。

**反证、现金与稀释。** 同比增速含并购，不能全称有机增长；债务、协同与服务器现金转换。  

**完整交易日价格与量价。** 2026-09-29收盘 61.49 USD；当日-1.82%，5/20/60交易日+0.75%/+17.71%/+42.50%。20日均价58.34，50日均价54.62；20日高/低65.65/45.70；末日量/20日均量1.71倍，共104根日线。 20日相对QQQ为+14.75%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/HPE/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：27.90 / 59.51 / 100.74 USD。以分部和持续SBC调整后的利润，Q3FCF9.58亿不能不顾季节性直接年化。 Q3 EPS1.06；2028基准4.8依赖Juniper整合与网络利润，倍数低于纯网络设备企业以反映服务器和债务。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    3.0,
    4.8,
    6.5
  ],
  "pe": [
    12.0,
    16.0,
    20.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**价格地图。** 高安全边际研究参考≤42；合理参与研究上限62 USD。两者都不是损失保证。超过上限须重新评估，不自动追涨。

**公司事件。** 今晚23:30北京时间有Networking Investor Day，属于已知时间风险；公告未显示重大二元结果，不自动否决。当天材料一旦改变假设，价格图即须重算。 [核查入口](https://www.hpe.com/us/en/newsroom/press-release/2026/09/hpe-to-webcast-networking-investor-day-event.html)

**经济失效。** 网络增长和协同未兑现同时服务器低毛利扩张，致ROIC低于融资成本。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 网络与Juniper利润贡献形成较低倍数参与路径；基准59.51美元，上限62保留约4%误差带。9个月经营现金42.29亿美元、现金62.16亿、债务202.44亿，含金融服务业务，不能视作纯网络轻资产公司。

**触发与组合。** 估值日无新反证且价格不超过上限，可进入账户门计算；不要求完美回踩。若选择盘中执行路径，使用常规盘开盘30分钟后的承接/第二次上破，本报告未核9月30日分钟触发。不因一家公司通过而同时推荐多只高度相关AI股。账户资金、整数1股比例及计划损失未验证；不构成当前股数或订单指令。

**一手与本地证据。**

- [10-Q 2026-09-03](https://www.sec.gov/Archives/edgar/data/1645590/000164559026000080/hpe-20260731.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/215_HPE.txt)
- [Sep 2 Q326 HPE Earnings Transcript (https://investors.hpe.com/~/media/Files/H/HP-Enterprise-IR/documents/q3-2026/q3-2026-transcript.pdf)](https://investors.hpe.com/~/media/Files/H/HP-Enterprise-IR/documents/q3-2026/q3-2026-transcript.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/060_HPE.txt)
- [IR事项补核](https://www.hpe.com/us/en/newsroom/press-release/2026/09/hpe-to-webcast-networking-investor-day-event.html)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001645590.json)；采集时间2026-09-30T07:49:16.793999+00:00，索引存在不等于全部正文已审核。


## WDC — 排除

**业务与瓶颈。** 云存储HDD容量与供给纪律，Q4收入37.5亿、FCF12.8亿。

**反证、现金与稀释。** GAAP EPS8.21高于调整3.56，投资收益不能年化；HAMR竞争与云客户周期。  

**完整交易日价格与量价。** 2026-09-29收盘 453.48 USD；当日+0.06%，5/20/60交易日-2.39%/+0.65%/-21.47%。20日均价449.87，50日均价472.78；20日高/低495.49/407.12；末日量/20日均量0.86倍，共104根日线。 20日相对QQQ为-2.30%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/WDC/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：61.99 / 185.98 / 387.46 USD。按中周期现金盈利而非重估净利；不能拿历史拆分前集团财报混算。 Q4调整EPS3.56对比GAAP8.21；2028基准16去重估收益，HDD中周期倍数不当软件平台。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    8.0,
    16.0,
    25.0
  ],
  "pe": [
    10.0,
    15.0,
    20.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 单TB价格/毛利持续回落且单位出货增长不足弥补，或客户转单。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价453.48高于本轮作者基准价值185.98及合理参与上限195.28，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-K 2026-08-14](https://www.sec.gov/Archives/edgar/data/106040/000162828026057139/wdc-20260703.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/216_WDC.txt)
- [(https://www.sec.gov/Archives/edgar/data/106040/000162828026053305/a4ex991-pressreleaseq426.htm)](https://www.sec.gov/Archives/edgar/data/106040/000162828026053305/a4ex991-pressreleaseq426.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/061_WDC.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000106040.json)；采集时间2026-09-30T07:49:17.502740+00:00，索引存在不等于全部正文已审核。


## STX — 排除

**业务与瓶颈。** HAMR产品升级与HDD单位容量提升；FY26自由现金流31亿。

**反证、现金与稀释。** 价格和毛利周期、技术良率与客户认证；股价上涨远超收入增长时须做反向估值。  

**完整交易日价格与量价。** 2026-09-29收盘 913.45 USD；当日-0.87%，5/20/60交易日-0.69%/+10.27%/+5.20%。20日均价857.85，50日均价854.64；20日高/低944.43/758.35；末日量/20日均量0.91倍，共104根日线。 20日相对QQQ为+7.32%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/STX/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：92.99 / 263.47 / 596.69 USD。规范化EPS/FCF，不能把本轮极高隐含增长视作必然。 FY26 EPS13.90；2028基准20、强景35分别要求HAMR利润增量不同，压力10为价格周期回落。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    10.0,
    20.0,
    35.0
  ],
  "pe": [
    12.0,
    17.0,
    22.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** HAMR成本/可靠性无法商业兑现，或云客户订购和行业供给纪律逆转。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价913.45高于本轮作者基准价值263.47及合理参与上限276.65，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-K 2026-08-04](https://www.sec.gov/Archives/edgar/data/1137789/000113778926000159/stx-20260703.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/217_STX.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001137789.json)；采集时间2026-09-30T07:49:15.869391+00:00，索引存在不等于全部正文已审核。


## FN — 条件观察

**业务与瓶颈。** 光模块精密制造服务随800G/1.6T客户放量；FY26营收46.4亿、GAAP EPS13.05。

**反证、现金与稀释。** 制造服务利润率、客户集中、客户自建和产能约束；订单增长未必长期保持高倍数。 FY26净利含56.743百万非上市股权收益，规范化EPS约11.5而非直接13.05。CFO256.725百万减Capex252.503百万仅4.222百万；存货/应收共消耗702.159百万，股东现金转换偏弱。现金及短投875.1百万支持扩产，但2027Capex预计继续上升；须明确将此列为现金转换验收缺口。 

**完整交易日价格与量价。** 2026-09-29收盘 424.12 USD；当日+3.45%，5/20/60交易日+5.03%/+2.71%/-15.30%。20日均价401.43，50日均价452.36；20日高/低428.50/373.70；末日量/20日均量0.73倍，共104根日线。 20日相对QQQ为-0.24%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/FN/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：167.38 / 426.21 / 743.93 USD。Q1FY27收入指引13.75–14.25亿；以保留SBC的规范化利润估值。 FY26 GAAP EPS13.05，Q1FY27收入指引13.75–14.25亿美元；基准EPS22需要增长保持且制造利润率不下降。扩产FCF单独检验。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    12.0,
    22.0,
    32.0
  ],
  "pe": [
    18.0,
    25.0,
    30.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 最新年报及IR活动表已核，最后归档8月18日，未发现未来24小时已知重大公司事件。 [核查入口](https://investor.fabrinet.com/node/5826)

**经济失效。** 主客户转移制造或订单增速显著下修且经营现金流不再匹配利润。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 扩产阶段现金转换能否在现有流动性内恢复，缺少足以支撑基准EPS的现金回收桥。

**未闭合项（1项）。** 扩产阶段现金转换能否在现有流动性内恢复，缺少足以支撑基准EPS的现金回收桥。。Owner=current_thread_direct。以FY26年报营运资本和FY27扩产披露建立现金收款/库存/资本支出桥；只补这一现金质量缺口。无法从公开披露界定时标证据管线受阻及研究未完成，不重复无限观察。 复核到期：2026-10-02T18:00:00+08:00。

**一手与本地证据。**

- [10-K 2026-08-18](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/fn-20260626.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/218_FN.txt)
- [prior located primary, verify period](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000026/fn-2026811xex991q426.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/243_FN.txt)
- [IR事项补核](https://investor.fabrinet.com/node/5826)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001408710.json)；采集时间2026-09-30T07:49:15.954234+00:00，索引存在不等于全部正文已审核。


## AMKR — 研究未完成

**业务与瓶颈。** 先进封装和测试外包，Q2收入18.98亿美元、EPS0.70；Q3 EPS指引0.72–0.82。

**反证、现金与稀释。** 全年资本开支25–30亿美元，期末现金与债务均约25亿美元；美国厂折旧、补贴和股东回报可能错配。   完整6月30日10-Q已补核：H1 CFO381.573百万，支付PPE688.425百万，出售资产与补贴36.992百万，FCF负269.860百万。0% 2031可转债10亿美元及最多1.5亿美元期权须计转股；转股价106.37美元、cap call不保证消除一切稀释。9月8日第二阶段将Arizona总投资升至120亿美元，是多年项目，不能视为2026一次性支付，也不能忽略对后续资本回报的影响。当前唯一核心缺口是多年资金来源/折旧及订单利润的闭合预算。

**完整交易日价格与量价。** 2026-09-29收盘 54.14 USD；当日+1.81%，5/20/60交易日-0.82%/+14.46%/-22.52%。20日均价50.13，50日均价52.47；20日高/低55.13/45.30；末日量/20日均量0.91倍，共104根日线。 20日相对SOXX为+3.42%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AMKR/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：17.44 / 59.67 / 115.08 USD。规范化EPS结合扩产FCF；Q2计算业务仅22%，先进产品分类不能全部等同AI。 Q3 EPS指引0.72–0.82，基准2028 EPS3.5并非大幅外推；资本开支25–30亿美元及美国厂折旧使盈利价值需FCF复核。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    1.5,
    3.5,
    5.5
  ],
  "pe": [
    15.0,
    22.0,
    27.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 先进封装订单不足以覆盖新增折旧和资本成本，或扩建资金缺口依赖大额稀释。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** Arizona 120亿美元多年项目的资金/折旧/订单利润预算；9月新项目之后IR未来事件交叉核查

**未闭合项（2项）。** Arizona 120亿美元多年项目的资金/折旧/订单利润预算；9月新项目之后IR未来事件交叉核查。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [完整Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1047127/000104712726000046/amkr-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/307_AMKR.txt)
- [本轮重大事项追加核验](https://ir.amkor.com/press-releases)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://ir.amkor.com/news-releases/news-release-details/amkor-technology-announces-phase-2-arizona-advanced-packaging)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001047127.json)；采集时间2026-09-30T07:49:18.427483+00:00，索引存在不等于全部正文已审核。


## ASX — 排除

**业务与瓶颈。** Q2收入1910.64亿台币、稀释ADS EPS0.292美元；封装52%、测试13%、EMS34%。

**反证、现金与稀释。** H1 CFO834.01亿对资本支出1239.41亿台币；非经营收益45.66亿影响单季净利，不能当AI纯业务。  

**完整交易日价格与量价。** 2026-09-29收盘 45.31 USD；当日+3.47%，5/20/60交易日+0.24%/+22.63%/+4.59%。20日均价40.67，50日均价38.65；20日高/低45.74/36.24；末日量/20日均量1.02倍，共104根日线。 20日相对SOXX为+11.59%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ASX/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：9.92 / 27.28 / 56.41 USD。按ADS归母规范化EPS并复核ATM与EMS盈利；不能把台股EPS与美元价格直接相除。 Q2稀释ADS EPS0.292，剔除汇兑/投资收益并使用美国ADS单位；基准2028 1.6需ATM扩产利润兑现，负FCF仍须解释。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    0.8,
    1.6,
    2.6
  ],
  "pe": [
    16.0,
    22.0,
    28.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 先进封装利用率/盈利不随扩产增加，或ATM增长被EMS与资本开支拖累。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价45.31高于本轮作者基准价值27.28及合理参与上限28.64，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [Home | ASE Holdings (https://www.aseglobal.com/)](https://www.aseglobal.com/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/069_ASX.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001122411.json)；采集时间2026-09-30T07:49:17.052704+00:00，索引存在不等于全部正文已审核。


## TER — 排除

**业务与瓶颈。** 测试设备为主体，Q2营收13.29亿，其中机器人仅1亿；HBM和DRAM测试受益。

**反证、现金与稀释。** 机器人主题不能为全部半导体测试业务重估；测试周期与客户集中。  

**完整交易日价格与量价。** 2026-09-29收盘 403.02 USD；当日+0.43%，5/20/60交易日+1.09%/+15.20%/+6.19%。20日均价368.30，50日均价371.96；20日高/低415.61/326.00；末日量/20日均量0.97倍，共104根日线。 20日相对SOXX为+4.17%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/TER/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：92.99 / 238.68 / 447.91 USD。分部利润与中周期EPS，不把机器人小分部当全公司的右尾主体。 Q2 EPS2.38；2028基准11主要来自半导体测试，机器人小分部不单独给予全公司极高估值。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    6.0,
    11.0,
    17.0
  ],
  "pe": [
    20.0,
    28.0,
    34.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 测试收入连续下滑且机器人业务不能改善资本回报。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价403.02高于本轮作者基准价值238.68及合理参与上限250.61，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [Financial Results :: Teradyne, Inc. (TER) (https://investors.teradyne.com/financial-results)](https://investors.teradyne.com/financial-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/071_TER.txt)
- [Teradyne Reports Second Quarter 2026 Results :: Teradyne, Inc. (TER) (https://investors.teradyne.com/news-events/press-releases/detail/445/teradyne-reports-second-quarter-2026-results)](https://investors.teradyne.com/news-events/press-releases/detail/445/teradyne-reports-second-quarter-2026-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/070_TER.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000097210.json)；采集时间2026-09-30T07:49:17.871220+00:00，索引存在不等于全部正文已审核。


## KLAC — 排除

**业务与瓶颈。** 先进制程与先进封装增加检测/量测需求，FY26收入135.8亿、FCF37.7亿。

**反证、现金与稀释。** 客户资本开支周期和出口限制；已在6月11日实施10比1拆股，所有EPS需同口径。  

**完整交易日价格与量价。** 2026-09-29收盘 196.53 USD；当日+3.89%，5/20/60交易日+4.36%/+12.01%/-15.76%。20日均价180.14，50日均价188.20；20日高/低197.47/165.89；末日量/20日均量1.01倍，共104根日线。 20日相对SOXX为+0.98%个百分点差（非超额收益率比值）。 6月10比1拆股已识别；本20/60日窗口均在拆股后，EPS也使用拆股后口径。 [行情来源](https://api.nasdaq.com/api/quote/KLAC/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：64.78 / 139.49 / 230.54 USD。当前FY26EPS3.66和Q4 EPS1.04均为拆股后，历史价格需同口径。 所有数值为10比1拆股后；FY26 EPS3.66，2028基准6要求检测强度增长与周期持续。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    3.8,
    6.0,
    8.5
  ],
  "pe": [
    22.0,
    30.0,
    35.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 先进节点检测强度增长不足抵消WFE周期下行，服务与毛利同步恶化。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价196.53高于本轮作者基准价值139.49及合理参与上限146.46，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-K 2026-08-06](https://www.sec.gov/Archives/edgar/data/319201/000031920126000027/klac-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/219_KLAC.txt)
- [prior located primary, verify period](https://www.sec.gov/Archives/edgar/data/319201/000031920126000024/exhibit991earningsrelease7.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/244_KLAC.txt)
- [Press Releases :: KLA Corporation (KLAC) (https://ir.kla.com/news-events/press-releases)](https://ir.kla.com/news-events/press-releases)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/073_KLAC.txt)
- [KLA CORPORATION REPORTS FISCAL 2026 FOURTH QUARTER AND FULL YEAR RESULTS :: KLA Corporation (KLAC) (https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full)](https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/072_KLAC.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000319201.json)；采集时间2026-09-30T07:49:18.604590+00:00，索引存在不等于全部正文已审核。


## LRCX — 排除

**业务与瓶颈。** 高层数NAND、DRAM和先进制程刻蚀/沉积；6月季度收入67.2亿、EPS1.81。

**反证、现金与稀释。** 存储扩产周期、出口许可、先进节点竞争；强景气利润不能永久化。  

**完整交易日价格与量价。** 2026-09-29收盘 323.86 USD；当日+2.99%，5/20/60交易日+4.15%/+7.42%/-7.52%。20日均价298.18，50日均价304.95；20日高/低328.32/265.37；末日量/20日均量1.17倍，共104根日线。 20日相对SOXX为-3.62%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/LRCX/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：92.99 / 216.98 / 395.21 USD。用跨周期EPS压力/基准/强情景而非峰值单季年化。 FY26 EPS5.76、末季1.81；2028基准10须刻蚀/沉积增长，压力6体现存储扩产回落而非将峰值永久化。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    6.0,
    10.0,
    15.0
  ],
  "pe": [
    20.0,
    28.0,
    34.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 刻蚀/沉积份额下降或客户扩产取消，订单和毛利同步转弱。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价323.86高于本轮作者基准价值216.98及合理参与上限227.83，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-K 2026-08-07](https://www.sec.gov/Archives/edgar/data/707549/000070754926000037/lrcx-20260628.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/220_LRCX.txt)
- [Lam Research Corporation Reports Financial Results for the Quarter Ended June 28, 2026 - Jul 29, 2026 (https://investor.lamresearch.com/2026-07-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-June-28%2C-2026)](https://investor.lamresearch.com/2026-07-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-June-28%2C-2026)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/075_LRCX.txt)
- [Lam Research Corporation Reports Financial Results for the Quarter Ended June 28, 2026 - Jul 29, 2026 (https://investor.lamresearch.com/2026-07-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-June-28%2C-2026?asPDF=1)](https://investor.lamresearch.com/2026-07-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-June-28%2C-2026?asPDF=1)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/074_LRCX.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000707549.json)；采集时间2026-09-30T07:49:18.767160+00:00，索引存在不等于全部正文已审核。


## AMAT — 排除

**业务与瓶颈。** 材料工程、沉积与先进封装设备；FY26Q3收入91.15亿、GAAP EPS3.17。

**反证、现金与稀释。** 出口监管、客户自研/竞争技术、资本开支周期；研发与扩建资金需求。  

**完整交易日价格与量价。** 2026-09-29收盘 512.01 USD；当日+5.19%，5/20/60交易日+8.37%/+11.70%/-13.63%。20日均价455.75，50日均价489.11；20日高/低513.28/411.51；末日量/20日均量0.88倍，共104根日线。 20日相对SOXX为+0.66%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AMAT/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：139.49 / 329.34 / 557.95 USD。正常化EPS保留SBC；未来利润率不能机械固定在周期高点。 Q3 EPS3.17；2028基准17对应先进节点/封装增长，压力情景检验出口与WFE周期。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    10.0,
    17.0,
    24.0
  ],
  "pe": [
    18.0,
    25.0,
    30.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 核心设备份额受损且客户WFE计划下调，研发投资回报不兑现。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价512.01高于本轮作者基准价值329.34及合理参与上限345.81，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-20](https://www.sec.gov/Archives/edgar/data/6951/000162828026058235/amat-20260726.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/221_AMAT.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000006951.json)；采集时间2026-09-30T07:49:19.775989+00:00，索引存在不等于全部正文已审核。


## ASML — 排除

**业务与瓶颈。** EUV/High-NA与先进光刻生态，Q2销售93亿欧元、净利29亿欧元。

**反证、现金与稀释。** 订单波动、客户资本开支和出口控制；EUV/High-NA部署时间影响利润实现。   财报原文链接已经补入有效来源索引，来源为公司原文/SEC，非二手转述。

**完整交易日价格与量价。** 2026-09-29收盘 1834.39 USD；当日+3.56%，5/20/60交易日+4.95%/+8.16%/+0.51%。20日均价1697.16，50日均价1719.96；20日高/低1841.77/1572.84；末日量/20日均量1.14倍，共104根日线。 20日相对QQQ为+5.21%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ASML/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：639.31 / 1227.48 / 2105.47 USD。先以欧元估值再换算美元普通注册股，汇率是情景假设而非永久常数。 Q2 EPS7.59欧元；2028基准45需EUV/High-NA交付。美元图使用USD/EUR=1.10假设，非实时汇率；汇率±10%价值同步变动。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    30.0,
    45.0,
    65.0
  ],
  "pe": [
    25.0,
    32.0,
    38.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1.1,
  "currency": "USD",
  "input_currency": "EUR"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 关键客户持续延后先进制程扩产，High-NA经济性无法带动复购。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价1834.39高于本轮作者基准价值1227.48及合理参与上限1288.85，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [本轮重大事项追加核验](https://www.asml.com/en/news/press-releases/2026/q2-2026-financial-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.asml.com/en/investors/financial-results/q2-2026)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000937966.json)；采集时间2026-09-30T07:49:19.300101+00:00，索引存在不等于全部正文已审核。


## ACMR — 排除

**业务与瓶颈。** 中国半导体清洗与相关设备本土化，Q2营收2.929亿。

**反证、现金与稀释。** 归母净利高于经营利润，投资收益/非控股权益必须剔除；出口限制、中国子公司可用现金不同。   Q2稀释股数71.839百万、H1为70.679百万；持有ACM Shanghai约73.2%。基准EPS3按上市主体归母规范化盈利，剔除投资收益，不把合并利润全归母。即使把现金969.229百万、定存365.055百万与短投105.091百万不扣债务地乘73.2%再除74百万股，额外上界仅约14.24美元，基准39.43加此宽松上界仍低于现价75.61；此上界不是可分配现金事实。

**完整交易日价格与量价。** 2026-09-29收盘 75.61 USD；当日-0.45%，5/20/60交易日-0.25%/+3.83%/-23.25%。20日均价72.26，50日均价77.05；20日高/低82.78/62.78；末日量/20日均量1.23倍，共104根日线。 20日相对SOXX为-7.20%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ACMR/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：13.14 / 39.43 / 87.62 USD。采用归母正常化EPS，合并现金不可全视作上市股东可支配净现金。 2028归母规范化EPS而非合并净利；剔除投资收益/非控股份额，使用15%折现反映政策、治理及现金可用性。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    1.5,
    3.0,
    5.0
  ],
  "pe": [
    12.0,
    18.0,
    24.0
  ],
  "rate": 0.15,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 核心客户订单/许可被限制且无法替代，或增长不能传导到美国上市主体每股收益。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价75.61高于本轮作者基准价值39.43及合理参与上限41.40，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-07](https://www.sec.gov/Archives/edgar/data/1680062/000162828026054832/acmr-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/222_ACMR.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001680062.json)；采集时间2026-09-30T07:49:20.367943+00:00，索引存在不等于全部正文已审核。


## ENTG — 排除

**业务与瓶颈。** 先进制程纯度、过滤和材料消耗增加；Q2收入8.832亿、GAAP EPS0.61。

**反证、现金与稀释。** 期末债务34.56亿远高于现金3.536亿；扩产、整合和周期回落限制估值弹性。  

**完整交易日价格与量价。** 2026-09-29收盘 154.77 USD；当日+2.75%，5/20/60交易日+2.42%/+14.40%/+6.61%。20日均价140.43，50日均价140.21；20日高/低156.65/125.78；末日量/20日均量0.95倍，共104根日线。 20日相对QQQ为+11.45%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ENTG/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：38.75 / 104.61 / 185.98 USD。去杠杆后的正常化每股盈利与FCF，调整EPS0.93不能全作所有者盈利。 Q2 GAAP EPS0.61；2028基准5需耗材强度与去杠杆，债务利息已应体现在EPS，不能另把总现金作为净现金加上。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.5,
    5.0,
    7.5
  ],
  "pe": [
    20.0,
    27.0,
    32.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 利用率/耗材强度未改善而债务与资本成本持续挤压股东现金。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价154.77高于本轮作者基准价值104.61及合理参与上限109.85，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-04](https://www.sec.gov/Archives/edgar/data/1101302/000110130226000150/entg-20260627.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/223_ENTG.txt)
- [(https://www.sec.gov/Archives/edgar/data/1101302/000110130226000146/entgq22026ex992.htm)](https://www.sec.gov/Archives/edgar/data/1101302/000110130226000146/entgq22026ex992.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/083_ENTG.txt)
- [(https://www.sec.gov/Archives/edgar/data/1101302/000110130226000146/entgq22026ex991.htm)](https://www.sec.gov/Archives/edgar/data/1101302/000110130226000146/entgq22026ex991.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/082_ENTG.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001101302.json)；采集时间2026-09-30T07:49:20.790628+00:00，索引存在不等于全部正文已审核。


## RMBS — 条件观察

**业务与瓶颈。** DDR5/内存接口芯片与IP；Q2收入2.074亿、GAAP EPS0.61，产品收入增长。

**反证、现金与稀释。** 授权确认波动、DDR周期、客户集中；部分XBRL仍停留Q1须以Q2原公告纠正。  Q2经营现金6120万美元、资本支出1220万美元；净股权结算税款1430万美元另列融资流，不能视为零成本。8月5日1亿美元ASR不提前计未来注销；9月4日8-K会计负责人退休不涉及已披露意见分歧。

**完整交易日价格与量价。** 2026-09-29收盘 103.12 USD；当日+0.98%，5/20/60交易日-2.01%/+18.95%/-8.94%。20日均价91.24，50日均价93.26；20日高/低108.62/80.00；末日量/20日均量1.38倍，共104根日线。 20日相对SOXX为+7.92%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/RMBS/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：37.51 / 92.99 / 167.38 USD。分开经常产品利润与授权收益，再用规范化EPS估值。 Q2 GAAP EPS0.61；基准2028 EPS4需要内存接口产品增长，授权确认波动不当经常产品收入。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.2,
    4.0,
    6.0
  ],
  "pe": [
    22.0,
    30.0,
    36.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 9月4日8-K为已公告会计负责人退休/交接，8月5日为1亿美元ASR。SEC和IR最新新闻未发现未来24小时重大公司事件。 [核查入口](https://investor.rambus.com/press-releases/default.aspx)

**经济失效。** 内存接口份额或新标准认证落后，产品增长不能补足授权下滑。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 价格尚高于合理参与上限98美元；唯一缺口为价格。

**未闭合项（1项）。** 价格尚高于合理参与上限98美元；唯一缺口为价格。。Owner=current_thread_direct。当前Q2财报含现金、回购及产品/IP收入拆分已核；按下一完整交易日价格复核，满足上限即升级，不再临时要求完美回踩。 复核到期：2026-10-01T09:00:00+08:00。

**一手与本地证据。**

- [Rambus Reports Second Quarter 2026 Financial Results - Rambus (https://www.rambus.com/second-quarter-2026-financial-results/)](https://www.rambus.com/second-quarter-2026-financial-results/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/084_RMBS.txt)
- [Rambus Inc. - Press Releases (https://investor.rambus.com/press-releases/default.aspx)](https://investor.rambus.com/press-releases/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/085_RMBS.txt)
- [本轮重大事项追加核验](https://investor.rambus.com/press-releases/press-release-details/2026/Rambus-Reports-Second-Quarter-2026-Financial-Results/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/917273/000119312526383630/d80115d8k.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000917273.json)；采集时间2026-09-30T07:49:20.432757+00:00，索引存在不等于全部正文已审核。


## INTC — 排除

**业务与瓶颈。** CPU、代工和先进封装转型；Q2收入161.28亿、经营利润17.96亿，有经营改善。

**反证、现金与稀释。** GAAP净亏110.33亿含会计/非经营影响；客户验证、巨额投资、股权融资与政府安排。   完整Q2 10-Q已补核：Products季度经营利润4.817十亿美元，Foundry亏2.089十亿美元，Corporate未分配亏1.416十亿美元；Foundry收入大多集团内部，不能按57.65亿美元全作外部销售。Q2净亏主要受政府托管股份重估约125亿美元影响，不等于现金经营亏损。政府未释放托管股7100万及有条件Foundry控制权权证2.41亿股须另计；未来股数5.5–6.0十亿足以容纳已知部分及SBC压力情景，并不承诺未来不再融资。估值交叉桥（作者2028假设）：Products EBIT22/28/38十亿，Foundry -8/-4/+2十亿，企业成本4/3/3十亿，净利息1.5十亿、税20%、股数5.5/5.7/6.0十亿，EPS约1.24/2.74/4.73。原EPS1/3/6情景已更宽松，仍不支持当前115.93处于合理基准区。现金短投29.727十亿低于债务50.537十亿；不得给现金和资产重复加值。

**完整交易日价格与量价。** 2026-09-29收盘 115.93 USD；当日-0.09%，5/20/60交易日-6.40%/+29.52%/-5.13%。20日均价107.19，50日均价99.85；20日高/低127.44/85.72；末日量/20日均量1.08倍，共104根日线。 20日相对QQQ为+26.56%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/INTC/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：11.62 / 51.15 / 130.19 USD。分开产品和Foundry，剔除分部间销售；不能把58亿Foundry收入当外部收入。 净利会计噪声大；这是转型成功程度的盈利敏感性，不替代产品/Foundry SOTP及政府/融资权益桥接。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    1.0,
    3.0,
    6.0
  ],
  "pe": [
    15.0,
    22.0,
    28.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 外部代工客户未兑现、工艺良率落后，新增投资仍不能赚取资本成本。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价115.93高于本轮作者基准价值51.15及合理参与上限53.70，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [完整Q2 10-Q](https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/308_INTC.txt)
- [Intel Reports Second-Quarter 2026 Financial Results :: Intel Corporation (INTC) (https://www.intc.com/news-events/press-releases/detail/1776/intel-reports-second-quarter-2026-financial-results)](https://www.intc.com/news-events/press-releases/detail/1776/intel-reports-second-quarter-2026-financial-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/087_INTC.txt)
- [Intel Reports Second-Quarter 2026 Financial Results - Intel Newsroom (https://newsroom.intel.com/corporate/intel-reports-second-quarter-2026-financial-results)](https://newsroom.intel.com/corporate/intel-reports-second-quarter-2026-financial-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/086_INTC.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000050863.json)；采集时间2026-09-30T07:49:22.107167+00:00，索引存在不等于全部正文已审核。


## SKHY — 排除

**业务与瓶颈。** HBM、DRAM和NAND高端组合，Q2现金与盈利显著增长。

**反证、现金与稀释。** Q2净利润高于收入，必须拆投资/重估收益；KRW与美国ADS比例已核，模型不纳入非经营重估。 SEC IPO招股书已查到每ADS=0.1普通股。Q2净利超过收入，必须剔除非经营收益；不能拿韩股EPS直接比美元ADS。  ADS招股书已核：发行后728,865,500普通股，1ADS=0.1普通股；不能直接使用韩股EPS除美元ADS股价。采用未来740/750/770百万普通股，不把回购授权当已注销股。最新Q2净利高于收入，模型完全舍弃该非经营收益，改用中周期收入、税后经营净利率和未来净现金；压力/基准/强景不将76%季度营业利润率永续化。汇率假设1450KRW/USD，不是实时报价。资产重估明细仍未拆成逐项当期利润桥，但不进入估值分子；该缺项不会增加估值，不能据此掩盖当前价格相对中周期基准偏高。

**完整交易日价格与量价。** 2026-09-29收盘 186.68 USD；当日+2.62%，5/20/60交易日-4.45%/+13.43%/UNKNOWN。20日均价182.24，50日均价165.23；20日高/低199.87/157.73；末日量/20日均量0.94倍，共57根日线。 20日相对QQQ为+10.47%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/SKHY/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：60.81 / 139.78 / 255.50 USD。使用IPO后普通股本、中周期经营净利率及0.1普通股/ADS换算；禁止直接把韩股EPS与美元报价相除。 金额为百万KRW，股数为百万普通股；乘0.1转换ADS，再除1450汇率假设。2028中周期收入360/480/620万亿KRW、税后经营净利率22/28/32%，未来净现金50/80/110万亿扣扩产预算后的情景。剔除全部投资重估，不用Q2净利年化；IPO后728.8655百万普通股为股本起点。强景并非最大可能收益。

```json
{
  "method": "net_profit",
  "year": 2028,
  "rate": 0.12,
  "years": 2.25,
  "revenue_m": [
    360000000,
    480000000,
    620000000
  ],
  "net_margin": [
    0.22,
    0.28,
    0.32
  ],
  "pe": [
    10,
    14,
    18
  ],
  "net_cash_m": [
    50000000,
    80000000,
    110000000
  ],
  "shares_m": [
    740,
    750,
    770
  ],
  "currency": "USD",
  "input_currency": "KRW",
  "quote_multiplier": 6.896551724137931e-05
}
```

**公司事件。** SEC与新闻页已查，最新已报告Q2；未形成发行后完全稀释股本及投资收益桥接，未来事件状态未完整验证。

**经济失效。** HBM份额/良率下滑叠加存储ASP周期反转，扩产资本回报不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价186.68高于本轮作者基准价值139.78及合理参与上限146.77，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [ADS发行招股书](https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/310_SKHY.txt)
- [SK hynix Announces 2Q26 Financial Results – SK hynix Newsroom (https://news.skhynix.com/en/q2-2026-business-results-01/)](https://news.skhynix.com/en/q2-2026-business-results-01/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/088_SKHY.txt)
- [SK hynix Announces 2Q26 Financial Results – SK hynix Newsroom (https://news.skhynix.com/en/q2-2026-business-results/)](https://news.skhynix.com/en/q2-2026-business-results/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/089_SKHY.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0002120882.json)；采集时间2026-09-30T07:49:20.850237+00:00，索引存在不等于全部正文已审核。


## ON — 研究未完成

**业务与瓶颈。** 汽车/工业功率与感知，AI电源为增量；Q2收入16.04亿、FCF4.254亿。

**反证、现金与稀释。** 汽车和SiC周期仍核心，回购可能好于投资但并不创造终端需求。   Synaptics交易为约70亿美元EV全股票交易，每SYNA股换1.350股ON；尚不能用单体Q2 EPS直接代表合并后股东权益。收购公告标题Acquires不代表已交割，仍核审批和换股。 9月16日SEC 425 Investor Day材料已读：公司2030目标为2026E起收入CAGR12–14%、AI数据中心收入逾25亿美元、非GAAP毛利53%、FCF30–35%。这些是公司目标不是已实现利润。Synaptics全股票收购的200百万协同及约18个月EPS增厚目标须和1.350换股比例、新股及SBC一起计算；原EPS5基准仅单体敏感性，未作并表价格推荐。

**完整交易日价格与量价。** 2026-09-29收盘 75.95 USD；当日+0.40%，5/20/60交易日+3.19%/+2.51%/-19.79%。20日均价72.62，50日均价77.28；20日高/低77.68/65.80；末日量/20日均量1.35倍，共104根日线。 20日相对QQQ为-0.44%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ON/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：29.06 / 77.49 / 145.30 USD。跨周期EPS与FCF估值，不给全部业务AI高倍数。 Q2 EPS0.56；2028基准5假定汽车/工业复苏，非AI纯敞口，压力对SiC价格/利用率建模。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    2.5,
    5.0,
    7.5
  ],
  "pe": [
    15.0,
    20.0,
    25.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** SiC利用率长期低迷且价格竞争令毛利率难以回升，现金流结构性下降。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** Synaptics交易后经营利润/持续SBC/换股稀释的并表估值；交易后IR/股东投票及未来24小时事件交叉核查

**未闭合项（2项）。** Synaptics交易后经营利润/持续SBC/换股稀释的并表估值；交易后IR/股东投票及未来24小时事件交叉核查。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [10-Q 2026-08-03](https://www.sec.gov/Archives/edgar/data/1097864/000109786426000017/on-20260703.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/224_ON.txt)
- [onsemi Reports Second Quarter 2026 Results | onsemi (https://www.onsemi.com/company/newsroom/news-and-insights/onsemi-reports-second-quarter-2026-results)](https://www.onsemi.com/company/newsroom/news-and-insights/onsemi-reports-second-quarter-2026-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/090_ON.txt)
- [本轮重大事项追加核验](https://investor.onsemi.com/news-releases/news-release-details/onsemi-acquire-synaptics-enable-next-generation-intelligent)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/1097864/000114036126036771/ef20081954_425.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001097864.json)；采集时间2026-09-30T07:49:21.947565+00:00，索引存在不等于全部正文已审核。


## GFS — 排除

**业务与瓶颈。** 特色工艺代工、射频/汽车/工业及新增硅光方向。

**反证、现金与稀释。** Q2收入17.86亿、FCF约负300万，成熟制程利用率和资本开支；AI纯度较低。  

**完整交易日价格与量价。** 2026-09-29收盘 47.86 USD；当日+0.17%，5/20/60交易日-0.19%/+7.09%/-30.55%。20日均价45.96，50日均价48.69；20日高/低49.42/42.15；末日量/20日均量0.92倍，共104根日线。 20日相对QQQ为+4.14%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/GFS/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：9.30 / 31.00 / 67.81 USD。按中周期盈利和资本强度，不能用先进制程龙头倍数。 特色工艺代工的中周期盈利，基准2028 EPS2要求利用率改善；必须与资本成本、净债务复核。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    0.8,
    2.0,
    3.5
  ],
  "pe": [
    15.0,
    20.0,
    25.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 利用率回升无法提高资本回报，特色平台订单不足以抵消传统需求。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价47.86高于本轮作者基准价值31.00及合理参与上限32.55，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [GlobalFoundries Reports Second Quarter 2026 Financial Results | GlobalFoundries (https://gf.com/news-and-events/news/globalfoundries-reports-second-quarter-2026-financial-results/)](https://gf.com/news-and-events/news/globalfoundries-reports-second-quarter-2026-financial-results/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/093_GFS.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001709048.json)；采集时间2026-09-30T07:49:21.740275+00:00，索引存在不等于全部正文已审核。


## CCXI — 研究未完成

**业务与瓶颈。** Churchill Capital Corp XI，拟与Agility Robotics合并；研究对象已按CIK2074973纠正。

**反证、现金与稀释。** SPAC信托/赎回、发起人股份、PIPE、认股权证和并购目标预测；不是旧ChemoCentryx。  

**完整交易日价格与量价。** 2026-09-29收盘 12.33 USD；当日+2.32%，5/20/60交易日-6.16%/-7.85%/UNKNOWN。20日均价12.75，50日均价14.10；20日高/低14.16/11.76；末日量/20日均量1.76倍，共50根日线。 20日相对QQQ为-10.80%个百分点差（非超额收益率比值）。 [行情来源](https://stockanalysis.com/stocks/ccxi/history/)

**估值。** UNKNOWN，未用统一市销率补空。需完全摊薄pro forma股本、信托净值与Agility实际业务，报价源混码时不得估值。

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 并购条款、赎回或实际融资令普通股经济权益显著差于宣称企业价值。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** Agility并购赎回/PIPE/认股权证的完全稀释权益；目标公司现金消耗和可校准估值；并购投票与截止事件

**未闭合项（3项）。** Agility并购赎回/PIPE/认股权证的完全稀释权益；目标公司现金消耗和可校准估值；并购投票与截止事件。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [10-Q 2026-08-13](https://www.sec.gov/Archives/edgar/data/2074973/000121390026089245/ea0300779-10q_churchill11.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/225_CCXI.txt)
- [current discovered source](https://www.sec.gov/Archives/edgar/data/2074973/000121390026097764/ea0297114-04.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/249_CCXI.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0002074973.json)；采集时间2026-09-30T07:49:21.820211+00:00，索引存在不等于全部正文已审核。


## AEHR — 排除

**业务与瓶颈。** AI芯片老化测试打开SiC以外市场；FY27收入指引1.30–1.50亿，披露有效积压1亿。

**反证、现金与稀释。** 单一大客户大订单不等于稳定年金；FY26营收0.50亿、GAAP亏损，股价已计入高速扩张。  

**完整交易日价格与量价。** 2026-09-29收盘 100.78 USD；当日+2.33%，5/20/60交易日+0.18%/+27.14%/+39.34%。20日均价91.17，50日均价95.64；20日高/低108.40/74.23；末日量/20日均量1.19倍，共104根日线。 20日相对SOXX为+16.10%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AEHR/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：6.91 / 28.48 / 63.21 USD。按2029收入、净利率、稀释股数建模；不能把三倍指引增长无限外推。 FY27收入指引130–150百万；基准2029 260百万、强景450百万是作者假设，大客户订单需持续重复。完全稀释股数高于FY26约31百万。

```json
{
  "revenue": [
    130,
    260,
    450
  ],
  "net_margin": [
    0.096,
    0.184,
    0.24
  ],
  "shares": [
    36,
    40,
    45
  ],
  "pe": [
    25,
    35,
    40
  ],
  "net_cash": [
    80,
    120,
    160
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 大客户订单取消/移后，或FY27收入下修至1.20亿以下且不能用其他客户替代。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价100.78高于本轮作者基准价值28.48及合理参与上限29.91，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [Known current IR financial source](https://www.sec.gov/Archives/edgar/data/1040470/000165495426006655/aehr_ex991.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/096_AEHR.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001040470.json)；采集时间2026-09-30T07:49:24.098786+00:00，索引存在不等于全部正文已审核。


## AXTI — 排除

**业务与瓶颈。** InP衬底有高速光互连瓶颈敞口；Q2收入4759万、毛利44.9%、归母EPS0.17。

**反证、现金与稀释。** 出口许可、中国资产、非控股权益与新增产能；账面现金很大部分来自融资。  

**完整交易日价格与量价。** 2026-09-29收盘 78.18 USD；当日+6.12%，5/20/60交易日+0.50%/+28.99%/+23.08%。20日均价67.65，50日均价66.58；20日高/低82.14/52.76；末日量/20日均量0.78倍，共104根日线。 20日相对SOXX为+17.95%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AXTI/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：2.90 / 17.58 / 43.46 USD。按归母净利率、稀释股数建模，不能对合并利润直接套上市公司PE。 Q2收入47.59百万；净利率专指上市主体归母利润，少数股东和中国子公司现金不得重复加入。

```json
{
  "revenue": [
    200,
    450,
    800
  ],
  "net_margin": [
    0.08,
    0.16,
    0.22
  ],
  "shares": [
    70,
    78,
    90
  ],
  "pe": [
    20,
    30,
    35
  ],
  "net_cash": [
    0,
    0,
    0
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 出口许可约束使订单无法交付，或InP增长未能归属上市公司普通股股东。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价78.18高于本轮作者基准价值17.58及合理参与上限18.46，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-13](https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/226_AXTI.txt)
- [(https://www.sec.gov/Archives/edgar/data/1051627/000143774926025061/ex_974537.htm)](https://www.sec.gov/Archives/edgar/data/1051627/000143774926025061/ex_974537.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/098_AXTI.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001051627.json)；采集时间2026-09-30T07:49:25.023548+00:00，索引存在不等于全部正文已审核。


## SOI — 排除

**业务与瓶颈。** Photonics-SOI需求加速；9月2日上修FY27硅光收入至FY26略高于1亿美元的2.5–3倍。

**反证、现金与稀释。** RF-SOI库存周期仍拖累；新增5亿欧元ORNANE影响债务和潜在稀释；税务和扩产现金成本。 9月18日5亿欧元ORNANE：票息0.5%，转换价206.46欧元，2033年到期、5周年可要求偿还；全股票交付潜在稀释约6.3%。新债与等额现金在发行时不能凭空增加净现金。基准按债务计息，强景按转换增加股数，避免双重扣减。  已核5亿欧元ORNANE转换价206.46和潜在6.3%全股转换稀释。基准40百万股未给新债现金额外价值；即使宽松地把新增5亿全部当免费现金加在2029基准，现值也只增加约7.94欧元，104.00升至约111.94，仍低于155.50。排除依据为该估值情景过贵，而非债券条款缺证。

**完整交易日价格与量价。** 2026-09-29收盘 155.50 EUR；当日+9.08%，5/20/60交易日+2.27%/+40.66%/UNKNOWN。20日均价139.35，50日均价UNKNOWN；20日高/低156.60/109.00；末日量/20日均量1.03倍，共49根日线。 本币数据不直接减美元ETF收益；不足60根时不编造60日指标。 使用stockanalysis的155.50欧元；曾有另一二手源154.95的差异，未把该报价差当否决理由。 [行情来源](https://stockanalysis.com/quote/epa/SOI/history/)

**估值。** 压力/基准/强情景现值：20.32 / 104.00 / 248.07 EUR。采用光子与成熟业务分部利润；新增可转债转换价206.46、0.5%票息及潜在约242万股稀释已核，使用更新后模型。 FY26收入592百万欧元；硅光FY27上修至前年的2.5–3倍，但成熟RF业务仍承压。5亿欧元ORNANE票息0.5%、转换价206.46；强景43百万股包含全股票转换近2.42百万股和其他稀释，基准40百万假定债务不转换且净利含利息。净现金不叠加，即把募集500百万全当无偿现金加回，基准仍低于现价；正式估值不重复加现金。

```json
{
  "method": "net_profit",
  "year": 2029,
  "rate": 0.15,
  "years": 3.25,
  "revenue_m": [
    800,
    1300,
    2000
  ],
  "net_margin": [
    0.08,
    0.18,
    0.24
  ],
  "pe": [
    20,
    28,
    35
  ],
  "net_cash_m": [
    0,
    0,
    0
  ],
  "shares_m": [
    40,
    40,
    43
  ],
  "currency": "EUR"
}
```

**公司事件。** IR下次H1FY27财报11月18日，窗口外；债券条款已补核，发行后财务/股本桥接仍需完成。 [核查入口](https://www.soitec.com/home/investors)

**经济失效。** 硅光供货协议不能转为收入或成熟业务收缩超过光子增量，且净债务/FCF恶化。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价155.50高于本轮作者基准价值104.00及合理参与上限109.20，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [Subscribe to investor email alerts (https://soitec.sitefinity.cloud/home/investors/regulated-information/financial-reports--results-other-regulated-releases)](https://soitec.sitefinity.cloud/home/investors/regulated-information/financial-reports--results-other-regulated-releases)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/099_SOI.txt)
- [SOITEC REPORTS FISCAL 2026 FULL-YEAR RESULTS (https://www.soitec.com/docs/default-source/financial-documents/2025-2026/en/soitec-fy%2726-pr---en.pdf?Status=Master&sfvrsn=a4e6d7e6_1)](https://www.soitec.com/docs/default-source/financial-documents/2025-2026/en/soitec-fy%2726-pr---en.pdf?Status=Master&sfvrsn=a4e6d7e6_1)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/100_SOI.txt)
- [本轮重大事项追加核验](https://www.soitec.com/home/investors)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)


## IQE — 排除

**业务与瓶颈。** InP外延与化合物材料；H1收入6460万英镑同比43%，光子业务增长45%。

**反证、现金与稀释。** H1税前仍亏1260万英镑；现金改善含融资，租赁不在调整净现金内；GBX与GBP须换算100倍。 5月募资公告披露完成后有表决权股数1,312,586,857，募资8100万英镑；不是经营现金。估值采用2029股数15–18亿的稀释情景，现价47.30GBX=0.473英镑。 

**完整交易日价格与量价。** 2026-09-29收盘 47.30 GBX；当日+5.11%，5/20/60交易日+4.07%/+1.28%/UNKNOWN。20日均价44.81，50日均价UNKNOWN；20日高/低50.30/39.60；末日量/20日均量1.15倍，共49根日线。 本币数据不直接减美元ETF收益；不足60根时不编造60日指标。 [行情来源](https://stockanalysis.com/quote/aim/IQE/history/)

**估值。** 压力/基准/强情景现值：0.00 / 21.03 / 76.90 GBX。从毛利到折旧后净利建2029情景；不能用EBITDA当净利润，未来股数使用高于已发行的稀释情景。 5月募资后投票股数1,312.587百万；2029股数含继续稀释。H1收入64.6百万、税前亏损12.6百万，基准26%级收入CAGR及转盈仅为作者假设。图中单位GBX，不能将0.47英镑写成47英镑。

```json
{
  "method": "net_profit",
  "year": 2029,
  "rate": 0.15,
  "years": 3.25,
  "revenue_m": [
    160,
    260,
    450
  ],
  "net_margin": [
    0,
    0.08,
    0.15
  ],
  "pe": [
    18,
    25,
    32
  ],
  "net_cash_m": [
    0,
    10,
    20
  ],
  "shares_m": [
    1500,
    1600,
    1800
  ],
  "currency": "GBX",
  "quote_multiplier": 100
}
```

**公司事件。** IR日历最新为已发生的9月7日中报；完整RNS最新公司事件复核未闭合。 [核查入口](https://www.iqep.com/investors/events/financial-calendar/)

**经济失效。** 扩产转换后仍无法提高利用率/毛利，或净现金不足支持转盈路径。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价47.30高于本轮作者基准价值21.03及合理参与上限22.08，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [2026 Interim Results | IQE Corporate (https://www.iqep.com/media/press-releases/2026/2026-interim-results/)](https://www.iqep.com/media/press-releases/2026/2026-interim-results/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/101_IQE.txt)
- [IR事项补核](https://www.iqep.com/investors/events/financial-calendar/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)


## ESMT — 研究未完成

**业务与瓶颈。** 利基型存储供需紧张带来利润弹性；H1收入212.13亿台币、EPS27.58，8月收入79.05亿。

**反证、现金与稀释。** 极强涨价周期不代表长期利润，采购/库存、可转债与股数、现金转换仍需检验。   已核9月10日第二次有担保可转债转换价308.0台币、溢价102.44%。转换价不再属于未核项；发行总额、股数与最新现金/库存周转仍需合并复核，不把半年EPS翻倍年化。 已尝试公司财务入口、Q2董事会结果、公告及定向检索；官网本轮可定位完整现金流PDF仍是115Q1，不能冒充115Q2。二手数据展示H1 CFO105.85892亿台币，仅作待核线索，不升级一手结论。可转债308台币转换价已核；累计期末库存/应收、可转债股本和当地事件仍须MOPS/公司Q2原表补证，保持未完成。

**完整交易日价格与量价。** 2026-09-29收盘 285.00 TWD；当日+3.64%，5/20/60交易日-1.21%/-2.56%/UNKNOWN。20日均价284.55，50日均价UNKNOWN；20日高/低319.00/263.00；末日量/20日均量0.59倍，共49根日线。 本币数据不直接减美元ETF收益；不足60根时不编造60日指标。 [行情来源](https://stockanalysis.com/quote/tpe/3006/history/)

**估值。** 压力/基准/强情景现值：92.99 / 303.77 / 627.69 TWD。压力化中周期EPS而非把单月利润年化，台币报价与台湾交易日单列。 H1 EPS27.58为景气事实，2028正常化基准28故意不年化为55.16；强景45仍要求涨价持续及库存回款，完整现金/股本未闭合。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    12.0,
    28.0,
    45.0
  ],
  "pe": [
    10.0,
    14.0,
    18.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "TWD",
  "input_currency": "TWD"
}
```

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 利基DRAM报价回落且库存/应收上升，毛利正常化后盈利不能支撑估值。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 现金流与库存/采购质量；可转债总额到完全稀释股数和最新公司事件的桥

**未闭合项（2项）。** 现金流与库存/采购质量；可转债总额到完全稀释股数和最新公司事件的桥。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [Financial Information - ESMT (https://www.esmt.com.tw/en/investor/financial)](https://www.esmt.com.tw/en/investor/financial)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/102_ESMT.txt)
- [股東專區 - ESMT (https://www.esmt.com.tw/tw/investor/shareholder)](https://www.esmt.com.tw/tw/investor/shareholder)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/103_ESMT.txt)
- [本轮重大事项追加核验](https://www.esmt.com.tw/tw/press-room/2026091001?category=investor-Info)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.esmt.com.tw/tw/investor/financial)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.esmt.com.tw/tw/press-room/2026073001)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)


## HWM — 排除

**业务与瓶颈。** 航空与工业燃机热端精密铸造、材料和资格壁垒；Q2营收25.47亿，现金创造较强。

**反证、现金与稀释。** 航空占比大，并非纯AI燃机叶片；扩产、长认证和OEM后向整合共同影响收益。  

**完整交易日价格与量价。** 2026-09-29收盘 230.94 USD；当日+1.15%，5/20/60交易日+2.48%/-5.72%/-16.90%。20日均价234.34，50日均价261.40；20日高/低263.34/223.03；末日量/20日均量1.47倍，共104根日线。 20日相对QQQ为-8.67%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/HWM/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：81.83 / 174.36 / 278.97 USD。按航空/IGT利润并结合订单兑现；不给全公司AI纯敞口溢价。 Q2 EPS1.33；2028基准7.5要求航空和IGT双增长，未按纯AI热端给予更高倍数。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    4.8,
    7.5,
    10.0
  ],
  "pe": [
    22.0,
    30.0,
    36.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 关键客户资格丢失、产能投资不能维持良率或热端订单增量不转化为利润。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价230.94高于本轮作者基准价值174.36及合理参与上限183.08，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-06](https://www.sec.gov/Archives/edgar/data/4281/000000428126000025/hwm-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/227_HWM.txt)
- [Howmet Aerospace Reports Second Quarter 2026 Results | Howmet (https://www.howmet.com/press-release/2026-08-06/howmet-aerospace-reports-second-quarter-2026-results/)](https://www.howmet.com/press-release/2026-08-06/howmet-aerospace-reports-second-quarter-2026-results/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/104_HWM.txt)
- [Howmet Aerospace to Host Webcast and Announce Second Quarter 2026 Results | Howmet (https://www.howmet.com/press-release/2026-07-09/howmet-aerospace-to-host-webcast-and-announce-second-quarter-2026-results/)](https://www.howmet.com/press-release/2026-07-09/howmet-aerospace-to-host-webcast-and-announce-second-quarter-2026-results/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/105_HWM.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000004281.json)；采集时间2026-09-30T07:49:23.911247+00:00，索引存在不等于全部正文已审核。


## TSLA — 研究未完成

**业务与瓶颈。** 汽车、储能与机器人/自动驾驶多路径；当前自动驾驶和Optimus应按阶段证据区分。

**反证、现金与稀释。** Q2经营利润3.98亿远低于净利；高估值含未兑现可选业务，资本开支扩大。  

**完整交易日价格与量价。** 2026-09-29收盘 352.84 USD；当日-1.29%，5/20/60交易日-6.88%/-4.11%/-15.94%。20日均价365.36，50日均价347.45；20日高/低386.83/349.92；末日量/20日均量1.12倍，共104根日线。 20日相对QQQ为-7.06%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/TSLA/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** UNKNOWN，未用统一市销率补空。SOTP：现有业务与概率加权新业务分开；9月29日300亿美元授信尚未提款，不当已新增负债。

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 汽车/储能现金无法支持新增投资，且自动驾驶商业化/安全监管证据长期落后。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 现有汽车/储能与新业务SOTP；自动驾驶/机器人概率和持续资本支出校准

**未闭合项（2项）。** 现有汽车/储能与新业务SOTP；自动驾驶/机器人概率和持续资本支出校准。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [8-K 2026-09-29](https://www.sec.gov/Archives/edgar/data/1318605/000162828026063820/tsla-20260929.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/108_TSLA.txt)
- [Item 2.02 Results of Operations and Financial Condition. (https://ir.tesla.com/_flysystem/s3/sec/000162828026049213/tsla-20260722-gen.pdf)](https://ir.tesla.com/_flysystem/s3/sec/000162828026049213/tsla-20260722-gen.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/107_TSLA.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001318605.json)；采集时间2026-09-30T07:49:23.166681+00:00，索引存在不等于全部正文已审核。


## RXRX — 研究未完成

**业务与瓶颈。** AI药物发现平台与管线；Genentech行权体现合作进展。

**反证、现金与稀释。** 合作收入不等于药品销售或临床成功；H1经营现金流负1.870亿，未来试验与稀释。  

**完整交易日价格与量价。** 2026-09-29收盘 4.03 USD；当日+8.92%，5/20/60交易日-0.49%/+18.53%/+1.77%。20日均价3.55，50日均价3.35；20日高/低4.16/3.10；末日量/20日均量1.29倍，共104根日线。 20日相对XLV为+18.42%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/RXRX/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** UNKNOWN，未用统一市销率补空。需逐项目rNPV、适应症、成功率和成本；未知临床参数不以软件PS替代。

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 核心临床疗效/安全性失败或现金不足支持关键读出，且合作变现无法补足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 逐项目临床rNPV成功率/成本；至读出与融资的现金跑道/稀释

**未闭合项（2项）。** 逐项目临床rNPV成功率/成本；至读出与融资的现金跑道/稀释。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [10-Q 2026-08-05](https://www.sec.gov/Archives/edgar/data/1601830/000160183026000098/rxrx-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/228_RXRX.txt)
- [Full Transcript of Recursion's Second Quarter 2026 Earnings Call (https://recursion.com/news/full-transcript-of-recursions-second-quarter-2026-earnings-call)](https://recursion.com/news/full-transcript-of-recursions-second-quarter-2026-earnings-call)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/109_RXRX.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001601830.json)；采集时间2026-09-30T07:49:25.985832+00:00，索引存在不等于全部正文已审核。


## CLS — 条件观察

**业务与瓶颈。** 800G/1.6T交换与AI平台制造设计；Q2营收46.99亿同比62%，2026调整EPS指引11.30。

**反证、现金与稀释。** GAAP利润含TRS公允价值收益；供应商应付扩张缓冲了存货与应收；超大客户集中。 H1公司口径FCF285百万，但融资现金流另有SBC现金结算326.3百万，不能将公司FCF等同股东自由现金。未来EPS保留持续SBC、剔除TRS；扩产和现金结算是持续复核项。 8月7日8-K对应普通股增发，不是发债：9677419股、310美元/股，加已全额行权1451612股，预计净募资33.9亿美元。改善扩产资金，也增加11129031股；2028 EPS22的旧敏感性尚未按新股数桥接，不能用409.16基准直接推荐。9月11日8-K为10月1日生效的CFO/总裁职务调整。 本轮将原EPS22敏感性下调为2028 EPS19基准，压力11.5、强29。基准可复算桥：380亿美元收入×8.4%含持续SBC经营利润率，减约1.04亿美元净利息，再乘80%税后/1.30亿稀释股，约19；未来1.30亿高于6月1.15亿基础股加新发1112.9万股。新募资约33.9亿美元补流动性但不作为利润，亦不重复加到PE估值。H1公司FCF285百万减融资类SBC现金结算326.3百万为负41.3百万，这是股东现金压力口径，不代表GAAP FCF错误；后续回款尚须完成预算。

**完整交易日价格与量价。** 2026-09-29收盘 366.47 USD；当日+2.79%，5/20/60交易日+2.91%/+22.40%/+4.65%。20日均价333.58，50日均价327.96；20日高/低381.30/273.80；末日量/20日均量0.90倍，共104根日线。 20日相对QQQ为+19.45%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/CLS/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：160.41 / 353.37 / 674.18 USD。以调整EPS扣持续SBC、剔除TRS，2028盈利不能只把最好单季乘四。 2026调整EPS指引11.30；管理层预期2027收入增速高于2026的65%、EPS更快。基准2028 EPS19按未来1.30亿股、380亿美元收入及含SBC利润率重算；现金转换仍为唯一待补项。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    11.5,
    19.0,
    29.0
  ],
  "pe": [
    18.0,
    24.0,
    30.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 8月7日发行11,129,031股；9月11日CFO交接公告，生效10月1日；10月27日Investor Day在24小时外。SEC及发行人新闻未发现窗口内已知重大二元结果，管理层交接保留普通风险。 [核查入口](https://corporate.celestica.com/news-releases)

**经济失效。** 2027增长未达到管理层加速框架且新平台计划被取消，或正常化经营利润率跌破7%。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 扩产、供应商账期和SBC现金结算之后的股东现金转换，尚缺可靠的2027预算桥；不是因为股价上涨而否决。

**未闭合项（1项）。** 扩产、供应商账期和SBC现金结算之后的股东现金转换，尚缺可靠的2027预算桥；不是因为股价上涨而否决。。Owner=current_thread_direct。以2026公司FCF600百万（不含融资分类SBC结算）、新募资用途及公开扩产预算建立2027压力现金表；已完成股份与TRS纠正。若公开披露仍不能限定回款/资本支出假设，标为估值现金证据未闭合，不继续照抄观察。 复核到期：2026-10-02T18:00:00+08:00。

**一手与本地证据。**

- [(https://www.sec.gov/Archives/edgar/data/1030894/000103089426000043/cls-20260630prcondensedfs.htm)](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000043/cls-20260630prcondensedfs.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/111_CLS.txt)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/1030894/000110465926092676/tm2621135d2_8k.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/1030894/000110465926107079/tm2625204d1_8k.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://corporate.celestica.com/news-releases/news-release-details/celestica-announces-second-quarter-2026-financial-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://corporate.celestica.com/news-releases/news-release-details/celestica-completes-equity-offering)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [IR事项补核](https://corporate.celestica.com/news-releases/news-release-details/celestica-host-2026-investor-and-analyst-day-october-27-2026)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)
- [公司事件核查路径](https://corporate.celestica.com/news-releases)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/final_decisions.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001030894.json)；采集时间2026-09-30T07:49:25.676780+00:00，索引存在不等于全部正文已审核。


## DPC — 排除

**业务与瓶颈。** Doncasters独立精密铸造与热端供应链；Q2收入2.687亿同比34%，Engine Products盈利较强。

**反证、现金与稀释。** IPO激励令GAAP亏损；IPO后偿债改变资本结构，6月末现金/借款不能直接套今天。 7月28日已发行149.393016百万股。6月末交易调整后净现金118.2百万已考虑MIP支付210.9百万及私募净款55.4百万，不能使用原始现金846.4百万。9月8日完成再融资，新的325百万循环授信替换旧设施，未承诺150百万增额不当现金。  H1 CFO−34.0百万、设备支出19.8百万，FCF−53.8百万；D&A14.8百万。以2028 EBITDA350减持续激励25、折旧/维护资本代理55、利息8，税率25%、155百万股、28倍PE及13%折现2.25年交叉算得约26.96美元，与EV法27.93接近。以上均作者假设；净现金上下100百万只影响约0.49美元，不足以填补现价41.46与基准差距。

**完整交易日价格与量价。** 2026-09-29收盘 41.46 USD；当日+2.27%，5/20/60交易日+1.99%/-1.19%/-14.55%。20日均价41.21，50日均价45.37；20日高/低46.50/38.50；末日量/20日均量1.26倍，共67根日线。 20日相对QQQ为-4.15%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/DPC/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：14.79 / 27.93 / 46.29 USD。需以IPO后净债务、正常化EBITDA减折旧/利息/税建模；不是GEV等OEM同类。 Q2 EBITDA48百万、LTM160.3百万；2028基准350百万需要规模和利润率增长。IPO后149.393百万股，未来含激励稀释。公司交易调整后净现金118.2百万，9月再融资未披露实时净现金，用100百万假设并做±100百万敏感性；授信325百万不是现金/已借款。折旧/资本开支是额外验收项，不因EBITDA模型忽略。

```json
{
  "method": "EV_EBITDA",
  "year": 2028,
  "rate": 0.13,
  "years": 2.25,
  "ebitda_m": [
    240,
    350,
    480
  ],
  "multiple": [
    12,
    16,
    20
  ],
  "net_cash_m": [
    100,
    100,
    150
  ],
  "shares_m": [
    153,
    155,
    160
  ],
  "currency": "USD"
}
```

**公司事件。** 9月8日再融资已发生；实时净债务和完整IR未来事件尚待交叉复核。 [核查入口](https://ir.doncasters.com/news-and-events/news/news-details/2026/Doncasters-Completes-Debt-Refinancing/default.aspx)

**经济失效。** IGT增长无法转为更高利用率/利润，或大客户内制、资格或铸造良率受损。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价41.46高于本轮作者基准价值27.93及合理参与上限29.33，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-11](https://www.sec.gov/Archives/edgar/data/2107018/000110465926093772/dpc-20260628x10q.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/229_DPC.txt)
- [本轮重大事项追加核验](https://ir.doncasters.com/news-and-events/news/news-details/2026/Doncasters-Completes-Debt-Refinancing/default.aspx)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0002107018.json)；采集时间2026-09-30T07:49:25.197697+00:00，索引存在不等于全部正文已审核。


## SCTX — 研究未完成

**业务与瓶颈。** Scribe表观遗传沉默/基因编辑，STX-1150已进入一期，首批临床数据预计2027H1。

**反证、现金与稀释。** 动物数据不等于人体长期安全/有效；IPO后股数、Sanofi配售与未来试验资金。  

**完整交易日价格与量价。** 2026-09-29收盘 23.03 USD；当日+5.79%，5/20/60交易日-17.96%/-24.59%/UNKNOWN。20日均价28.25，50日均价UNKNOWN；20日高/低35.40/20.21；末日量/20日均量1.81倍，共47根日线。 20日相对XLV为-24.70%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/SCTX/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** UNKNOWN，未用统一市销率补空。Q2现金投资4300万加IPO净募1.406亿是pro forma起点；rNPV成功率与市场份额未校准，不能凑价格。

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 人体安全性/持久降脂失败，或关键试验延期导致融资后现金跑道不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 临床一期rNPV和人体疗效/安全证据边界；IPO及后续融资现金跑道和完全稀释股数

**未闭合项（2项）。** 临床一期rNPV和人体疗效/安全证据边界；IPO及后续融资现金跑道和完全稀释股数。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [10-Q 2026-09-02](https://www.sec.gov/Archives/edgar/data/1853921/000119312526380191/sctx-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/230_SCTX.txt)
- [8-K (https://www.sec.gov/Archives/edgar/data/1853921/000119312526380184/sctx-20260902.htm)](https://www.sec.gov/Archives/edgar/data/1853921/000119312526380184/sctx-20260902.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/114_SCTX.txt)
- [(https://www.sec.gov/Archives/edgar/data/1853921/000119312526380184/sctx-ex99_1.htm)](https://www.sec.gov/Archives/edgar/data/1853921/000119312526380184/sctx-ex99_1.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/115_SCTX.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001853921.json)；采集时间2026-09-30T07:49:26.712043+00:00，索引存在不等于全部正文已审核。


## AMZN — 研究未完成

**业务与瓶颈。** AWS与自研芯片是AI基础设施锚，零售与广告产生分散现金流。

**反证、现金与稀释。** Q2净利润626.5亿含投资重估，不能年化；AI资本开支和租赁支出是股东现金的重要负担。   完整Q2 10-Q已补入：TTM CFO161.403十亿美元，净资本开支169.007十亿，FCF负7.604十亿；再扣融资租赁本金1.599及其他融资义务.308十亿，股东现金口径约负9.511十亿，且CFO还加回SBC，不能视为SBC无成本。Q2 AWS营业利润16.6十亿、北美9.1、国际1.7；投资重估不进入未来EPS。规范化EPS模型虽有敏感性，但AI资产更新周期、持续资本开支与分部股东现金DCF尚未闭合，不能仅看增长宣布通过。

**完整交易日价格与量价。** 2026-09-29收盘 246.67 USD；当日+0.21%，5/20/60交易日-3.26%/-5.04%/+1.03%。20日均价252.64，50日均价256.09；20日高/低261.12/244.30；末日量/20日均量0.94倍，共104根日线。 20日相对QQQ为-8.00%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AMZN/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：116.24 / 272.77 / 471.15 USD。按AWS/零售广告分部或规范化EPS，并与含融资租赁的FCF交叉检查。 投资重估剔除；基准2028 EPS11依赖AWS/广告和零售经营利润，不用Q2 EPS5.75直接年化，AI资本开支仍须DCF复核。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    6.0,
    11.0,
    16.0
  ],
  "pe": [
    25.0,
    32.0,
    38.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** AWS增长/利用率不足覆盖折旧与资本成本，且零售现金流不足填补长期资本缺口。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** AWS/零售广告SOTP或持续资本开支DCF；投资重估与融资租赁支出对股东现金的桥

**未闭合项（2项）。** AWS/零售广告SOTP或持续资本开支DCF；投资重估与融资租赁支出对股东现金的桥。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [完整Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/309_AMZN.txt)
- [8-A12B 2026-09-24](https://www.sec.gov/Archives/edgar/data/1018724/000110465926110227/tm2625860d1_8a12b.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/118_AMZN.txt)
- [Amazon Q2 2026 earnings report: Read the release (https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report)](https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/117_AMZN.txt)
- [(https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm)](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/116_AMZN.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001018724.json)；采集时间2026-09-30T07:49:27.084246+00:00，索引存在不等于全部正文已审核。


## AIP — 排除

**业务与瓶颈。** SoC互连NoC IP与设计复杂度提高，设计赢单有潜在长期版税收益。

**反证、现金与稀释。** 签约额/ACV和收入确认不同；Q2收入2413万、经营亏损1391万，SBC与授权转版税时滞。  

**完整交易日价格与量价。** 2026-09-29收盘 23.26 USD；当日+0.61%，5/20/60交易日-6.13%/+6.31%/-33.20%。20日均价22.41，50日均价25.61；20日高/低24.98/20.02；末日量/20日均量0.97倍，共104根日线。 20日相对QQQ为+3.35%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/AIP/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：2.31 / 15.24 / 38.10 USD。用2029收入、正常化利润和稀释；不能把IP标签自动等同高质量软件年金。 Q2收入24.13百万且经营亏损13.91百万。2029基准需量产版税显著提升；从授权到版税有时滞，避免只按EV/Sales。

```json
{
  "revenue": [
    140,
    230,
    350
  ],
  "net_margin": [
    0.04,
    0.16,
    0.25
  ],
  "shares": [
    55,
    57,
    60
  ],
  "pe": [
    25,
    35,
    40
  ],
  "net_cash": [
    60,
    80,
    100
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 设计赢单不转为量产版税、合同增长长期停滞，且融资持续稀释抵消经营增长。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价23.26高于本轮作者基准价值15.24及合理参与上限16.00，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-06](https://www.sec.gov/Archives/edgar/data/1667011/000162828026054464/aip-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/231_AIP.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001667011.json)；采集时间2026-09-30T07:49:28.132404+00:00，索引存在不等于全部正文已审核。


## ASMPT — 条件观察

**业务与瓶颈。** TCB、光子封装及高精度SMT；H1持续业务收入89.03亿港元、订单127.54亿，book-to-bill1.43。

**反证、现金与稀释。** AP仅约30%收入；HBM新设备购买受客户节奏影响；NEXX已出售，不等同于SMT整体出售。   已读2026中报现金流：H1 CFO727.255百万港元，设备购置131.216百万及预付5.518百万；减另列融资流利息75.070百万、租赁109.088百万后约406.363百万。出售NEXX净收492.335百万在投资现金流，未计经营FCF。H1持续经营稀释EPS1.78，调整2.34不直接年化；当前净现金36.3亿港元。 已读取完整中报：H1 CFO727.255百万港元，扣PPE131.216、预付PPE5.518、融资分类利息75.070和租赁109.088后为406.363百万；NEXX出售492.335百万属于投资现金流，不冒充经营现金。8月月报因字体编码不可读，已渲染第2页人工核实发行股数419,408,233、月内零变化、库存股零。2028 EPS8相当约33.6亿港元利润（假设4.2亿稀释股），不是将H1调整EPS直接年化。

**完整交易日价格与量价。** 2026-09-29收盘 162.60 HKD；当日+2.72%，5/20/60交易日-4.47%/+1.82%/UNKNOWN。20日均价163.02，50日均价UNKNOWN；20日高/低175.80/153.20；末日量/20日均量0.64倍，共49根日线。 本币数据不直接减美元ETF收益；不足60根时不编造60日指标。 [行情来源](https://stockanalysis.com/quote/hkg/0522/history/)

**估值。** 压力/基准/强情景现值：55.79 / 154.98 / 278.97 HKD。净现金36.3亿港元；持续经营与终止业务分开，港元EPS模型；本币日线已核，仍待本地市场相对强度比较。 H1持续经营GAAP EPS1.79、调整2.34；2028基准8需TCB订单交付，剔除NEXX终止业务，净现金不重复加到PE模型。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    4.0,
    8.0,
    12.0
  ],
  "pe": [
    18.0,
    25.0,
    30.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "HKD",
  "input_currency": "HKD"
}
```

**公司事件。** 8月中报、员工奖励及9月1日8月月报已核；最新披露入口未显示未来24小时已排期重大二元事件，保留未披露风险。 [核查入口](https://www.asmpt.com/en/investor-relations/announcements-circulars/tc/)

**经济失效。** 连续两季订单收入比低于1且TCB认证/重复订单停滞。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 本币日线已取得，但相对香港本地市场的同窗走势尚未完成核对；不能拿港币收益直接减美元QQQ。

**未闭合项（1项）。** 本币日线已取得，但相对香港本地市场的同窗走势尚未完成核对；不能拿港币收益直接减美元QQQ。。Owner=current_thread_direct。用港交所/恒指公司或同源恒指已结束交易日日线补齐同窗相对强度；轻微落后不是硬否决，只检查广泛市场是否失控及走势是否与论点明显冲突。 复核到期：2026-10-01T18:00:00+08:00。

**一手与本地证据。**

- [2026 H1中报现金流及权益全文](https://www.asmpt.com/site/assets/files/85541/e_00522ir-20260827.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/300_ASMPT.txt)
- [月报或可转证券条款](https://doc.irasia.com/listco/hk/asmpt/announcement/ca260901.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/303_ASMPT.txt)
- [Known current IR financial source](https://www.asmpt.com/en/investor-relations/financial-information/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/120_ASMPT.txt)
- [公司事件核查路径](https://www.asmpt.com/en/investor-relations/announcements-circulars/tc/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/final_decisions.json)


## Lenovo — 排除

**业务与瓶颈。** PC、服务器和服务；FY27Q1收入269.4亿，ISG业务增长带来利润弹性。

**反证、现金与稀释。** 调整净利与GAAP亏损差距含金融负债估值；PC仍大，AI相关收入标签不是纯AI净利润。   已读取完整Q1及9月14日债券转换公告。Q1 CFO382.301百万美元，扣PPE91.009、在建工程115.183、无形资产168.018后仅8.091百万，未扣租赁和并购。2029旧债已全部转股/注销；2028 CB转换价9.37港元，最多约16.67亿股；认股权证11.51港元、最多12.299亿股；2033 CB转换价35.74港元。未来股本修正为160/170/180亿股，不能沿用无稀释的124亿股。即采用当前基础124.047亿股且假定不发生任何未来稀释，基准现值约22.8港元，仍低于35.48；未来权证现金也不能把当前低价转股视作无成本。

**完整交易日价格与量价。** 2026-09-29收盘 35.48 HKD；当日-0.06%，5/20/60交易日-3.43%/+16.02%/UNKNOWN。20日均价33.74，50日均价UNKNOWN；20日高/低37.88/28.62；末日量/20日均量0.76倍，共49根日线。 本币数据不直接减美元ETF收益；不足60根时不编造60日指标。 [行情来源](https://stockanalysis.com/quote/hkg/0992/history/)

**估值。** 压力/基准/强情景现值：5.31 / 16.65 / 39.15 HKD。港币每股价值需从美元归母利润、完全稀释股本、汇率和净债务桥接；以新核CB/权证条款修正未来股本情景。 完整Q1及2028/2033 CB与认股权证已核。未来160/170/180亿股为作者稀释情景；净利润含利息、税、SBC，USD/HKD=7.8假设，净现金不另加。旧债2029已全部转股/注销；即不计进一步稀释仍不足现价。

```json
{
  "method": "net_profit",
  "year": 2029,
  "rate": 0.13,
  "years": 3.25,
  "revenue_m": [
    90000,
    120000,
    160000
  ],
  "net_margin": [
    0.018,
    0.03,
    0.042
  ],
  "pe": [
    10,
    15,
    20
  ],
  "net_cash_m": [
    0,
    0,
    0
  ],
  "shares_m": [
    16000,
    17000,
    18000
  ],
  "currency": "HKD",
  "quote_multiplier": 7.8
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** ISG利润改善不能持续且PC周期转弱，或债务/可转证券稀释侵蚀每股收益。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价35.48高于本轮作者基准价值16.65及合理参与上限17.49，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [追加完整财务报表](https://doc.irasia.com/listco/hk/lenovo/interim/2027/int1q.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/302_Lenovo.txt)
- [月报或可转证券条款](https://doc.irasia.com/listco/hk/lenovo/announcement/a260914.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/304_Lenovo.txt)
- [月报或可转证券条款](https://doc.irasia.com/listco/hk/lenovo/announcement/a260723c.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/305_Lenovo.txt)
- [月报或可转证券条款](https://doc.irasia.com/listco/hk/lenovo/announcement/a260723b.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/306_Lenovo.txt)
- [LENOVO GROUP: Q1 FINANCIAL RESULTS 2026/27 (https://investor.lenovo.com/en/financial/results/press_2627_q1.pdf)](https://investor.lenovo.com/en/financial/results/press_2627_q1.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/121_Lenovo.txt)
- [Results & Presentations | Lenovo (https://investor.lenovo.com/en/financial/results.php)](https://investor.lenovo.com/en/financial/results.php)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/122_Lenovo.txt)


## LASR — 排除

**业务与瓶颈。** 高能激光与国防项目带来增量；Q2收入8259万美元，经营亏损已较小。

**反证、现金与稀释。** 激光国防不等于AI光互连；研发合同与量产毛利差异、政府预算和客户集中。  

**完整交易日价格与量价。** 2026-09-29收盘 39.01 USD；当日-1.37%，5/20/60交易日-5.32%/-7.71%/-40.26%。20日均价39.92，50日均价50.64；20日高/低42.44/37.33；末日量/20日均量0.69倍，共104根日线。 20日相对QQQ为-10.67%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/LASR/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：2.74 / 17.03 / 44.08 USD。分开发研收入与产品利润；按转盈和稀释情景，不用热门光子标签给倍数。 Q2收入82.59百万且经营接近盈亏平衡；需验证高能激光量产及预算兑现，未来股数含SBC和可能融资。

```json
{
  "revenue": [
    350,
    550,
    850
  ],
  "net_margin": [
    0.04,
    0.12,
    0.18
  ],
  "shares": [
    65,
    70,
    78
  ],
  "pe": [
    20,
    28,
    35
  ],
  "net_cash": [
    0,
    30,
    60
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 主要高能激光合同延期/取消，或量产收入不能将经营利润持续转正。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价39.01高于本轮作者基准价值17.03及合理参与上限17.89，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-07](https://www.sec.gov/Archives/edgar/data/1124796/000112479626000038/lasr-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/232_LASR.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001124796.json)；采集时间2026-09-30T07:49:28.990965+00:00，索引存在不等于全部正文已审核。


## TEM — 排除

**业务与瓶颈。** 临床检测与医疗数据AI，Q2收入3.825亿、肿瘤检测量和MRD增加。

**反证、现金与稀释。** GAAP净利小幅转正但经营仍亏7591万，投资收益、SBC、并购和医疗支付质量。   财报原文链接已经补入有效来源索引，来源为公司原文/SEC，非二手转述。

**完整交易日价格与量价。** 2026-09-29收盘 82.58 USD；当日-2.94%，5/20/60交易日+6.98%/+30.98%/+36.05%。20日均价71.14，50日均价60.71；20日高/低89.09/57.72；末日量/20日均量0.92倍，共104根日线。 20日相对XLV为+30.86%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/TEM/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：2.42 / 26.96 / 70.78 USD。按检测与数据两分部利润和稀释估值，不能套SOXX或把重估收益作持续利润。 2026收入指引1595–1605百万，Q2经营仍亏损75.91百万。2029净利情景须包含诊断、数据许可、持续SBC和并购融资成本。

```json
{
  "revenue": [
    2200,
    3200,
    4600
  ],
  "net_margin": [
    0.02,
    0.09,
    0.16
  ],
  "shares": [
    210,
    235,
    265
  ],
  "pe": [
    25,
    35,
    40
  ],
  "net_cash": [
    -300,
    -100,
    100
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 报销/回款显著恶化、数据许可增长不及成本，或监管限制数据商业化。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价82.58高于本轮作者基准价值26.96及合理参与上限28.31，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [本轮重大事项追加核验](https://www.tempus.com/news/pr/tempus-reports-second-quarter-2026-results/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/1717115/000119312526326083/tem-ex99_1.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001717115.json)；采集时间2026-09-30T07:49:27.941914+00:00，索引存在不等于全部正文已审核。


## NBIS — 研究未完成

**业务与瓶颈。** GPU云通过容量、客户与长期合同扩张；Q2收入5.823亿，同比454%。

**反证、现金与稀释。** 昂贵GPU折旧、巨额资本开支、客户预付款、债务和稀释；ARR不是已实现年收入。  

**完整交易日价格与量价。** 2026-09-29收盘 237.35 USD；当日+2.36%，5/20/60交易日+0.52%/+15.04%/+11.42%。20日均价224.68，50日均价217.75；20日高/低254.74/194.80；末日量/20日均量0.64倍，共104根日线。 20日相对QQQ为+12.09%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/NBIS/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** UNKNOWN，未用统一市销率补空。采用合同现金流减GPU更新和融资成本；单纯市销率不可闭合，完整资本结构尚缺。

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 新部署利用率/单卡收益下降，同时融资成本超过合同全周期利润。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 合同收益减GPU更新/资本成本的DCF；客户预付与巨额融资后的普通股权益

**未闭合项（2项）。** 合同收益减GPU更新/资本成本的DCF；客户预付与巨额融资后的普通股权益。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [(https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-1.htm)](https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-1.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/128_NBIS.txt)
- [Nebius reports second quarter 2026 financial results (https://nebius.com/newsroom/nebius-reports-second-quarter-2026-financial-results)](https://nebius.com/newsroom/nebius-reports-second-quarter-2026-financial-results)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/127_NBIS.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001513845.json)；采集时间2026-09-30T07:49:28.547819+00:00，索引存在不等于全部正文已审核。


## ALAB — 排除

**业务与瓶颈。** PCIe/CXL连接、retimer及Scorpio交换产品，AI服务器连接复杂度增加。

**反证、现金与稀释。** Q2收入3.924亿、经营利润0.892亿但净利含税务影响；客户认股权证冲减收入、SBC和客户集中。  

**完整交易日价格与量价。** 2026-09-29收盘 357.84 USD；当日+1.86%，5/20/60交易日-1.55%/+20.49%/-17.31%。20日均价309.35，50日均价306.96；20日高/低377.87/251.62；末日量/20日均量1.03倍，共104根日线。 20日相对SOXX为+9.46%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/ALAB/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：20.79 / 76.62 / 177.78 USD。必须将权证、持续SBC和稀释计入规范化每股盈利，不以税务受益年化。 Q2收入392.4百万、经营89.25百万；净利含税务收益。基准25%净利率已假设规模效应，股数包含SBC/权证稀释。

```json
{
  "revenue": [
    1700,
    3000,
    5000
  ],
  "net_margin": [
    0.15,
    0.25,
    0.32
  ],
  "shares": [
    210,
    225,
    245
  ],
  "pe": [
    25,
    35,
    42
  ],
  "net_cash": [
    500,
    900,
    1400
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** Scorpio量产或主要平台份额不达预期，毛利率持续恶化且应收/库存扩张。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价357.84高于本轮作者基准价值76.62及合理参与上限80.45，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-05](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000035/alab-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/233_ALAB.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001736297.json)；采集时间2026-09-30T07:49:30.229582+00:00，索引存在不等于全部正文已审核。


## GNRC — 排除

**业务与瓶颈。** 备用电源和数据中心发电扩张，仍有住宅备用电源主业务。

**反证、现金与稀释。** 天气和住宅周期、燃机/柴油不同技术路线、数据中心订单纯度有限。  

**完整交易日价格与量价。** 2026-09-29收盘 212.22 USD；当日+3.42%，5/20/60交易日+2.93%/+14.48%/-17.68%。20日均价192.69，50日均价200.96；20日高/低231.89/173.25；末日量/20日均量1.39倍，共104根日线。 20日相对QQQ为+11.52%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/GNRC/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：74.39 / 187.53 / 347.17 USD。分部盈利/正常化EPS；不把所有销售增长视作AI供电收益。 Q2 EPS2.40；2028基准11包含住宅正常需求和部分数据中心增量，天气不能永续化。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    6.0,
    11.0,
    16.0
  ],
  "pe": [
    16.0,
    22.0,
    28.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 按住宅备用电源与数据中心增量共同估值，2028 EPS11、22倍退出PE的现值约187.53美元；当前212.22高于本轮合理上限195，不能把住宅周期利润全给AI倍数。重入条件是价格回到195以内且基本面不变，或已披露数据中心利润贡献使基准EPS上调。

**经济失效。** 数据中心积压取消且住宅需求走弱，使增量资本开支回报不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 按住宅备用电源与数据中心增量共同估值，2028 EPS11、22倍退出PE的现值约187.53美元；当前212.22高于本轮合理上限195，不能把住宅周期利润全给AI倍数。重入条件是价格回到195以内且基本面不变，或已披露数据中心利润贡献使基准EPS上调。

**一手与本地证据。**

- [10-Q 2026-08-04](https://www.sec.gov/Archives/edgar/data/1474735/000143774926025669/gnrc20260630_10q.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/234_GNRC.txt)
- [(https://www.sec.gov/Archives/edgar/data/1474735/000143774926024731/ex_994826.htm)](https://www.sec.gov/Archives/edgar/data/1474735/000143774926024731/ex_994826.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/132_GNRC.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001474735.json)；采集时间2026-09-30T07:49:29.707154+00:00，索引存在不等于全部正文已审核。


## OUST — 排除

**业务与瓶颈。** 工业/机器人激光雷达与立体视觉，Q2收入5463万，需求有实际产品落地。

**反证、现金与稀释。** 并购后传感器数含相机，不能全算激光雷达；H1现金消耗、ATM融资和股数增长。  

**完整交易日价格与量价。** 2026-09-29收盘 40.00 USD；当日-2.20%，5/20/60交易日-0.62%/+16.14%/-19.73%。20日均价36.93，50日均价38.75；20日高/低43.97/32.24；末日量/20日均量0.80倍，共104根日线。 20日相对QQQ为+13.19%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/OUST/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：2.84 / 19.05 / 47.30 USD。按2029收入→经营利润→税后盈利及稀释，不以销量增长代替每股价值。 Q2收入54.63百万。基准2029收入600百万和12%净利要求显著经营杠杆；未来股数高于当前约66百万，净现金是扣烧钱的假设。

```json
{
  "revenue": [
    350,
    600,
    900
  ],
  "net_margin": [
    0.04,
    0.12,
    0.2
  ],
  "shares": [
    85,
    90,
    100
  ],
  "pe": [
    20,
    35,
    40
  ],
  "net_cash": [
    100,
    180,
    250
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 产品毛利和经营现金消耗不随规模改善，或主要工业订单递延。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价40.00高于本轮作者基准价值19.05及合理参与上限20.00，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-06](https://www.sec.gov/Archives/edgar/data/1816581/000162828026054467/oust-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/235_OUST.txt)
- [(https://www.sec.gov/Archives/edgar/data/1816581/000162828026054297/exhibit991-6302026.htm)](https://www.sec.gov/Archives/edgar/data/1816581/000162828026054297/exhibit991-6302026.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/134_OUST.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001816581.json)；采集时间2026-09-30T07:49:30.036146+00:00，索引存在不等于全部正文已审核。


## HSAI — 排除

**业务与瓶颈。** 激光雷达量产与机器人/汽车客户；Q2美元收入1.269亿、Q3指引1.62–1.69亿。

**反证、现金与稀释。** 营业利润仅约32万美元，净利大量来自利息/投资；价格竞争、监管和ADS换算。   9月证券月报：A股215990888、B股1041146800，按1ADS=8普通股折合157.142百万ADS（含为激励预发给存托行股份，不能与期权全额重复相加）。未来175–190百万ADS留稀释。H1 CFO−15.115百万美元、设备和无形支出21.876百万，受限现金1.982百万；报告现金储备含短投/定存，并非全为银行现金。 2029基准归母经营净利为11亿美元收入×12%=1.32亿美元；较Q2近盈亏平衡需明显运营杠杆。净现金650百万是扣未来消耗后的作者假设，相对当前约10亿美元流动性有缓冲；175–190百万未来ADS高于8月约157.142百万ADS等价股数。IR新闻/事件与9月17日中报、9月8日月报核对，未发现未来24小时已排期重大公司二元事件。价格15.52高于本轮模型基准及约14.63上限；不因Q2净利转正就年化。

**完整交易日价格与量价。** 2026-09-29收盘 15.52 USD；当日-0.45%，5/20/60交易日-9.24%/-3.72%/-11.16%。20日均价17.02，50日均价17.24；20日高/低19.16/15.34；末日量/20日均量0.73倍，共104根日线。 20日相对QQQ为-6.68%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/HSAI/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：5.53 / 13.93 / 26.57 USD。按税后经营利润并将非经营净现金单独计入，1ADS与普通股换算须保留来源。 Q3收入162–169百万美元；Q2经营近盈亏平衡，当前净利润不能年化。份额和单价决定营业利润；shares为ADS。

```json
{
  "revenue": [
    800,
    1100,
    1500
  ],
  "net_margin": [
    0.064,
    0.12,
    0.16
  ],
  "shares": [
    175,
    180,
    190
  ],
  "pe": [
    20,
    25,
    30
  ],
  "net_cash": [
    500,
    650,
    750
  ],
  "method": "作者情景敏感性，不是公司预测；2029年归母净利润乘退出PE，加2029可分配净现金，再除以完全稀释股数和(1.15^3.25)。金额和股数均为百万；净利率已经含持续SBC、利息及所得税，净现金不包含客户待履约资金。",
  "currency": "USD",
  "rate": 0.15,
  "years": 3.25
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 单位经济性继续下降且毛利无法覆盖研发，或重要市场准入受实质限制。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价15.52高于本轮作者基准价值13.93及合理参与上限14.63，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/1861737/000110465926108451/tm2625559d1_ex99-1.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://investor.hesaitech.com/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001861737.json)；采集时间2026-09-30T07:49:31.451804+00:00，索引存在不等于全部正文已审核。


## INOD — 研究门通过，账户门待确认

**业务与瓶颈。** AI训练数据与高价值数据集已有收入/利润；Q2营收9214万同比58%、净利1441万。

**反证、现金与稀释。** 前两客户分别37%与34%，不是单客户71%；现金含6700万预付款和6180万未付相关项目成本。 2025收入251.663百万；2026指引至少40%增长，对应下限352.328百万。Q2前两客户37%与34%；H1 CFO164.441百万含67百万客户预付和61.8百万未付项目款。以全部扣除两项余额的压力算法，剩35.641百万，再扣Capex5.309百万为30.332百万；这不是会计调整后FCF，仅检验现金并非全由预付支撑。未来利润计持续SBC，现金不重复加值。 8月6日ATM发行授权上限3亿美元；按66.94美元测算最多约448万新增股，不代表已经售出。未来40–41百万股是假设，实际低价融资或大额收购会使其失效。9月15日8-K是独立董事任命。

**完整交易日价格与量价。** 2026-09-29收盘 66.94 USD；当日+0.22%，5/20/60交易日-4.33%/+18.65%/-8.45%。20日均价59.68，50日均价60.62；20日高/低74.93/51.97；末日量/20日均量0.91倍，共104根日线。 20日相对QQQ为+15.69%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/INOD/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：26.34 / 66.24 / 106.40 USD。2027前瞻归母利润与40–41百万稀释股情景；不额外把全部现金叠加到PE估值。 2025收入251.663百万、2026公司指引同比40%以上；作者2027基准460百万比2026指引下限352.328百万高30.56%。基准净利率16%接近Q2实际，股数比Q2稀释34.771百万增15%；压力保留大客户减单与额外稀释。

```json
{
  "method": "2027前瞻PE在估值日定价；不再按2027退出价格重复折现，不单独叠加现金。金额和股数为百万美元及百万股。",
  "revenue": [
    360,
    460,
    560
  ],
  "net_margin": [
    0.12,
    0.16,
    0.19
  ],
  "shares": [
    41,
    40,
    40
  ],
  "pe": [
    25,
    36,
    40
  ],
  "currency": "USD"
}
```

**价格地图。** 高安全边际研究参考≤45；合理参与研究上限69 USD。两者都不是损失保证。超过上限须重新评估，不自动追涨。

**公司事件。** 9月15日8-K为已生效的独立董事任命；8月6日ATM上限3亿美元，不代表已全部发行。IR无已排期未来24小时重大事件，CEO交接单列管理层风险。 [核查入口](https://investor.innodata.com/events-and-presentations/)

**经济失效。** 前两客户削减订单且新客户无法补足，或正常化净利率持续低于12%/数据集毛利优势消失。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 训练数据已有盈利，扣客户预付及未付项目款后仍有现金生成；2027基准前瞻PE估值66.24美元，合理参与上限取69，包含约4%模型误差带。新增3亿美元ATM按当前价约448万股，40–41百万未来稀释股情景已容纳，但更低价融资会使假设失效。

**触发与组合。** 估值日无新反证且价格不超过上限，可进入账户门计算；不要求完美回踩。若选择盘中执行路径，使用常规盘开盘30分钟后的承接/第二次上破，本报告未核9月30日分钟触发。不因一家公司通过而同时推荐多只高度相关AI股。账户资金、整数1股比例及计划损失未验证；不构成当前股数或订单指令。

**一手与本地证据。**

- [10-Q 2026-08-06](https://www.sec.gov/Archives/edgar/data/903651/000110465926092021/inod-20260630x10q.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/236_INOD.txt)
- [(https://www.sec.gov/Archives/edgar/data/903651/000110465926092010/tm2621499d1_ex99-1.htm)](https://www.sec.gov/Archives/edgar/data/903651/000110465926092010/tm2621499d1_ex99-1.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/137_INOD.txt)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/903651/000110465926092131/tm2622086-4_424b5.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [本轮重大事项追加核验](https://www.sec.gov/Archives/edgar/data/903651/000110465926107790/tm2625393d1_8k.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/latest_material_corrections.json)
- [IR事项补核](https://investor.innodata.com/events-and-presentations/)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/review_overrides.json)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0000903651.json)；采集时间2026-09-30T07:49:31.995108+00:00，索引存在不等于全部正文已审核。


## VPG — 排除

**业务与瓶颈。** 精密应变/力传感有机器人选项，现有工业业务需独立成立。

**反证、现金与稀释。** Q2收入8394万但GAAP经营亏损、毛利下滑；没有证据可将全部收入升级机器人倍数。  

**完整交易日价格与量价。** 2026-09-29收盘 71.70 USD；当日+1.16%，5/20/60交易日+2.56%/+16.00%/-41.71%。20日均价64.84，50日均价73.14；20日高/低73.30/59.00；末日量/20日均量0.46倍，共104根日线。 20日相对QQQ为+13.05%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/VPG/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：5.81 / 34.10 / 86.79 USD。工业盈利正常化为主，机器人只能有条件增量，不凭传感器题材估值。 Q2仍亏损；基准2028 EPS2是工业复苏，强景4需真实机器人增量，现有主题并非量产收入证据。

```json
{
  "method": "2028 EPS x exit PE / (1+r)^2.25",
  "eps": [
    0.5,
    2.0,
    4.0
  ],
  "pe": [
    15.0,
    22.0,
    28.0
  ],
  "rate": 0.12,
  "years": 2.25,
  "fx": 1,
  "currency": "USD",
  "input_currency": "USD"
}
```

**公司事件。** 已检索SEC/本地披露与IR线索，未来24小时事件未完成逐项闭合；当前排除依据为独立估值反证，不将事件缺证当风险已发生。

**经济失效。** 订单改善不能转为利润，或机器人收入始终不足抵消传统业务疲弱。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 当前价71.70高于本轮作者基准价值34.10及合理参与上限35.80，对未来利润要求偏强；属于估值判断，不是因上涨或技术弱势排除。重新入池：回到上限以内且业务无新反证，或一手新增利润/订单证据使规范化盈利上修后重算。

**一手与本地证据。**

- [10-Q 2026-08-05](https://www.sec.gov/Archives/edgar/data/1487952/000143774926025797/vpg20260513_10q.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/237_VPG.txt)
- [(https://www.sec.gov/Archives/edgar/data/1487952/000143774926025779/ex_962771.htm)](https://www.sec.gov/Archives/edgar/data/1487952/000143774926025779/ex_962771.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/140_VPG.txt)
- [VISHAY PRECISION GROUP, INC._10K_2026_V4_CWO-71193.pdf (https://www.sec.gov/Archives/edgar/data/1487952/000143774926011817/vpg20260409_ars.pdf)](https://www.sec.gov/Archives/edgar/data/1487952/000143774926011817/vpg20260409_ars.pdf)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/139_VPG.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001487952.json)；采集时间2026-09-30T07:49:33.735955+00:00，索引存在不等于全部正文已审核。


## RR — 研究未完成

**业务与瓶颈。** 服务机器人及RaaS；现金和短期投资约3.396亿美元，对股价有资产参考。

**反证、现金与稀释。** 9个月收入394.5万、经营亏损3067万；股数大增、资本开支和收购使现金不是清算保证。  

**完整交易日价格与量价。** 2026-09-29收盘 1.59 USD；当日+1.27%，5/20/60交易日-8.09%/-14.97%/-23.92%。20日均价1.68，50日均价1.66；20日高/低1.90/1.56；末日量/20日均量0.72倍，共104根日线。 20日相对QQQ为-17.93%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/RR/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** 压力/基准/强情景现值：0.55 / 0.99 / 1.57 USD。采用现金消耗后的资产价值加经营期权，不用低股价或融资现金证明生意成功。 Class A+B合计约224.386百万，未来股数考虑持续稀释。资产中投融资用途、收购和资本支出能使账面现金快速改变。

```json
{
  "method": "一年后的现金消耗资产敏感性；(现金及短投339.595 - 总负债4.104 - 未来一年消耗 + 经营期权价值)/未来稀释股数/1.15。单位百万美元及百万股。不是可兑现清算价值。",
  "cash_and_investments": 339.595,
  "liabilities": 4.104,
  "burn": [
    160,
    80,
    40
  ],
  "operating_option": [
    0,
    30,
    120
  ],
  "shares": [
    280,
    250,
    230
  ],
  "currency": "USD"
}
```

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 现金用途或继续稀释使每股资产明显减少，且付费部署不能形成正向单位经济。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 投资/收购/资本开支后的可用现金桥；付费部署单位经济性和持续稀释

**未闭合项（2项）。** 投资/收购/资本开支后的可用现金桥；付费部署单位经济性和持续稀释。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [10-Q 2026-08-19](https://www.sec.gov/Archives/edgar/data/1963685/000121390026091798/ea0302286-10q_richtech.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/238_RR.txt)
- [rr-20260331 (https://www.sec.gov/Archives/edgar/data/1963685/000121390026086762/ea0296191-10q_richtech.htm)](https://www.sec.gov/Archives/edgar/data/1963685/000121390026086762/ea0296191-10q_richtech.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/141_RR.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001963685.json)；采集时间2026-09-30T07:49:33.047122+00:00，索引存在不等于全部正文已审核。


## SERV — 研究未完成

**业务与瓶颈。** 末端配送机器人实际部署，有一定商业化收入。

**反证、现金与稀释。** Q2收入323.8万、经营亏损6606.5万；H1经营现金流负8474万，现金余额不能替代单位经济性。  

**完整交易日价格与量价。** 2026-09-29收盘 4.63 USD；当日+4.51%，5/20/60交易日+1.76%/-4.93%/-28.22%。20日均价4.54，50日均价4.81；20日高/低5.06/4.17；末日量/20日均量0.56倍，共104根日线。 20日相对QQQ为-7.88%个百分点差（非超额收益率比值）。 [行情来源](https://api.nasdaq.com/api/quote/SERV/historical?assetclass=stocks&fromdate=2026-05-01&todate=2026-09-29&limit=5000)

**估值。** UNKNOWN，未用统一市销率补空。按配送量×单次贡献减总部成本和未来融资；当前每台/每单完整经济性未闭合。

**公司事件。** SEC/本地披露、IR事件线索已检索，但最新重大事项的有限充分核验尚未闭合；UNKNOWN。

**经济失效。** 配送密度和单台贡献无法覆盖维护运营，融资跑道缩短而扩张继续烧钱。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**处置。** 每单/每台全成本单位经济性；扩张至盈亏平衡的融资与股本情景

**未闭合项（2项）。** 每单/每台全成本单位经济性；扩张至盈亏平衡的融资与股本情景。Owner=current_thread_direct。继续使用本底稿所列公司IR/SEC或当地交易所原文，按上述独立缺口补证；不得以同一工具失败转成排除。 

**一手与本地证据。**

- [10-Q 2026-08-06](https://www.sec.gov/Archives/edgar/data/1832483/000183248326000035/serv-20260630.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/239_SERV.txt)
- [(https://www.sec.gov/Archives/edgar/data/1832483/000183248326000034/serv-20260630_ex991earning.htm)](https://www.sec.gov/Archives/edgar/data/1832483/000183248326000034/serv-20260630_ex991earning.htm)；[保存文本](/Users/USER/Documents/serenity/docs/research/serenity-full-20260930/primary/144_SERV.txt)

- [SEC披露索引](https://data.sec.gov/submissions/CIK0001832483.json)；采集时间2026-09-30T07:49:33.374591+00:00，索引存在不等于全部正文已审核。
