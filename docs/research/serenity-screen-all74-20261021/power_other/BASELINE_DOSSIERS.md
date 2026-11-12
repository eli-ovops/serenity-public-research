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

**估值。** 压力/基准/强情景现值：69.74 / 154.98 / 255.73 USD。须做收购后利润与利息/股数桥接，不能用Q2资产负债表当9月底净债务。 Q2 EPS1.32；基准8是收购后总盈利假设，新增利息桥已核为压力预算，2028增长是假设；9/30历史事件缺口已被本轮SEC索引与公司IR核验替代；本轮事件状态以event_gate及event_asof为准。

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
