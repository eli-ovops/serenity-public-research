# 研究包：IRTC（iRhythm Holdings, Inc.）

> 数据抓取 2026-11-06T04:34:29Z · 连接器 v9.1.0 · 用时 3.5 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `IRTC` | 130.19 USD | 4.38B | -32.4% | -26.1% | 854.04M | +14.9% | -1.1% | 74.2% (2026-09-30) | +3.1pp | 5.1x | +4.3% | unregistered_equity_sale_8k_3_02, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, supply_concentration |

## 2. 主体要点

- 最新季度收入：221.59M USD（期末 2026-09-30）；营业利润率 -14.7%；现金+短投 560.72M；FCF 跑道 — 季。
- 计算市值：4.38B USD（130.19 × 33,618,146 股，股本截至 2026-10-29）。
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 11（主文档 6/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3841 (Surgical & Medical Instruments & Apparatus)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 1 · ✅ 8 · ℹ️ 5 · — 1

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 14.88% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 74.23% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 3.14pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | -4.52% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -21.79% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | -1.44x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 7381000 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 9.62% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 83.77% | 👀 | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 0.49% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | -8.36pp | ✅ | 应收账款同比（2025-09-30→2026-09-30）− 收入同比 |
| W2 存货增速 − 收入增速 | 3.85pp | ℹ️ | 存货同比（2025-09-30→2026-09-30）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| W3 合同负债/预收同比 | 10.51% | ℹ️ | 期末合同负债 / 去年同期 − 1；合同负债不足 TTM 收入的 1%，基数小，百分比只作参考 |
| D1 股本变化（约一年） | 4.34% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 5.12x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 43.77亿 USD · P/B 24.7x · P/S 5.1x · P/FCF 593.0x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-19，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1388658/000138865826000011/irtc-20251231.htm

- **customer_deposits** ×3：…1, 2025 2024 2023 Balance, beginning of year $ 50,961 $ 52,689 $ 41,389 Add: provision for contractual adjustments 68,831 50,880 52,523 Less: contractual adjustments (70,866) (52,608) (41,223) Balance, end of year $ 48,926 $ 50,961 $ 52,689 99 Contract Liabilities ASC 606, Revenue from Contracts with Customers, requires an entity to present a revenue contract as a contract liability when the Company has an obligatio
- **long_term_supply_agreement** ×1：…incorporation into our devices or recall of finished products; •delays in device shipments resulting from quality issues or defects, reliability issues, or a supplier’s failure to consistently produce quality components; •price fluctuations due to a lack of long-term supply arrangements with our suppliers for key components; •inability to control the quality of products manufactured by third parties; •delays in deli
- **sole_source** ×6：…easures relating to the release, use, storage, treatment, transportation, discharge, disposal, sale, labeling, collection, recycling, treatment, and remediation of hazardous substances. We purchase certain components and materials used in manufacturing from single sources due to quality considerations, costs, or constraints resulting from regulatory or other requirements. As of December 31, 2025, those single source
- **material_weakness** ×1：…e costly to resolve and distract management’s attention, limit our ability to access the capital markets, or cause our stock to be delisted from The Nasdaq Global Select Market or any other securities exchange on which it is then listed. Failure to remedy any material weakness in our internal control over financial reporting, or to implement or maintain other effective control systems required of public companies, c
- **default_covenant** ×2：…n a default on our debt obligations. In addition, any of our future current or future debt agreements may contain restrictive covenants that may prohibit us from adopting any of these alternatives. Our failure to comply with these covenants could result in an event of default which, if not cured or waived, could result in the acceleration of our debt. In addition, we may be unable to repurchase the 2029 Notes upon a

### 10-Q（提交 2026-11-05，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1388658/000138865826000094/irtc-20260930.htm

- **customer_deposits** ×3：…d September 30, 2025 Balance, beginning of period $ 48,926 $ 50,961 $ 50,961 Add: Provision for contractual adjustments 57,679 68,831 55,318 Less: Contractual adjustments (55,616) (70,866) (49,405) Balance, end of period $ 50,989 $ 48,926 $ 56,874 Contract Liabilities ASC 606, Revenue from Contracts with Customers, requires an entity to present a revenue contract as a contract liability when the Company has an oblig
- **long_term_supply_agreement** ×1：…incorporation into our devices or recall of finished products; •delays in device shipments resulting from quality issues or defects, reliability issues, or a supplier’s failure to consistently produce quality components; •price fluctuations due to a lack of long-term supply arrangements with our suppliers for key components; •inability to control the quality of products manufactured by third parties; •delays in deli
- **sole_source** ×4：…able, net: Payor Type September 30, 2026 December 31, 2025 CMS Centers for Medicare & Medicaid Services 20 % 14 % Customer A Healthcare institutions 19 % 15 % Customer B Contracted third-party payors <10% 12 % Supply Risk The Company relies on single-source vendors to supply some of its disposable housings, instruments and other materials used to manufacture the Zio patches and the adhesive that binds the Zio patch 
- **material_weakness** ×1：…e costly to resolve and distract management’s attention, limit our ability to access the capital markets, or cause our stock to be delisted from The Nasdaq Global Select Market or any other securities exchange on which it is then listed. Failure to remedy any material weakness in our internal control over financial reporting, or to implement or maintain other effective control systems required of public companies, c
- **default_covenant** ×5：…he Credit Agreement. If we violate these or any other covenants under the Credit Agreement, fail to make payments in connection therewith, or experience certain other events, including a default under our other material indebtedness or a change of control, an event of default could occur, which would give the lenders the right to terminate their commitments to provide additional loans and declare all borrowings outs

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 IRTC 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `IRTC`：sec_stale_series_dropped:rnd:last_end_2024-06-30_vs_newest_2026-09-30
- `IRTC`：sec_stale_series_dropped:total_debt:last_end_2023-12-31_vs_newest_2026-09-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
