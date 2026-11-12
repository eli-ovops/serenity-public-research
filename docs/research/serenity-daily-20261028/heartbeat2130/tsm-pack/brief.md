# 研究包：TSM（Taiwan Semiconductor Manufacturing Company Limited）

> 数据抓取 2026-10-28T13:38:04Z · 连接器 v9.1.0 · 用时 2.67 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `TSM` | 437.505 USD | — | -10.2% | +45.6% | 152.79B | +51.0% | +17.6% | 66.4% (2026-09-30) | +7.0pp | — | +0.0% | pricing_power, acceleration, beneficial_owner_filings, insider_form4_activity, going_concern_exhibit_only |

## 2. 主体要点

- 最新季度收入：1.49T TWD（期末 2026-09-30）；营业利润率 —；现金+短投 2.13T；FCF 跑道 — 季。
- ⚠️ 市值未计算：foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 2（主文档 2/2）；customer_concentration 2（主文档 2/2）；atm_program 12（主文档 0/6）；capacity_signal 12（主文档 2/6）；going_concern 4（主文档 0/4）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3674 (Semiconductors & Related Devices)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 TWD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 0 · ✅ 4 · ℹ️ 2 · — 6

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 50.95% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 66.41% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 6.96pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | — | — | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | — | — | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | — | — | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | 36.05% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | — | — | 应收账款同比（2023-12-31→2024-12-31）− 收入同比；应收账款不足 TTM 收入的 5%，只作参考 |
| W2 存货增速 − 收入增速 | -36.26pp | ℹ️ | 存货同比（2023-12-31→2024-12-31）− 收入同比；资产负债表期末 2024-12-31 与收入期末 2026-09-30 相差 638 天，口径不一致，只作参考 |
| D1 股本变化（约一年） | 0.01% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |

**估值（TWD 口径）**

- 未计算：market cap withheld: foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

- 无 SEC 文件（非 SEC 申报主体或未抓取）。非美股以 2b 的交易所公告为准，必要时打开原文（references/market-source-playbook.md）。
## 4. 图谱位置与下一跳候选

- 链 `advanced_packaging` / 节点 `cowos`（CoWoS / 先进封装产能，状态 filling，类型 demand）；同层：AMKR, BESI.AS
  - 图谱状态最后核验：2026-10-19（9 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。
  - 下一跳 `3110.T` Nitto Boseki — 高端玻璃纤维布（T-glass）（now，依据 serenity_lead）
  - 下一跳 `LPK.DE` LPKF Laser — 玻璃基板（TGV / LIDE）（coming，依据 serenity_lead）
  - 下一跳 `011790.KS` SKC — 玻璃基板（TGV / LIDE）（coming，依据 serenity_lead）
  - 下一跳 `2802.T` Ajinomoto — ABF 增层膜（monopoly_not_bottleneck，依据 serenity_lead）

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2025-10-16 `1978716322453492060` REAFFIRM/bullish
  - 2026-10-15 `2110645575469461611` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `TSM`：share_count_older_than_200_days
- `TSM`：reporting_currency_TWD_differs_from_quote_currency_USD: use usd_view or convert before ratios
- `TSM`：market_cap_withheld: foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).
- `TSM`：foreign_private_issuer: 20-F/6-K filer; quarterly XBRL may be missing and US quote may be an ADR
- `TSM`：financials_from_fallback: yahoo_timeseries (SEC XBRL latest quarter missing)

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
