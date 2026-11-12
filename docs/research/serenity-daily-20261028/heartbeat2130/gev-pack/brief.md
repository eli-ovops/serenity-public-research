# 研究包：GEV（GE Vernova Inc.）

> 数据抓取 2026-10-28T13:41:37Z · 连接器 v9.1.0 · 用时 3.09 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `GEV` | 843.48 USD | 223.25B | -29.5% | +44.1% | 44.04B | +26.8% | +13.8% | 24.6% (2026-09-30) | +5.5pp | 5.1x | -2.5% | pricing_power, shelf_registration_on_file, repeated_prospectus_takedowns, beneficial_owner_filings, insider_form4_activity |

## 2. 主体要点

- 最新季度收入：12.64B USD（期末 2026-09-30）；营业利润率 11.0%；现金+短投 16.76B；FCF 跑道 — 季。
- 计算市值：223.25B USD（843.48 × 264,677,066 股，股本截至 2026-09-30）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 3（主文档 1/3）；atm_program 7（主文档 2/6）；capacity_signal 44（主文档 2/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3600 (Electronic & Other Electrical Equipment (No Computer Equip))）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 2 · 👀 1 · ✅ 9 · ℹ️ 2 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 26.81% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 508.45% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 24.58% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 5.55pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 23.54% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 91.09% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 1.85x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | 85.46% | 🚩 | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 84.42% | 🚩 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 30.32pp | 👀 | 应收账款同比（2025-09-30→2026-09-30）− 收入同比 |
| W2 存货增速 − 收入增速 | 3.22pp | ✅ | 存货同比（2025-09-30→2026-09-30）− 收入同比 |
| W3 合同负债/预收同比 | 126.63% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | -2.45% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 5.07x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 2,232.50亿 USD · P/E(TTM) 21.5x · P/B 19.6x · P/S 5.1x · 股息率 0.21% · 回购收益率 2.85%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] B1 资产负债率：到定期报告原文核对口径与一次性因素
- [ ] B2 商誉 / 归母权益：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-01-29，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/gev-20251231.htm

- **remaining_performance_obligations** ×4：…al source of reliable and dispatchable power to support industrialization, grid stability needs, and rising electricity demand from hyperscalers and data centers. As of December 31, 2025, our fundamentals remained strong with approximately $94.4 billion in remaining performance obligations (RPO) and a gas turbine installed base of approximately 7,000 units with approximately 1,800 units under long-term service agree
- **customer_deposits** ×18：…ent and Long-Term Receivables 49 Note 5 Inventories, Including Deferred Inventory Costs 49 Note 6 Property, Plant, and Equipment 50 Note 7 Leases 50 Note 8 Goodwill and Other Intangible Assets 51 Note 9 Contract and Other Deferred Assets & Contract Liabilities and Deferred Income 51 Note 10 Current and All Other Assets 52 Note 11 Equity Method Investments 53 Note 12 Accounts Payable and Equipment Project Payables 54
- **long_term_supply_agreement** ×1：…shortages of materials and skilled labor, inflationary pressures, transportation and logistics challenges, and manufacturing disruptions that affect revenues, profitability, cash flow, and on-time fulfillment. While we pursue mitigation measures, such as long-term supply agreements, dual-sourcing, increased inventory levels, factory capacity expansion, lean initiatives, alternative logistics, product or component re
- **sole_source** ×1：…lternative logistics, product or component redesign, and cost-sharing with customers and suppliers, supply chain pressures are expected to persist and may continue to adversely affect our operations and financial performance. Certain inputs are limited or sole-sourced, concentrated with a small number of suppliers, or primarily available from a single country, including semiconductor chips and critical materials (su
- **export_controls** ×4：…act each of these capacities. 2025 FORM 10-K 9 •Manufacturer and Servicer. Our production cycle and products are subject to global regulations, such as permitting, quality controls, environmental and eco-design regulations, health and safety regulations, export control laws, product specifications, market-related policies, and distribution regulations in countries in which our products are manufactured or sold. We m

### 10-Q（提交 2026-10-28，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1996810/000199681026000163/gev-20260930.htm

- **remaining_performance_obligations** ×1：…ent liabilities 14,550 6,449 2,796 23,798 Contract liabilities and current deferred income $16,527 $6,449 $2,796 $25,774 Non-current deferred income 20 13 142 175 Total contract liabilities and deferred income $16,547 $6,462 $2,938 $25,950 Remaining Performance Obligation (RPO). As of September 30, 2026, the aggregate amount of the contracted revenues allocated to our unsatisfied (or partially unsatisfied) performan
- **customer_deposits** ×15：…rm Receivables 12 Note 5 Inventories, Including Deferred Inventory Costs 12 Note 6 Property, Plant, and Equipment 12 Note 7 Leases 13 Note 8 Acquisitions, Goodwill, and Other Intangible Assets 13 Note 9 Contract and Other Deferred Assets & Contract Liabilities and Deferred Income 14 Note 10 Current and All Other Assets 15 Note 11 Equity Method Investments 15 Note 12 Accounts Payable and Equipment Project Payables 15

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 GEV 本身的表态（覆盖至 2026-10-19）。另有 1 条只是和其他公司一起被列出，不算表态。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `GEV`：sec_stale_series_dropped:sbc:last_end_2024-12-31_vs_newest_2026-09-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
