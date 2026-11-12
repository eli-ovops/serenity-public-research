# AAON事件门增量与10:00 ET宏观发布核对

**截至2026-10-20 14:14 UTC／北京22:14／美东10:14：AAON的SEC submissions重新读取成功，`filingDate≥2026-10-19`无新行；可用官方IR新闻与活动页的公开解析未显示自13:44 UTC基线后的新公司公告或未来24小时已排期重大公司级二元事件。事件门仍可记“未发现已知重大事件，保留未披露/页面延迟风险”，不能写成确认没有事件。** 9月待完成房屋销售原定今日10:00 ET发布，官方实际数本次未取得；不能把8月+0.3%当今天数值，也不能把宏观日历未读升格为AAON公司事件硬FAIL。本文件只补AAON事件和宏观发布，不核价格/15分钟触发、不决定当前买入股数。

## 实际读取与时间

| 对象 | 本次读取回执 | 可用结论及限制 |
|---|---|---|
| [AAON SEC submissions（CIK 824142）](https://data.sec.gov/submissions/CIK0000824142.json) | 14:12:26 UTC标准Python严格TLS握手超时，无HTTP；查询本地阻断记录后，14:13:03—14:13:04 UTC同一公开URL、同一无身份UA由`curl`严格HTTPS **HTTP200**，JSON 163,528字节；公司名`AAON, INC.`，`filings.recent`的`filingDate≥2026-10-19`为空 | 比13:43—13:44 UTC基线无新**已入档**表单；不是证明公司未披露/未入档事情不存在。没有把首次TLS超时当SEC无记录。 |
| [AAON官方Investor News](https://investors.aaon.com/investor-news) | 14:12:26 UTC直接严格TLS握手超时，无HTTP拒绝；14:12—14:13 UTC原生公开解析显示网页内容（工具标Crawled today），页面前列8月21日企业标识、8月13日股息、8月10日Q2结果 | 可见范围未列10月20日新闻，也未见自13:44 UTC新增业绩、订单、融资。**解析抓取具体时分不明**、页面筛选/动态展示可能滞后，不能声称覆盖此刻所有官方消息。无再取已拒资源。 |
| [AAON官方Investor Events](https://investors.aaon.com/events) | 同一直接TLS超时；原生公开解析（Crawled today）展示Featured为8月10日Q2电话会，`All Upcoming Events`区域未列未来活动 | 在该列表的可见范围内未发现本截点后24小时已排期公司级重大二元事件；未披露事件残余风险保留。并非“未来24小时绝无事件”。 |
| [NAR待完成房屋销售官方页](https://www.nar.realtor/research-and-statistics/housing-statistics/pending-home-sales)与[发布日程](https://www.nar.realtor/press-releases/nar-statistical-news-release-schedule) | 原生公开搜索/解析仍显示**8月**环比+0.3%和“9月数据10月20日10:00 ET发布”，页面缓存最近抓取数日前；14:13:21—14:13:31 UTC普通严格HTTPS GET超时、0字节、HTTP状态`000`；限定官方新闻搜索未找到本日9月新公告 | **9月实际值、修订和预期比较UNKNOWN。** 不能用旧8月数填今天，也不能从下载超时推断发布取消或利空。该项是宏观时间风险，不是AAON独有的公司二元事件硬门。 |

本次公司事件增量不改变[09:46 ET冻结的AAON新图](../serenity-intraday-20261020-open/AAON_RECHECK.md)中已读的Q2经营/三情景，但也**不能证明其价格触发或账户门已过**。根Owner应按用户刚确认的五笔减卖更新已知数量与相关暴露，独立核当前行情是否先碰72、10:00 ET后是否收回73.65并出现规定承接、是否≤74.50；当前资金C及可用现金未知则不得给个性化股数。真实成交价/费用、执行与资金不能由本文件推断。若NAR官方新实际随后可用，须按发布时点补读并评估市场影响，不机械把一个宏观数据转成全市场一票否决。本轮无账户、秘密、订单、后台或交易操作。
