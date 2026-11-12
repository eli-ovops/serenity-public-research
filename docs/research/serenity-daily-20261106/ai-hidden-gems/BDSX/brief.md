# 研究包：BDSX（Biodesix, Inc.）

> 数据抓取 2026-11-06T04:34:29Z · 连接器 v9.1.0 · 用时 4.02 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `BDSX` | 19.84 USD | 220.00M | -37.9% | +163.1% | 105.21M | +10.4% | -10.5% | — | — | 2.1x | +39.4% | dilution, shelf_registration_on_file, beneficial_owner_filings, insider_form4_activity, customer_concentration |

## 2. 主体要点

- 最新季度收入：24.04M USD（期末 2026-09-30）；营业利润率 -25.4%；现金+短投 28.41M；FCF 跑道 6.0 季。
- 计算市值：220.00M USD（19.84 × 11,088,511 股，股本截至 2026-10-30）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 17（主文档 4/6）；customer_concentration 2（主文档 1/2）；atm_program 27（主文档 3/6）；capacity_signal 6（主文档 2/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 8071 (Services-Medical Laboratories)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 4 · 👀 2 · ✅ 4 · ℹ️ 5 · — 2

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 10.44% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | — | ℹ️ | 毛利 / 收入（最新期） |
| P2 净利率（TTM） | -25.74% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -312.14% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 0.67x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -19074000 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 3.67% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 90.77% | 🚩 | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 173.27% | 🚩 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | -21,591,000.00 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | -38.51pp | ✅ | 应收账款同比（2025-09-30→2026-09-30）− 收入同比 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（2025-09-30→2026-09-30）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| W3 合同负债/预收同比 | -87.02% | ℹ️ | 期末合同负债 / 去年同期 − 1；合同负债不足 TTM 收入的 1%，基数小，百分比只作参考 |
| D1 股本变化（约一年） | 39.38% | 🚩 | 最新股本 / 4 个观测点前 − 1；每股收入同比 -20.8%；核实融资方式：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| R1 现金跑道（月） | 17.90 月 | 👀 | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 2.09x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 2.20亿 USD · P/B 25.4x · P/S 2.1x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素
- [ ] B1 资产负债率：到定期报告原文核对口径与一次性因素
- [ ] B2 商誉 / 归母权益：到定期报告原文核对口径与一次性因素
- [ ] D1 股本变化（约一年）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-26，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1439725/000119312526076547/bdsx-20251231.htm

- **sole_source** ×14：…icant fluctuation in our operating results, causing our operating results to fall below expectations or any guidance we provide; • product performance and reliability to maintain and grow our business; • third-party suppliers, including courier services and single source suppliers; making us vulnerable to supply problems and price fluctuations; • the impact of a pandemic, epidemic, or outbreak of an infectious disea
- **customer_concentration** ×1：…Company received $3.0 million as a non-refundable, up-front payment during the three months ended December 31, 2025. As of December 31, 2025, approximately $0.7 million remains in ‘Deferred revenue’ in the balance sheet. We collect reimbursement on behalf of customers covered by Medicare, which accounted for 32% and 39% of the Company’s total revenue for the years ended December 31, 2025 and 2024, respectively. No o
- **material_weakness** ×2：…ed persons to serve on our Board of Directors or as executive officers. Accordingly, increases in costs incurred as a result of being a publicly traded company may adversely affect our business, financial condition and results of operations. If we experience material weaknesses in the future or otherwise fail to maintain an effective system of internal controls in the future, we may not be able to accurately report 
- **export_controls** ×2：…ing groups and integrated delivery networks having a material adverse effect on our sales and profitability; • potential effects of litigation and other proceedings; • general economic and financial market conditions, including enhanced U.S. tariffs, import/export restrictions or other trade barriers, which may have a negative effect on global economic conditions, financial markets and our business; • our ability to
- **at_the_market** ×4：…s proceeds of any shares sold and has agreed to provide the sales agents with customary indemnification, contribution and reimbursement rights. Sales of common stock under the 2024 ATM Program, if any, will be made at market prices by methods deemed to be an “at-the-market offering” as defined in Rule 415 promulgated under the Securities Act of 1933, as amended, including sales made directly on the Nasdaq Global Mar
- **default_covenant** ×3：…tains customary affirmative and negative covenants for a loan, requires us to comply with a minimum cash requirement covenant, and has a trailing twelve month net revenue requirement. Failure to comply with the covenants and loan requirements may result in an event of default. The Perceptive Term Loan Facility also contains certain covenants limiting our ability to, among other things, engage in certain corporate ch

### 10-Q（提交 2026-11-05，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1439725/000119312526449763/bdsx-20260930.htm

- **sole_source** ×3：…icant fluctuation in our operating results, causing our operating results to fall below expectations or any guidance we provide; • product performance and reliability to maintain and grow our business; • third-party suppliers, including courier services and single source suppliers, which make us vulnerable to supply problems and price fluctuations; • the impact of a pandemic, epidemic, or outbreak of an infectious d
- **customer_concentration** ×1：…were as follows: Three Months Ended September 30, Nine Months Ended September 30, 2026 2025 2026 2025 United Healthcare 11 % 11 % 10 % 8 % Humana 10 % 8 % 10 % 6 % In addition to the above table, we collect reimbursement on behalf of customers covered by Medicare, which accounted for 35% and 34% of the Company’s total revenue for the three and nine months ended September 30, 2026 compared to 30% and 34% for the thre
- **export_controls** ×1：…ing groups and integrated delivery networks having a material adverse effect on our sales and profitability; • potential effects of litigation and other proceedings; • general economic and financial market conditions, including enhanced U.S. tariffs, import/export restrictions or other trade barriers, which may have a negative effect on global economic conditions, financial markets and our business; • our ability to
- **at_the_market** ×4：…026 Remainder of 2026 $ 1,071 2027 5,180 2028 4,463 2029 4,484 2030 4,453 2031 and thereafter 19,534 Total future minimum lease payments 39,185 Less amount representing interest (13,891 ) Total lease liabilities $ 25,294 Note 8 – Equity At-The-Market Program The Company maintains an at-the-market (ATM) facility that enables equity financing on an ongoing basis at the Company’s discretion. On November 1, 2024, the Co
- **default_covenant** ×1：…lts to material contracts, certain regulatory-related events and events constituting a change of control. As of September 30, 2026, the Company was in compliance with all restrictive and financial covenants associated with its borrowings. The occurrence of an Event of Default could result in, among other things, the declaration that all outstanding principal and interest under the Perceptive Term Loan Facility are i

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 BDSX 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
