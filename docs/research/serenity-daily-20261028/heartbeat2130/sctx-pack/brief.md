# 研究包：SCTX（Scribe Therapeutics Inc.）

> 数据抓取 2026-10-28T13:38:18Z · 连接器 v9.1.0 · 用时 2.86 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SCTX` | 16.28 USD | 308.21M | -58.9% | — | 7.67M | -60.8% | -60.8% | — | — | 40.2x（latest_quarter_x4_2026-06-30） | — | acceleration, shelf_registration_on_file, beneficial_owner_filings, insider_form4_activity, going_concern |

## 2. 主体要点

- 最新季度收入：1.92M USD（期末 2026-06-30）；营业利润率 -489.8%；现金+短投 43.01M；FCF 跑道 — 季。
- 计算市值：308.21M USD（16.28 × 18,931,680 股，股本截至 2026-08-31）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 10（主文档 2/6）；capacity_signal 19（主文档 0/6）；going_concern 8（主文档 2/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 2836 (Biological Products, (No Diagnostic Substances))）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 2 · 👀 0 · ✅ 0 · ℹ️ 2 · — 8

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | -60.84% | 🚩 | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | — | ℹ️ | 毛利 / 收入（最新期） |
| P2 净利率（TTM） | — | — | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | — | — | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | — | — | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | 176.80% | 🚩 | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | — | — | 应收账款同比（2025-06-30→2026-06-30）− 收入同比；应收账款不足 TTM 收入的 5%，只作参考 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（2025-06-30→2026-06-30）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| W3 合同负债/预收同比 | -35.29% | ℹ️ | 期末合同负债 / 去年同期 − 1；合同负债不足 TTM 收入的 1%，基数小，百分比只作参考 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |

**估值（USD 口径）**

- 市值 3.08亿 USD
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] G1 收入同比：到定期报告原文核对口径与一次性因素
- [ ] B1 资产负债率：到定期报告原文核对口径与一次性因素

> 数据不足：可打分的项目少于 3 项，0 个红旗不代表“干净”，请先补数据（ETF/基金/新股/停牌常见）。
> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-Q（提交 2026-09-02，期末 2026-06-30）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1853921/000119312526380191/sctx-20260630.htm

- **customer_deposits** ×4：…obable as of June 30, 2026 and December 31, 2025. As of June 30, 2026, the Company had $10.6 million classified as current deferred revenue related to this agreement, which is expected to be recognized over the remaining term of the performance obligations. Contract Liabilities The following table presents changes in the Company’s total contract liabilities for the six months ended June 30, 2026 and 2025(in thousand
- **long_term_supply_agreement** ×1：…roval to market and commercialize a product candidate, an inability to meet commercial demands for our products. In addition, we do not have any long-term commitments or supply agreements with any third-party manufacturers. We may be unable to establish any long-term supply agreements with third-party manufacturers or to do so on acceptable terms, which increases the risk of failing to timely obtain sufficient quant
- **sole_source** ×7：…on. • If we are unable to establish sales and marketing capabilities, we may not successfully commercialize any approved products. • We rely, and expect to continue to rely, on third parties — including collaborators, licensors, clinical trial partners, and single-source manufacturers and suppliers — and the failure of these parties to perform, or conflicts within these relationships, could delay or harm our develop
- **customer_concentration** ×1：…e Company recognized revenue from collaboration partners in the three and six months ended June 30, 2026 and 2025, with all revenue generated within the United States. The percentages of collaboration revenue and accounts receivable from each of the Company’s customers that individually accounted for 10% or more of its total collaboration revenue and accounts receivable were as follows: Accounts Receivable, net Reve
- **going_concern** ×8：…concurrent private placement, will be sufficient to fund its planned operating expenses and capital expenditure requirements for at least the next twelve months from the issuance date of these financial statements. Accordingly, management concluded that the substantial doubt about the Company's ability to continue as a going concern that existed as of June 30, 2026 was alleviated prior to the issuance of these finan
- **export_controls** ×2：…ws and regulations. Compliance with these legal standards could impair our ability to compete in domestic and international markets. We can face criminal liability and other serious consequences for violations, which can harm our business. We are subject to export control and import laws and regulations, including the U.S. Export Administration Regulations, U.S. Customs regulations, various economic and trade sancti

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 SCTX 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `SCTX`：revenue_ttm_unavailable: P/S uses latest_quarter_x4_2026-06-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
