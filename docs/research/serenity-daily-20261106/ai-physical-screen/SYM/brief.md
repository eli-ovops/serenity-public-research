# 研究包：SYM（Symbotic Inc.）

> 数据抓取 2026-11-06T04:28:37Z · 连接器 v9.1.0 · 用时 2.83 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SYM` | 35.04 USD | 4.52B | -60.1% | -50.5% | 2.65B | +21.7% | +6.6% | 22.3% (2026-06-27) | +3.4pp | 1.7x | — | shelf_registration_on_file, repeated_prospectus_takedowns, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity |

## 2. 主体要点

- 最新季度收入：720.84M USD（期末 2026-06-27）；营业利润率 4.6%；现金+短投 1.75B；FCF 跑道 — 季。
- 计算市值：4.52B USD（35.04 × 128,931,651 股，股本截至 2026-06-30）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 4（主文档 2/4）；customer_concentration 12（主文档 5/6）；atm_program 3（主文档 2/3）；capacity_signal 16（主文档 4/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3569 (General Industrial Machinery & Equipment, NEC)）
- 数据：sec_companyfacts，报告期 2026-06-27，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 2 · 👀 1 · ✅ 8 · ℹ️ 2 · — 2

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 21.74% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 22.32% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 3.43pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 0.31% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 1.16% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 108.96x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C3 股权激励费用 / 收入（TTM） | 8.86% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 67.82% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 8.45% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 90.05pp | 🚩 | 应收账款同比（2025-06-28→2026-06-27）− 收入同比 |
| W2 存货增速 − 收入增速 | 37.25pp | 👀 | 存货同比（2025-06-28→2026-06-27）− 收入同比 |
| W3 合同负债/预收同比 | 69.24% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 1.71x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 45.18亿 USD · P/E(TTM) 550.3x · P/B 6.4x · P/S 1.7x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素
- [ ] W1 应收增速 − 收入增速：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2025-11-24，期末 2025-09-27）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1837240/000183724025000278/sym-20250927.htm

- **remaining_performance_obligations** ×11：…re the goods reach our solution, which include order qualities, pricing and packaging. There are also benefits for our customers after the goods leave our solution, which include optimized trailer utilization and optimal sequencing for routing and receiving. Remaining Performance Obligations (i.e., backlog) As of September 27, 2025, we had approximately $22.5 billion of backlog of orders from our customers, of which
- **customer_deposits** ×8：…significant reversal of revenue. Typically, consideration is due from customers in advance or upon the achievement of billing milestones, the timing of which does not always align with the satisfaction of performance obligations, creating contract assets or contract liabilities. Contract assets primarily relate to the Company’s rights to consideration for work completed but not billed at the reporting date. Contract
- **sole_source** ×2：…n our business may not be timely available at reasonable rates, or at all. These disruptions could cause a delay in our manufacturing and construction of our systems and thus a delay in our implementation schedules for our customers. We also maintain several single-source supplier relationships because the relationship is advantageous due to performance, quality, support, delivery, capacity or price considerations. 
- **customer_concentration** ×6：…our operating results and financial position could be materially affected. We depend heavily on our larger customers, and therefore, our success is heavily dependent on their ability to grow their businesses and their adoption of our systems. Walmart, our largest customer, accounted for approximately 85% of our total revenue in the fiscal year ended September 27, 2025 and for a significant majority of our $22.5 bill
- **material_weakness** ×18：…ess; •successfully defend litigation; •issue equity securities in connection with future transactions; •meet future liquidity requirements and, if applicable, comply with restrictive covenants related to long-term indebtedness; •timely and effectively remediate any material weaknesses in our internal control over financial reporting; •anticipate rapid technological changes; •maintain the listing of our common stock 
- **export_controls** ×4：…y with governmental regulations that are applicable to our business, which include, among others, laws, regulations and permitting requirements of federal, state and local authorities, including related to environmental, health and safety, anti-corruption and export controls. Environmental Matters We are subject to domestic and foreign environmental laws and regulations governing our operations including, but not li

### 10-Q（提交 2026-08-05，期末 2026-06-27）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1837240/000183724026000043/sym-20260627.htm

- **remaining_performance_obligations** ×10：…ts or services to customers. During the nine months ended June 28, 2025, the Company recognized $567.9 million of the contract liability balance at September 28, 2024, as revenue upon transfer of the products or services to customers. 18 Table of Contents Remaining Performance Obligations Remaining performance obligations represent the aggregate amount of the transaction price allocated to performance obligations no
- **customer_deposits** ×6：…these categories best depict how the nature, amount, timing, and uncertainty of revenue and cash flows are affected by economic factors. Contract Balances The following table provides information about accounts receivable, unbilled accounts receivable, and contract liabilities from contracts with customers (in thousands): June 27, 2026 September 27, 2025 Accounts receivable $ 288,533 $ 186,705 Unbilled accounts rece
- **customer_concentration** ×1：…epresents this customer’s aggregate percent of total revenue. Three Months Ended Nine Months Ended June 27, 2026 June 28, 2025 June 27, 2026 June 28, 2025 Customer A 90.5 % 83.8 % 87.0 % 85.1 % At June 27, 2026 and September 27, 2025, one customer accounted for over 10% of the Company’s accounts receivable balance. The following table represents this customer’s aggregate percent of total accounts receivable. June 27
- **material_weakness** ×6：…usiness; •successfully defend litigation; •issue equity securities in connection with future transactions; •meet future liquidity requirements and, if applicable, comply with restrictive covenants related to long-term indebtedness; •timely and effectively remediate any material weaknesses in its internal control over financial reporting; •anticipate rapid technological changes; •maintain the listing of the Symbotic 

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 SYM 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `SYM`：sec_stale_series_dropped:capex:last_end_2024-12-28_vs_newest_2026-06-27

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
