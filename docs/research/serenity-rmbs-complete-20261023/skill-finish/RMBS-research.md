# Rambus Inc.（RMBS）· Serenity 框架卡点透镜

<!-- section:verdict -->
> **🟡 观察/等触发** · Amber：RMBS是内存接口芯片与IP设计商，非VECO同类设备商。85.73美元对作者2028基准现值约93.56仅留有限缓冲；真实独占供给未确立。
> 截止 2026-10-23 · 类型 `fabless_designer` · 市值 9.30B USD（2026-10-22）

<!-- section:thirty-sec -->
## 30 秒看懂
Q2收入207.385百万美元、产品99.2百万/+22%、GAAP净利67.605百万、SBC15.886百万。标准FCF52.178百万，但6M CFO同比降15.9%。作者2028 EPS2.2/4/6×PE22/30/36，未来110百万股，不重复加净现金；终值须以12%贴现。新PMIC仍抽样，ChipAgents合作和投资金额未披露，不当订单或盈利。Renesas有竞争产品，机构尚未发现与供给独占均未证实，保留amber。

**分级理由：** 产品/IP捕获有财报支持，但物理独占、机构预期差与充分安全边际未确立；2028利润增长尚为作者情景，非green。

**重估触发条件：** 10/26财报产品增长同时转化到毛利、经营现金及完全稀释EPS；LPDDR6 SOCAMM2 PMIC从抽样进入可核客户量产并有经济贡献；ASR最终结算及持续SBC后的每股现金捕获可量化

<!-- section:live-data -->
## 0. 实时数据
- 快照：`/Users/USER/Documents/serenity/docs/research/serenity-rmbs-complete-20261023/snapshots/RMBS.json` · 取数 2026-10-23T02:25:28Z · 来源 data.sec.gov, news.google.com, query1.finance.yahoo.com, www.sec.gov
- ⚠️ `share_count_older_than_200_days` → 原3/31股数过期警告保留；10Q正文刷新6/30common108.461603m，Q2加权diluted109.977m另列。ASR最终当前股数未知，不直接扣796k。
- ⚠️ `financials_from_fallback: yahoo_timeseries (SEC XBRL latest quarter 2026-03-31)` → 原Yahoo fallback已由Q2 SEC正文逐项核对替代；非GAAP、现金流期间与来源差异均保留，不沿用aggregator作为决定性证据。
- ⚠️ `sec_stale_series_dropped:total_debt:last_end_2023-09-30_vs_newest_2026-03-31` → 2023债务序列陈旧，不沿用。6/30传统银行/债券/可转债无余额，但EDA28.182m+运营租赁21.803m共49.985m；债务类敏感口径净现金774.963m。PE不另加。
- ⚠️ `net_debt_unknown: total debt not found in the financial data; scenarios use net debt 0 until you set valuation.current.net_debt from the balance sheet` → 原未知警告保留并修正：按6/30现金824.948m减EDA及运营租赁49.985m，net_debt=-774.963m；不是当前ASR后现金。PE已含利息，不重复加现金/扣债。
- ⚠️ `post_ASR_actual_common_and_current_cash_not_disclosed` → 已读8/5 ASR协议100m预付与初交796k，未有最终总股本/现金更新；保持6/30common108.461603m且未来110m作者缓冲。不以当前价反推回购股数，不同时保留全部旧现金和完成回购的分母利益。
- ⚠️ `reported_share_date_differs_from_quote_date` → 85.73为10/22常规收盘，108.461603m为6/30已报common；计算市值是混日期示意非实时总股本。Q2加权diluted109.977m单列，未来110m只在情景分母应用一次。
- ⚠️ `debt_includes_EDA_and_operating_lease_sensitivity` → 6/30传统借款无余额不等于无负债：EDA28.182m及运营租赁21.803m计入debt-like49.985m。netdebt=-774.963m为敏感口径；EPS×PE不再加净现金。
- ⚠️ `cash_conversion_H1_CFO_down15_9pct` → H1 CFO144.458m同比-15.9%，库存现金占用30.738m及deferred revenue减少8.241m，确有现金转换反证。Q2FCF52.178m，含installment49.008m；TTM299.535/286.445m，不用错期365.814mCFO掩盖。
- ⚠️ `DOJ_investigation_known_since_Q1_unquantified_tail_risk` → 已比Q1/Q2正文，Q1开始回应DOJ刑事反垄断调查subpoena，未量化损失不等于零。保留尾部风险、不认定有罪、不冒充10/22新二元事件；专业费+7m不能全部归因DOJ。

<!-- section:doctrine -->
## 框架定位（Doctrine）
| 维度 | 判断 | 说明 |
|---|---|---|
| 框架适配 | 卡点 · 部分 | 有架构必需接口功能和IP复用，但RMBS独占性/物理供给瓶颈NOT_ESTABLISHED，不能沿用错误设备图强fit。（PB-FIT-01） |
| 瓶颈状态 | 未知 · demand | 需求增长有收入支持，供给短缺、独供、份额与提价权未有充分一手证据，不把Q2增长改称物理卡点。 [E-LIVE-SEC-01] [E-PRIMARY-RENESAS] |
| 阶段 | 稳态 | 公司已有持续产品/IP收入和盈利；新LPDDR6 PMIC仅sampling子项目，不把整个RMBS当亏损放量故事。 [E-LIVE-SEC-01] [E-PRIMARY-PMIC] |
| 纯度 | 未知（unknown） | Q2产品99.2百万占总收入约47.8%，其余IP/服务也有内存关联但AI专属敞口未单列；不将47.8%伪称纯AI比例。精确产品99.154m/royalties84.261m/contract23.970m约48/40/12%。产品主要客户Micron/Samsung/SKhynix及系统/云；前五客户Q2占60%/H1占64%，不伪造逐笔不可取消订单。 |
| 风险档 | 重估 | PB-STYLE-03 |

<!-- section:variant -->
## 差异化观点
- **市场共识**：可靠实时机构一致预期/渠道订单共识UNKNOWN；不能把股价或旧社交背景当完整市场盈利预期。 
- **我们的看法**：作者基准2028 EPS4、110百万股和30倍PE现值约93.56，较85.73仅有限空间；产品47.8%收入占比不等于AI纯度。
- **为什么市场可能错**：PB-VP-01
- **市场何时会看到**：2026-10-26财报及10/27电话后检验现金/产品指引，不预判发布结果。
- **第一个证伪数字**：`quarterly_operating_cash_flow_USD < 40000000`（2026-10-27 前检查）
- **档案之后的变化**：10/22公司公布ChipAgents合作且投资，金额/收益未披露；10/13新PMIC仍抽样，不能填入量产净利；10/22市场收盘只用于当期估值比较。

<!-- section:capex -->
## 1. 资本开支确定性
- 需求来源：`mixed`
- 服务器/AI内存带宽与模块电源需求支持RCD/PMIC内容增加；公司Q2产品销售是已实现证据。缺客户逐笔不可取消订单、排期和产能预约金额，不能把行业capex直接变RMBS收入。PB-CORE-01。 [E-LIVE-SEC-01] [E-PRIMARY-PRODUCT]

<!-- section:chain -->
## 2. 卡点地图：AI服务器内存接口、模块供电及可许可半导体IP；DDR5/LPDDR6与HBM逻辑不同
- **下游对照**：AI/通用服务器与内存模块客户（unknown）：带宽、功耗及可靠性要求；不假定具体独占合同
- **中游系统**：Micron `MU`：LPDDR6 SOCAMM2生态引言是需求/验证线索，不是向Rambus量产采购承诺
- **中游器件**：**Rambus Inc.** `RMBS`：RCD/PMIC及内存/互连/安全IP；设计、授权、销售而非前道设备；Renesas Electronics `6723.T`：DDR5 RCD/PMIC等真实替代供应商；需逐产品认证比较
- **上游材料/代工**：外部晶圆制造、封装与测试（unknown）：Fabless制造投入和客户资格认证依赖；未具名份额/交期UNKNOWN，不虚构本轮供应商

<!-- section:chokepoint -->
**卡点中的卡点**（hypothesis）：内存接口芯片设计与平台资格认证 — 假设关键层是高速度接口/供电设计、客户认证与IP可复用性；独占制造产能、不可替代认证和涨价权未被本轮证据确立。NOT_ESTABLISHED。 [E-PRIMARY-PRODUCT] [E-PRIMARY-RENESAS] [E-LIVE-DOC-01]

| 卡点原型 | 命中 | 理由 |
|---|---|---|
| ARC-SOLE-SOURCE | no | 公司对外部制造的集中依赖不证明公司自身独占供给；Renesas竞品反驳无替代叙述。 [E-LIVE-DOC-01] [E-PRIMARY-RENESAS] |

<!-- section:gates -->
## 3. 三道闸门
- 🔒 真瓶颈：◐ 部分 — 接口/供电的架构用途成立，已有产品收入；物理短缺、独供及经济定价权NOT_ESTABLISHED，不能给pass。 [E-LIVE-SEC-01] [E-PRIMARY-PRODUCT] [E-PRIMARY-RENESAS]
- 👁️ 前机构：？未知 — 没有经过充分核实的机构持股/覆盖变化和一致预期分布，13G/13D索引不是尚未被发现的证明。 [E-LIVE-SEC-07] [E-LIVE-SEC-08]
- 💰 便宜且去风险：◐ 部分 — 85.73对基准现值约93.56缓冲有限，压力现值约37.74；财报与竞争、现金兑现风险尚在。未来终值120不等于今天现值，不称便宜且已去风险。TTM净利239.680m较229.105m仅+4.62%；基准EPS4从TTM约2.18需约32%CAGR/2.2年并达40%净利率。85.73在30x/12%尺下隐含2028EPS约3.665，已在定价增长，不是低增长便宜股。 [E-LIVE-QUOTE] [E-LIVE-SEC-01] [E-AUTHOR-SCENARIOS]

<!-- section:valuation -->
## 4. 估值不对称（尺子：`chokepoint_comparable`）
现价 85.73 USD × 股本 108,461,603 = 市值 9.30B USD [E-LIVE-QUOTE] [E-LIVE-SHARES]

| 情景（假设） | 期限 | 收入 | 倍数 | 隐含市值 | 隐含每股 | 相对现价 | 叙事 |
|---|---|---|---|---|---|---|---|
| bear | 2.195756y | 900.0M USD | 22x pe @ 27% 净利率 | 5.32B USD | 48.40 | -43.5% | 作者2028归母EPS2.2美元，归母净利242.0百万，收入900百万，PE22倍；利润已含持续SBC/税/利息，不再加净现金或扣第二次稀释。原生输出是2028终值，另用12%和固定2.195756年折现，非当日参与指令。 |
| base | 2.195756y | 1.10B USD | 30x pe @ 40% 净利率 | 13.20B USD | 120.00 | +40.0% | 作者2028归母EPS4美元，归母净利440.0百万，收入1100百万，PE30倍；利润已含持续SBC/税/利息，不再加净现金或扣第二次稀释。原生输出是2028终值，另用12%和固定2.195756年折现，非当日参与指令。 |
| bull | 2.195756y | 1.50B USD | 36x pe @ 44% 净利率 | 23.76B USD | 216.00 | +151.9% | 作者2028归母EPS6美元，归母净利660.0百万，收入1500百万，PE36倍；利润已含持续SBC/税/利息，不再加净现金或扣第二次稀释。原生输出是2028终值，另用12%和固定2.195756年折现，非当日参与指令。 |

同层对照：`6723.T` Renesas DDR5接口/供电真实竞品；本轮未做其财务估值，不声称更便宜或已通过。

> 情景是“要成立需要什么”的假设推演，不是目标价、收益预测或交易建议。

<!-- section:signals -->
## 5. 先行信号（不等财报）
- **内存接口芯片产品收入与资格认证**（filing）— 确认：产品增长伴毛利和每股现金改善，新PMIC由抽样进入获证量产；否定：主要客户取消认证、竞争替代，产品收入连续下滑；下次检查：2026-10-26 results / 2026-10-27 call
- **现金转换和资本分配**（filing）— 确认：营运资本释放且FCF支持SBC及资本分配，ASR结算股数明确；否定：CFO继续落后且库存/应收恶化，回购减少现金却不改善每股捕获；下次检查：2026-10-26

<!-- section:memory -->
## 6. Serenity 公开言论记录（时点）
状态：`available` · 当前 `bull` · 首提 2026-01-22 · 最近 2026-02-16 · 提及 2 次
- 2026-01-22 `WATCH`/neutral · post 2014354847202681059 · 内存超级周期供应链二线受益清单；RMBS 是 HBM 的 ARM（高毛利授权，定价权弱于三大厂）；MRAM 不在 HBM4 栈内
- 2026-02-16 `REAFFIRM`/bullish · post 2023314364757934115 · 内存'收费站'分层：T1 原厂、T2 控制器；MRVL 内存业务占比小、RMBS 授权不受价格上涨益处；Phison CEO 驳中国扩产冲击

档案覆盖至 2026-10-19；此后 Serenity 是否有新表态未知（沉默不等于卖出或看空）。

公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。

<!-- section:serenity-view -->
## 7. 按 Serenity 框架会怎么看
框架是否关注：**maybe** — 按框架先看已盈利接口芯片/IP的设计和认证价值，再核物理瓶颈与每股现金。抽样/合作不当订单（例外9）；需求不等于利润率（例外12–15）；ASR与SBC分开核（例外1）。股价回落本身不证明经营失败（例外17），但不能覆盖本项目独立保护。（规则：PB-FIT-01, PB-CORE-01, PB-LAW-08）

<!-- section:next-hop -->
## 下一跳候选（研究线索，非推荐）
| 代码 | 名称 | 关系 | 节点 | 理由 | 依据 | 先验证 |
|---|---|---|---|---|---|---|
| `6723.T` | Renesas Electronics | 同层 | DDR5接口/PMIC | 真实替代产品，必须比较功耗、验证和商业份额；不是错误VECO设备同业。 | Serenity 公开线索 | 完整客户认证与产品收入口径，不将候选直接升级通过。 |

<!-- section:red-flags -->
## 8. 红旗筛查
- [watch] material_agreement_8k_1_01：**yes** — 8/4 ASR协议、8/5披露100百万预付及初交796千股；是回购现金流而非新经营订单，最终回购总数和当前股本未知。 [E-LIVE-SEC-04]
- [watch] beneficial_owner_filings：**unknown** — 已见13G/A与13G条目，但本轮未完整读持股人及比例，不声称机构新发现或未发现；不为该未知生成绿色结论。 [E-LIVE-SEC-07] [E-LIVE-SEC-08]
- [watch] insider_form4_activity：**unknown** — Form4条目不能单凭数量区分P购买与S销售、授予或税款结算；未作内部人看好论据。 [E-LIVE-DOC-01]
- [watch] supply_concentration：**yes** — Fabless依赖外部制造与客户认证，依赖单一来源不等于自身独供；须同时监控竞争器件替换。 [E-LIVE-DOC-01] [E-PRIMARY-RENESAS]
- [watch] capacity_language：**unknown** — 本轮没有可验证的RMBS产能利用率、不可取消订单与交期数据；销售增长不单独证明供给受限。 [E-LIVE-SEC-01]
- [watch] drawdown：**yes** — 10/22收85.73/-7.62%，日低85.01；SOXX同日-6.79%。共同调整不证明经济论点破裂，也不能取消项目独立风险规则。 [E-LIVE-QUOTE] [E-MARKET-CONTEXT]
- [watch] DOJ_subpoena：**yes** — DOJ subpoena已在Q1披露，非10/22突发新事件；潜在损失无法估计，专业服务费约增7百万不能全部归因DOJ。 [E-LIVE-SEC-02] [E-LIVE-SEC-01]
- [watch] cash_conversion：**yes** — 6M CFO144.458百万同比-15.9%，库存与营运资本增加。Q2标准FCF52.178百万/含分期无形资产支付49.008百万，SBC不是免费，仍检验每股现金兑现。 [E-LIVE-SEC-01]
- [watch] stock_inventory_W2：**yes** — 原技能repairedhealth为13ok/1flag/3info，唯一W2机械flag：库存由2025-06-30的38.603m升至2026-06-30的74.836m（约+93.86%），超过Q2收入同比+20.43%约73.43pp。6/30库存74.836m与12/31的44.098m见10-Q资产负债表及Note5；同比基期38.603m来自已存SEC companyfacts库存系列，见snapshots/RMBS.json。最强替代解释是DDR5放量备货，但没有锁定订单/不可取消承诺或后续销售兑现，不能视为已证。此机械flag不是自动veto；Q3检查库存原值、产品收入、周转和经营现金是否同步兑现。 [E-LIVE-SEC-01] [E-LIVE-FIN]

**阶段 KPI（该阶段看什么，而不是看当期利润）**

| KPI | 状态 | 说明 |
|---|---|---|
| 每股现金转换 | 落后 | 6M CFO同比-15.9%，不能被净利增长覆盖。 [E-LIVE-SEC-01] |
| LPDDR6 SOCAMM2 PMIC量产 | 未开始 | 公开披露抽样中，Micron引言不是采购单。 [E-PRIMARY-PMIC] |

**稀释分类（看方式，不只看幅度）**

- 方式：无明显稀释 · 每股增长能否覆盖稀释：未知
- none仅指本轮已读材料没有可据以认定的新股融资，不代表零SBC。6/30common108.461603m→future110m约1.418%作者稀释；Q2diluted109.977m；ASR初交不推断当前股数。（资金用途：不是已发现ATM融资；ASR是公司现金回购） [E-LIVE-SEC-01] [E-LIVE-SEC-04]

**财务需核实清单（到定期报告/公告原文确认）**

- ☑ 已核实无问题 收入/利润/现金/SBC及股数期间 — Q2/6M分别列明，详FINANCIAL_BRIDGE，不把Q2现金当6M。 [E-LIVE-SEC-01]
- ☐ 待核实 ASR及当前总股本 — 8/5已读100百万预付与初交796千股；最终结算未知，用future110m缓冲，非已确认实际股数。 [E-LIVE-SEC-04]
- ☐ 待核实 客户逐笔订单及前五长约/可取消比例 — 本轮未充分取得逐笔合同，保留UNKNOWN；不作独供或确定放量论据。 [E-LIVE-DOC-01]
- ☑ 已核实无问题 F-FACT/F-TIMING复核 — 已纠正设备同业误分类、错期TTM、ASR推断；抽样不当订单，10/26为明确复核点，未用方向正确无限后移。 [E-LIVE-SEC-01] [E-LIVE-SEC-04] [E-PRIMARY-PMIC]
- ⚠️ 发现问题 W2库存增速超收入：核原值及后续周转 — 10Q资产负债表/Note5库存74.836m（6/30）对44.098m（12/31）；SEC companyfacts同口径2025-06-30为38.603m，YoY约93.86%对收入20.43%，差73.43pp。DDR5备货仅替代解释，订单锁定未证实。10/26 Q3披露后核库存与产品收入、周转、现金兑现，不把机械flag自动当veto或静默删除。 [E-LIVE-SEC-01] [E-LIVE-FIN]

<!-- section:red-team -->
## 9. 红队：杀死这个判断的最短路径
1. 为什么可能不是真瓶颈？Renesas等可提供RCD/PMIC替代器件，客户可以多源认证；模块需求与设计难度不证明RMBS不可替代或供给约束。
2. 为什么可能不变现？Q2盈利和产品收入已有兑现，但授权确认不等于现金royalty，6M CFO下降且SBC、营运资本会削弱每股现金回报。
3. 市场是否已定价？以85.73对作者2028基准EPS4与30倍PE贴现约93.56，缓冲有限；若增长已被资本化，利润上修不足以抵消倍数下降。
4. 更优替代：`6723.T` — Renesas是真实DDR5接口与供电替代来源，应核认证/功耗/客户量产比较；本轮未证明其股票更优。

**最大杀点：** 内存客户通过竞争产品或自研完成新代认证，RMBS每模块价值/份额下降；叠加许可收入现金收取落后，2028 EPS4在持续SBC后无法兑现。

<!-- section:falsification -->
## 10. 证伪条件
- 作者基准现金转换复核阈值：若单季经营现金低于40百万，触发重新承销而非自动证明破产；阈值为作者风险检验。 `机器可检: quarterly_operating_cash_flow_USD < 40000000`（检查：2026-10-27）（PB-EXIT-03）
- 关键客户认证取消或被竞品替代且管理层实质下调中期利润；需原披露，不能用价格下跌替代。（检查：2026-10-27）（PB-EXIT-01）

<!-- section:evidence -->
## 证据
- [E-LIVE-QUOTE] Nasdaq RMBS Oct22 regular close85.73 O88.09 H90.50 L85.01 — https://api.nasdaq.com/api/quote/RMBS/info?assetclass=stocks（2026-10-22，market_data）
- [E-LIVE-SHARES] 10Q common108461603 June30; Q2weighted diluted109977000, distinct measures — https://www.sec.gov/Archives/edgar/data/917273/000119312526321000/rmbs-20260630.htm（2026-07-28，filing）
- [E-LIVE-FIN] Q2 SEC revenue207.385m/NI67.605m/SBC15.886m; 6M CFO144.458m — https://www.sec.gov/Archives/edgar/data/917273/000119312526321000/rmbs-20260630.htm（2026-07-28，filing）
- [E-LIVE-SEC-01] 10-Q filed 2026-07-28 — https://www.sec.gov/Archives/edgar/data/917273/000119312526321000/rmbs-20260630.htm（2026-07-28，filing）
- [E-LIVE-SEC-02] 10-Q filed 2026-04-28 — https://www.sec.gov/Archives/edgar/data/917273/000119312526186931/rmbs-20260331.htm（2026-04-28，filing）
- [E-LIVE-SEC-03] 8-K filed 2026-09-04 (officer/director change) — https://www.sec.gov/Archives/edgar/data/917273/000119312526383630/d80115d8k.htm（2026-09-04，filing）
- [E-LIVE-SEC-04] 8-K filed 2026-08-05 (material definitive agreement, new debt obligation, exhibits) — https://www.sec.gov/Archives/edgar/data/917273/000119312526333887/d122300d8k.htm（2026-08-05，filing）
- [E-LIVE-SEC-05] 8-K filed 2026-07-27 (results of operations, exhibits) — https://www.sec.gov/Archives/edgar/data/917273/000119312526318063/rmbs-20260727.htm（2026-07-27，filing）
- [E-LIVE-SEC-06] 8-K filed 2026-04-29 (officer/director change, exhibits) — https://www.sec.gov/Archives/edgar/data/917273/000119312526192210/d20390d8k.htm（2026-04-29，filing）
- [E-LIVE-SEC-07] SCHEDULE 13G/A filed 2026-07-29 — https://www.sec.gov/Archives/edgar/data/917273/000201238326002936/xslSCHEDULE_13G_X02/primary_doc.xml（2026-07-29，filing）
- [E-LIVE-SEC-08] SCHEDULE 13G filed 2026-06-05 — https://www.sec.gov/Archives/edgar/data/917273/000031506626001421/xslSCHEDULE_13G_X02/primary_doc.xml（2026-06-05，filing）
- [E-LIVE-NEWS-01] [lead] Rambus And Chipagents Collaborate To Accelerate Chip Design With Agentic Ai - TradingView — https://news.google.com/rss/articles/CBMi3gFBVV95cUxQeEtzSHBMcE9OVDF5NUZleV9qLXh4eGpWTVM3Y1BfczBKc1ZSSkVjcUdjZjRrY184eUpqWUFRWUZ6a2ZkSmhKZmNUd20xWmtlamJRbGp1OS1jRHVvaGVZNXZ4Um9QSG10V0dJS0F0Q0gzV1I1YmFDcDdsc2lzdHhXSVFQdFVrLVNWcFY3YzNFV1JNY3N1aWc4X0lxWUpxd2ExYzNMX2Q2Rll5THg1aVRQNDJTakc0a3RGalBYdzVqRlE5ODZKUGwyUC1jRWJRb1pMQjU3amZ5RjRyRXBlRlE?oc=5（2026-10-22，news）
- [E-LIVE-NEWS-02] [lead] Rambus invests in ChipAgents, adopts its AI chip design platform - StreetInsider — https://news.google.com/rss/articles/CBMiwwFBVV95cUxNdXlSU01JMXBvbVJzckYwMXhKZVFsbG5WX2xCUmVYT2VDdUlxRzVvb2FLTEI4b3JEUVB1ajBaN2ZYSGlCOWp1S0dhRjBsS2RDUnVtSmcwUEkxZmk2OWRRWGR5M2JwT0pIckNNV2VmRVZsUlcyRHg1TUZfMXpnSnlZRm52ZEhqbkFjYzN5YjU4Ukw5MzdhYmZyeGVZa3d6UHhxS21OaHd3ZTNSUGRuV3ZoeG8zM2k1ZlNBaHM5WGtZLW5hVEk?oc=5（2026-10-22，news）
- [E-LIVE-NEWS-03] [lead] Rambus Could Be an Overlooked Winner in the AI Memory Boom - Yahoo Finance — https://news.google.com/rss/articles/CBMingFBVV95cUxOazlnUVlFV2RvcWoxWmdNemlZOVhOVzY0WnVpLWtfQk1KRDdJWFRycndEMXhhREJTQVhwM0k1TWJVZnJWbUEwVWlidlRhZ2FSdnlHbXI2MU1TcjFmcU1WUC1yODdfZ1FGVjFidHM5bnFYNmliMUxCaURyWWROUHVNVGpIYmM2YnJEV2hMUkVfaDFWMGFoamhWVFFOaVhyUQ?oc=5（2026-10-22，news）
- [E-LIVE-NEWS-04] [lead] Rambus Could Be an Overlooked Winner in the AI Memory Boom - AOL.com — https://news.google.com/rss/articles/CBMigwFBVV95cUxNTnhNa016RXRSWWVaVm1ZSXQ1bFpfeWlHanpiRXZfdWJ0YmVJemhBVnJSd19YY1ZlODgtX2Z0VENjdU04bnBvemlxeEk2SnVJN3ZEcWtqMTFMQnE5eG82d3duaFk1QWFjWkR4aW9hWGJCeExvWFBkQXpKZjhncmk4LWl1SQ?oc=5（2026-10-22，news）
- [E-LIVE-NEWS-05] [lead] Rambus Could Be an Overlooked Winner in the AI Memory Boom - 24/7 Wall St. — https://news.google.com/rss/articles/CBMipAFBVV95cUxOTklDenl2bkRkbVFua09yS28tR2pnX1lsd18wZ0dwQTJKSWlDcmZQcmNVMlM1b3BreVJCcFR6YWhoYk9MMXE5cHJOUTF0QnU2eGlLNDhFeXptbV9rWEYyY1hmcjBsR1BSTm5fMkk4TDFPN1BrY2dudWlBa0Y4dGIwbUpidFlqZ2FPWC1WczhIQW9SUV9FTHdtS01HN2g0c2ZpZ3BUQQ?oc=5（2026-10-22，news）
- [E-LIVE-NEWS-06] [lead] Rambus, Inc. (RMBS) Stock Forecasts - Yahoo Finance — https://news.google.com/rss/articles/CBMijwFBVV95cUxQc2ZJeXdHWWgyOUZYSzFTOVlZM1F4NnlLVjVRYXhwNmZVdVdHVXpsTlU3NXdSalJOLVdVMDVhUFpING9vTnJRcHM4aDNMelJTVGljeXBucHFVV3p5RXo1aU1zcmt2cGtlNlltYzB5LUFITFRiSURyUlloRDFTdVlNWXB4TzNROHctYVRvY1FMZw?oc=5（2026-10-21，news）
- [E-LIVE-DOC-01] 10-K filed 2026-02-18 (primary document) — https://www.sec.gov/Archives/edgar/data/917273/000119312526057101/rmbs-20251231.htm（2026-02-18，filing）
- [E-LIVE-DOC-02] 10-Q filed 2026-07-28 (primary document) — https://www.sec.gov/Archives/edgar/data/917273/000119312526321000/rmbs-20260630.htm（2026-07-28，filing）
- [E-PRIMARY-PRODUCT] Rambus RCD/PMIC memoryinterface product architecture — https://www.rambus.com/memory-interface-chips/（2026-10-23，company_release）
- [E-PRIMARY-RENESAS] Renesas DDR5 competing RCD/PMIC products — https://www.renesas.com/en/products/memory-logic/memory-interface-products/ddr5-solutions（2026-10-23，company_release）
- [E-PRIMARY-PMIC] Oct13 LPDDR6 SOCAMM2 PMIC sampling; Microncomment notpurchaseorder — https://www.rambus.com/rambus-advances-power-efficient-ai-infrastructure-with-industry-leading-pmic-designed-for-lpddr6-socamm2/（2026-10-13，company_release）
- [E-PRIMARY-CHIPAGENTS] Oct22 ChipAgents collaboration/investment; amount not disclosed — https://www.rambus.com/rambus-and-chipagents-collaborate-to-accelerate-chip-design-with-agentic-ai/（2026-10-22，company_release）
- [E-PRIMARY-CALENDAR] Company notice Oct26 14:00PT Q3call, BeijingOct27 05:00 — https://www.nasdaq.com/press-release/rambus-announce-third-quarter-fiscal-year-2026-results-2026-10-05（2026-10-05，company_release）
- [E-AUTHOR-SCENARIOS] Author frozen EPS/PE/revenue/share sensitivity; not guidance — /Users/USER/Documents/serenity/docs/research/serenity-rmbs-complete-20261023/present-values.json（2026-10-23，analysis）
- [E-MARKET-CONTEXT] Oct22 SOXX-6.79%,QQQ-2.86%; marketdata no businessproof — /Users/USER/Documents/serenity/docs/research/serenity-rmbs-complete-20261023/public/INFO_SOXX.json（2026-10-22，market_data）

审计层：research_output `research:rmbs-2026-10-23`，bundle 校验 未运行

<!-- section:disclaimer -->
---
⚠️ 框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。

<!-- serenity-lens lens_id=lens:rmbs-2026-10-23 sha256=f41bf7878527ead533d65704f1da89c3ccd87c469f8473f38d4018e3cab790c2 -->
