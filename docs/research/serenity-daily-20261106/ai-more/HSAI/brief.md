# 研究包：HSAI（Hesai Group）

> 数据抓取 2026-11-06T04:39:40Z · 连接器 v9.1.0 · 用时 4.46 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `HSAI` | 12.84 USD | — | -56.2% | -44.3% | 500.26M | +21.9% | +26.5% | 40.1% (2026-06-30) | -2.4pp | — | — | beneficial_owner_filings, insider_form4_activity, going_concern_exhibit_only, customer_concentration, supply_concentration |

## 2. 主体要点

- 最新季度收入：860.83M CNY（期末 2026-06-30）；营业利润率 —；现金+短投 4.76B；FCF 跑道 — 季。
- ⚠️ 市值未计算：foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 2（主文档 1/2）；customer_concentration 2（主文档 0/2）；capacity_signal 10（主文档 4/6）；going_concern 3（主文档 0/3）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3569 (General Industrial Machinery & Equipment, NEC)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 CNY；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 0 · ✅ 3 · ℹ️ 5 · — 6

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 21.86% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 40.11% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | -2.43pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | — | — | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | — | — | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | — | — | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | 20.45% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 44.77亿 CNY | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | 43.13pp | ℹ️ | 应收账款同比（2024-12-31→2025-12-31）− 收入同比；资产负债表期末 2025-12-31 与收入期末 2026-06-30 相差 181 天，口径不一致，只作参考 |
| W2 存货增速 − 收入增速 | 17.20pp | ℹ️ | 存货同比（2024-12-31→2025-12-31）− 收入同比；资产负债表期末 2025-12-31 与收入期末 2026-06-30 相差 181 天，口径不一致，只作参考 |
| W3 合同负债/预收同比 | -36.29% | ℹ️ | 期末合同负债 / 去年同期 − 1；合同负债不足 TTM 收入的 1%，基数小，百分比只作参考 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |

**估值（CNY 口径）**

- 未计算：market cap withheld: foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 20-F（提交 2026-04-24，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1861737/000110465926048025/hsai-20251231x20f.htm

- **customer_deposits** ×5：…,192,115 599,464 TOTAL ASSETS 5,989,611 11,261,278 1,610,341 LIABILITIES AND SHAREHOLDERS’ EQUITY Current liabilities: Short-term borrowings 345,253 448,233 64,096 Notes payable 10,096 150,199 21,478 Accounts payable 345,011 592,560 84,735 Contract liabilities 32,994 21,019 3,006 Amounts due to related parties 335,253 — — Accrued warranty liability 43,607 77,672 11,107 Income tax payable — 27,157 3,883 Accrued expen
- **customer_concentration** ×5：…ch could have a material adverse effect on our operating results, financial condition and business prospects. Our sales and operations in international markets outside of China expose us to operational, financial and regulatory risks. Sales to international customers accounted for 47.2%, 25.7% and 22.2% of our revenues in 2023, 2024 and 2025, respectively. We are committed to growing our international sales, and hav
- **material_weakness** ×3：…December 31, 2025, as stated in its report, which appears on page F-4 of this annual report. Internal Control over Financial Reporting In connection with the audits of our consolidated financial statements as of and for the year ended December 31, 2024, we identified one material weakness in our internal control over financial reporting. As defined in the standards established by the U.S. Public Company Accounting O
- **export_controls** ×19：…e relating to autonomous driving applications, could be subject to restrictions by the U.S. or other foreign governments. As a result, government policies that restrict international trade and investment, such as capital controls, economic or trade sanctions, export controls, tariffs or foreign investment filings and approvals, may affect the demand for our products and services, impact the competitive position of o

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 HSAI 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `HSAI`：share_count_older_than_200_days
- `HSAI`：reporting_currency_CNY_differs_from_quote_currency_USD: use usd_view or convert before ratios
- `HSAI`：market_cap_withheld: foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).
- `HSAI`：foreign_private_issuer: 20-F/6-K filer; quarterly XBRL may be missing and US quote may be an ADR
- `HSAI`：financials_from_fallback: yahoo_timeseries (SEC XBRL latest quarter missing)
- `HSAI`：sec_stale_series_dropped:goodwill:last_end_2023-12-31_vs_newest_2025-12-31

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
