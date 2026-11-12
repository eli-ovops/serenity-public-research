# 研究包：NOVT（Novanta Inc.）

> 数据抓取 2026-11-06T04:39:40Z · 连接器 v9.1.0 · 用时 4.05 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `NOVT` | 131.82 USD | 4.99B | -25.3% | +26.8% | 1.03B | +10.3% | +3.1% | 45.5% (2026-07-03) | +1.2pp | 4.8x | +5.1% | shelf_registration_on_file, repeated_prospectus_takedowns, unregistered_equity_sale_8k_3_02, material_agreement_8k_1_01, beneficial_owner_filings |

## 2. 主体要点

- 最新季度收入：265.81M USD（期末 2026-07-03）；营业利润率 6.8%；现金+短投 718.65M；FCF 跑道 — 季。
- 计算市值：4.99B USD（131.82 × 37,817,770 股，股本截至 2026-07-29）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 5（主文档 3/5）；customer_concentration 1（主文档 0/1）；atm_program 2（主文档 0/2）；capacity_signal 21（主文档 2/6）；going_concern 5（主文档 0/5）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3690 (Miscellaneous Electrical Machinery, Equipment & Supplies)）
- 数据：sec_companyfacts，报告期 2026-07-03，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 3 · ✅ 11 · ℹ️ 3 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 10.27% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 0.66% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 45.49% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 1.21pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 6.00% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 3.82% | 👀 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 2.17x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 1.14亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 3.36% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 24.45% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 39.74% | 👀 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 5.30亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | 0.61pp | ✅ | 应收账款同比（2025-06-27→2026-07-03）− 收入同比 |
| W2 存货增速 − 收入增速 | 4.39pp | ✅ | 存货同比（2025-06-27→2026-07-03）− 收入同比 |
| W3 合同负债/预收同比 | 327.41% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 5.13% | 👀 | 最新股本 / 4 个观测点前 − 1；每股收入同比 +4.9%；核实融资方式：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 4.84x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 49.85亿 USD · P/E(TTM) 80.7x · P/B 3.1x · P/S 4.8x · P/FCF 43.6x · 回购收益率 1.04%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-23，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1076930/000119312526064230/novt-20251231.htm

- **remaining_performance_obligations** ×1：…ount of consideration for the effects of a financing component because the time period between the transfer of a promised good to a customer and the customer’s payment for that good is typically one year or less. The Company does not disclose the value of the remaining performance obligation for contracts with an original expected length of one year or less. Contract Liabilities Contract liabilities consist of defer
- **customer_deposits** ×7：…nsfer of a promised good to a customer and the customer’s payment for that good is typically one year or less. The Company does not disclose the value of the remaining performance obligation for contracts with an original expected length of one year or less. Contract Liabilities Contract liabilities consist of deferred revenue and advance payments from customers, including amounts that are refundable. These contract
- **sole_source** ×7：…rts and components used in our products in case of supply chain shortages. For certain raw materials, components and parts used in the production of some of our principal products, we have identified only a limited number of suppliers or, in some instances, a single source of supply. We also rely on a limited number of suppliers to manufacture subassemblies for some of our products. For a further discussion of the i
- **customer_concentration** ×3：…customers, each operating primarily in the medical end market across multiple product lines, represented approximately 12% and 11%, respectively, of our consolidated revenue. During the years ended December 31, 2024, and December 31, 2023, revenue from an OEM customer primarily in the medical end market accounted for approximately 10% of our consolidated revenue. Our customers include many OEMs who integrate our pro
- **material_weakness** ×1：…such action or other negative results caused by our inability to meet our internal control and financial reporting requirements or to comply with legal and regulatory requirements could adversely affect our business and the trading price of our common shares. Material weaknesses in our internal control over financial reporting could also reduce our ability to obtain financing or could increase the cost of any financ
- **export_controls** ×1：…sely affected. Products we sell into certain other foreign markets could also become subject to retaliatory tariffs, making our products uncompetitive to similar products not subjected to such import tariffs. Further changes in trade policies, tariffs, taxes, export restrictions or other trade barriers, or restrictions on raw materials or components may limit our ability to produce products, increase our manufacturi
- **default_covenant** ×1：…lable to repay our debt. Our Fourth Amended and Restated Credit Agreement, as amended, contains covenants that limit our ability to engage in activities that may be in our long-term best interest. Our failure to comply with those covenants could result in an event of default which, if not cured or waived, could result in the acceleration of all of our borrowings thereunder. General Risk Factors The market price for 

### 10-Q（提交 2026-08-05，期末 2026-07-03）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1076930/000119312526335404/novt-20260703.htm

- **remaining_performance_obligations** ×1：…adjust the promised amount of consideration for the effects of a financing component because the transfer of a promised good to a customer and the customer’s payment for that good are typically one year or less. The Company does not disclose the value of the remaining performance obligation for contracts with an original expected length of one year or less. Contract Liabilities Contract liabilities consist of deferr
- **customer_deposits** ×8：…sfer of a promised good to a customer and the customer’s payment for that good are typically one year or less. The Company does not disclose the value of the remaining performance obligation for contracts with an original expected length of one year or less. Contract Liabilities Contract liabilities consist of deferred revenue and advance payments from customers, including amounts that are refundable. These contract
- **sole_source** ×5：…our indemnity or insurance is inadequate. Any such liabilities may have a material adverse effect on our financial position or results of operations. Disruptions in the supply of certain key components and other goods from our suppliers, including limited or single source suppliers, have adversely affected the results of our business operations, and could damage our relationships with customers. The production of ou
- **export_controls** ×1：…we have sought but have been unable to obtain the licenses necessary to receive certain shipments of these materials, which has caused delays in fulfilling customer orders and increases in certain manufacturing costs. If we are unable to obtain the necessary export licenses on a timely basis or at all, or if similar restrictions are imposed on other raw materials or components, our ability to fulfill customer orders
- **default_covenant** ×1：…lable to repay our debt. Our Fourth Amended and Restated Credit Agreement, as amended, contains covenants that limit our ability to engage in activities that may be in our long-term best interest. Our failure to comply with those covenants could result in an event of default which, if not cured or waived, could result in the acceleration of all of our borrowings thereunder. Item 2. Unregistered Sales of Equity Secur

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 NOVT 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
