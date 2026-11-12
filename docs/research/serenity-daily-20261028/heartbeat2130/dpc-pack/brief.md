# 研究包：DPC（DPC Holdings PLC）

> 数据抓取 2026-10-28T13:38:12Z · 连接器 v9.1.0 · 用时 3.11 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `DPC` | 28.735 USD | 4.29B | -49.8% | — | 1.07B | +33.8% | +33.8% | 25.8% (2026-06-28) | +0.7pp | 4.0x（latest_quarter_x4_2026-06-28） | — | shelf_registration_on_file, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, going_concern_exhibit_only |

## 2. 主体要点

- 最新季度收入：268.70M USD（期末 2026-06-28）；营业利润率 —；现金+短投 844.80M；FCF 跑道 — 季。
- 计算市值：4.29B USD（28.735 × 149,393,016 股，股本截至 2026-07-28）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 5（主文档 1/5）；customer_concentration 5（主文档 1/5）；capacity_signal 11（主文档 1/6）；going_concern 12（主文档 0/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3360 (Nonferrous Foundries (Castings))）
- 数据：sec_companyfacts，报告期 2026-06-28，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 0 · ✅ 4 · ℹ️ 2 · — 7

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 33.75% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 25.83% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 0.69pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | — | — | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | — | — | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | — | — | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | 59.07% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 9.94% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 2.72亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | — | — | 应收账款同比（2025-06-29→2026-06-28）− 收入同比；应收账款不足 TTM 收入的 5%，只作参考 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（2025-06-29→2026-06-28）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |

**估值（USD 口径）**

- 市值 42.93亿 USD · P/B 5.6x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-Q（提交 2026-08-11，期末 2026-06-28）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/2107018/000110465926093772/dpc-20260628x10q.htm

- **material_weakness** ×2：…trol objectives, and management is required to apply judgment in evaluating the cost-benefit relationship of possible controls and objectives. As disclosed in the Company’s Registration Statement on Form S-1, as amended (File No. 333-296215), the Company has identified material weaknesses in its internal control over financial reporting. The material weaknesses will not be considered remediated until the applicable 

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 DPC 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `DPC`：revenue_ttm_unavailable: P/S uses latest_quarter_x4_2026-06-28

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
