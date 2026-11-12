# 资料使用说明

REPORT.md是用户可读的当前结果，DOSSIERS.md和REVIEW_TABLE.csv是逐股状态。原始抓取、搜索、旧假设及追加纠正保留作研究证据，不代表全部内容有效。请勿把primary_status的ok解释成正文已验收，或把companyfacts最近一条当最新季度。

当前模型66家，未建立数值模型8家；当前全池仍未完成。final_decisions.json是状态决策输入。compile_review.py、build_dossiers.py可重新生成算式与底稿；closure_updates.py、final_bridge_updates.py、last_financial_review.py为一次性追加操作记录，不应重复运行，以免重复追加文字。write_report.py生成用户报告。

重要纠正：CCXI的旧Amgen链接无效；FPI/XBRL可能滞后且部分股数单位异常；行情用9月29日完整交易日；HKD/SEK/EUR/GBX/TWD与ADS不得混算。ASMPT中文月报文本有字体乱码，其股数已通过公开PDF第2页渲染人工核对。所有未来EPS、利润率、股数、折现率及汇率均为作者假设，不是公司承诺。

TradingAgents本轮未获得完成输出；两个目录是失败调用证据，不能当多agent研究报告。研究不访问任何账户、持仓、密钥或交易系统。
