# 研究包：MSAI（MultiSensor AI Holdings, Inc.）

> 数据抓取 2026-11-06T04:34:29Z · 连接器 v9.1.0 · 用时 3.41 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `MSAI` | 3.054 USD | 6.74M | -94.9% | -93.6% | 6.27M | +19.4% | +5.0% | — | — | 1.1x | -93.6% | shelf_registration_on_file, repeated_prospectus_takedowns, unregistered_equity_sale_8k_3_02, material_agreement_8k_1_01, beneficial_owner_filings |

## 2. 主体要点

- 最新季度收入：1.70M USD（期末 2026-06-30）；营业利润率 -153.4%；现金+短投 21.00M；FCF 跑道 10.3 季。
- 计算市值：6.74M USD（3.054 × 2,205,648 股，股本截至 2026-08-10）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 8（主文档 2/6）；customer_concentration 15（主文档 4/6）；atm_program 33（主文档 6/6）；capacity_signal 18（主文档 2/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3827 (Optical Instruments & Lenses)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 2 · 👀 1 · ✅ 6 · ℹ️ 3 · — 2

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 19.45% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | — | ℹ️ | 毛利 / 收入（最新期） |
| P2 净利率（TTM） | -141.70% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -31.19% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 0.91x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C3 股权激励费用 / 收入（TTM） | 11.23% | 👀 | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 14.56% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 287.28pp | 🚩 | 应收账款同比（2025-06-30→2026-06-30）− 收入同比 |
| W2 存货增速 − 收入增速 | -42.99pp | ✅ | 存货同比（2025-06-30→2026-06-30）− 收入同比 |
| W3 合同负债/预收同比 | 33.18% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | -93.62% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 1.07x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 6,736,048.99 USD · P/B 0.2x · P/S 1.1x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素
- [ ] W1 应收增速 − 收入增速：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-03-19，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1863990/000110465926032148/msai-20251231x10k.htm

- **customer_deposits** ×13：…entories, noncurrent 379 865 Other noncurrent assets 129 — Total assets $ 35,474 $ 15,478 Liabilities and shareholders’ equity Current liabilities Accounts payable $ 291 $ 825 Income taxes payable — 59 Accrued expense 981 1,095 Contract liabilities 1,255 483 Legacy SMAP promissory notes — 172 Right-of-use liabilities, current — 138 Other current liabilities 121 245 Total current liabilities 2,648 3,017 Contract liab
- **prepayment** ×1：…re to enter into bankruptcy proceedings or similar proceedings whereby contractual commitments are subject to stay of execution and the possibility of legal or other modification, we could be forced to record a substantial loss. From time to time, we may make prepayments associated with long-term supply agreements to secure supply of inventory components. While we are implementing procedures to monitor and limit exp
- **long_term_supply_agreement** ×1：…proceedings or similar proceedings whereby contractual commitments are subject to stay of execution and the possibility of legal or other modification, we could be forced to record a substantial loss. From time to time, we may make prepayments associated with long-term supply agreements to secure supply of inventory components. While we are implementing procedures to monitor and limit exposure to credit risk on our 
- **sole_source** ×1：…nnot assure that it will not face increased prices in the future or, if we do, whether we will be effective in containing margin pressures from any further component price increases. 25 Table of Contents Key components in our products come from limited or single source third party suppliers. Interruptions in our relationships with these third parties could adversely impact our business. We rely on third parties to s
- **customer_concentration** ×3：…e. Customers We primarily target customers in the distribution and logistics, manufacturing and data center markets. For the year ended December 31, 2025, one customer in the distribution and logistics market accounted for 36% of total net revenue. No other customer accounted for more than 10% of total net revenue. Distribution and Logistics Our customers in the distribution and logistics market are generally engage
- **going_concern** ×2：…t significantly improved its liquidity position. After considering the proceeds from these equity financings, the Company’s current cash flow forecasts, and its planned operating and investing activities, management has concluded that the previously disclosed substantial doubt regarding the Company’s ability to continue as a going concern has been alleviated for a period of at least 12 months following the date of t
- **export_controls** ×8：…ing exportation of our thermal imaging technology vary from country to country and product to product. Exporting our thermal cameras, infrared cameras, or infrared sensors to certain countries may be restricted by the United States Government’s thermal camera export restrictions and many fall under International Traffic in Arms Regulations (“ITAR”). All ITAR items are designated by the U.S. Department of State. Some
- **at_the_market** ×2：…the Company utilized the B. Riley Committed Equity Facility to sell 1,814,731 and 23,999 shares of Common Stock for cash proceeds totaling $4.7 million and $58 thousand, respectively. Effective February 2, 2026, the Company terminated the Purchase Agreement. At the Market Sales Agreement On March 28, 2025, we entered into an at market issuance sales agreement (the “2025 Sales Agreement”) with B. Riley Securities, In

### 10-Q（提交 2026-08-13，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1863990/000110465926095907/msai-20260630x10q.htm

- **customer_deposits** ×9：…ventories, noncurrent 306 379 Other noncurrent assets 181 129 Total assets $ 33,349 $ 35,474 Liabilities and shareholders’ equity Current liabilities Accounts payable $ 258 $ 291 Income taxes payable 7 — Accrued expense 772 981 Contract liabilities 2,950 1,255 Other current liabilities 59 121 Total current liabilities $ 4,046 $ 2,648 Contract liabilities, noncurrent 768 751 Warrants — 10 Deferred tax liabilities, ne
- **customer_concentration** ×2：…estimates and assumptions that affect the amounts reported in our condensed consolidated financial statements and accompanying notes. Actual results may differ materially from those estimates. Customer Concentration For the three months ended June 30, 2026, one customer accounted for 66% or $1,119 of total net revenue, which was recorded under the entity’s one operating segment. For the six months ended June 30, 202
- **at_the_market** ×2：…he Company did not utilize the ELOC. During the three months ended June 30, 2025, the Company did not utilize the ELOC. During the six months ended June 30, 2025, the Company sold 44,793 shares of Common Stock under the facility for cash proceeds of $4,657. At the Market Sales Agreements On March 13, 2026, the Company entered into an at market issuance sales agreement (the “2026 Sales Agreement”) with Roth Capital P

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 MSAI 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `MSAI`：sec_stale_series_dropped:total_debt:last_end_2024-06-30_vs_newest_2026-06-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
