# 研究包：TER（Teradyne, Inc.）

> 数据抓取 2026-10-28T13:41:43Z · 连接器 v9.1.0 · 用时 3.39 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `TER` | 300.905 USD | 47.04B | -38.3% | +65.5% | 4.46B | +103.9% | +3.6% | 59.8% (2026-06-28) | +2.6pp | 10.5x | -1.7% | acceleration, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, going_concern_exhibit_only |

## 2. 主体要点

- 最新季度收入：1.33B USD（期末 2026-06-28）；营业利润率 32.9%；现金+短投 349.54M；FCF 跑道 — 季。
- 计算市值：47.04B USD（300.905 × 156,340,750 股，股本截至 2026-07-27）。
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 3（主文档 2/3）；customer_concentration 2（主文档 0/2）；capacity_signal 12（主文档 4/6）；going_concern 1（主文档 0/1）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3825 (Instruments For Meas & Testing of  Electricity & Elec Signals)）
- 数据：sec_companyfacts，报告期 2026-06-28，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 0 · ✅ 11 · ℹ️ 2 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 103.90% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 145.16% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 59.79% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 2.56pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 25.77% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 33.46% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 0.93x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 8.00亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 1.66% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 29.48% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 19.31% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 52.38pp | 🚩 | 应收账款同比（2025-06-29→2026-06-28）− 收入同比 |
| W2 存货增速 − 收入增速 | -88.84pp | ✅ | 存货同比（2025-06-29→2026-06-28）− 收入同比 |
| D1 股本变化（约一年） | -1.72% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |

**估值（USD 口径）**

- 市值 470.44亿 USD · P/E(TTM) 40.9x · P/B 13.7x · P/S 10.5x · P/FCF 58.8x · 股息率 0.17% · 回购收益率 1.07%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] W1 应收增速 − 收入增速：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-19，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/97210/000119312526059002/ter-20251231.htm

- **customer_deposits** ×10：…s, net 51,271 15,927 Goodwill 521,019 395,367 Total assets $ 4,183,599 $ 3,708,714 LIABILITIES Current liabilities: Accounts payable $ 269,185 $ 134,792 Accrued employees’ compensation and withholdings 254,973 204,991 Deferred revenue and customer advances 153,124 107,710 Other accrued liabilities 111,845 90,777 Operating lease liabilities 19,340 18,699 Short-term debt 200,000 — Income taxes payable 106,740 67,610 T
- **sole_source** ×2：…se delays have impacted and may continue to impact the manufacturing of certain products and the timing of delivery of those products to our customers. While the majority of our components are available from multiple suppliers, certain items are obtained from sole sources. We may experience a temporary adverse impact if any of our sole source suppliers delay or cease to deliver products. Intellectual Property and Li
- **customer_concentration** ×10：…to support of high volume manufacturing test, the Product Test solutions aid customers in the development, verification, and scaling of next-generation technologies. Sales and Distribution In each of the years, 2025, 2024 and 2023, our five largest direct customers in aggregate accounted for 44%, 36%, and 32% of our consolidated revenues, respectively. Teradyne typically has a specifying customer such as an OEM, IDM
- **export_controls** ×16：…are limiting our ability to be competitive, particularly in certain markets, where some competitors are not subjected to the same restrictions. We continue to monitor developments in international trade policy, including potential changes to tariffs, further export controls, and other regulatory measures that could affect our supply chain, cost structure, or market access. For information regarding risks associated 
- **default_covenant** ×1：…ertain thresholds, making investments, loans and other advances, and prepaying any additional indebtedness while our indebtedness under our Credit Facility is outstanding. Our failure to comply with financial and other restrictive covenants could result in an event of default, which if not cured or waived, could result in the lenders requiring immediate payment of all outstanding borrowings or foreclosing on collate

### 10-Q（提交 2026-07-31，期末 2026-06-28）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/97210/000119312526327715/ter-20260628.htm

- **customer_deposits** ×13：…, net 101,910 51,271 Goodwill 663,817 521,019 Total assets $ 4,925,617 $ 4,183,599 LIABILITIES Current liabilities: Accounts payable $ 383,422 $ 269,185 Accrued employees’ compensation and withholdings 220,690 254,973 Deferred revenue and customer advances 193,840 153,124 Other accrued liabilities 133,399 111,845 Operating lease liabilities 17,258 19,340 Short-term debt — 200,000 Income taxes payable 164,907 106,740
- **export_controls** ×2：…uybacks and $40.7 million of dividend payments. Government Regulations We are subject to numerous U.S. and foreign laws and regulations, including, without limitation, tariffs, trade sanctions, trade barriers, trade embargoes, regulations relating to import-export control, technology transfer restrictions, and other laws and regulations. However, our trade compliance program may not identify or prevent all potential

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-04-14 `2044094868079906990` REAFFIRM/bullish
  - 2026-07-21 `2079479755481776221` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `TER`：sec_stale_series_dropped:short_term_investments:last_end_2014-06-29_vs_newest_2026-06-28
- `TER`：sec_stale_series_dropped:total_debt:last_end_2014-12-31_vs_newest_2026-06-28

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
