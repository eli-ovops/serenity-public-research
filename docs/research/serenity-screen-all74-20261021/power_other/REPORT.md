# Power / Other 23家公司逐只研究 — 2026-10-21

Owner `screen_power_other`。准则v1.1已工具全文读；PERMISSIONS-2026-10-14-v1/ROUTING-2026-10-13-v4。目标模型gpt-6-astra/medium，实际不可核UNKNOWN。冻结23不缩池。研究、账户门、用户决定严格分开。

本分支处置：{'研究门通过，账户门待确认': 7, '排除': 16}；条件观察0，研究未完成0（独立反证排除允许保留与该反证无关的有限证据覆盖限制）。行情统一取10:58–11:00 ET常规盘，完整日线止10月20日；公司事件逐源检索约约14:20 UTC起逐源采集，实际工具时钟15:07:19 UTC完成汇总，窗口至10月22日15:07:19 UTC。未披露事件不能排除。

优先次序：AAON、INOD、DPC、HSAI；MOD/NVT/VRT亦在合理参与区，但拆分/并购/现金预付使承销更复杂。优先级不是个人买股数。已有DPC1、INOD1不可自动再加，AAON/MOD/VRT/NVT高相关只研究一个新挂单。

父线程已确认市场门：QQQ723.35/+0.80%、SPY771.05/+0.26%、RSP216.315/+0.21%，VIX16.98/−1.91%为延迟且不同时点；未见广泛市场同步失控。XLV−0.80%与XBI+0.69%须分开匹配医疗。详见 [MARKET_CONTEXT](../shared/MARKET_CONTEXT.md)。

最新用户成交：DPC已卖1剩1；TEM已卖3剩0；CAMT/AIP卖完由总控登记。本分支不重发已完成卖出。用户当轮NAV/cash UNKNOWN。RXRX20/SCTX2的现仓是临床期权风险选择，本分支新买排除不能自动当已执行退出。

所有金额模型默认百万美元/百万股；每股图USD。模型参数与逐情景中间值见 [MODELS.json](MODELS.json)，可运行 [build_cards.py](build_cards.py) 和 [finalize.py](finalize.py) 复算。临床概率、上市时间、净定价、渗透与现金消耗均为作者敏感性。无假定公司已披露成功率；无永续终值。

|标的|参考价|压力/基准/强|合理上限|固定保护L|研究状态|
|---|---:|---|---:|---:|---|
|MOD|150.860|46.99 / 161.27 / 307.79|169.34|141.55|研究门通过，账户门待确认|
|AAON|73.000|31.05 / 83.80 / 143.39|84.00|71.19|研究门通过，账户门待确认|
|NVT|143.485|67.65 / 154.66 / 257.30|162.40|133.92|研究门通过，账户门待确认|
|PWR|606.005|187.13 / 436.63 / 742.28|458.47|-|排除|
|ETN|391.170|155.94 / 336.83 / 548.91|353.67|-|排除|
|VRT|212.780|94.34 / 210.52 / 364.90|221.05|195.92|研究门通过，账户门待确认|
|GEV|920.680|137.23 / 514.60 / 1122.77|540.33|-|排除|
|HWM|207.550|82.34 / 175.43 / 280.69|184.20|-|排除|
|DPC|28.620|14.89 / 28.12 / 46.59|29.52|27.57|研究门通过，账户门待确认|
|GNRC|200.980|74.85 / 188.69 / 349.31|198.12|-|排除|
|FLNC|6.025|0.00 / 7.26 / 21.14|7.63|-|排除|
|TSLA|386.130|19.19 / 121.71 / 357.21|127.79|-|排除|
|RXRX|3.665|0.17 / 0.60 / 2.24|0.63|-|排除|
|SCTX|20.325|0.92 / 2.73 / 13.67|2.86|-|排除|
|TEM|68.030|19.69 / 46.54 / 92.21|48.87|-|排除|
|LASR|36.470|2.76 / 17.16 / 44.41|18.02|-|排除|
|CCXI|10.395|0.00 / 5.56 / 18.73|5.84|-|排除|
|OUST|30.330|2.86 / 19.19 / 47.66|20.15|-|排除|
|HSAI|13.000|5.57 / 14.04 / 26.77|14.74|12.24|研究门通过，账户门待确认|
|INOD|57.430|26.34 / 66.24 / 106.40|69.00|52|研究门通过，账户门待确认|
|VPG|63.115|5.85 / 34.31 / 87.33|36.02|-|排除|
|RR|1.265|0.55 / 0.99 / 1.57|1.04|-|排除|
|SERV|3.055|0.00 / 0.56 / 17.21|0.59|-|排除|

**订单与风险。** 通过者仅为研究框架：DAY、到10月21日16:00 ET或更早重大新事实失效，不创建订单。合理上限不是建议追到该价；计划损失按实际P−L，1股最低总资金=max(10P,200(P−L))。L基于截至昨收结构与1%容差、从当前起冻结，没有按旧资金倒造。常规收盘破L后下一可交易时点退出，实际跳空风险可更大；限价不封顶损失。当天首股不再加仓，同时只保留一个高相关新单。

**燃机链双向检验。** 数据中心负荷/接网→发电/备用→OEM→热端叶片/导向叶片→单晶/定向铸造→合金/涂层/检测与认证。DPC是Doncasters上市母公司/独立铸造，HWM是多终端热端与航空零部件，GEV是大型OEM/电网/服务；不能互换倍数或声称纯度相同。

[Siemens Energy Q3原件](https://assets.siemens-energy.com/dam/d0147174-31a9-4a78-b062-b49d00428fc4/earnings-release-q3-fy2026-en-pdf_Original%20file.pdf)显示Gas Services订单€9.967bn、收入€3.756bn、调整利润率17.3%、积压€73bn，现金受客户预付/预留费影响。[MHI最新季度](https://www.mhi.com/finance/finance/quarterly-results) Energy Systems订单¥1,359.3bn，跨OEM需求有一手支持。[Berkshire Q2 p43](https://www.berkshirehathaway.com/qtrly/2ndqtr26.pdf) PCC收入$3.1bn、同比14.4%，税前利润增34.2%，航空和工业燃机共同驱动。PCC私人子公司不可直接下单，BRK间接敞口被其他业务稀释，三家证据不证明“仅三家铸造商”。

客户自制叶片一方面说明交期/供给瓶颈，另一方面是后向整合、现有供应商订单转移和估值压缩风险。本轮没有核到足以证明Tesla/SpaceX自产热端已量产并通过长期认证的一手产量/良率证据，不能把传闻当订单利好或现有商已被替代。DPC/HWM的四方长期合作、认证/良率和客户订单兑现必须继续可证伪；OEM扩产还可能增加采购，但不保证独立铸造定价权。

**临床与机器人。** RXRX基准已包含618.428m起始股本、未来融资和SBC，FAP达到作者峰值$1.5bn仍需可付费患者/净价与注册成功；SCTX从18.932m而非IPO前股数起算，IPO并不资助到商业成熟。两者非成熟ROE或统一PS。CCXI的>300m订单附产品/里程碑条件，10k产能不是发货；RR账面现金是融资后资产不是经营价值；SERV实际毛利亏损和指引削减比部署数更影响每股回报。

**原件与边界。** SEC身份/增量见 [SEC_DELTA.json](SEC_DELTA.json)，数值出处/期间/unit/context见 [FINANCIAL_EXTRACT.json](FINANCIAL_EXTRACT.json)。基础完整原件沿用9/30 primary与10/6 reports；正文历史原件和本轮新事件相互桥接，旧价格/状态不延续。本轮16个SEC Archives正文均403已停止，不换客户端重取拒绝资源；独立公司IR/发行人通讯社/HKEX公告用于有限充分替代。WEB_*.json保存检索回执，200空壳不当全文。财务tag并非自动审计，控制数值以逐卡current_bridge为准。

## MOD — 研究门通过，账户门待确认

**身份。** MODINE MANUFACTURING CO / CIK 0000067347 / ['NYSE'] / USD。

**事实、现金与稀释。** Q1FY27 DC revenue348.6/EBIT46.3, HVAC261.6/EBIT31.4; DC gross20.2% down960bp despite sales+90%. Corporate cost/stock compensation remains. Total debt528.2,cash95.3,CFO41.4,capex46.4. Oct1 PT spin closed; received156 cash used repay debt; holders got0.44619 THRM perMOD, no newMODshares. Tax benefit makesEPS1.37 unsuitable annualization.

**估值。** Post-spin continuing business: ((DC sales*EBITmargin+HVAC sales*EBITmargin-corporate-interest)*(1-tax)/shares)*PE/1.12^years。压力/基准/强 46.99/161.27/307.79；参数与融资情景逐项保留于MODELS.json。

拆分后14完整交易日价格变化-19.83%，最近5日-14.99%。原20/60日跨拆分不可直接当经济回撤；本轮新买只看当前业务与拆分后结构，保留原始资料供总回报修复。

**公司事件。** Oct1spincompleted; Nov13shareholdermeeting/Nov18investorday outside24h；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前150.8601，作者基准161.27/参与上限169.34。盈利/现金与稀释桥、有限事件核对、匹配行业走势和当前市场门支持GARP首股研究参与；账户门另验。

**经济失效。** 数据中心订单增速低于新增产能增速且经营利润率持续下降。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**首股框架。** 估值上限169.34；高安全边际参考112.89，不是唯一买价。L=141.55；Oct20已完成20日低点142.9818下方1%容差，按已披露波动结构冻结；此为研究资本保护，不是企业清算/公允价值，不按未知账户倒造。 现价1股金额150.860，计划价差9.310，最低总资金公式结果1862.02，当前账户门未知。常规盘触及L预警并停止新买；常规收盘低于L则首股研究退出，下一可交易常规盘执行；新经济/事件反证无需等收盘。跳空/未监测可超过计划损失。 DAY当日收盘到期。

**一手入口。** [2](https://investors.modine.com/news/news-details/2026/Modine-Reports-First-Quarter-Fiscal-2027-Results/default.aspx)；[3](https://www.sec.gov/Archives/edgar/data/67347/000110465926088569/mod-20260630x10q.htm)；[4](https://data.sec.gov/submissions/CIK0000067347.json)；[5](https://investors.modine.com/news/default.aspx)；[6](https://investors.modine.com/news/news-details/2026/Modine-Completes-Spin-off-and-Combination-of-its-Performance-Technologies-Business-with-Gentherm/default.aspx)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## AAON — 研究门通过，账户门待确认

**身份。** AAON, INC. / CIK 0000824142 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Q2 revenue627,+101.2%,BASX345,backlog2000; gross24.3%; FYgrowth55–60%,gross25–26%,SG&A13–14%. H1CFO54.968,capex97.282,FCF−42.314. Revolver435,available163.692,cash.013,restricted12.714 excluded. Tax9.8% normalized25%; future85–87m shares includesSBC.

**估值。** ((2028 revenue*(gross_margin-opex_margin)-interest)*0.75/shares)*PE/1.12^years。压力/基准/强 31.05/83.80/143.39；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-6.75%，相对XLI -4.71pp；量比1.03。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** IR latestAug21brand,Aug13dividend,Aug10Q2; no knownscheduledbinary next24h；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前73.0000，作者基准83.80/参与上限84.00。盈利/现金与稀释桥、有限事件核对、匹配行业走势和当前市场门支持GARP首股研究参与；账户门另验。

**经济失效。** 积压不能转化为出货，资本开支持续超过融资可承受范围且毛利下滑。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**首股框架。** 估值上限84.00；高安全边际参考58.66，不是唯一买价。L=71.19；Oct20已完成20日低点71.9050下方1%容差，按已披露波动结构冻结；此为研究资本保护，不是企业清算/公允价值，不按未知账户倒造。 现价1股金额73.000，计划价差1.810，最低总资金公式结果730.00，当前账户门未知。常规盘触及L预警并停止新买；常规收盘低于L则首股研究退出，下一可交易常规盘执行；新经济/事件反证无需等收盘。跳空/未监测可超过计划损失。 DAY当日收盘到期。

**一手入口。** [2](https://investors.aaon.com/events)；[3](https://www.sec.gov/Archives/edgar/data/824142/000082414226000055/aaon-20260630.htm)；[4](https://investors.aaon.com/investor-news)；[5](https://investors.aaon.com/)；[6](https://www.sec.gov/Archives/edgar/data/824142/000082414226000059/irpresentationaugust26ta.htm)；[7](https://www.sec.gov/Archives/edgar/data/824142/000082414226000057/aaon-20260812.htm)；[8](https://data.sec.gov/submissions/CIK0000824142.json)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## NVT — 研究门通过，账户门待确认

**身份。** nVent Electric plc / CIK 0001720635 / ['NYSE'] / USD。

**事实、现金与稀释。** Q2 sales1471.3; diluted164.1m shares vs actual161.858m; H1SBC23.1. Oct1Maverickclosed; 1750price +up550earnout; actual June debt1492.4 not October debt. Old noearnout EPS model revised.

**估值。** 2028 EPS x exit PE / (1+r)^2.25。压力/基准/强 67.65/154.66/257.30；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-14.06%，相对XLI -12.02pp；量比1.14。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct30Q3;Oct1Maverickclosed;Oct13AMDHeliosannouncement notbinarynext24h；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前143.4850，作者基准154.66/参与上限162.40。盈利/现金与稀释桥、有限事件核对、匹配行业走势和当前市场门支持GARP首股研究参与；账户门另验。

**经济失效。** 收购协同不能覆盖融资成本或整合令自由现金流/债务比恶化。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**首股框架。** 估值上限162.40；高安全边际参考108.27，不是唯一买价。L=133.92；Oct20已完成20日低点135.2700下方1%容差，按已披露波动结构冻结；此为研究资本保护，不是企业清算/公允价值，不按未知账户倒造。 现价1股金额143.485，计划价差9.565，最低总资金公式结果1913.00，当前账户门未知。常规盘触及L预警并停止新买；常规收盘低于L则首股研究退出，下一可交易常规盘执行；新经济/事件反证无需等收盘。跳空/未监测可超过计划损失。 DAY当日收盘到期。

**一手入口。** [2](https://investors.nvent.com/press-releases/default.aspx)；[3](https://www.sec.gov/Archives/edgar/data/1720635/000110465926111938/tm2626249d1_8k.htm)；[4](https://investors.nvent.com/press-releases/press-release-details/2026/nVent-to-Acquire-Maverick-Power/default.aspx)；[5](https://data.sec.gov/submissions/CIK0001720635.json)；[6](https://investors.nvent.com/investor-relations/default.aspx)；[7](https://investors.nvent.com/press-releases/press-release-details/2026/nVent-Completes-Acquisition-of-Maverick-Power/default.aspx)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## PWR — 排除

**身份。** QUANTA SERVICES, INC. / CIK 0001050915 / ['NYSE'] / USD。

**事实、现金与稀释。** Q2 sales9557,backlog53400,execution/labor constraints; H1CFO1487.188-capex451.048=1036.14FCF,SBCH1126.013; actual150.274m/diluted152.439m. Use profit including financing andSBC; acquisition payment is not operating capex.

**估值。** 2028 EPS x exit PE / (1+r)^2.25。压力/基准/强 187.13/436.63/742.28；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-7.26%，相对XLI -5.22pp；量比1.66。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct29Q3 announcedOct13；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前606.0050，作者基准436.63/参与上限458.47。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 接网项目连续取消/推迟且利润率下降，或并购ROIC不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://investors.quantaservices.com/news-events/press-releases/detail/402/quanta-services-reports-second-quarter-2026-results)；[3](https://investors.quantaservices.com/_assets/_fc69198b082640a1f770638c0383eb48/quantaservices/news/2026-07-30_QUANTA_SERVICES_REPORTS_SECOND_QUARTER_2026_402.pdf)；[4](https://data.sec.gov/submissions/CIK0001050915.json)；[5](https://investors.quantaservices.com/news-events)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## ETN — 排除

**身份。** Eaton Corp plc / CIK 0001551182 / ['NYSE'] / USD。

**事实、现金与稀释。** Q2sales8531,+21%,adjEPS3.15 vsGAAP2.11; FYadjEPS13.40–13.60 vsGAAP10.36–10.56. H1CFO1634-capex446=1188FCF; debt18509+current11,cash483+shortinvest212; approxnetdebt17825m. Weightedshares389.5 vsactual388.4m; no buyback assumed. Mobility RMT Q12027 conditional; Oct16historical recast filing does not equal newQ3results.

**估值。** 2028 EPS x exit PE / (1+r)^2.25。压力/基准/强 155.94/336.83/548.91；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-13.67%，相对XLI -11.64pp；量比1.30。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct16SEC8Kindexrecastfinancial;Oct5transactionfiling; IR no knownnext24h event; bodieslimited；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前391.1700，作者基准336.83/参与上限353.67。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 电气订单下降叠加交期缩短/提价回吐，导致增量利润不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.eaton.com/us/en-us/company/news-insights/news-releases/2026/eaton-reports-record-second-quarter-2026-results.html)；[3](https://data.sec.gov/submissions/CIK0001551182.json)；[4](https://www.eaton.com/us/en-us/company/news-insights/news-releases/2026.html)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only. Oct5/16SECbody403; IR/public historical-recast exhibit trace checked. Valuation counterevidence independent; no event clean bill beyond bounded disclosedindex.

## VRT — 研究门通过，账户门待确认

**身份。** Vertiv Holdings Co / CIK 0001674101 / ['NYSE'] / USD。

**事实、现金与稀释。** Q2revenue3274. H1CFO1866.6-capex285.9=1580.7FCF includes customeradvance timing; cash2810.6 vs noncurrentdebt2939.8 (not exhaustive lease/current debt). SBCH130.8; actual384.937m vsdiluted392.747m. KingEnvironmentalpendingQ4 andUtilityInnovation integration needreturns; targetEPS includesSBC.

**估值。** 2028 EPS x exit PE / (1+r)^2.25。压力/基准/强 94.34/210.52/364.90；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-19.69%，相对XLI -17.65pp；量比1.35。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct28premarketQ3/11amcall；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前212.7800，作者基准210.52/参与上限221.05。盈利/现金与稀释桥、有限事件核对、匹配行业走势和当前市场门支持GARP首股研究参与；账户门另验。

**经济失效。** 订单增长转负同时利润率和回款下降，或新液冷架构令现有系统份额受损。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**首股框架。** 估值上限221.05；高安全边际参考147.36，不是唯一买价。L=195.92；Oct20已完成20日低点197.9000下方1%容差，按已披露波动结构冻结；此为研究资本保护，不是企业清算/公允价值，不按未知账户倒造。 现价1股金额212.780，计划价差16.860，最低总资金公式结果3372.00，当前账户门未知。常规盘触及L预警并停止新买；常规收盘低于L则首股研究退出，下一可交易常规盘执行；新经济/事件反证无需等收盘。跳空/未监测可超过计划损失。 DAY当日收盘到期。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1674101/000162828026050323/q22026exhibit991vrt07292026.htm)；[3](https://www.sec.gov/Archives/edgar/data/1674101/000162828026063311/vrt-20260924.htm)；[4](https://data.sec.gov/submissions/CIK0001674101.json)；[5](https://investors.vertiv.com/news/news-details/2026/Vertiv-Announces-Date-of-Third-Quarter-2026-Earnings-Release-and-Conference-Call/)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## GEV — 排除

**身份。** GE Vernova Inc. / CIK 0001996810 / ['NYSE'] / USD。

**事实、现金与稀释。** Q2revenue11104,H1CFO10680 heavily includes customer advances. Backlog176284m,116GW comprises contracts AND reservations. Debt/lease2849m,current55 included. Actual266.334m vsquarterdiluted270m; H1equitycomp recognition135m. Wind liabilities offset power upside; cannot value as pure smallfoundry.

**估值。** 2028 EPS x exit PE / (1+r)^2.25。压力/基准/强 137.23/514.60/1122.77；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-6.31%，相对XLI -4.27pp；量比1.15。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct28Q3 7:30amET；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前920.6800，作者基准514.60/参与上限540.33。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 预留转单率下降或取消增加，燃机/电网订单不能带动可持续利润率。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev2q2026form10-q.pdf)；[3](https://www.gevernova.com/investors/events/2nd-quarter-2026-earnings-webcast)；[4](https://data.sec.gov/submissions/CIK0001996810.json)；[5](https://www.gevernova.com/investors)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## HWM — 排除

**身份。** Howmet Aerospace Inc. / CIK 0000004281 / ['NYSE'] / USD。

**事实、现金与稀释。** Q2sales2547. H1CFO1036-capex198=838FCF; cash563,debt4050+1,netdebt3488. Actual400m vs diluted402m. Aerospace ismajority exposure; qualified hotcastings value not fullOEM installedbase economics.

**估值。** 2028 EPS x exit PE / (1+r)^2.25。压力/基准/强 82.34/175.43/280.69；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-6.09%，相对XLI -4.05pp；量比2.08。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct29Q3 7amrelease/10amcall；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前207.5500，作者基准175.43/参与上限184.20。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 关键客户资格丢失、产能投资不能维持良率或热端订单增量不转化为利润。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/4281/000000428126000025/hwm-20260630.htm)；[3](https://www.howmet.com/press-release/2026-08-06/howmet-aerospace-reports-second-quarter-2026-results/)；[4](https://www.howmet.com/press-release/2026-07-09/howmet-aerospace-to-host-webcast-and-announce-second-quarter-2026-results/)；[5](https://data.sec.gov/submissions/CIK0000004281.json)；[6](https://www.howmet.com/press-release/2026-10-01/howmet-aerospace-to-host-webcast-and-announce-third-quarter-2026-results/)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## DPC — 研究门通过，账户门待确认

**身份。** DPC Holdings PLC / CIK 0002107018 / ['NYSE'] / USD。

**事实、现金与稀释。** Q2sales268.7,+34%,EBITDA48,LTM160.3; FYsales1000–1040/EBITDA182–187. H1CFO−34,capex19.8,D&A14.8. IPO149.393016m shares; adjustednetcash118.2 includesMIP210.9 payout/private55.4; 846.4rawcash invalid. September325revolver iscapacity. Fourcustomerpartnerships potential>200annualsales,not currentearnings. Oct12Ivostud nonmaterial assetdisposal; booknetassets12.3/FV14.8m so noinvented windfall.

**估值。** EV_EBITDA。压力/基准/强 14.89/28.12/46.59；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整82根日线；20日-28.36%，相对XLI -26.33pp；量比1.99。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Issuer BusinessWire releaseOct20: Nov12premarket8amcall;Oct12nonmaterialIvostuddisposalQ4closing；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前28.6200，作者基准28.12/参与上限29.52。盈利/现金与稀释桥、有限事件核对、匹配行业走势和当前市场门支持GARP首股研究参与；账户门另验。

**经济失效。** IGT增长无法转为更高利用率/利润，或大客户内制、资格或铸造良率受损。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**首股框架。** 估值上限29.52；高安全边际参考19.68，不是唯一买价。L=27.57；Oct20已完成20日低点27.8500下方1%容差，按已披露波动结构冻结；此为研究资本保护，不是企业清算/公允价值，不按未知账户倒造。 现价1股金额28.620，计划价差1.050，最低总资金公式结果286.20，当前账户门未知。常规盘触及L预警并停止新买；常规收盘低于L则首股研究退出，下一可交易常规盘执行；新经济/事件反证无需等收盘。跳空/未监测可超过计划损失。 DAY当日收盘到期。

**一手入口。** [2](https://ir.doncasters.com/news-and-events/news/news-details/2026/Doncasters-Completes-Debt-Refinancing/default.aspx)；[3](https://www.sec.gov/Archives/edgar/data/2107018/000110465926093772/dpc-20260628x10q.htm)；[4](https://data.sec.gov/submissions/CIK0002107018.json)；[5](https://finance.yahoo.com/markets/stocks/articles/dpc-holdings-announces-date-time-203000078.html)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## GNRC — 排除

**身份。** GENERAC HOLDINGS INC. / CIK 0001474735 / ['NYSE'] / USD。

**事实、现金与稀释。** cash264.921,debt1212.527,netdebt947.606. H1CFO240.496-capex87.687=152.809FCF; SBC27.447,quarterdiluted59.635m. Residential/weather demand plus datacenterC&I orders; not puregasturbine manufacturer.

**估值。** 2028 EPS x exit PE / (1+r)^2.25。压力/基准/强 74.85/188.69/349.31；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-5.61%，相对XLI -3.57pp；量比0.71。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct28premarketQ3,10amcall；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前200.9800，作者基准188.69/参与上限198.12。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 数据中心积压取消且住宅需求走弱，使增量资本开支回报不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1474735/000143774926025669/gnrc20260630_10q.htm)；[3](https://www.sec.gov/Archives/edgar/data/1474735/000143774926024731/ex_994826.htm)；[4](https://data.sec.gov/submissions/CIK0001474735.json)；[5](https://investors.generac.com/)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## FLNC — 排除

**身份。** Fluence Energy, Inc. / CIK 0001868941 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Sep16revisedFYsales2400 vs3000,adjEBITDA−200 vs−10; contractmanufacturing ramp/supplychain failure is actual economic counterevidence. Nine monthsCFO−366.5,cash339.3; backlog/newOct14Vattenfall1GWh cannot repair prior cash/operating economics by itself.

**估值。** net_profit。压力/基准/强 0.00/7.26/21.14；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-18.43%，相对XLI -16.39pp；量比0.77。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** LatestOct14Vattenfallaward/Sept24EVE;Oct9SECbodyunread; independenteconomicexclusion；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 已披露收入/利润指引重大下修且现金/单位经济兑现失败；新订单或部署数量未修复经营反证。

**经济失效。** 现金和可用授信不足履约，或主要项目毛利/回款持续低于合同预算。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://ir.fluenceenergy.com/news-releases/news-release-details/fluence-energy-announces-revised-guidance-fiscal-year-2026)；[3](https://www.sec.gov/Archives/edgar/data/1868941/000186894126000029/flnc-20260630.htm)；[4](https://data.sec.gov/submissions/CIK0001868941.json)；[5](https://ir.fluenceenergy.com/)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only. Recent presentation/form fullbody coverage limited; independent guidance/unit-economics counterevidence determines exclusion, not missing body.

## TSLA — 排除

**身份。** Tesla, Inc. / CIK 0001318605 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Q2operatingincome398m; H1CFO8634-capex8282=352FCF,SBC2181; cash15219+shortinvest28305=43524,not all surplus fordistribution. Future4300/4200/4500m shares exceeds historical quarterweighted3540m to reflect awards/dilution. TonightOct21Q3 release excludesnewbuy.

**估值。** 2029 SOTP: automotiveEPS*PE + storageEPS*PE + (robotaxiEV+robotEV)/future dilutedshares; sum discounted1.15^years. No duplicate cash addback; automotiveEPS includes financing and ongoing SBC.。压力/基准/强 19.19/121.71/357.21；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-1.37%，相对XLI +0.67pp；量比0.92。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct21aftercloseQ3 INSIDE24h；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 今晚10月21日盘后财报在未来24h，公司事件硬门失败；估值另含极高未兑现自动驾驶/机器人价值。

**经济失效。** 汽车/储能现金无法支持新增投资，且自动驾驶商业化/安全监管证据长期落后。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1318605/000162828026063820/tsla-20260929.htm)；[3](https://ir.tesla.com/_flysystem/s3/sec/000162828026049213/tsla-20260722-gen.pdf)；[4](https://data.sec.gov/submissions/CIK0001318605.json)；[5](https://ir.tesla.com/)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## RXRX — 排除

**身份。** RECURSION PHARMACEUTICALS, INC. / CIK 0001601830 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Oct15offering61.54m@$3.25,gross200/net187.2; Septembercashinclrestricted561 +net187.2=748.2 estimatepreburn,not Octoberbankbalance. Shares533.191318+Q3ATM23.696330+61.54=618.427648m. H1CFO−187; cashopex≤375 guidance notCFO. REC4881FAP phase1b/2polyp−47%12wk;registrationtrial2H2027 conditionalFDA,Nov2extra data. REC1245phase1earlyresponse,noapproval. Sanofi10option and>300potentialmilestones not guaranteed.

**估值（已修订）。** 月度融资现金不为负的压力/基准/概率加权强景为 0.17/0.60/2.24；同强商业假设、全部PoS=1的条件成功情景为6.52，不是成功上限。融资与反推成功率见CLINICAL_REVISION.md；参数未经实证校准。

截至Oct20完整119根日线；20日-9.63%，相对XBI -4.30pp；量比0.68。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct15financing;Nov2additionalFAPdata outside24h；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 作者审慎估值框架排除新买；总控决定现仓保留20股，不因本次模型更正立即减半。原提议已不采纳，见holding_decision_history。

**经济失效。** 核心临床疗效/安全性失败或现金不足支持关键读出，且合作变现无法补足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1601830/000160183026000098/rxrx-20260630.htm)；[3](https://recursion.com/news/full-transcript-of-recursions-second-quarter-2026-earnings-call)；[4](https://data.sec.gov/submissions/CIK0001601830.json)；[5](https://ir.recursion.com/news-releases/news-release-details/recursion-announces-200-million-oversubscribed-follow-offering)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only. rNPV commercially/probabilistically highly uncertain; no company probability. BIO aggregate clinical success context is not calibrated to this issuer. New-buy valuation conclusion does not mechanically require liquidation of a separately authorized small clinical option position.

## SCTX — 排除

**身份。** Scribe Therapeutics, Inc. / CIK 0001853921 / ['Nasdaq'] / USD。

**事实、现金与稀释。** June cash/securities~43 +IPOnet/concurrent140.6=183.6 beforeburn; Sanofi7.5 included, no doublecount. Aug31shares18.931680m includespreferredconversion. Q2rev1.9,R&D8.8,G&A2.5; H1CFO−12.892,SBC2.197. STX1150humanphase1,firstdata1H2027; preclinical STX1200/1400 is nohuman efficacy. IPO runwaymanagement1H2029; latertrialneed includedfinancing.

**估值（已修订）。** 月度融资现金不为负的压力/基准/概率加权强景为 0.92/2.73/13.67；同强商业假设、全部PoS=1的条件成功情景为69.62，不是成功上限。融资与反推成功率见CLINICAL_REVISION.md；参数未经实证校准。

截至Oct20完整62根日线；20日-29.43%，相对XBI -24.09pp；量比0.42。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** LatestOct7corporatearticle;firstclinicaldata1H2027,not24h；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 作者审慎估值框架排除新买；总控决定现仓保留2股，不因本次模型更正立即减半。原提议已不采纳，见holding_decision_history。

**经济失效。** 人体安全性/持久降脂失败，或关键试验延期导致融资后现金跑道不足。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1853921/000119312526380191/sctx-20260630.htm)；[3](https://www.sec.gov/Archives/edgar/data/1853921/000119312526380184/sctx-20260902.htm)；[4](https://www.sec.gov/Archives/edgar/data/1853921/000119312526380184/sctx-ex99_1.htm)；[5](https://data.sec.gov/submissions/CIK0001853921.json)；[6](https://investors.scribetx.com/news-releases)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only. rNPV commercially/probabilistically highly uncertain; no company probability. BIO aggregate clinical success context is not calibrated to this issuer. New-buy valuation conclusion does not mechanically require liquidation of a separately authorized small clinical option position.

## TEM — 排除

**身份。** Tempus AI, Inc. / CIK 0001717115 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Q2rev382.5,operatingloss75.91 despiteGAAPpositive netincome dueinvestment effects. Oct20S4Nov30vote. Sale3→0 userconfirmed. Modeluses netobligations761.096,actual180.060637m plusSBC10m and deal22.368m; future cashchoice changes denominator andobligations,not completed acquisition.

**估值。** (frozen 2028 enterprise value6150/13500/26000 - netobligations761.096 - cash consideration) / (190.060637 + 1500/referenceprice) /1.12^2.25。压力/基准/强 19.69/46.54/92.21；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-13.53%，相对XLV -19.37pp；量比0.72。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct20S4Nov30Personalisvote not24h；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前68.0300，作者基准46.54/参与上限48.87。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 报销/回款显著恶化、数据许可增长不及成本，或监管限制数据商业化。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.tempus.com/news/pr/tempus-reports-second-quarter-2026-results/)；[3](https://www.sec.gov/Archives/edgar/data/1717115/000119312526326083/tem-ex99_1.htm)；[4](https://data.sec.gov/submissions/CIK0001717115.json)；[5](https://investors.tempus.com/)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## LASR — 排除

**身份。** NLIGHT, INC. / CIK 0001124796 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Q2sales82.59,nearoperatingbreakeven. Cash295.761; H1CFO30.416-capex6.963=23.453FCF,SBC21.849. Actual57.658m vs lossweighted56.983m; future65–78m. $627mJLWScontract conditional budget/milestones,notyearlyrevenue; defense lasers not AIopticalinterconnect.

**估值。** (2029 revenue * net_margin * PE + distributable net_cash) / diluted shares / 1.15^years。压力/基准/强 2.76/17.16/44.41；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-12.09%，相对XLI -10.05pp；量比1.29。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Nov5aftercloseQ3,5pmcall；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前36.4700，作者基准17.16/参与上限18.02。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 主要高能激光合同延期/取消，或量产收入不能将经营利润持续转正。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1124796/000112479626000038/lasr-20260630.htm)；[3](https://data.sec.gov/submissions/CIK0001124796.json)；[4](https://investors.nlight.net/news-releases/news-details/2026/nLIGHT-to-Announce-Third-Quarter-2026-Financial-Results-on-November-5th/default.aspx)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## CCXI — 排除

**身份。** Churchill Capital Corp XI / CIK 0002074973 / ['Nasdaq', 'Nasdaq', 'Nasdaq'] / USD。

**事实、现金与稀释。** ChurchillCapitalCorpXI CIK2074973,Agilitymerger notclosed,expectedAGLTNov2026. OfficialOct13S4effective,Nov2vote. >620m grossproceeds conditionalredemptions; >300mDigit5orders conditional features/milestones;65krealoperatinghours and10kannualcapacity are notdeliveries/profit.

**估值。** 2031 annual paying robot shipments * ASP * sustainable netmargin * PE + terminal netcash, divided by future fully diluted shares and1.18^years; present SPAC trust is NOT permanent downside floor after redemption/closing.。压力/基准/强 0.00/5.56/18.73；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整109根日线；20日-21.19%，相对XLI -19.16pp；量比1.54。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Nov2mergervote; Oct21solicitationindex; detailedlatestproformauncertain；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 即给予2031年1万台/台10万美元、15%净利及30倍PE，含融资稀释基准仍显著低于现价；SPAC现金不是并购后价格底。最新资本条款未读部分仅作残余限制，不冒充独立事件反证。

**经济失效。** 并购条款、赎回或实际融资令普通股经济权益显著差于宣称企业价值。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [1](https://stockanalysis.com/stocks/ccxi/history/)；[2](https://www.sec.gov/Archives/edgar/data/2074973/000121390026089245/ea0300779-10q_churchill11.htm)；[3](https://www.sec.gov/Archives/edgar/data/2074973/000121390026097764/ea0297114-04.htm)；[4](https://data.sec.gov/submissions/CIK0002074973.json)；[5](https://www.agilityrobotics.com/content/agility-robotics-and-churchill-capital-corp-xi-s-4-registration-statement-declared-effective-by-sec-in-connection-with-proposed-business-combination)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only. Oct13finalcaptable fullbody403. Independent conservative no-redemption current-share-plus52.14moptions4.19mwarrants cases already belowmarket; exact postclose ordinary rights need original final proxy before any new recommendation.

## OUST — 排除

**身份。** Ouster, Inc. / CIK 0001816581 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Q2sales54.63; actual68.490m vsweighted65.990m,SBCH118.879. Cash91.759+shortinvest169.322; H1CFO−20.039-capex5.209=−25.248FCF. Future85–100m shares and reducedcash reflect acquisition/SBC; sensorcount includescamera andmust not bealllidar.

**估值。** (2029 revenue * net_margin * PE + distributable net_cash) / diluted shares / 1.15^years。压力/基准/强 2.86/19.19/47.66；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-26.34%，相对XLI -24.30pp；量比0.90。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Nov3aftercloseQ3,5pmcall；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前30.3300，作者基准19.19/参与上限20.15。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 产品毛利和经营现金消耗不随规模改善，或主要工业订单递延。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1816581/000162828026054467/oust-20260630.htm)；[3](https://www.sec.gov/Archives/edgar/data/1816581/000162828026054297/exhibit991-6302026.htm)；[4](https://data.sec.gov/submissions/CIK0001816581.json)；[5](https://investors.ouster.com/news-releases/news-release-details/ouster-announces-date-third-quarter-2026-earnings-call)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## HSAI — 研究门通过，账户门待确认

**身份。** Hesai Group / CIK 0001861737 / ['Nasdaq', 'OTC'] / USD。

**事实、现金与稀释。** USDADSNasdaq; financialRMBconverted bycompanyrelease Q2USD126.9,opprofit.32,netprofit10.4 includesinterest. Q3rev162–169. H1CFO−15.115-capex21.876=−36.991FCF,restricted1.982 excluded. Sept30 ordinaryA215990888+B1045146800 /8=157.642211mADS; 4mnewBdeposited forawards alreadygranted. 2.5704mBnewRSU(0.3213mADS),58.298576mBoptions+19.396736mBRSU partlyprefunded; not alldoubleadded. Future175–190mADS budget. Netcash650m2029 below~1bncurrentliquidity; permanentpricepressure/geopoliticalconstraints risk.

**估值。** (2029 revenue * net_margin * PE + distributable net_cash) / diluted shares / 1.15^years。压力/基准/强 5.57/14.04/26.77；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-18.19%，相对XLI -16.15pp；量比2.18。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** IssuerOct20release+HKEXboardnotice: Nov10premarketQ3/7amcall; current6Kmatchedindependentannouncement；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前13.0000，作者基准14.04/参与上限14.74。盈利/现金与稀释桥、有限事件核对、匹配行业走势和当前市场门支持GARP首股研究参与；账户门另验。

**经济失效。** 单位经济性继续下降且毛利无法覆盖研发，或重要市场准入受实质限制。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**首股框架。** 估值上限14.74；高安全边际参考9.83，不是唯一买价。L=12.24；Oct20已完成20日低点12.3600下方1%容差，按已披露波动结构冻结；此为研究资本保护，不是企业清算/公允价值，不按未知账户倒造。 现价1股金额13.000，计划价差0.760，最低总资金公式结果152.00，当前账户门未知。常规盘触及L预警并停止新买；常规收盘低于L则首股研究退出，下一可交易常规盘执行；新经济/事件反证无需等收盘。跳空/未监测可超过计划损失。 DAY当日收盘到期。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1861737/000110465926108451/tm2625559d1_ex99-1.pdf)；[3](https://investor.hesaitech.com/)；[4](https://data.sec.gov/submissions/CIK0001861737.json)；[5](https://www.globenewswire.com/news-release/2026/10/20/3384091/0/en/index.html)；[6](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/1007/2026100701060.pdf)；[7](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0930/2026093001987.pdf)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## INOD — 研究门通过，账户门待确认

**身份。** INNODATA INC / CIK 0000903651 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Q2rev92.14,+58%,netincome14.412,quarterdiluted34.771m. H1CFO164.441 -67prepay -61.8unpaidprojectcost -5.309capex=30.332m conservative cashstress,notGAAPFCF. SBCH113.104/Q27.196; topclients37% and34%,not one71%. ATMauthorized300m notsales;future40–41m coversmeaningfuldilution; CEO/director8KAitem5.02 isnot earnings.

**估值。** 2027前瞻PE在估值日定价；不再按2027退出价格重复折现，不单独叠加现金。金额和股数为百万美元及百万股。。压力/基准/强 26.34/66.24/106.40；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-21.33%，相对QQQ -17.34pp；量比0.39。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct15issuerrelease Nov5afterclose5pmcall;Sept30amendeddirectorfiling；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前57.4300，作者基准66.24/参与上限69.00。盈利/现金与稀释桥、有限事件核对、匹配行业走势和当前市场门支持GARP首股研究参与；账户门另验。

**经济失效。** 前两客户削减订单且新客户无法补足，或正常化净利率持续低于12%/数据集毛利优势消失。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**首股框架。** 估值上限69.00；高安全边际参考46.37，不是唯一买价。L=52.00；Oct20已完成20日低点50.6800下方1%容差，按已披露波动结构冻结；此为研究资本保护，不是企业清算/公允价值，不按未知账户倒造。 现价1股金额57.430，计划价差5.430，最低总资金公式结果1086.00，当前账户门未知。常规盘触及L预警并停止新买；常规收盘低于L则首股研究退出，下一可交易常规盘执行；新经济/事件反证无需等收盘。跳空/未监测可超过计划损失。 DAY当日收盘到期。

**一手入口。** [2](https://investor.innodata.com/events-and-presentations/)；[3](https://www.sec.gov/Archives/edgar/data/903651/000110465926092021/inod-20260630x10q.htm)；[4](https://www.sec.gov/Archives/edgar/data/903651/000110465926092010/tm2621499d1_ex99-1.htm)；[5](https://www.sec.gov/Archives/edgar/data/903651/000110465926092131/tm2622086-4_424b5.htm)；[6](https://www.sec.gov/Archives/edgar/data/903651/000110465926107790/tm2625393d1_8k.htm)；[7](https://data.sec.gov/submissions/CIK0000903651.json)；[8](https://investor.innodata.com/news/news-details/2026/Innodata-to-Report-Third-Quarter-2026-Results/default.aspx)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## VPG — 排除

**身份。** Vishay Precision Group, Inc. / CIK 0001487952 / ['NYSE'] / USD。

**事实、现金与稀释。** Q2rev83.9,gross38.6%,opmargin−.4%,adj1.7%; Q3rev84–89;Q2orders96m. Cash75.702,debt15.640;H1CFO−.325,SBC1.555;~13.31mshares. 2026adjustedearnings newlyexcludeSBC; modeldoesnot. RobotQ1orders1m cannotjustify entireindustrialbusiness robotpremium.

**估值。** 2028 EPS x exit PE / (1+r)^2.25。压力/基准/强 5.85/34.31/87.33；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-12.02%，相对XLI -9.98pp；量比0.84。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct8issuerrelease Nov4premarketQ3；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前63.1150，作者基准34.31/参与上限36.02。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 订单改善不能转为利润，或机器人收入始终不足抵消传统业务疲弱。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1487952/000143774926025797/vpg20260513_10q.htm)；[3](https://www.sec.gov/Archives/edgar/data/1487952/000143774926025779/ex_962771.htm)；[4](https://www.sec.gov/Archives/edgar/data/1487952/000143774926011817/vpg20260409_ars.pdf)；[5](https://data.sec.gov/submissions/CIK0001487952.json)；[6](https://ir.vpgsensors.com/News/)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## RR — 排除

**身份。** RICHTECH ROBOTICS INC. / CIK 0001963685 / ['Nasdaq'] / USD。

**事实、现金与稀释。** 9mosales3.945,oploss30.67;CFO−3.568 andcapex21.749,SBC9.006. Cash301.962+shortinvest37.633=339.595,liab4.104;ClassA+B224.386m. Cashfinancing-funded,not operatingproof;Oct2meetingvote/Oct7S8POSnoearnings.

**估值。** 一年后的现金消耗资产敏感性；(现金及短投339.595 - 总负债4.104 - 未来一年消耗 + 经营期权价值)/未来稀释股数/1.15。单位百万美元及百万股。不是可兑现清算价值。。压力/基准/强 0.55/0.99/1.57；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-28.90%，相对XLI -26.86pp；量比0.97。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct2meetingresults/Oct7S8POS; no knownnext24h announcement inindex/news；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 当前1.2650，作者基准0.99/参与上限1.04。超过合理参与区；基准兑现回报不足，估值排除。重入需要回到上限以内且基本面无新反证，或一手新增利润/现金证据上修模型。

**经济失效。** 现金用途或继续稀释使每股资产明显减少，且付费部署不能形成正向单位经济。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1963685/000121390026091798/ea0302286-10q_richtech.htm)；[3](https://www.sec.gov/Archives/edgar/data/1963685/000121390026086762/ea0296191-10q_richtech.htm)；[4](https://data.sec.gov/submissions/CIK0001963685.json)；[5](https://ir.richtechrobotics.com/financial-information/sec-filings)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only.

## SERV — 排除

**身份。** Serve Robotics Inc. /DE/ / CIK 0001832483 / ['Nasdaq'] / USD。

**事实、现金与稀释。** Q2rev3.238,costrevenue12.017,grossloss8.779,oploss66.065. H1CFO−84.738,SBC22.038;cash79.112+shortsecurities156.295=235.407,liab26.832. August4shares86.707507m,June86.496060;H1ATMnet84.922. Q2guidanceFYsales9–10 vsprior26,nonGAAPopex140–150: poor deliverydensity isactual counterevidence. Oct5presentation costrevenueupdate not blanket recovery.

**估值。** 2029 delivery unit sensitivity: deployedrobots * utilization * revenue/day *365 /1e6 * netmargin *PE, plus postburn netcash; /future shares /1.18^years。压力/基准/强 0.00/0.56/17.21；参数与融资情景逐项保留于MODELS.json。

截至Oct20完整119根日线；20日-32.97%，相对XLI -30.93pp；量比0.72。均线/回撤是执行软证据，不能替经营估值门。

**公司事件。** Oct5conferencepresentation; no knownnext24h binary; operatingcounterevidence independently excludes；SEC增量索引及上述IR/发行人公告交叉核到所列截点，未发现已知未来24h公司重大二元事件（TSLA明确FAIL）。

**决定。** 已披露收入/利润指引重大下修且现金/单位经济兑现失败；新订单或部署数量未修复经营反证。

**经济失效。** 配送密度和单台贡献无法覆盖维护运营，融资跑道缩短而扩张继续烧钱。 新财报、指引、融资、并购或监管事实改变假设时，本价格图立即失效。

**一手入口。** [2](https://www.sec.gov/Archives/edgar/data/1832483/000183248326000035/serv-20260630.htm)；[3](https://www.sec.gov/Archives/edgar/data/1832483/000183248326000034/serv-20260630_ex991earning.htm)；[4](https://data.sec.gov/submissions/CIK0001832483.json)；[5](https://ir.serverobotics.com/)

**有限覆盖/残余风险。** Forecasts and multiples are author scenarios not certainty; stress not floor. No account access; user-confirmed holdings only. Recent presentation/form fullbody coverage limited; independent guidance/unit-economics counterevidence determines exclusion, not missing body.


## 验收修订：现仓与资本缺口

事件截点采用真实clock回执2026-10-21 15:07:19 UTC，不预填未来15:10。source_tag_receipts的filed=Oct6为继承采集标签，不当SEC真实申报日；SEC_DELTA/submissions才是申报时序。TEM已核旧模型2050×3、2700×5、3250×8，来自serenity-alternatives-20261020-2230/TEM_MODEL.json；随当前68.03静态换股更新，既非固定报价也非已完成并购。

INOD原持仓52收盘保护优先，不下移50.17；原反弹61–65、QQQ<743且无新盈利改善退出同一1股条件保留。上文通用结构说明只适用于新建图；个别数值以CARDS修订为准。

CCXI最新最终资本表正文仍未读；特意列非阻塞现价估值排除的缺口。基准2031年收入1bn、净利15%、30倍与末期现金100m，甚至不计未来稀释且分母仅235.273m，现值8.27；再极端删除全部SPAC/PIPE/激励，仅保留Agility200.871m份额，现值9.69，仍不足现价合理参与。强经营情景可以更高，不能称机器人注定失败；任何重新推荐须先补最终权利表。

### DPC 最新确认现仓判断

{
  "confirmed_shares": 1,
  "research_target_remaining": 1,
  "action": "Hold1, noautomaticadd. Alreadyexecutedsale1 not repeated.",
  "reason": "Price28.62near28.12base, explicit cash/IPO/interest bridge and independent OEM demand retain right-tail46.59; normal operatingcash weakness remains.",
  "protection": "New regular-close27.57 capital-protection review forremaining1; fundamental cancellations/qualification/yield/cash obligations deterioration can exit immediately. Old30.15 secondbatch not reapplied."
}

### RXRX 最新确认现仓判断

{
  "status": "ROOT_DECISION_RECORDED_FOR_FINAL_ACCEPTANCE",
  "confirmed_shares": 20,
  "research_target_remaining": 20,
  "action": "Hold existing position, no add; root retained current9-position facts. Prior half-reduction proposal not adopted and not execution.",
  "reason": "No newly verified clinical/regulatory/financing deterioration during this model-only review and original protection not triggered at the source snapshot. Existing funding supports the next milestone; RXRX has real preliminary efficacy and a registration-development path, SCTX remains early human study with IPO runway. Clinical and commercial upside can exceed risk-adjusted strong. This supports retaining finite existing option exposure while declining new exposure; not proof marketprice is cheap. Prior RXRX reduction already recognized.",
  "limitations": "Current NAV, fees and exact new cash unknown; no budget compliance claim, no continuous monitoring. Clinical data remain early; total loss and future dilution possible.",
  "deadline": "2026-10-30 before11/2 clinical-data event; at next requested review decide event exposure using updated evidence, not indefinite temporaryhold.",
  "exit": "Material efficacy/safety failure or viable registration path denied ->20to0. Cash/financing worsens enough to threaten milestone -> reunderwrite and reduce quantified exposure. Old3.6/4automatic batches remain retired."
}

### SCTX 最新确认现仓判断

{
  "status": "ROOT_DECISION_RECORDED_FOR_FINAL_ACCEPTANCE",
  "confirmed_shares": 2,
  "research_target_remaining": 2,
  "action": "Hold existing position, no add; root retained current9-position facts. Prior half-reduction proposal not adopted and not execution.",
  "reason": "No newly verified clinical/regulatory/financing deterioration during this model-only review and original protection not triggered at the source snapshot. Existing funding supports the next milestone; RXRX has real preliminary efficacy and a registration-development path, SCTX remains early human study with IPO runway. Clinical and commercial upside can exceed risk-adjusted strong. This supports retaining finite existing option exposure while declining new exposure; not proof marketprice is cheap. Prior RXRX reduction already recognized.",
  "limitations": "Current NAV, fees and exact new cash unknown; no budget compliance claim, no continuous monitoring. Clinical data remain early; total loss and future dilution possible.",
  "deadline": "Next material safety/financing update and before2027H1firsthuman data; requested-review only.",
  "protection": "Original mutually exclusive FIRST reduction remains: rebound25-26 without new human evidence ->2to1; OR regularclose<16.7 AND XBI<145 ->2to1. Neither inferred triggered by this model revision. Serious safety/registration/funding failure triggers earlier reassessment including exit; no new lower threshold."
}

### INOD 最新确认现仓判断

{
  "confirmed_shares": 1,
  "research_target_remaining": 1,
  "action": "Hold1, noadd.",
  "reason": "IR Nov5date now closed, normalizedcash stress stillpositive, current57.43 below66.24base. Existingprotect52 and recovery61–65+QQQ<743 unchanged; economiccustomerloss/normalizedmargin<12% exits.",
  "protection": "Existing regularclose52; no relaxation to50.17 despite new20daylow."
}


复算顺序：`python3 build_cards.py` → `python3 finalize.py` → `python3 audit_fix.py`；最后一步包含验收修订，不能省略。VALIDATION.json验证23身份/公式输出/日线截至日/通过者价格与保护关系；验证不等于预测被证实。


## 临床模型独审修订（优先于此前草稿）

只更新RXRX/SCTX。原RXRX20→10、SCTX2→1为未采纳提议，已移入两卡holding_decision_history，未有成交。总控维持RXRX20/SCTX2；融资支持下一里程碑、真实初步疗效/研发路径和可超过概率加权强景的右尾支持保留现有期权敞口，旧保护未因模型修订触发或取消。当前概率/净价未校准，不能把模型差额直接认定确定损失。

统一2028融资已改为现金储备不足前的月初分段融资，假设资金能获得时所有月末现金非负；无法融资则必须停止/缩减研发或寻找合作，不能负现金继续经营。融资价为外生假设，即使高于rNPV亦不意味着确定融到。全预算消耗计入失败路径会高估费用，已增加失败后缩减成本且归零管线价值的配对敏感性。成功率=1条件价值、市场价反推必要成功率/峰销组合、半价融资稀释详见 [CLINICAL_REVISION.md](CLINICAL_REVISION.md) 与两卡模型。复现最后追加 `python3 clinical_repair.py`。
