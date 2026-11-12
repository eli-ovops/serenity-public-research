from pathlib import Path
import json,datetime
B=Path(__file__).resolve().parent
P=B.parents[2]
draft=P/'docs/research/serenity-skill-integration-20261023/rmbs-live/lens-draft.json'
d=json.loads(draft.read_text());now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
d.update(research_cutoff=now,as_of=now)
d['subject'].update(company_type='fabless_designer',taxonomy_codes=['MEM.INTERFACE.RCD.PMIC','SEMICONDUCTOR.IP'])
d['one_liner']='Amber：RMBS是内存接口芯片与IP设计商，非VECO同类设备商。85.73美元对作者2028基准现值约93.56仅留有限缓冲；真实独占供给未确立。'
d['thirty_second_summary']='Q2收入207.385百万美元、产品99.2百万/+22%、GAAP净利67.605百万、SBC15.886百万。标准FCF52.178百万，但6M CFO同比降15.9%。作者2028 EPS2.2/4/6×PE22/30/36，未来110百万股，不重复加净现金；终值须以12%贴现。新PMIC仍抽样，ChipAgents合作和投资金额未披露，不当订单或盈利。Renesas有竞争产品，机构尚未发现与供给独占均未证实，保留amber。'
d['capex_certainty']={'demand_source':'mixed','statement':'服务器/AI内存带宽与模块电源需求支持RCD/PMIC内容增加；公司Q2产品销售是已实现证据。缺客户逐笔不可取消订单、排期和产能预约金额，不能把行业capex直接变RMBS收入。PB-CORE-01。','evidence_ids':['E-LIVE-SEC-01','E-PRIMARY-PRODUCT']}
def node(name,role,ticker=None,subject=False):
 x={'name':name,'role':role,'listing_status':'listed' if ticker else 'unknown'}
 if ticker:x['ticker']=ticker
 if subject:x['is_subject']=True
 return x
d['chain_map']={'theme':'AI服务器内存接口、模块供电及可许可半导体IP；DDR5/LPDDR6与HBM逻辑不同','layers':[
 {'layer':'downstream_reference','nodes':[node('AI/通用服务器与内存模块客户','带宽、功耗及可靠性要求；不假定具体独占合同')]},
 {'layer':'midstream_system','nodes':[node('Micron','LPDDR6 SOCAMM2生态引言是需求/验证线索，不是向Rambus量产采购承诺','MU')]},
 {'layer':'midstream_component','nodes':[node('Rambus Inc.','RCD/PMIC及内存/互连/安全IP；设计、授权、销售而非前道设备','RMBS',True),node('Renesas Electronics','DDR5 RCD/PMIC等真实替代供应商；需逐产品认证比较','6723.T')]},
 {'layer':'upstream_material','nodes':[node('外部晶圆制造、封装与测试','Fabless制造投入和客户资格认证依赖；未具名份额/交期UNKNOWN，不虚构本轮供应商')]}
]}
d['chokepoint_of_chokepoint']={'statement':'假设关键层是高速度接口/供电设计、客户认证与IP可复用性；独占制造产能、不可替代认证和涨价权未被本轮证据确立。NOT_ESTABLISHED。','node':'内存接口芯片设计与平台资格认证','status':'hypothesis','evidence_ids':['E-PRIMARY-PRODUCT','E-PRIMARY-RENESAS','E-LIVE-DOC-01']}
d['archetype_hits']=[{'archetype':'ARC-SOLE-SOURCE','applies':'no','why':'公司对外部制造的集中依赖不证明公司自身独占供给；Renesas竞品反驳无替代叙述。','evidence_ids':['E-LIVE-DOC-01','E-PRIMARY-RENESAS']}]
d['gates']={
 'real_bottleneck':{'status':'partial','why':'接口/供电的架构用途成立，已有产品收入；物理短缺、独供及经济定价权NOT_ESTABLISHED，不能给pass。','evidence_ids':['E-LIVE-SEC-01','E-PRIMARY-PRODUCT','E-PRIMARY-RENESAS']},
 'pre_institutional':{'status':'unknown','why':'没有经过充分核实的机构持股/覆盖变化和一致预期分布，13G/13D索引不是尚未被发现的证明。','evidence_ids':['E-LIVE-SEC-07','E-LIVE-SEC-08']},
 'cheap_derisked':{'status':'partial','why':'85.73对基准现值约93.56缓冲有限，压力现值约37.74；财报与竞争、现金兑现风险尚在。未来终值120不等于今天现值，不称便宜且已去风险。','evidence_ids':['E-LIVE-QUOTE','E-LIVE-SEC-01','E-AUTHOR-SCENARIOS']}}
d['gates']['cheap_derisked']['why']+='TTM净利239.680m较229.105m仅+4.62%；基准EPS4从TTM约2.18需约32%CAGR/2.2年并达40%净利率。85.73在30x/12%尺下隐含2028EPS约3.665，已在定价增长，不是低增长便宜股。'
details={
 'material_agreement_8k_1_01':('yes','8/4 ASR协议、8/5披露100百万预付及初交796千股；是回购现金流而非新经营订单，最终回购总数和当前股本未知。',['E-LIVE-SEC-04']),
 'beneficial_owner_filings':('unknown','已见13G/A与13G条目，但本轮未完整读持股人及比例，不声称机构新发现或未发现；不为该未知生成绿色结论。',['E-LIVE-SEC-07','E-LIVE-SEC-08']),
 'insider_form4_activity':('unknown','Form4条目不能单凭数量区分P购买与S销售、授予或税款结算；未作内部人看好论据。',['E-LIVE-DOC-01']),
 'supply_concentration':('yes','Fabless依赖外部制造与客户认证，依赖单一来源不等于自身独供；须同时监控竞争器件替换。',['E-LIVE-DOC-01','E-PRIMARY-RENESAS']),
 'capacity_language':('unknown','本轮没有可验证的RMBS产能利用率、不可取消订单与交期数据；销售增长不单独证明供给受限。',['E-LIVE-SEC-01']),
 'drawdown':('yes','10/22收85.73/-7.62%，日低85.01；SOXX同日-6.79%。共同调整不证明经济论点破裂，也不能取消项目独立风险规则。',['E-LIVE-QUOTE','E-MARKET-CONTEXT'])}
d['red_flags']=[{'flag':k,'severity':'watch','triggered':v[0],'detail':v[1],'evidence_ids':v[2]} for k,v in details.items()]
d['red_flags'] += [ {'flag':'DOJ_subpoena','severity':'watch','triggered':'yes','detail':'DOJ subpoena已在Q1披露，非10/22突发新事件；潜在损失无法估计，专业服务费约增7百万不能全部归因DOJ。','evidence_ids':['E-LIVE-SEC-02','E-LIVE-SEC-01']}, {'flag':'cash_conversion','severity':'watch','triggered':'yes','detail':'6M CFO144.458百万同比-15.9%，库存与营运资本增加。Q2标准FCF52.178百万/含分期无形资产支付49.008百万，SBC不是免费，仍检验每股现金兑现。','evidence_ids':['E-LIVE-SEC-01']}]
cur=d['valuation']['current'];cur.update(price=85.73,shares_outstanding=108461603,price_as_of='2026-10-22T20:00:00Z',shares_as_of='2026-06-30T00:00:00Z',evidence_ids=['E-LIVE-QUOTE','E-LIVE-SHARES'])
cur.pop('net_debt',None)
cur['share_count_note']='6/30已报common，不冒充10/23实际股本；Q2加权diluted109.977m，ASR最终结算未知，场景future110m。'
d['valuation']['ruler']='chokepoint_comparable'
dil=110000000/108461603-1
d['valuation']['scenarios']=[]
for name,eps,pe,rev in [('bear',2.2,22,900000000),('base',4,30,1100000000),('bull',6,36,1500000000)]:
 d['valuation']['scenarios'].append({'name':name,'label':'hypothesis','horizon_years':2.195756,'assumptions':{'revenue':rev,'net_margin':eps*110000000/rev,'multiple':pe,'multiple_basis':'pe','dilution_pct':dil},'implied_market_cap':0,'implied_per_share':0,'vs_current_pct':0,'assumption_sources':['E-LIVE-SEC-01','assumption:2028 EPS2.2/4/6 times PE22/30/36, future110m diluted, not guidance'],'narrative':f'作者2028归母EPS{eps}美元，归母净利{eps*110:.1f}百万，收入{rev/1e6:.0f}百万，PE{pe}倍；利润已含持续SBC/税/利息，不再加净现金或扣第二次稀释。原生输出是2028终值，另用12%和固定2.195756年折现，非当日参与指令。'})
d['valuation']['comparables']=[{'ticker':'6723.T','note':'Renesas DDR5接口/供电真实竞品；本轮未做其财务估值，不声称更便宜或已通过。','evidence_ids':['E-PRIMARY-RENESAS']}]
d['leading_signals']=[{'signal':'内存接口芯片产品收入与资格认证','type':'filing','confirms_if':'产品增长伴毛利和每股现金改善，新PMIC由抽样进入获证量产','refutes_if':'主要客户取消认证、竞争替代，产品收入连续下滑','next_check':'2026-10-26 results / 2026-10-27 call'}, {'signal':'现金转换和资本分配','type':'filing','confirms_if':'营运资本释放且FCF支持SBC及资本分配，ASR结算股数明确','refutes_if':'CFO继续落后且库存/应收恶化，回购减少现金却不改善每股捕获','next_check':'2026-10-26'}]
d['osint_leads']=[]
d['red_team']={'not_real_bottleneck':'Renesas等可提供RCD/PMIC替代器件，客户可以多源认证；模块需求与设计难度不证明RMBS不可替代或供给约束。','not_monetized':'Q2盈利和产品收入已有兑现，但授权确认不等于现金royalty，6M CFO下降且SBC、营运资本会削弱每股现金回报。','already_priced':'以85.73对作者2028基准EPS4与30倍PE贴现约93.56，缓冲有限；若增长已被资本化，利润上修不足以抵消倍数下降。','better_alternative':{'ticker':'6723.T','why':'Renesas是真实DDR5接口与供电替代来源，应核认证/功耗/客户量产比较；本轮未证明其股票更优。'},'biggest_kill_shot':'内存客户通过竞争产品或自研完成新代认证，RMBS每模块价值/份额下降；叠加许可收入现金收取落后，2028 EPS4在持续SBC后无法兑现。'}
d['falsification']=[{'condition':'作者基准现金转换复核阈值：若单季经营现金低于40百万，触发重新承销而非自动证明破产；阈值为作者风险检验。','machine_checkable':True,'metric':'quarterly_operating_cash_flow_USD','operator':'<','threshold':40000000,'check_by':'2026-10-27','exit_rule':'PB-EXIT-03'}, {'condition':'关键客户认证取消或被竞品替代且管理层实质下调中期利润；需原披露，不能用价格下跌替代。','machine_checkable':False,'check_by':'2026-10-27','exit_rule':'PB-EXIT-01'}]
d['serenity_view']={'would_he_care':'maybe','why':'按框架先看已盈利接口芯片/IP的设计和认证价值，再核物理瓶颈与每股现金。抽样/合作不当订单（例外9）；需求不等于利润率（例外12–15）；ASR与SBC分开核（例外1）。股价回落本身不证明经营失败（例外17），但不能覆盖本项目独立保护。','playbook_rules':['PB-FIT-01','PB-CORE-01','PB-LAW-08']}
d['research_tier']='amber';d['tier_reason']='产品/IP捕获有财报支持，但物理独占、机构预期差与充分安全边际未确立；2028利润增长尚为作者情景，非green。'
d['rerate_triggers']=['10/26财报产品增长同时转化到毛利、经营现金及完全稀释EPS','LPDDR6 SOCAMM2 PMIC从抽样进入可核客户量产并有经济贡献','ASR最终结算及持续SBC后的每股现金捕获可量化']
d['framework_fit']={'role':'chokepoint','fit':'partial','rationale':'有架构必需接口功能和IP复用，但RMBS独占性/物理供给瓶颈NOT_ESTABLISHED，不能沿用错误设备图强fit。','rule_ids':['PB-FIT-01']}
d['bottleneck_status']={'status':'unknown','kind':'demand','rationale':'需求增长有收入支持，供给短缺、独供、份额与提价权未有充分一手证据，不把Q2增长改称物理卡点。','evidence_ids':['E-LIVE-SEC-01','E-PRIMARY-RENESAS']}
d['phase']={'stage':'steady_state','evidence':'公司已有持续产品/IP收入和盈利；新LPDDR6 PMIC仅sampling子项目，不把整个RMBS当亏损放量故事。','evidence_ids':['E-LIVE-SEC-01','E-PRIMARY-PMIC'],'kpis':[{'kpi':'每股现金转换','status':'behind','note':'6M CFO同比-15.9%，不能被净利增长覆盖。','evidence_ids':['E-LIVE-SEC-01']},{'kpi':'LPDDR6 SOCAMM2 PMIC量产','status':'not_started','note':'公开披露抽样中，Micron引言不是采购单。','evidence_ids':['E-PRIMARY-PMIC']}]}
d['purity']={'exposure_pct_estimate':None,'basis':'unknown','rationale':'Q2产品99.2百万占总收入约47.8%，其余IP/服务也有内存关联但AI专属敞口未单列；不将47.8%伪称纯AI比例。'}
d['purity']['rationale']+='精确产品99.154m/royalties84.261m/contract23.970m约48/40/12%。产品主要客户Micron/Samsung/SKhynix及系统/云；前五客户Q2占60%/H1占64%，不伪造逐笔不可取消订单。'
d['verify_checklist']=[{'item':'收入/利润/现金/SBC及股数期间','status':'ok','note':'Q2/6M分别列明，详FINANCIAL_BRIDGE，不把Q2现金当6M。','evidence_ids':['E-LIVE-SEC-01']},{'item':'ASR及当前总股本','status':'pending','note':'8/5已读100百万预付与初交796千股；最终结算未知，用future110m缓冲，非已确认实际股数。','evidence_ids':['E-LIVE-SEC-04']},{'item':'客户逐笔订单及前五长约/可取消比例','status':'pending','note':'本轮未充分取得逐笔合同，保留UNKNOWN；不作独供或确定放量论据。','evidence_ids':['E-LIVE-DOC-01']}]
d['dilution']={'class':'none','share_count_yoy_pct':None,'per_share_growth_covers':'unknown','use_of_funds':'不是已发现ATM融资；ASR是公司现金回购','detail':'none仅指本轮已读材料没有可据以认定的新股融资，不代表零SBC。6/30common108.461603m→future110m约1.418%作者稀释；Q2diluted109.977m；ASR初交不推断当前股数。','evidence_ids':['E-LIVE-SEC-01','E-LIVE-SEC-04']}
d['variant_perception']={'consensus':'可靠实时机构一致预期/渠道订单共识UNKNOWN；不能把股价或旧社交背景当完整市场盈利预期。','consensus_sources':['assumption:institutional consensus unavailable, no unsupported street EPS claimed'],'our_view':'作者基准2028 EPS4、110百万股和30倍PE现值约93.56，较85.73仅有限空间；产品47.8%收入占比不等于AI纯度。','reason_codes':['PB-VP-01'],'when_market_sees':'2026-10-26财报及10/27电话后检验现金/产品指引，不预判发布结果。','first_number_to_prove_wrong':{'metric':'quarterly_operating_cash_flow_USD','operator':'<','threshold':40000000,'check_by':'2026-10-27'},'what_changed_since_archive':'10/22公司公布ChipAgents合作且投资，金额/收益未披露；10/13新PMIC仍抽样，不能填入量产净利；10/22市场收盘只用于当期估值比较。'}
d['next_hop_picks']=[{'ticker':'6723.T','name':'Renesas Electronics','relation':'peer','node':'DDR5接口/PMIC','why':'真实替代产品，必须比较功耗、验证和商业份额；不是错误VECO设备同业。','basis':'author_lead','verify_first':'完整客户认证与产品收入口径，不将候选直接升级通过。'}]
d['audit_link']['bundle_validated']=False
fb=B/'FINANCIAL_BRIDGE.json'
if fb.exists():
 f=json.loads(fb.read_text())
 d['financial_period_bridge']={'source':str(fb),'TTM_to_June30_USDm':f['financial_periods']['TTM_to_2026_06_30'],'balance_June30_USDm':f['balance_20260630'],'warning':'TTM uses FY25+H126-H125; prior pack230.010mNI/365.814mCFO wrong-period replaced. Not standaloneforecast.'}
 cur['net_debt']=-774963000
 cur['net_debt_definition']='June30 cash+securities824.948m minus EDA28.182m and operatingleases21.803m; conventional fundeddebt absent, debtlike49.985m; not currentASR-adjustedcash. PE does not add netcash.'
 d['verify_checklist'].append({'item':'F-FACT/F-TIMING复核','status':'ok','note':'已纠正设备同业误分类、错期TTM、ASR推断；抽样不当订单，10/26为明确复核点，未用方向正确无限后移。','evidence_ids':['E-LIVE-SEC-01','E-LIVE-SEC-04','E-PRIMARY-PMIC']})
e={x['evidence_id']:x for x in d['evidence']}
e['E-LIVE-QUOTE'].update(title='Nasdaq RMBS Oct22 regular close85.73 O88.09 H90.50 L85.01',locator='https://api.nasdaq.com/api/quote/RMBS/info?assetclass=stocks',retrieved_at=now)
e['E-LIVE-SHARES'].update(title='10Q common108461603 June30; Q2weighted diluted109977000, distinct measures',locator=e['E-LIVE-SEC-01']['locator'],published_at='2026-07-28T00:00:00Z',period_end='2026-06-30T00:00:00Z',retrieved_at=now)
e['E-LIVE-FIN'].update(title='Q2 SEC revenue207.385m/NI67.605m/SBC15.886m; 6M CFO144.458m',locator=e['E-LIVE-SEC-01']['locator'],published_at='2026-07-28T00:00:00Z',source_type='filing',available_basis='SEC filingdate primarydocument independently read',retrieved_at=now)
new=[('E-PRIMARY-PRODUCT','Rambus RCD/PMIC memoryinterface product architecture','https://www.rambus.com/memory-interface-chips/','company_release',now),('E-PRIMARY-RENESAS','Renesas DDR5 competing RCD/PMIC products','https://www.renesas.com/en/products/memory-logic/memory-interface-products/ddr5-solutions','company_release',now),('E-PRIMARY-PMIC','Oct13 LPDDR6 SOCAMM2 PMIC sampling; Microncomment notpurchaseorder','https://www.rambus.com/rambus-advances-power-efficient-ai-infrastructure-with-industry-leading-pmic-designed-for-lpddr6-socamm2/','company_release','2026-10-13T00:00:00Z'),('E-PRIMARY-CHIPAGENTS','Oct22 ChipAgents collaboration/investment; amount not disclosed','https://www.rambus.com/rambus-and-chipagents-collaborate-to-accelerate-chip-design-with-agentic-ai/','company_release','2026-10-22T00:00:00Z'),('E-PRIMARY-CALENDAR','Company notice Oct26 14:00PT Q3call, BeijingOct27 05:00','https://www.nasdaq.com/press-release/rambus-announce-third-quarter-fiscal-year-2026-results-2026-10-05','company_release','2026-10-05T00:00:00Z'),('E-AUTHOR-SCENARIOS','Author frozen EPS/PE/revenue/share sensitivity; not guidance',str(B/'present-values.json'),'analysis',now),('E-MARKET-CONTEXT','Oct22 SOXX-6.79%,QQQ-2.86%; marketdata no businessproof',str(B/'public/INFO_SOXX.json'),'market_data','2026-10-22T20:00:00Z')]
for eid,title,url,typ,pub in new:e[eid]={'evidence_id':eid,'title':title,'locator':url,'source_type':typ,'published_at':pub,'retrieved_at':now,'provenance_note':'root supplied independently read primary content; local financial/source receipts in same researchdir. Undatedproduct pages time is observation, not claimed publication date.'}
d['evidence']=list(e.values())
snapshot=B/'snapshots/RMBS.json';d['live_data']['snapshot_path']=str(snapshot);d['live_data']['retrieved_at']=now
handling={
'share_count_older_than_200_days':'原3/31股数过期警告保留；10Q正文刷新6/30common108.461603m，Q2加权diluted109.977m另列。ASR最终当前股数未知，不直接扣796k。',
'financials_from_fallback':'原Yahoo fallback已由Q2 SEC正文逐项核对替代；非GAAP、现金流期间与来源差异均保留，不沿用aggregator作为决定性证据。',
'sec_stale_series_dropped':'2023债务序列陈旧，不沿用。6/30传统银行/债券/可转债无余额，但EDA28.182m+运营租赁21.803m共49.985m；债务类敏感口径净现金774.963m。PE不另加。',
'net_debt_unknown':'原未知警告保留并修正：按6/30现金824.948m减EDA及运营租赁49.985m，net_debt=-774.963m；不是当前ASR后现金。PE已含利息，不重复加现金/扣债。'}
handling.update({
'post_ASR_actual_common_and_current_cash_not_disclosed':'已读8/5 ASR协议100m预付与初交796k，未有最终总股本/现金更新；保持6/30common108.461603m且未来110m作者缓冲。不以当前价反推回购股数，不同时保留全部旧现金和完成回购的分母利益。',
'reported_share_date_differs_from_quote_date':'85.73为10/22常规收盘，108.461603m为6/30已报common；计算市值是混日期示意非实时总股本。Q2加权diluted109.977m单列，未来110m只在情景分母应用一次。',
'debt_includes_EDA_and_operating_lease_sensitivity':'6/30传统借款无余额不等于无负债：EDA28.182m及运营租赁21.803m计入debt-like49.985m。netdebt=-774.963m为敏感口径；EPS×PE不再加净现金。',
'cash_conversion_H1_CFO_down15_9pct':'H1 CFO144.458m同比-15.9%，库存现金占用30.738m及deferred revenue减少8.241m，确有现金转换反证。Q2FCF52.178m，含installment49.008m；TTM299.535/286.445m，不用错期365.814mCFO掩盖。',
'DOJ_investigation_known_since_Q1_unquantified_tail_risk':'已比Q1/Q2正文，Q1开始回应DOJ刑事反垄断调查subpoena，未量化损失不等于零。保留尾部风险、不认定有罪、不冒充10/22新二元事件；专业费+7m不能全部归因DOJ。'})
warnings=[x['warning'] for x in d['live_data']['warnings_addressed']]
if snapshot.exists():warnings+=json.loads(snapshot.read_text()).get('warnings',[])
d['live_data']['warnings_addressed']=[{'warning':w,'handling':next((v for k,v in handling.items() if w.startswith(k)),'保留此快照不利标记；需结合FINANCIAL_BRIDGE逐项核对，不能作已排除风险或绿色证明。该项未解析完整时保留UNKNOWN。')} for w in dict.fromkeys(warnings)]
(B/'lens.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('lens built',now,'TODO unresolved',str(d).count('TODO:'))
