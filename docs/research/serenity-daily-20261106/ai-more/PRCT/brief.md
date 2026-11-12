# 研究包：PRCT（PROCEPT BioRobotics Corporation）

> 数据抓取 2026-11-06T04:39:40Z · 连接器 v9.1.0 · 用时 2.41 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `PRCT` | 20.27 USD | 1.17B | -46.8% | -34.5% | 352.30M | +18.0% | +4.0% | 66.3% (2026-09-30) | +1.5pp | 3.3x | +3.0% | material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, customer_concentration, supply_concentration |

## 2. 主体要点

- 最新季度收入：98.29M USD（期末 2026-09-30）；营业利润率 -27.9%；现金+短投 218.37M；FCF 跑道 10.3 季。
- 计算市值：1.17B USD（20.27 × 57,536,121 股，股本截至 2026-10-29）。
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 2（主文档 2/2）；customer_concentration 7（主文档 6/6）；capacity_signal 13（主文档 3/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3841 (Surgical & Medical Instruments & Apparatus)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 2 · ✅ 9 · ℹ️ 4 · — 2

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 17.96% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 66.28% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 1.47pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | -32.60% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -34.92% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 0.67x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -85074000 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 15.19% | 👀 | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 30.57% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 1.67亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | 6.33pp | ✅ | 应收账款同比（2025-09-30→2026-09-30）− 收入同比 |
| W2 存货增速 − 收入增速 | 4.07pp | ✅ | 存货同比（2025-09-30→2026-09-30）− 收入同比 |
| W3 合同负债/预收同比 | 46.61% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 2.97% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| R1 现金跑道（月） | 30.80 月 | ✅ | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 3.31x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 11.66亿 USD · P/B 3.5x · P/S 3.3x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-26，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1588978/000158897826000009/prct-20251231.htm

- **long_term_supply_agreement** ×1：…erations; •delays in product shipments resulting from uncorrected defects, reliability issues or a third party’s failure to produce components or complete sterilizations that consistently meet our quality specifications; •price fluctuations due to a lack of long-term supply arrangements with our third parties for key components or sterilization requirements; •inability to obtain adequate supply or services in a time
- **sole_source** ×9：…large-scale commercial quantities, and we face a number of manufacturing risks that may adversely affect our manufacturing abilities which could delay, prevent or impair our growth. •We depend upon third-party suppliers, including contract manufacturers and single source suppliers, making us vulnerable to supply shortages and price fluctuations that could negatively affect our business, financial condition and resul
- **customer_concentration** ×3：…l. These customers could also potentially pressure us to reduce the prices we charge for our disposables, which could have an adverse effect on our margins and financial position and could negatively affect our revenue and results of operations. If any of our largest customers terminates its relationship with us, such termination could negatively affect our revenues and results of operations. If product liability la
- **material_weakness** ×1：…ulated and communicated to management, and recorded, processed, summarized and reported within the time periods specified in the rules and forms of the SEC. If we are not able to maintain adequate internal control over financial reporting, or if we identify material weaknesses in future periods, we may not be able to produce timely or accurate financial statements, investors may lose confidence in our operating resu
- **export_controls** ×5：…y distributors in foreign markets, our ability to effectively screen, recruit and retain qualified third-party distributors and training them in our technology and product offering and business; •compliance with various U.S. and international laws, including export control laws and the U.S. Foreign Corrupt Practices Act of 1977, or the FCPA, and anti-money laundering laws; •differing regulatory requirements for obta
- **default_covenant** ×1：…an approved forecast or maintain a minimum amount of unrestricted cash. The loan and security agreement also contains customary events of default. If we fail to comply with such covenants, payments or other terms of the agreement, our lender could declare an event of default, which would give it the right to declare all borrowings outstanding, together with accrued and unpaid interest and fees, to be immediately due

### 10-Q（提交 2026-11-04，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1588978/000158897826000039/prct-20260930.htm

- **customer_concentration** ×2：…tems within net income (loss) include interest expense, and interest and other income, net on an aggregate basis for the purposes of allocating resources and evaluating financial performance. The Company’s assets are primarily based in the United States. No customers accounted for more than 10% of revenue during the three and nine months ended September 30, 2026 and 2025. No customer accounted for more than 10% of a

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 PRCT 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
