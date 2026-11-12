# SERENITY_FOSUN_TRADABILITY_AUDIT_REPORT

任务名称: SERENITY_FOSUN_SECURITIES_TRADABILITY_AUDIT_PUBLIC_ONLY  
生成时间: 20260601_173131  
模式: public-only / no broker login / no account access / no trading action

## Final Decision

PUBLIC_LEVEL_AUDIT_COMPLETED_APP_CONFIRMATION_REQUIRED

本报告只判断公开资料层面的 ticker 可交易性边界。能搜到公开行情或交易所挂牌，不等于用户在复星证券 / 复星财富 / 星财富 App 账户内一定可以买。最终必须以用户自己在星财富 App 内是否出现“买入/交易”按钮为准。

## Broker Scope Evidence

券商对象限定为复星证券 / 复星财富 / 星财富 App / Fosun Wealth / Fosun International Securities。

公开资料依据:

- Google Play 星财富公开页: 覆盖 Hong Kong stocks, US stocks, A-shares, US stock options, ETFs 等，并提及 US stocks 全时段/夜盘相关功能。Source: https://play.google.com/store/apps/details?hl=en&id=com.fosunhani.stock
- Apple App Store 星财富公开页: 开发者/卖方为 Fosun International Securities Limited，描述品种包括正股、ETF 等，版本记录提及港股/美股市价单与美股期权页面。Source: https://apps.apple.com/us/app/id1629355060
- 复星财富官网: 产品与服务包含环球交易服务，但官网可见文本未逐一列明 OTC/Pink/外国本地市场支持。Source: https://www.fosunwealth.com/
- 星财富公开页/下架公告: 仅作为 App/服务对象确认，不作为单 ticker 可买证据。Source: https://fotechwealth.com.cn/

结论: 公开范围支持“美股正股/ETF”类别，但不能外推为所有 OTC/Pink、外国本地股票、已退市/并购/停牌/公司行动 ticker 均可买。

## Classification Counts

- A_US_EXCHANGE_LISTED_LIKELY_SUPPORTED_BY_FOSUN_SCOPE: 35
- B_OTC_OR_PINK_APP_CHECK_REQUIRED: 1
- C_FOREIGN_LOCAL_MARKET_APP_CHECK_REQUIRED: 1
- D_CORPORATE_ACTION_OR_LISTING_STATUS_APP_CHECK_REQUIRED: 3
- E_BLOCKED_NOT_ENOUGH_PUBLIC_EVIDENCE: 0

## Priority App Manual Check Tickers

SKYT, INVZ, LAZR, SIVE, SIVEF

说明: CSV 中所有 ticker 的 `app_manual_check_required_yes_no` 均为 yes，因为本任务没有、也不允许取得用户 App 内买入按钮证据。B/C/D/E 为高优先级人工复核。

## Special Notes

- SIVE: 按公开资料为 Sivers Semiconductors AB 瑞典 Nasdaq Stockholm 本地股，分类为 C_FOREIGN_LOCAL_MARKET_APP_CHECK_REQUIRED。
- SIVEF: 按公开资料为美国 OTC Markets / OTC Pink-style foreign ordinary quotation，分类为 B_OTC_OR_PINK_APP_CHECK_REQUIRED。
- LAZR: 公开资料显示 Nasdaq 退市/转 LAZRQ OTC，分类为 D_CORPORATE_ACTION_OR_LISTING_STATUS_APP_CHECK_REQUIRED。
- SKYT: 公开资料显示 IonQ 收购 SkyWater 的 pending transaction / merger agreement，分类为 D_CORPORATE_ACTION_OR_LISTING_STATUS_APP_CHECK_REQUIRED。
- INVZ: 公开资料显示 Nasdaq minimum-bid non-compliance / deficiency cure period，分类为 D_CORPORATE_ACTION_OR_LISTING_STATUS_APP_CHECK_REQUIRED。
- POET / LWLG: 即使公开层面为 Nasdaq listed，本报告仍标注 Serenity research status = caution / blocked；这不代表研究合格。

## Source Method

- US exchange data: SEC company tickers exchange JSON, Nasdaq Trader nasdaqlisted.txt, Nasdaq Trader otherlisted.txt, Nasdaq quote pages.
- OTC/Pink and foreign local: OTC Markets, MarketScreener/Yahoo quote, Sivers annual report.
- Corporate action/listing risk: company IR, SEC filings, Nasdaq/TradingView listing-status evidence.

## Limitations

- 未登录复星证券 / 星财富 / 任何券商账户。
- 未读取账户余额、持仓、订单、交易记录。
- 未点击买入、卖出、下单、确认。
- 未读取 .env、API key、secret、token、cookie、SSH key。
- 未输出买入/卖出建议、目标价、仓位、入场点或交易计划。
- 复星/星财富没有公开逐 ticker tradability matrix；所有 ticker 最终都需要 App 内人工确认。
