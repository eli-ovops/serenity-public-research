# 研究包：SOPH（SOPHiA GENETICS SA）

> 数据抓取 2026-11-06T04:34:29Z · 连接器 v9.1.0 · 用时 3.1 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SOPH` | 6.62 USD | — | -26.3% | +52.2% | 86.17M | +27.2% | +7.5% | 64.6% (2026-06-30) | -2.4pp | — | +7.2% | shelf_registration_on_file, repeated_prospectus_takedowns, beneficial_owner_filings, insider_form4_activity, customer_concentration |

## 2. 主体要点

- 最新季度收入：23.31M USD（期末 2026-06-30）；营业利润率 —；现金+短投 70.29M；FCF 跑道 — 季。
- ⚠️ 市值未计算：foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：customer_concentration 18（主文档 0/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 7374 (Services-Computer Processing & Data Preparation)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 2 · ✅ 2 · ℹ️ 3 · — 5

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 27.22% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 64.61% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | -2.36pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | — | — | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | — | — | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | — | — | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | 71.08% | 👀 | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 74.51pp | ℹ️ | 应收账款同比（2024-12-31→2025-12-31）− 收入同比；资产负债表期末 2025-12-31 与收入期末 2026-06-30 相差 181 天，口径不一致，只作参考 |
| W2 存货增速 − 收入增速 | -18.99pp | ℹ️ | 存货同比（2024-12-31→2025-12-31）− 收入同比；资产负债表期末 2025-12-31 与收入期末 2026-06-30 相差 181 天，口径不一致，只作参考 |
| D1 股本变化（约一年） | 7.25% | 👀 | 最新股本 / 4 个观测点前 − 1；每股收入同比 +18.6%；核实融资方式：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |

**估值（USD 口径）**

- 未计算：market cap withheld: foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 20-F（提交 2026-03-03，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1840706/000184070626000006/soph-20251231.htm

- **remaining_performance_obligations** ×1：…one year or less. There are also certain biopharma and Alamut contracts in which performance obligations extend over multiple years, however, these contracts are immaterial. The Company has elected to apply the practical expedient not to disclose the value of remaining performance obligations associated with these types of contracts. Disaggregated revenue When disaggregating revenue, the Company considered all of th
- **prepayment** ×1：…mance obligations prior to invoicing and is primarily related to Dry Lab to be invoiced for the most recently completed month and some portions of biopharma contracts. F-16 Table of Contents Deferred contract revenue Deferred contract revenue relates to prepayments received from customers before revenue is recognized and is primarily related to SOPHiA DDM Platform analyses invoiced in advance of the customers perfor
- **sole_source** ×1：…25, we collaborated with seven laboratories across seven countries to provide this service. We continually assess our dependence on our suppliers and manufacturers and evaluate alternative solutions. We have built our business such that we do not rely on any single supplier or manufacturer, such that we are able to switch suppliers and manufacturers as necessary. We believe that this mitigates risks to our business 
- **customer_concentration** ×1：…ted (in USD thousands): 2025 2024 As of January 1 $ 394 $ 1,181 Increase 520 114 Reversals (463) (637) Write-off (155) (213) Currency translation adjustments 70 (51) As of December 31 $ 366 $ 394 As of December 31, 2025 and 2024, the Company’s largest customer balance represented 15% and 18% of accounts receivable, respectively. All customer balances that individually exceeded 1% of accounts receivable in aggregate 
- **going_concern** ×2：…lized internal software development costs, defined benefit liability and share-based compensation. Disclosed in the corresponding sections within the footnotes are the areas which require a high degree of judgment, significant assumptions, and/or estimates. Going concern basis The consolidated financial statements have been prepared on a going concern basis (See Note 27 – “Capital management”). Historical cost conve
- **at_the_market** ×2：…-based compensation as a result of appreciation in the price of our stock. Additional increases related to $2.4 million in legal expenses related to the Guardant Health litigation and $0.9 million in costs related to our shelf registration statements and an at-the-market offering program which allows for sales of our stock. In connection with the Guardant Health litigation, as discussed in "Recent Developments—Guard
- **default_covenant** ×3：…re scheduled to mature on the fifth anniversary of the closing date and accrue interest at Term Secured Overnight Financing Rate (“Term SOFR”) (floored at 4% per annum) plus 6.25% per annum; provided that upon the occurrence and during the continuation of any event of default, the term loans will accrue interest at Term SOFR plus 9.25% per annum. The Perceptive Credit Agreement also contains certain mandatory prepay

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 SOPH 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `SOPH`：share_count_older_than_200_days
- `SOPH`：market_cap_withheld: foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).
- `SOPH`：foreign_private_issuer: 20-F/6-K filer; quarterly XBRL may be missing and US quote may be an ADR
- `SOPH`：financials_from_fallback: yahoo_timeseries (SEC XBRL latest quarter missing)
- `SOPH`：sec_stale_series_dropped:total_debt:last_end_2021-12-31_vs_newest_2025-12-31

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
