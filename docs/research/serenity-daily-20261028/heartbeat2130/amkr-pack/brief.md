# 研究包：AMKR（Amkor Technology, Inc.）

> 数据抓取 2026-10-28T13:41:40Z · 连接器 v9.1.0 · 用时 2.82 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `AMKR` | 40.33 USD | 9.99B | -58.3% | +24.9% | 7.46B | +0.2% | +4.9% | 18.3% (2026-09-30) | +3.9pp | 1.3x | +0.2% | repeated_prospectus_takedowns, unregistered_equity_sale_8k_3_02, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity |

## 2. 主体要点

- 最新季度收入：1.99B USD（期末 2026-09-30）；营业利润率 11.3%；现金+短投 2.38B；FCF 跑道 60.9 季。
- 计算市值：9.99B USD（40.33 × 247,810,189 股，股本截至 2026-10-20）。
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 11（主文档 6/6）；customer_concentration 11（主文档 4/6）；atm_program 2（主文档 0/2）；capacity_signal 19（主文档 4/6）；going_concern 3（主文档 0/3）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3674 (Semiconductors & Related Devices)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 1 · ✅ 12 · ℹ️ 3 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 0.18% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 101.27% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 18.26% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 3.94pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 8.30% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 12.91% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 2.44x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -1.56亿 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| B1 资产负债率 | 51.84% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 0.37% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 58,463,000.00 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | 7.79pp | ✅ | 应收账款同比（2025-09-30→2026-09-30）− 收入同比 |
| W2 存货增速 − 收入增速 | 50.81pp | 🚩 | 存货同比（2025-09-30→2026-09-30）− 收入同比 |
| W3 合同负债/预收同比 | 126.62% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 0.25% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| R1 现金跑道（月） | 182.70 月 | ✅ | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 1.34x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 99.94亿 USD · P/E(TTM) 16.1x · P/B 2.1x · P/S 1.3x · 股息率 0.83%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] W2 存货增速 − 收入增速：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-20，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1047127/000104712726000014/amkr-20251231.htm

- **customer_deposits** ×16：…nd test equipment and the Arizona Facility. Net cash provided by operating activities was $1,095.6 million for the year ended December 31, 2025, compared to $1,088.9 million for the year ended December 31, 2024. This increase was primarily due to changes in contract liabilities due to customer advance payments and higher operating profits, offset by changes in working capital. In November 2025, our Board of Director
- **capacity_reservation** ×1：…st their own in-house packaging and test services. As a result, at any time and for a variety of reasons, IDMs and foundries may decide to shift some or all of their outsourced packaging and test services to internally sourced capacity. To the extent we limit capacity commitments for certain customers, these customers may increase their level of in-house packaging and test capabilities, which could make it more diff
- **long_term_supply_agreement** ×2：…ments including interest payments. For additional information regarding our leases, please refer to Note 9 to our Consolidated Financial Statements in Part II, Item 8 of this Form 10-K. We had off-balance sheet purchase obligations for capital expenditures, long-term supply contracts and other contractual commitments. As of December 31, 2025, the purchase obligations were $1,152.4 million, with $1,084.8 million paya
- **customer_concentration** ×6：…kets that use our products and sets forth, for the periods indicated, the percentage of net sales in each end market: 2025 2024 2023 End Market Distribution Data (an approximation including representative devices and applications based on a sampling of our largest customers): Communications (smartphones, tablets) 46 % 48 % 50 % Computing (data center, infrastructure, PC/laptop, storage) 20 % 19 % 16 % Automotive, in
- **export_controls** ×12：…llenges with integrating diverse operations. Risks Related to Our International Sales and Operations •dependence on international factories and operations, and risks relating to trade restrictions and regional conflict, including restrictive trade barriers, export controls, tariffs, customs and duties. Risks Related to Cybersecurity, Data Privacy and Intellectual Property •our ability to develop new proprietary tech
- **default_covenant** ×1：…utstanding obligations thereunder could become immediately due and payable, which could result in a default under our other outstanding debt and could lead to an acceleration of obligations related to other outstanding debt. The existence of such a default or event of default could also preclude us from borrowing funds under our revolving credit facilities. Our ability to comply with the provisions of the indentures

### 10-Q（提交 2026-10-27，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1047127/000104712726000052/amkr-20260930.htm

- **customer_deposits** ×13：…solidated Balance Sheets contained in this Form 10-Q reflects adjustments for foreign currency translation. Unbilled Receivables. Total unbilled receivables as of September 30, 2026 and December 31, 2025 were $329.9 million and $294.1 million, respectively. Contract Liabilities. Contract liabilities were $547.6 million and $390.8 million as of September 30, 2026 and December 31, 2025, respectively. As of September 3
- **capacity_reservation** ×1：…st their own in-house packaging and test services. As a result, at any time and for a variety of reasons, IDMs and foundries may decide to shift some or all of their outsourced packaging and test services to internally sourced capacity. To the extent we limit capacity commitments for certain customers, these customers may increase their level of in-house packaging and test capabilities, which could make it more diff
- **long_term_supply_agreement** ×1：…respectively, with $25.2 million and $52.2 million payable within 12 months, respectively. The lease obligations represent our future minimum lease payments including interest payments. We have off-balance sheet purchase obligations for capital expenditures, long-term supply contracts and other contractual commitments. As of September 30, 2026, the purchase obligations were $2,687.6 million, with $2,635.3 million pa
- **customer_concentration** ×1：…tions and financial results. We have derived and expect to continue to derive a large portion of our revenues from a small group of customers during any particular period due in part to the concentration of market share in the semiconductor industry. Our ten largest customers accounted for, in the aggregate, 72% of our net sales for the year ended December 31, 2025. In addition, we have significant customer concentr
- **export_controls** ×13：…diverse operations. -36- Table of Contents Risks Related to Our International Sales and Operations •dependence on international factories and operations, and risks relating to trade restrictions and regional conflict, including restrictive trade barriers, export controls, tariffs, customs and duties. Risks Related to Cybersecurity, Data Privacy and Intellectual Property •our ability to develop new proprietary techno
- **default_covenant** ×1：…utstanding obligations thereunder could become immediately due and payable, which could result in a default under our other outstanding debt and could lead to an acceleration of obligations related to other outstanding debt. The existence of such a default or event of default could also preclude us from borrowing funds under our revolving credit facilities. Our ability to comply with the provisions of the indentures

## 4. 图谱位置与下一跳候选

- 链 `advanced_packaging` / 节点 `cowos`（CoWoS / 先进封装产能，状态 filling，类型 demand）；同层：TSM, BESI.AS
  - 图谱状态最后核验：2026-10-19（9 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。
  - 下一跳 `3110.T` Nitto Boseki — 高端玻璃纤维布（T-glass）（now，依据 serenity_lead）
  - 下一跳 `LPK.DE` LPKF Laser — 玻璃基板（TGV / LIDE）（coming，依据 serenity_lead）
  - 下一跳 `011790.KS` SKC — 玻璃基板（TGV / LIDE）（coming，依据 serenity_lead）
  - 下一跳 `2802.T` Ajinomoto — ABF 增层膜（monopoly_not_bottleneck，依据 serenity_lead）

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-03-24 `2036451073045700967` REAFFIRM/bullish
  - 2026-07-31 `2083274448845906083` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `AMKR`：sec_stale_series_dropped:buybacks:last_end_2013-12-31_vs_newest_2026-09-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
