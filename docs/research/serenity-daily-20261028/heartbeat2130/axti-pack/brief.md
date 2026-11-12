# 研究包：AXTI（AXT, Inc.）

> 数据抓取 2026-10-28T13:41:55Z · 连接器 v9.1.0 · 用时 3.38 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `AXTI` | 61.65 USD | 4.04B | -56.9% | +675.5% | 125.51M | +164.8% | +76.8% | 44.9% (2026-06-30) | +36.9pp | 32.2x | +42.2% | pricing_power, acceleration, dilution, shelf_registration_on_file, repeated_prospectus_takedowns |

## 2. 主体要点

- 最新季度收入：47.59M USD（期末 2026-06-30）；营业利润率 21.9%；现金+短投 417.20M；FCF 跑道 85.3 季。
- 计算市值：4.04B USD（61.65 × 65,573,212 股，股本截至 2026-08-03）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 8（主文档 6/6）；customer_concentration 8（主文档 6/6）；atm_program 6（主文档 5/6）；capacity_signal 21（主文档 5/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3674 (Semiconductors & Related Devices)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 2 · 👀 2 · ✅ 8 · ℹ️ 2 · — 2

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 164.77% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 44.90% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 36.93pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 3.23% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 0.46% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | -1.42x | 🚩 | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -19565000 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 3.04% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 13.25% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | -103.87pp | ✅ | 应收账款同比（2025-06-30→2026-06-30）− 收入同比 |
| W2 存货增速 − 收入增速 | -144.46pp | ✅ | 存货同比（2025-06-30→2026-06-30）− 收入同比 |
| W3 合同负债/预收同比 | 3,548.94% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 42.16% | 👀 | 最新股本 / 4 个观测点前 − 1；增长快于稀释（例外规则：融资用于扩产且每股收入仍高增长）；每股收入同比 +86.2%；核实融资方式：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| R1 现金跑道（月） | 255.90 月 | ✅ | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |

**估值（USD 口径）**

- 市值 40.43亿 USD · P/E(TTM) 997.2x · P/B 4.6x · P/S 32.2x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素
- [ ] C1 经营现金流 / 净利润（TTM）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-03-17，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1051627/000143774926008612/axti20251231_10k.htm

- **customer_deposits** ×2：…ur completed performance under the contracts. Accounts receivables are recorded when the right to this consideration becomes unconditional. We do not have any material contract assets as of December 31, 2025 or 2024. December 31, December 31, 2025 2024 Contract liabilities $ 103 $ 1,590 During the year ended December 31, 2025, the Company recognized $1.6 million of revenue that was included in the contract balances 
- **long_term_supply_agreement** ×3：…r limited number of suppliers for certain critical materials used in the production of our substrates, such as quartz tubing, arsenic, phosphorus and polishing solutions. We generally purchase our materials through standard purchase orders and not pursuant to long-term supply contracts. Recycling We developed a proprietary process technology that enables us to recycle remnants of indium phosphide processing material
- **customer_concentration** ×3：…idated subsidiaries, in aggregate, accounted for 25% of raw material sales. For the year ended December 31, 2024, three customers of our consolidated subsidiaries, in aggregate, accounted for 31% of raw material sales and for the year ended December 31, 2023, three customers accounted for 31% of raw material sales. Our subsidiaries and consolidated raw material companies are a key strategic benefit for us as they fu
- **export_controls** ×29：…ing statements, but are not the exclusive means of identifying forward-looking statements in this annual report. Additionally, statements concerning future matters such as our strategy and plans, industry trends, tariffs and trade wars, geopolitical tensions, export restrictions in China, the potential impact of epidemic diseases, such as COVID-19, or other pandemics on our business, results of operations and financ
- **default_covenant** ×2：…ly of cash, restricted cash, cash equivalents, short-term investments, and accounts receivable. We invest primarily in money market accounts, certificates of deposits, corporate bonds and notes, and government securities. We are exposed to credit risks in the event of default by the issuers to the extent of the amount recorded on the consolidated balance sheets. Our cash, restricted cash, cash equivalents and short-

### 10-Q（提交 2026-08-13，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm

- **remaining_performance_obligations** ×1：…June 30, 2026. In some contracts we require payment in advance of shipment, per a billing schedule reflected in our customer contracts, and the payment is recorded as a contract liability. As of June 30, 2026, the aggregate transaction price allocated to the remaining performance obligations under the long-term supply agreements was approximately $98.5 million, excluding applicable taxes. We expect to recognize this
- **customer_deposits** ×10：…ilities are summarized below (in thousands): June 30, December 31, 2026 2025 Accrued compensation and related charges $ 4,466 $ 5,090 Preferred stock dividends payable 2,901 2,901 Payable in connection with construction in progress 1,483 1,676 Advances from customers 12,078 103 Accrued income taxes 2,271 841 Current portion of operating lease liabilities 633 579 Accrued professional services 959 1,023 Other tax paya
- **prepayment** ×5：…InP wafer substrates (the “Coherent Products”) for an initial term of three (3) years. We agreed to increase the manufacturing capacity of the Products at our Beijing, China facility in 2026 through 2028 and committed to the delivery of an agreed upon product capacity to Coherent (the “Capacity Commitment”) for a prepayment of $22,288,500 (the “Prepayment”), The Prepayment is refundable to Coherent at its sole optio
- **capacity_reservation** ×6：…. He, the general manager of BoYu, to acquire approximately 0.58% of Tongmei's outstanding shares for approximately $6 million. The transaction had not closed as of the date these financial statements were issued. On July 26, 2026, we entered into a six-year capacity reservation agreement with a customer for the supply of InP wafer substrates. In consideration for the reserved product capacity, the customer agreed t
- **long_term_supply_agreement** ×9：…payment in advance of shipment, per a billing schedule reflected in our customer contracts, and the payment is recorded as a contract liability. As of June 30, 2026, the aggregate transaction price allocated to the remaining performance obligations under the long-term supply agreements was approximately $98.5 million, excluding applicable taxes. We expect to recognize this amount as revenue through the first half of
- **customer_concentration** ×4：…of our revenue for six months ended June 30, 2026 and 2025, respectively. We perform ongoing credit evaluations of our customers’ financial condition, and limit the amount of credit extended when deemed necessary, but generally do not require collateral. No customer accounted for more than 10% of our accounts receivable balance as of June 30, 2026 and one customer accounted for more than 10% of our accounts receivab
- **export_controls** ×30：…to differ materially from those expressed or implied in the forward-looking statement. Additionally, statements concerning future matters such as our strategy and plans, industry trends and the impact of trends, tariffs and trade wars, geopolitical tensions, export restrictions in China, results of operations and financial condition, mandatory factory shutdowns in China, changes in policies and regulations in China 

## 4. 图谱位置与下一跳候选

- 链 `ai_photonics` / 节点 `inp_raw`（高纯红磷 / 铟 / 6N-7N InP 多晶原料，状态 now，类型 material）；同层：4092.T, 5714.T
  - 图谱状态最后核验：2026-10-19（9 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。
- 链 `ai_photonics` / 节点 `inp_substrate`（InP 衬底，状态 now，类型 material）；同层：5802.T, 5016.T
  - 图谱状态最后核验：2026-10-19（9 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。
  - 下一跳 `4092.T` Nippon Chemical Industrial — 高纯红磷 / 铟 / 6N-7N InP 多晶原料（now，依据 serenity_lead）
  - 下一跳 `5714.T` Dowa Holdings — 高纯红磷 / 铟 / 6N-7N InP 多晶原料（now，依据 serenity_lead）

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2025-12-26 `2004569946492453003` REAFFIRM/bullish
  - 2026-04-06 `2041249789195813291` BEARISH/bearish
  - 2026-04-07 `2041521462075633945` REAFFIRM/bullish
  - 2026-10-10 `2108916977616179207` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `AXTI`：sec_stale_series_dropped:buybacks:last_end_2015-12-31_vs_newest_2026-06-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
