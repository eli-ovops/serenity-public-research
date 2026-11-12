# 研究包：STXS（Stereotaxis, Inc.）

> 数据抓取 2026-11-06T04:34:29Z · 连接器 v9.1.0 · 用时 3.51 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `STXS` | 1.05 USD | 105.21M | -63.7% | -62.4% | 30.07M | -12.8% | +21.9% | 58.5% (2026-06-30) | +6.4pp | 3.5x | +10.5% | pricing_power, acceleration, dilution, shelf_registration_on_file, repeated_prospectus_takedowns |

## 2. 主体要点

- 最新季度收入：7.67M USD（期末 2026-06-30）；营业利润率 -59.6%；现金+短投 10.49M；FCF 跑道 2.7 季。
- 计算市值：105.21M USD（1.05 × 100,202,178 股，股本截至 2026-07-31）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 5（主文档 5/5）；atm_program 17（主文档 6/6）；capacity_signal 16（主文档 3/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3845 (Electromedical & Electrotherapeutic Apparatus)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**亏损且不增长**（TTM 亏损且收入增速 < 10%）；该阶段看：现金跑道、融资方式与稀释、收入能否恢复增长
- 结果：🚩 5 · 👀 2 · ✅ 4 · ℹ️ 3 · — 1

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | -12.82% | 🚩 | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 58.49% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 6.44pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | -74.24% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -182.33% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 0.68x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C3 股权激励费用 / 收入（TTM） | 28.83% | 🚩 | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 68.56% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 30.74% | 👀 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 84.66pp | 🚩 | 应收账款同比（2025-06-30→2026-06-30）− 收入同比 |
| W2 存货增速 − 收入增速 | 43.13pp | 👀 | 存货同比（2025-06-30→2026-06-30）− 收入同比 |
| W3 合同负债/预收同比 | 1.45% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 10.53% | 🚩 | 最新股本 / 4 个观测点前 − 1；每股收入同比 -21.1%；核实融资方式：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 3.50x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 1.05亿 USD · P/B 8.6x · P/S 3.5x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] G1 收入同比：到定期报告原文核对口径与一次性因素
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素
- [ ] C3 股权激励费用 / 收入（TTM）：到定期报告原文核对口径与一次性因素
- [ ] W1 应收增速 − 收入增速：到定期报告原文核对口径与一次性因素
- [ ] D1 股本变化（约一年）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-03-12，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1289340/000149315226009881/form10-k.htm

- **remaining_performance_obligations** ×2：…4 (in thousands): Schedule of Revenue Disaggregated by Type Year Ended December 31, 2025 2024 Systems $ 10,223 $ 8,632 Disposables, service and accessories 22,154 18,286 Total revenue $ 32,377 $ 26,918 Transaction price allocated to remaining performance obligations relates to amounts allocated to products and services for which the revenue has not yet been recognized. A significant portion of this amount relates to
- **customer_deposits** ×3：…nce between the revenue that was earned but not billed on service contracts and revenue from system contracts that was recognized based on the relative selling price of the related performance obligations and the contractual billing terms in the arrangements. Customer deposits primarily relate to future system sales but can also include deposits on disposable sales. Deferred revenue is primarily related to service c
- **long_term_supply_agreement** ×1：…by sole-sourced suppliers (the only recognized supply source available to us) or single-sourced suppliers (the only approved supply source for us among other sources). We purchase most of our components and major assemblies through purchase orders rather than long-term supply agreements and generally do not maintain large volumes of finished goods. Disposable Interventional Devices Our historical manufacturing strat
- **sole_source** ×6：…mbly and inspection in-house. We purchase both custom and off-the-shelf components from many suppliers and subject them to quality specifications and processes. Some of the components necessary for the assembly of our products are currently provided to us by sole-sourced suppliers (the only recognized supply source available to us) or single-sourced suppliers (the only approved supply source for us among other sourc
- **customer_concentration** ×2：…in the process of obtaining necessary approvals in other geographies. We are also currently seeking regulatory clearances for the EMAGIN 5F catheter guide designed to robotically navigate tortuous venous and arterial vasculature. FINANCIAL INFORMATION ABOUT CUSTOMERS No single customer accounted for more than 10% of total revenue for the years ended December 31, 2025 and 2024. No single country, other than the U.S.,
- **export_controls** ×2：…nufacturer in China. Given the complex relationships between China and the U.S., political, diplomatic, military, or other events could result in business disruptions, including increased regulatory enforcement against companies, tariffs, trade embargoes, and export restrictions relating to this production work. For example, in 2020, the U.S. government amended the Entity List rules to expand the requirement to obta
- **at_the_market** ×2：…ions 26,376 55 - 55 Stock-based compensation 242,861 9,852 - 9,852 Issuance of common stock through the direct offering and regulatory milestone achievement 7,669,523 8 15,987 - 15,995 Issuance of common stock through at-the-market offering 963,723 1 2,901 - 2,902 Components of net loss - (21,643 ) (21,643 ) Employee stock purchase plan 61,078 128 - 128 Preferred stock conversion (450 ) (112 ) 1,049,510 1 111 - 112 
- **default_covenant** ×2：…rcial paper, non-U.S. government agency securities, and municipal notes. The Company’s exposure to any individual corporate entity is limited by policy. Deposits may exceed federally insured limits, and the Company is exposed to credit risk on deposits in the event of default by the financial institutions to the extent account balances exceed the amount insured by the Federal Deposit Insurance Corporation (FDIC). Th

### 10-Q（提交 2026-08-12，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1289340/000149315226037357/form10-q.htm

- **remaining_performance_obligations** ×2：…nded June 30, 2026 2025 2026 2025 Systems $ 1,479 $ 3,038 $ 2,798 $ 5,002 Disposables, service and accessories 6,191 5,760 11,163 11,268 Total revenue $ 7,670 $ 8,798 $ 13,961 $ 16,270 13 Transaction price allocated to remaining performance obligations relates to amounts allocated to products and services for which the revenue has not yet been recognized. A significant portion of this amount relates to the Company’s
- **customer_deposits** ×3：…ble summarizes the Company’s contract assets and liabilities (in thousands): Summary of Contract Assets and Liabilities June 30, 2026 December 31, 2025 Contract Assets - unbilled receivables $ 783 $ 276 Total unbilled receivables $ 783 $ 276 Customer deposits $ 994 $ 1,070 Product shipped, revenue deferred 594 993 Deferred service and license fees 4,724 4,167 Total deferred revenue $ 6,312 $ 6,230 Less: Long-term de
- **at_the_market** ×8：…t March 31, 2026 21,008 $ 5,240 97,491,248 $ 97 $ 603,696 $ (206 ) $ (589,229 ) $ 14,358 Stock issued for the exercise of stock options 4,079 7 7 Stock-based compensation 3,938 1,608 1,608 Issuance of common stock through at-the-market offering 356,271 1 687 688 Components of net loss (4,468 ) (4,468 ) Employee stock purchase plan 21,668 44 44 Preferred stock conversion (25 ) (6 ) 60,887 - 6 - - 6 Balance at June 30

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 STXS 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `STXS`：sec_stale_series_dropped:total_debt:last_end_2021-03-31_vs_newest_2026-06-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
