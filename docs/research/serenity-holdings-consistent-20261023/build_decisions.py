"""Freeze this holdings-only research decision; never query accounts or trade."""
import json, datetime, math
from pathlib import Path
P=Path(__file__).resolve().parent
ROOT=P.parents[2]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text())
def write(p,x): Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
market=read(P/'shared/MARKET.json')
old={c['symbol']:c for c in read(ROOT/'docs/research/serenity-screen-all74-20261021/ALL74_CARDS.json')['cards']}
compute=read(P/'compute/CARDS.json')['cards']
bio=read(P/'bio/CARDS.json')
cards=[]
for original in compute:
 c=dict(original);t=c['symbol'];c['source_owner_card']='compute/CARDS.json#'+t
 c['root_revision']={'asof':NOW,'reason':'Independent review rejected single-day-low automatic exits and ambiguous profit execution. Final rules below supersede delegated draft protection only; financial sources and old-trigger audit remain.'}
 c['warning_policy']='单日低/单根K线只作预警，不是新增自动清仓；结构保护采用冻结前20完整交易日低点和匹配行业低点，连续两未来常规收盘确认。风险策略未验证盈利优势，可能卖飞；不是财务公允价。'
 level={'NVDA':212.77,'TSM':407.13,'CLS':286.35}[t]
 c['final_protection']={'effective_from':NOW,'warning':('原214收盘首批已触发；减后剩1不重复该首批。' if t=='NVDA' else '')+f'{t}常规收低于{level}进入结构预警；10/22已有弱势事实但不计为新规则历史触发。',
 'regular_close_exit':{'stock_below':level,'benchmark':'SOXX','benchmark_below':489.70,'consecutive_future_sessions':2,'count_starts_regular_session':'2026-10-23','target_remaining':0,'quantity_scope':'NVDA仅首批减后剩1；其余本来各1','execution':'两项须在连续两次未来常规收盘同时成立；下一实际可交易时点退出该剩余股。普通反弹不移动冻结线；不回填10/22为旧触发，不保证阈值成交。'},
 'basis':'股票及SOXX各自在10/22之前20个完整交易日的低点，考察此前区间被持续失守，而非紧贴昨天最低价；两次未来确认减少单日噪声，代价是多承担一日/周末及财报跳空。它是资本保护政策，不证明企业价值失效或净回报改善。',
 'preemptive_economic_exit':c.get('economic_invalidation'),
 'company_event_effect':'重大新披露先出现时当次替换估值/风险图，不等待价格确认；仅日历临近不自动反向交易。'}
 profit={'NVDA':(320,327.48),'TSM':(467.82,470),'CLS':(320,355.54)}[t]
 c['final_protection']['profit']={'warning_regular_price_gte':profit[0],'exit_regular_price_gte':profit[1],'target_remaining':0,'scope':'NVDA首批减后剩1，TSM/CLS各1','condition':'截至触价时尚无已核新披露足以上调原2028每股盈利/现金及未来稀释桥、因而上调同尺基准。不是只要一般新闻看多就取消。','execution':'常规盘有效价达到退出价，满足条件则卖该剩余1股；跳空高开超过阈值仍算，不要求恰在窄价带。临盘未读新披露不假装没有，先处理该具体材料并同次决定。','no_repeated_batch':True}
 if t=='NVDA':c['final_event_policy']='剩1继续按原GARP承担正常业绩/订单披露风险；本轮未核得下一财报具体日期，UNKNOWN，不编排期。新日期公布后原规模1复核，不把临近日期本身当清仓理由；重大经营/风险条件先到先处置。21:30下一指定运行补官方动态日历的具体日期。'
 if t=='TSM':c['final_event_policy']='原1股允许跨已核11/10月营收发布；出现Q4收入/毛利或每ADS现金盈利实质下修先重审/退出，不等股价。下一季度财报具体日UNKNOWN。本轮精确期后股本/10/22被拒6-K内容未全读，临时留1不加；21:30指定运行以独立发行人股本披露/MOPS有限补证，不重取被拒正文。'
 if t=='CLS':c['final_event_policy']='保留1明确承担10/26盘后Q3及10/27投资者日/08ET会议；若新保护/经济退出先满足则退出，不加事件仓。两未来收盘确认最早跨到10/26收盘，不能承诺在盘后报告前成交；接受隔夜跳空。'
 cards.append(c)
for c in bio:
 c=dict(c);c['confirmed_quantity']=c['latest_confirmed_quantity'];c['target_remaining']=c['research_target_remaining_now'];c['source_owner_card']='bio/CARDS.json#'+c['symbol'];cards.append(c)

def root_base(t,n):
 return {'symbol':t,'confirmed_quantity':n,'target_remaining':n,'owner':'/root','evaluated_utc':NOW,'principal_mode':'existing fundamental/GARP or limited qualification-stage right-tail; no silent switch to pure trend', 'quote':market['stats'][t]['latest_completed_regular_bar'],'technicals':market['stats'][t],'old_model':old[t]['valuation'],'scenario_values':old[t]['values'],'input_A_to_B':'No new verified operating/dilution input changes; same horizon/rate/model retained. New completed price session is risk evidence, not new corporate deterioration.','account':'Current NAV/cash/fees UNKNOWN; user quantities only, no new buys/percentage invented','execution_confirmed':False,'source_owner_card':'root/CARDS.json#'+t,'new_policy_effective_from':NOW}
dpc=root_base('DPC',1)
dpc.update(decision='hold1_noadd',reason='IGT收入+42%、Engine Products EBITDA+53%与23.5%利润率，以及有客户投入/量承诺的四项伙伴关系，支撑保留已减后1股的规模化盈利机会。原基准28.12/强46.59未下修；26.01并非因跌便宜就新增买点，基准余量仅8.11%，20日落后XLI35.84pp已是严重风险预警。没有新增指引/客户资格失败或原剩1硬退出证据，不能把旧IPO会计损失再说成今日坏消息。',
 financial={'period':'Q2/H1 ended2026-06-28, millionUSD except shares','q2_revenue':269,'q2_revenue_yoy_pct':34,'IGT_revenue_yoy_pct':42,'EngineProducts_EBITDA_yoy_pct':53,'EngineProducts_EBITDA_margin_pct':23.5,'q2_GAAP_net_income':-131,'q2_adjusted_net_income':6,'h1_GAAP_net_income':-178.5,'h1_CFO':-34.0,'h1_PPE':19.8,'h1_FCF':-53.8,'q2_CFO':-27.0,'q2_PPE':9.5,'q2_FCF':-36.5,'h1_DA_PPE':9.6,'cash_and_restricted':846.4,'borrowings':572.7,'IPO_adjusted_netcash':273.7,'postclose_MIP_and_tax':210.9,'postclose_placement_net':55.4,'transaction_adjusted_netcash':118.2,'reported_common_at_0628':149393016,'FY26_revenue_guide':[1000,1040],'FY26_adjusted_EBITDA_guide':[182,187],'MIP_and_IPO':'Separate old incentive/IPO expense from persistent dilution/cash cost; do not call GAAP loss pure operating collapse or ignore cash MIP.','current_cash_and_latest_exact_shares':'UNKNOWN; 325m credit facility is not cash or drawn debt.'},
 original='第一批3→2、后2→1的旧30.15减仓已经用户确认；现剩1只按后续规则。10/21新股27.57保护不是该既有股规则，不追认已触发。',
 trigger_audit='10/22收26.01、前20日低27.82已失守；这是预警。30.15旧首批不能重复、27.57新买规则不适用。未取得新增已触发剩1经济退出。',
 protection={'warning':'当前已进入预警：20日落后XLI35.84pp、股价失守27.82；反弹至基准28.12提前复核，而非只盼回本。',
 'price_exit':'从10/23起，连续两个未来常规收盘同时满足DPC<27.82及XLI<164.66，现剩1→0，下一实际可交易时点执行。这是前20日区间失守+行业持续确认的新资本保护，不回填历史、不复活27.57，不保证成交或收益改善。',
 'profit_exit':'常规有效价≥29.52，若未有已核新披露提高2028 EBITDA350m、净现金/股本桥及同尺基准，卖剩1→0。28.12先预警；29.52是原合理参与上限、已高于基准，不等旧成本/44.25前高。跳过阈值高开仍算。',
 'economic_exit':'公司下修全年2026 adjusted EBITDA指引至原182m下限以下且非等值每股现金改善可抵消，或四项OEM伙伴中的重大IGT资格/量承诺终止、良率/毛利恶化使350m2028桥失去支持，剩1→0/当次新图，不等股价。一次金属转嫁或正常扩产负营运资本不单独推出失败。',
 'event':'现剩1允许跨11/12盘前Q3，11/11常规盘前先核新增伙伴/现金/指引材料；无新反证不因日期临近临时默认卖。财报同次重算扣MIP后现金、持续激励稀释、客户投入与资本回报。报告/现金硬失败先到先退出。',
 'milestone_expiry':'11/12实际新结果公布时本旧财务图过期，下一次可读运行必须替换，不沿旧28.12卖/买图无限续期。',
 'cost':'保护可能在反弹中卖飞，持有可能承受压力14.89或更低；1股仍有全部26.01名义归零风险，场景不是下限。'},
 strongest_countercase='IPO后股本/激励重定价、客户集中和内制、高capex与H1负FCF；基准仅8.11%余量不足证明新增吸引力，保持1仍付机会成本。强46.59需要EBITDA480m、20x与未来160m股，非必达。',
 primary_sources=['https://data.sec.gov/submissions/CIK0002107018.json','https://ir.doncasters.com/news-and-events/news/news-details/2026/DPC-Holdings-Reports-Strong-Second-Quarter-2026-Results/default.aspx','https://ir.doncasters.com/news-and-events/news/news-details/2026/Doncasters-Completes-Debt-Refinancing/default.aspx','https://finance.yahoo.com/markets/stocks/articles/dpc-holdings-announces-date-time-203000078.html'],
 source_limits='CurrentSEC200 no new since9/8; issuerQ2 full financial/cash tables read200; IRlist is dynamic Loading shell, not successful list coverage. Nov12 schedule from company-authored BusinessWire release previously preserved; current independent search copies confirm but are not independent company facts. OldSEC10Q403 not re-requested. No new-buy event PASS claimed.')
poet=root_base('POET',10)
poet.update(decision='hold10_noadd',reason='光学封装/光源架构与实际已公告客户订单支持有限量产右尾，现存现金足够近期建设；但Q2只有0.570m收入、持续烧钱且高于作者基准4.25，所以不增加。原10股是减后剩余量，未见新增认证/订单失败；不能把已知融资和conditional500m框架重新读成新利空来反向清仓。现在主动固定反弹先减一半及剩余5的退出，而非等全仓回撤才讨论。',
 financial={'period':'Q2 ended2026-06-30, millionUSD unless noted','revenue':0.569925,'revenue_yoy_pct':112,'revenue_qoq_pct':13,'net_loss':-11.3,'CFO':-12.2,'Q1_CFO':-8.8,'prior_year_q2_CFO':-7.8,'SBC':3.816906,'R_and_D':5.8,'noncash_derivative_warrant_gain':5.5,'financial_advisory_fees':6.1725,'cash_and_short_investments':796.3,'Lumilens_initial_PO':50,'conditional_5year_framework_over':500,'another_PO':2.4,'May18_units_issued':19047620,'unit_price_USD':21,'attached_warrant_strike_USD':26.25,'warrant_expiry':'2029-05-18','Aug11_RSU_grant':2453271,'current_cash_and_exact_common':'UNKNOWN; future model shares210/230/270m include dilution, not current official shares. No unearned26.25warrant cash counted.','stage':'Qualification/volume ramp, not profitable operating company; cash was mainly equity-raised not earnings.','FAQ_correction':'JulyFAQ summary830m cash/shortinvest claim conflicts with detailed wording830m capital raised over12months; use later Q2 financial796.3m, do not double add fundraising.'},
 original='用户确认20股卖10，当前10；旧5.70自动退出已退休，Q3Nov16/2H2026ramp为里程碑。',
 trigger_audit='10/22收5.33、前20低5.30附近、20日落后SOXX15.26pp进入预警；旧5.70不是现行失效，不以跌破它补造历史清仓。',
 protection={'warning':'现已预警：在前20日5.30附近、相对SOXX20日落后15.26pp；到5.75前检查有无真正新增量产收入/客户验收，而非新增市场规模宣传。',
 'first_batch_downside':'从10/23起连续两个未来常规收盘同时POET<5.30及SOXX<489.70，10→目标5；新结构风险政策，不是旧5.70。',
 'first_batch_rebound':'常规有效价≥5.75，且没有已核新增付费出货/客户量产验收、归母单位经济与股本桥足以上调原4.25基准，10→目标5。5.75沿原昂贵区边界，非新增公允价；高开跳过仍算。',
 'batch_deduplication':'下行与反弹是同一首批5股，只执行一次。用户确认剩5后退休，绝不因仍满足条件再卖同5。未确认前事实仍10。',
 'remaining5_profit':'剩5常规有效价≥8.20（冻结前20日高），且仍无上述已核量产/每股现金改善上调模型，剩5→0；保留至此的右尾可能卖飞。新实质公告先到时当次重算，不机械以旧价卖也不凭宣传抬线。',
 'economic_exit':'主要客户认证/订单被终止、正式撤回2H2026量产且无可信新交付安排，或现金耗用/并购承诺导致关键量产前需要实质折价稀释且每股桥失效，现剩10或5→0，不等价格。',
 'event':'当前10（首批后5）明确允许跨11/16 07ET Q3，11/13常规盘前检查已公布新材料；如果原硬风险先触发则降至对应量，不新加事件仓。11/16不是已证量产成功，公布后当次核产品/NRE分拆、付费出货、毛利和现金。',
 'milestone_deadline':'2H2026窗口至12/31；若全年结束后仍无可核真实量产出货且未事前完成有明确日期/现金安排的新承销，2027首个正常交易时点剩余→0；不是把查询故障当没有出货。',
 'cost':'10股现名义53.30可全部损失，5股风险仍可26.65；两日确认/夜间公告可跳过计划价，既有现金不是股价底。'},
 strongest_countercase='50mPO和500m五年框架仍依赖开发、认证和量产，不能当现收入/确定backlog；796.3m现金来自股权融资，有capex/M&A/烧钱/认股权稀释；强12.06需要700m2029收入，不用社媒激光传闻证明。',
 primary_sources=['https://data.sec.gov/submissions/CIK0001437424.json','https://www.poet-technologies.com/news/poet-technologies-reports-second-quarter-2026-results-revenue-up-112-year-over-year-in-sixth-consecutive-quarter-of-sequential-growth','https://www.poet-technologies.com/blog/faq-production-orders-cash-position-and-the-path-to-greater-revenue','https://www.poet-technologies.com/news/poet-technologies-to-report-third-quarter-2026-financial-results-on-november-16'],
 source_limits='CurrentSEC200 no new material beyondOct19 notice; current issuernews/event/Q2/FAQ200 read. Index/sampling/ramp statements not actual paid volume or verified currentcash. Independent issuerQ2 replaces anyblockedSECtext, no auth/profile accessed.')
cards += [dpc,poet]
rmbs=read(ROOT/'docs/research/serenity-rmbs-complete-20261023/DECISION.json')
cards.append({'symbol':'RMBS','confirmed_quantity':1,'target_remaining':1,'decision':'hold1_noadd_original_plan_restored','original_decision':rmbs,'source_owner_card':'../serenity-rmbs-complete-20261023/DECISION.json','quote':market['stats']['RMBS']['latest_completed_regular_bar'],'technicals':market['stats']['RMBS'],'same_ruler_PV':[37.7376,93.5644,168.4159],'recheck':'same closed US10/22 session as fully repaired RMBS audited today; no changed input warrants rerun','protection':'Original regular effective price<=85 exits1; low85.01 did not touch;93.56review/98without new stronger per-share cash/profit exits1. No move lower.','event':'ExistingGARP1explicitly may crossOct26afterclose only while original/economic exits do not trigger; gap can skip85; noaddeventshare.','financial_source':'../serenity-rmbs-complete-20261023/FINANCIAL_BRIDGE.json','skill_source':'../serenity-rmbs-complete-20261023/skill-finish/RMBS-research.md','consistency':'Earlier unconditionalexit withdrawn; no reversal due to this request, old inventory/CFO/DOJ facts not new bad news.'})
order=['NVDA','TSM','CLS','RMBS','RXRX','DPC','POET','SCTX'];cards.sort(key=lambda c:order.index(c['symbol']))
out={'schema_version':'holdings-consistent-20261023-v1','frozen_at_utc':NOW,'rules':'SERENITY-DECISION-2026-10-23-v1.3','scope':'8 current confirmed positions only, not74screen','new_policies_effective_from':NOW,'current_CAPITAL':'UNKNOWN','no_account_access':True,'latest_regular_session':'2026-10-22','regular_open_next_Beijing':'2026-10-23T21:30:00+08:00','cards':cards,'actual_user_fills_not_changed':True,'upstream_model_check_not_return_proof':True}
write(P/'DECISIONS.json',out)
write(P/'root_CARDS.json',[dpc,poet])
checks=[]
quantities={'NVDA':2,'TSM':1,'CLS':1,'RMBS':1,'RXRX':20,'DPC':1,'POET':10,'SCTX':2}
for c in cards:
 assert c['confirmed_quantity']==quantities[c['symbol']]
 assert 0<=c['target_remaining']<=c['confirmed_quantity']
 checks.append({'symbol':c['symbol'],'confirmed':c['confirmed_quantity'],'target':c['target_remaining']})
assert len(cards)==8 and len({c['symbol'] for c in cards})==8
assert market['stats']['NVDA']['latest_completed_regular_bar']['close']<214
assert market['stats']['RMBS']['latest_completed_regular_bar']['low']>85
assert not (market['stats']['SCTX']['latest_completed_regular_bar']['close']<16.7 and market['stats']['XBI']['latest_completed_regular_bar']['close']<145)
for t in ['DPC','POET']:
 m=old[t]['valuation']
 if t=='DPC': vals=[(e*x+n)/s/(1+m['rate'])**m['years'] for e,x,n,s in zip(m['ebitda_m'],m['multiple'],m['net_cash_m'],m['shares_m'])]
 else:
  m=m['model']; vals=[(r*g*x+n)/s/(1+m['rate'])**m['years'] for r,g,x,n,s in zip(m['revenue'],m['net_margin'],m['pe'],m['net_cash'],m['shares'])]
 assert all(abs(a-b)<1e-8 for a,b in zip(vals,old[t]['values']))
write(P/'ARITHMETIC_ACCEPTANCE.json',{'asof':NOW,'counts':checks,'all8_counts':True,'frozen_trigger_checks':True,'root_model_recomputed':True,'new_future_sessions_no_backfill':True,'capital_unknown_preserved':True,'scope_limit':'arithmetic/state/provenance consistency only; not investment edge or predictive validation'})
print(json.dumps({'asof':NOW,'decisions':checks,'status':'arithmetic/state checks pass; decision policy still requires qualitative review'},ensure_ascii=False))
