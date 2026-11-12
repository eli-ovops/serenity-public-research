import json
from pathlib import Path
P=Path(__file__).resolve().parent
read=lambda n:json.loads((P/n).read_text())
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2))
d=read('final_decisions.json');c=read('latest_material_corrections.json');cm=read('complex_models.json')
def note(t,text,urls):
 old=c.get(t,{'text':'','urls':[]});old['text']+=' '+text;old['urls']=list(dict.fromkeys(old['urls']+urls));c[t]=old
note('CAMT','Q2调整净利39.448百万减持续SBC4.873百万为34.575百万；保留收购摊销时更低，不能直接使用0.78 EPS。H1/Q2稀释股数为51.433/51.520百万而不是5万股。未来2028基准EPS5.6对应约54百万股、302.4百万归母净利；按30%净利率须约10.08亿美元收入，比2026 H1的254.9百万显著提高，是有风险的作者增长假设。当前价即使对该假设仍高于估值上限，故按价格排除；可转债不把总现金直接加回。',['https://www.sec.gov/Archives/edgar/data/1109138/000117891326003975/zk2635905.htm','https://www.camtek.com/investors/'])
note('HSAI','2029基准归母经营净利为11亿美元收入×12%=1.32亿美元；较Q2近盈亏平衡需明显运营杠杆。净现金650百万是扣未来消耗后的作者假设，相对当前约10亿美元流动性有缓冲；175–190百万未来ADS高于8月约157.142百万ADS等价股数。IR新闻/事件与9月17日中报、9月8日月报核对，未发现未来24小时已排期重大公司二元事件。价格15.52高于本轮模型基准及约14.63上限；不因Q2净利转正就年化。',['https://investor.hesaitech.com/','https://www.sec.gov/Archives/edgar/data/1861737/000110465926108451/tm2625559d1_ex99-1.pdf'])
note('NOK','完整Q2报告现已读取：H1 CFO162百万欧元、资本开支266百万，FCF负104百万；Q2 FCF负732百万，2026重组现金流出700–800百万。净现金2776百万不等于所有者当期盈利；Network Infrastructure Q2收入2037百万、经营利润166百万，传统Mobile仍为2680百万收入。2025年报核实1 ADS=1普通股。基准EPS0.45欧元×18倍经折现及1.10汇率假设约6.90美元；即把净现金按约58亿股粗略全加回，仍不足当前10.36。业务可能增长不等于当前价安全。',['https://www.nokia.com/newsroom/nokia-corporation-report-for-q2-and-half-year-2026/','https://www.nokia.com/system/files/2026-03/nokia-annual-report-2025.pdf'])
note('Lenovo','已读取完整Q1及9月14日债券转换公告。Q1 CFO382.301百万美元，扣PPE91.009、在建工程115.183、无形资产168.018后仅8.091百万，未扣租赁和并购。2029旧债已全部转股/注销；2028 CB转换价9.37港元，最多约16.67亿股；认股权证11.51港元、最多12.299亿股；2033 CB转换价35.74港元。未来股本修正为160/170/180亿股，不能沿用无稀释的124亿股。即采用当前基础124.047亿股且假定不发生任何未来稀释，基准现值约22.8港元，仍低于35.48；未来权证现金也不能把当前低价转股视作无成本。',['https://doc.irasia.com/listco/hk/lenovo/interim/2027/int1q.pdf','https://doc.irasia.com/listco/hk/lenovo/announcement/a260914.pdf','https://doc.irasia.com/listco/hk/lenovo/announcement/a260723b.pdf','https://doc.irasia.com/listco/hk/lenovo/announcement/a260723c.pdf'])
cm['Lenovo']['shares_m']=[16000,17000,18000];cm['Lenovo']['basis']='完整Q1及2028/2033 CB与认股权证已核。未来160/170/180亿股为作者稀释情景；净利润含利息、税、SBC，USD/HKD=7.8假设，净现金不另加。旧债2029已全部转股/注销；即不计进一步稀释仍不足现价。'
cm['SIVE']['basis']=cm['SIVE']['basis'].replace('当前完全稀释股数仍待核，情景股数为融资假设，不是已发行事实。','8月13日公告已发行356.740332百万股；390–480百万为未来融资稀释情景，不是当前已发行事实。')
cm['SOI']['basis']=cm['SOI']['basis'].replace('未来财务净债务桥接仍需验收。','即把募集500百万全当无偿现金加回，基准仍低于现价；正式估值不重复加现金。')
for t in ['CAMT','HSAI','NOK','Lenovo']:
 d['incomplete'].pop(t,None)
 if t not in d['valuation_exclude']:d['valuation_exclude'].append(t)
# 财务桥已补齐，不再保留旧的两项缺口。
d['incomplete'].pop('NVT',None)
d['conditional']['NVT']={'gap':'近期IR活动/新闻的当前完整列表无法从动态页面直接读出，未来24小时事件有限核查尚差这一条交叉证据。','cap':162,'owner':'current_thread_direct','deadline':'2026-10-01T09:00:00+08:00','path':'SEC重大融资及Maverick公告已读；用公司可读活动列表或发行人新闻联合核对，无新增重大二元事件即可闭合，不把动态页面故障当公司有风险。若仍受阻，明确证据管线受阻并降为未完成。','event_url':'https://investors.nvent.com/press-releases/default.aspx','event':'9月29日债券完成，6.15%票息；Maverick交易仍须交割，outside date为11月20日可延至2027年2月19日。不是9月30日已知排期交割。IR列表动态框架未完整显示，保留唯一事件缺口。'}
note('NVT','收购利息桥为作者预算：Maverick 2026收入700百万，1750/11.5约152.2百万调整EBITDA；800百万债券×6.15%+600百万定贷×假设6%+250百万循环借款×假设6%=100.2百万年息。再扣20百万D&A、25%税后约24百万新增利润，按160百万股约0.15 EPS，不能把全部EBITDA当增厚。2028 EPS8需原业务增长及收购后运营改善；最高550百万earnout另作未来资本负担，基准不假定新增回购。当前新增利率并非所有余额已实借，计算是全额融资压力预算。',['https://investors.nvent.com/press-releases/press-release-details/2026/nVent-to-Acquire-Maverick-Power/default.aspx','https://www.sec.gov/Archives/edgar/data/1720635/000110465926111938/tm2626249d1_8k.htm'])
d['incomplete'].pop('ASMPT',None)
d['conditional']['ASMPT']={'gap':'本币日线已取得，但相对香港本地市场的同窗走势尚未完成核对；不能拿港币收益直接减美元QQQ。','cap':163,'owner':'current_thread_direct','deadline':'2026-10-01T18:00:00+08:00','path':'用港交所/恒指公司或同源恒指已结束交易日日线补齐同窗相对强度；轻微落后不是硬否决，只检查广泛市场是否失控及走势是否与论点明显冲突。','event_url':'https://www.asmpt.com/en/investor-relations/announcements-circulars/tc/','event':'8月中报、员工奖励及9月1日8月月报已核；最新披露入口未显示未来24小时已排期重大二元事件，保留未披露风险。'}
note('ASMPT','已读取完整中报：H1 CFO727.255百万港元，扣PPE131.216、预付PPE5.518、融资分类利息75.070和租赁109.088后为406.363百万；NEXX出售492.335百万属于投资现金流，不冒充经营现金。8月月报因字体编码不可读，已渲染第2页人工核实发行股数419,408,233、月内零变化、库存股零。2028 EPS8相当约33.6亿港元利润（假设4.2亿稀释股），不是将H1调整EPS直接年化。',['https://www.asmpt.com/site/assets/files/85541/e_00522ir-20260827.pdf','https://doc.irasia.com/listco/hk/asmpt/announcement/ca260901.pdf'])
# CLS 已完成稀释桥；保留现金转换单缺口，避免未证实的加仓结论。
d['incomplete'].pop('CLS',None)
d['conditional']['CLS']={'gap':'扩产、供应商账期和SBC现金结算之后的股东现金转换，尚缺可靠的2027预算桥；不是因为股价上涨而否决。','cap':370,'owner':'current_thread_direct','deadline':'2026-10-02T18:00:00+08:00','path':'以2026公司FCF600百万（不含融资分类SBC结算）、新募资用途及公开扩产预算建立2027压力现金表；已完成股份与TRS纠正。若公开披露仍不能限定回款/资本支出假设，标为估值现金证据未闭合，不继续照抄观察。','event_url':'https://corporate.celestica.com/news-releases','event':'8月7日发行11,129,031股；9月11日CFO交接公告，生效10月1日；10月27日Investor Day在24小时外。SEC及发行人新闻未发现窗口内已知重大二元结果，管理层交接保留普通风险。'}
note('CLS','本轮将原EPS22敏感性下调为2028 EPS19基准，压力11.5、强29。基准可复算桥：380亿美元收入×8.4%含持续SBC经营利润率，减约1.04亿美元净利息，再乘80%税后/1.30亿稀释股，约19；未来1.30亿高于6月1.15亿基础股加新发1112.9万股。新募资约33.9亿美元补流动性但不作为利润，亦不重复加到PE估值。H1公司FCF285百万减融资类SBC现金结算326.3百万为负41.3百万，这是股东现金压力口径，不代表GAAP FCF错误；后续回款尚须完成预算。',['https://corporate.celestica.com/news-releases/news-release-details/celestica-announces-second-quarter-2026-financial-results','https://corporate.celestica.com/news-releases/news-release-details/celestica-completes-equity-offering','https://www.sec.gov/Archives/edgar/data/1030894/000110465926107079/tm2625204d1_8k.htm'])
# 更新过期叙述，不留下已经补齐但仍称缺失的矛盾。
p=P/'valuation_assumptions.psv';s=p.read_text();s=s.replace('CLS|13,22,35|','CLS|11.5,19,29|').replace('基准2028 EPS22不照单全收强指引，剔除TRS并保留持续SBC。','基准2028 EPS19按未来1.30亿股、380亿美元收入及含SBC利润率重算；现金转换仍为唯一待补项。').replace('尚须新增利息和Maverick现金流桥接，不可直接作买价。','新增利息桥已核为压力预算，2028增长是假设；IR事件交叉核验未完成，不可直接作买价。').replace('ADS单位须核实。','已核1ADS=1普通股。').replace('当前CFO/营运资本和优先股权益桥接未闭合，仅作敏感性。','FY26末Series B已为零，稀释股与新融资已核；经营现金弱，增长仍是敏感性。').replace('优先股/转换稀释仍须完整核对。','稀释来源已核：基本89.7百万股之外仍有优先股、转换及RSU，未来股数压力约106百万。');p.write_text(s)
p=P/'analyst_notes.psv';s=p.read_text().replace('新增可转债条款未核清前，历史净债务模型失效。','新增可转债转换价206.46、0.5%票息及潜在约242万股稀释已核，使用更新后模型。').replace('但融资与资本开支表未完整验收。','融资与资本开支已补核；现金仅1.3万美元不能脱离授信余额解读。').replace('完整股数待核。','未来股数使用高于已发行的稀释情景。').replace('最新Q2全文与合并现金流未闭合。','最新Q2全文及ADS比例已核，重组现金与光网络增量分开。').replace('目前UNKNOWN。','以新核CB/权证条款修正未来股本情景。').replace('股价及长期量价待同源校对。','本币日线已核，仍待本地市场相对强度比较。');p.write_text(s)
save('final_decisions.json',d);save('latest_material_corrections.json',c);save('complex_models.json',cm)
print('pass',len(d['pass']),'conditional',len(d['conditional']),'exclude',len(d['valuation_exclude'])+len(d['hard_exclude']),'incomplete',len(d['incomplete']))
