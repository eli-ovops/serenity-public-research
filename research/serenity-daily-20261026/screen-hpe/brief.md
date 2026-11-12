# 研究包：HPE（Hewlett Packard Enterprise Company）

> 数据抓取 2026-10-26T15:13:42Z · 连接器 v9.1.0 · 用时 7.73 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `HPE` | 58.63 USD | 77.83B | -20.3% | +140.1% | 41.87B | +33.7% | +14.4% | — | — | 1.9x | +0.6% | material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, going_concern, supply_concentration |

## 2. 主体要点

- 最新季度收入：12.21B USD（期末 2026-07-31）；营业利润率 11.4%；现金+短投 6.22B；FCF 跑道 — 季。
- 计算市值：77.83B USD（58.63 × 1,327,464,779 股，股本截至 2026-08-27）。
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 5（主文档 3/5）；capacity_signal 30（主文档 0/6）；going_concern 4（主文档 2/4）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3570 (Computer & office Equipment)）
- 数据：sec_companyfacts，报告期 2026-07-31，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 1 · ✅ 9 · ℹ️ 3 · — 1

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 33.68% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 123.64% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | — | ℹ️ | 毛利 / 收入（最新期） |
| P2 净利率（TTM） | 6.67% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 10.53% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 2.40x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C3 股权激励费用 / 收入（TTM） | 1.90% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | — | — | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 90.17% | 🚩 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | -111.27亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | -24.33pp | ✅ | 应收账款同比（2025-07-31→2026-07-31）− 收入同比 |
| W2 存货增速 − 收入增速 | 31.38pp | 👀 | 存货同比（2025-07-31→2026-07-31）− 收入同比 |
| W3 合同负债/预收同比 | 4.71% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 0.61% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 1.86x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 778.29亿 USD · P/E(TTM) 27.9x · P/B 2.9x · P/S 1.9x · 股息率 0.95% · 回购收益率 0.70%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] B2 商誉 / 归母权益：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2025-12-18，期末 2025-10-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1645590/000164559025000130/hpe-20251031.htm

- **remaining_performance_obligations** ×3：…Balance at end of year(1) $ 284 $ 301 $ 318 (1)The Company included the current portion in Other accrued liabilities, and amounts due after one year in Other non-current liabilities in the accompanying Consolidated Balance Sheets. Contract Liabilities and Remaining Performance Obligations Contract liabilities consist of deferred revenue and customer deposits. A summary of contract liabilities were as follows: As of 
- **customer_deposits** ×18：…rvices contracts where a service has been performed and control has transferred, but invoicing to the customer is subject to future milestone billings or other contractual payment schedules. The Company classifies unbilled receivables as Accounts receivable. Contract liabilities A contract liability is an obligation to transfer products or services to a customer for which the Company has received consideration, or t
- **sole_source** ×17：…stomers. We purchase materials, supplies, and product subassemblies from a substantial number of vendors. For most of our products, we have existing alternate sources of supply or such alternate sources of supply are readily available. However, we do rely on single-source suppliers for certain customized parts (although some of these sources have operations in multiple locations in the event of a disruption) and a d
- **customer_concentration** ×2：…the financial condition of its customers and may require collateral, such as letters of credit and bank guarantees, in certain circumstances. As of October 31, 2025, one distributor accounted for 10% of the Company's accounts receivable balance and no single customer accounted for more than 10% of the Company’s financing receivables. As of October 31, 2024, no single customer accounted for more than 10% of the Compa
- **export_controls** ×6：…an approach to ethical standards and strong governance that are the foundations of our business. Global Trade As a global company, the import and export of our products and services are subject to laws and regulations including international treaties, U.S. export controls and sanctions laws, customs regulations, and local trade rules around the world. Such laws, rules, and regulations may delay the introduction of s

### 10-Q（提交 2026-09-03，期末 2026-07-31）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1645590/000164559026000080/hpe-20260731.htm

- **remaining_performance_obligations** ×3：…borrowings in its Condensed Consolidated Balance Sheets as of July 31, 2026 and October 31, 2025, respectively, related to the trade receivables sold and collected from the third-party for which the revenue recognition was deferred. Contract Liabilities and Remaining Performance Obligations Contract liabilities consist of deferred revenue and customer deposits. A summary of contract liabilities were as follows: 22 T
- **customer_deposits** ×12：…development — — 7 31 Selling, general and administrative 15 — 41 147 Acquisition, disposition and other charges 9 15 46 15 Total severance charges $ 38 $ 15 $ 120 $ 256 Contract Balances The Company’s contract balances consist of contract assets, contract liabilities, and costs to obtain a contract with a customer. Contract Assets A summary of accounts receivable, net, including unbilled receivables was as follows: 

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 HPE 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `HPE`：sec_stale_series_dropped:cost_of_revenue:last_end_2020-10-31_vs_newest_2026-07-31
- `HPE`：sec_stale_series_dropped:total_liabilities:last_end_2018-11-01_vs_newest_2026-07-31

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
