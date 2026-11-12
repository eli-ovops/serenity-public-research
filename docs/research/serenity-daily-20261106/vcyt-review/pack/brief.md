# 研究包：VCYT（Veracyte, Inc.）

> 数据抓取 2026-11-06T04:06:15Z · 连接器 v9.1.0 · 用时 2.9 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCYT` | 24.0 USD | 1.94B | -60.6% | -43.3% | 581.78M | +15.1% | +0.9% | 70.6% (2026-09-30) | +1.4pp | 3.3x | +2.1% | material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, supply_concentration, capacity_language |

## 2. 主体要点

- 最新季度收入：151.75M USD（期末 2026-09-30）；营业利润率 10.9%；现金+短投 199.83M；FCF 跑道 — 季。
- 计算市值：1.94B USD（24.0 × 80,695,480 股，股本截至 2026-10-30）。
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 11（主文档 4/6）；capacity_signal 14（主文档 6/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 8071 (Services-Medical Laboratories)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 0 · ✅ 11 · ℹ️ 4 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 15.08% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 318.41% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 70.58% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 1.36pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 21.80% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 8.85% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 1.37x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 1.62亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 8.89% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 8.90% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 59.69% | 🚩 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 3.66pp | ✅ | 应收账款同比（2025-09-30→2026-09-30）− 收入同比 |
| W2 存货增速 − 收入增速 | -20.62pp | ℹ️ | 存货同比（2025-09-30→2026-09-30）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| W3 合同负债/预收同比 | 107.19% | ℹ️ | 期末合同负债 / 去年同期 − 1；合同负债不足 TTM 收入的 1%，基数小，百分比只作参考 |
| D1 股本变化（约一年） | 2.08% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 3.33x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 19.37亿 USD · P/E(TTM) 15.3x · P/B 1.4x · P/S 3.3x · P/FCF 12.0x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] B2 商誉 / 归母权益：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-26，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1384101/000138410126000010/vcyt-20251231.htm

- **sole_source** ×13：…garding our capital requirements; the timing and success of our transition to offering more of our tests as in vitro diagnostic tests on multiple platforms worldwide, and our ability to continue to receive quality reagents and other raw materials from certain single source suppliers, for such products; our ability to obtain and maintain Medicare coverage for each of our tests; our need for additional financing; pote
- **material_weakness** ×3：…onfidence in the accuracy and completeness of our reported financial information and the market price of our common stock may be negatively affected. As a public company, we are required to maintain internal control over financial reporting and to report any material weaknesses in such internal control. Section 404 of the Sarbanes-Oxley Act of 2002 requires that we evaluate and determine the effectiveness of our int
- **export_controls** ×1：…r payment cycles, difficulty in collecting from payers, the effect of local and regional financial crises, and exposure to foreign currency exchange rate fluctuations; •changes in international trade policies, including tariffs, sanctions, or other import or export restrictions; •natural disasters, political and economic instability, including wars, terrorism, political unrest and other regional conflicts, outbreak 

### 10-Q（提交 2026-11-05，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1384101/000138410126000055/vcyt-20260930.htm

- **sole_source** ×4：…ur expectations regarding the timing and success of our transition to offering more of our tests as in vitro diagnostic, or IVD, tests on multiple platforms worldwide; •our ability to continue to receive quality reagents and other raw materials from certain single-source suppliers; •our ability to develop and launch tests, and enter into supply agreements, with manufacturers of alternative systems; •our expectations

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 VCYT 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `VCYT`：sec_stale_series_dropped:cost_of_revenue:last_end_2019-12-31_vs_newest_2026-09-30
- `VCYT`：sec_stale_series_dropped:total_debt:last_end_2021-12-31_vs_newest_2026-09-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
