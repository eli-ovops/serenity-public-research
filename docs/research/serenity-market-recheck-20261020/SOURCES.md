# 来源、读取范围与时点

本轮主要报价截点：2026-10-20 08:17—08:19 UTC（北京16:17—16:19，美东04:17—04:19，盘前）；各股更早成交时刻、少量后续抓取和日期型旧价逐条保留于SNAPSHOT.json。68个正式池代码返回数值报价不等于68家证券身份、估值、事件或买入研究全部通过。

## 原始公开证据

- Nasdaq公开报价：`public/QUOTE_*.raw`为原体、`.json`为解析、`.receipt.json`为URL/抓取时点/hash；同时保留盘前primary与昨收secondary，不把非实时日期型价当盘前成交。INTC原Python TLS失败和一次严格TLS、同身份curl恢复均保留，无关闭证书验证。
- SEC公开最新索引：`public/SEC_*.raw/.json`，本轮7家（NVDA、TSLA、CLS、NVT、CAMT、INOD、SCTX）。报告仅解释Oct19—20窗口；未见新项不是绝对无未公开事件。13G与代理材料不作财报变化或当日机构买入证据。
- 原冻结条件：[Oct15持仓退出原图](../serenity-holdings-exits-20261015/REPORT.md)。历史触发用原定义和日线；本轮新POET20→0、RXRX30→20单独标明，不回写旧指令。
- 同日上午已核原始日线/财务重点章节：[优化研究证据索引](../serenity-optimization-prd-20261020/EVIDENCE_INDEX.md)、[日线诊断](../serenity-optimization-prd-20261020/root/market_diagnostics.json)。这是明确复用，不称本轮重读所有11家全部财报。
- 本轮独立定向读取：[RXRX/TSM一手来源](rxrx_tsm/SOURCES.md)、[复核](rxrx_tsm/REPORT.md)、[计算](rxrx_tsm/CALCULATION.csv)。含已读、条件现金桥、尚未完成的完整rNPV与失败替代边界。

## 官方页面与有限解析回执

- [CBOE VIX](https://www.cboe.com/tradable-products/vix/)：18.62、+0.98%，页面时区未明且至少20分钟延迟，不视为与QQQ同步；昨收18.44来自同日上午保存的CBOE CSV。今日完整OHLC未独立取得。
- [Treasury收益率](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026)：Oct19 2y4.77%、10y5.15%，不是Oct20实时债市。
- [NY Fed十月日历](https://www.newyorkfed.org/research/calendars/i-oct26.html)、[BLS十月日历](https://www.bls.gov/schedule/2026/10_sched_list.htm)、[Fed十月官方日历](https://www.federalreserve.gov/newsevents/2026-october.htm)：采用官方日期，不采二手冲突日历；没有全量官员发言/特朗普个人社媒读取。
- [Tesla IR](https://ir.tesla.com/)、[CLS业绩/投资者日](https://celestica.gcs-web.com/news-releases/news-release-details/celestica-hold-q3-2026-financial-results-and-2026-investor-and)、[NVT事件](https://investors.nvent.com/events-and-presentations/default.aspx?LanguageId=1)、[INOD业绩时间](https://investor.innodata.com/news/news-details/2026/Innodata-to-Report-Third-Quarter-2026-Results/default.aspx)、[POET新闻](https://www.poet-technologies.com/news-media)、[SCTX新闻](https://www.scribetx.com/newsroom)：报告分别保留实际事件日期与有限读取范围。
- [CAMT Oct14 SEC附件](https://www.sec.gov/Archives/edgar/data/1109138/000117891326004769/zk2636226.htm)：>800m订单/2027展望不是已实现利润。原错误IR落地页404后使用SEC原披露，没有把工具失败当排除。
- [NVT/AMD合作](https://investors.nvent.com/press-releases/press-release-details/2026/nVent-and-AMD-Collaborate-on-Cooling-for-AMD-Helios-Rackscale-Solution/default.aspx)：有合作无订单金额。
- DPC IR新闻页为动态空框架，不能据此判无新事件；NVDA部分IR页面不可读，明确只用已读财务章节及本轮SEC更新。6海外代码未统一完成时区与证券报价/事件校验。

`market_recheck_*.txt`保存本轮部分网页工具解析输出；它们是有限解析结果，不冒充完整网页、视频/图表或社交线程全文。本轮不声称读取X情绪、74家全部财报或完整估值。无账户/订单/凭据/profile访问、无后台进程。

`VALIDATION.json`核对原体hash、11只数量边界/目标、CSV一致性、估值算术与链接；不替代策略前瞻收益验证或成交证据。`MANIFEST.json`冻结本次目录文件hash，之后新事实另轮记录。
