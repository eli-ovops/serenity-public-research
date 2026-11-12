# 研究包：AGLT（Churchill Capital Corp XI Class A Ordinary Shares）

> 数据抓取 2026-11-06T04:28:37Z · 连接器 v9.1.0 · 用时 1.5 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `AGLT` | 11.51 USD | — | -5.3% | — | — | — | — | — | — | — | — | — |

## 2. 主体要点

- 最新季度收入：— （期末 None）；营业利润率 —；现金+短投 —；FCF 跑道 — 季。

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：no sector marker in the snapshot; treated as an operating company）
- 数据：—，报告期 —，币种 —；证据 —
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 0 · ✅ 0 · ℹ️ 1 · — 10

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | — | — | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | 最新报告期累计归母净利润同比 |
| P1 毛利率 | — | ℹ️ | 毛利 / 收入（最新期） |
| P2 净利率（TTM） | — | — | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | — | — | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | — | — | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | — | — | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | — | — | 应收账款同比（None→None）− 收入同比；应收账款不足 TTM 收入的 5%，只作参考 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（None→None）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |

**估值（— 口径）**

- 未计算：no share count

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 数据不足：可打分的项目少于 3 项，0 个红旗不代表“干净”，请先补数据（ETF/基金/新股/停牌常见）。
> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

- 无 SEC 文件（非 SEC 申报主体或未抓取）。非美股以 2b 的交易所公告为准，必要时打开原文（references/market-source-playbook.md）。
## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-06-29 `2071730699363881241` REAFFIRM/bullish
  - 2026-10-13 `2109937773440577755` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `AGLT`：symbol_resolution_review_needed
- `AGLT`：filings_unavailable

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
