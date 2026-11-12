# 研究包：SPCX（Space Exploration Technologies Corp.）

> 数据抓取 2026-10-26T15:15:53Z · 连接器 v9.1.0 · 用时 31.86 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SPCX` | 149.11 USD | 2.02T | -33.9% | — | 58.30B | +161.4% | +86.5% | 62.4% (2026-09-30) | +10.9pp | 34.7x（latest_quarter_x4_2026-09-30） | — | pricing_power, acceleration, shelf_registration_on_file, unregistered_equity_sale_8k_3_02, material_agreement_8k_1_01 |

## 2. 主体要点

- 最新季度收入：14.57B USD（期末 2026-09-30）；营业利润率 19.1%；现金+短投 89.86B；FCF 跑道 13.7 季。
- 计算市值：2.02T USD（149.11 × 13,579,000,000 股，股本截至 2026-09-30）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 8（主文档 1/6）；atm_program 3（主文档 0/3）；capacity_signal 35（主文档 0/6）；going_concern 5（主文档 0/5）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 7370 (Services-Computer Programming, Data Processing, Etc.)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 0 · ✅ 4 · ℹ️ 2 · — 7

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 161.39% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 62.42% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 10.93pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | — | — | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | — | — | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | — | — | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | 30.42% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 27.39% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 519.94亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | — | — | 应收账款同比（2025-09-30→2026-09-30）− 收入同比；应收账款不足 TTM 收入的 5%，只作参考 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（2025-09-30→2026-09-30）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |

**估值（USD 口径）**

- 市值 2.02万亿 USD · P/B 11.4x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-Q（提交 2026-10-22，期末 2026-09-30）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm


## 4. 图谱位置与下一跳候选

- 链 `space` / 节点 `launch`（火箭发射，状态 monopoly_not_bottleneck，类型 demand）；同层：RKLB
  - 图谱状态最后核验：2026-10-19（7 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-06-27 `2070691462354993543` REAFFIRM/bullish
  - 2026-07-06 `2074109998544846954` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `SPCX`：revenue_ttm_unavailable: P/S uses latest_quarter_x4_2026-09-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
