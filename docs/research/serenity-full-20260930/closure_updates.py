import json
from pathlib import Path
P=Path(__file__).resolve().parent
def r(n):return json.loads((P/n).read_text())
def w(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2))
d=r('final_decisions.json');c=r('latest_material_corrections.json')
updates={
'COHR':('年报EPS附注已核：FY26稀释股数195.387百万，含Series B转换影响12.419百万；6月末Series B已发行股为0，不能继续说全部优先股未核。FY26 CFO79.514百万、资本支出1102.909百万，增长现金消耗仍是风险。按已含转换的EPS做2028基准10、PE28的现值216.98，当前292.21需要超出基准的兑现；不靠把全部融资现金加值证明便宜。','https://www.sec.gov/Archives/edgar/data/820318/000082031826000066/cohr-20260630.htm'),
'LITE':('年报已核8月14日普通股89.7百万，另有约2.9百万NVIDIA优先股一对一转换及FY26反稀释的转换/激励证券。以106百万未来股数作压力桥，相对于89.7百万约增加18%；原EPS20不能当保守基准。CFO751.4百万减Capex451.3百万为300.1百万，不能支持当前价格已隐含的利润而不依赖后续大幅成长。原三景仅敏感性，当前价相对基准过高。','https://www.sec.gov/Archives/edgar/data/1633978/000163397826000044/lite-20260627.htm'),
'ACMR':('Q2稀释股数71.839百万、H1为70.679百万；持有ACM Shanghai约73.2%。基准EPS3按上市主体归母规范化盈利，剔除投资收益，不把合并利润全归母。即使把现金969.229百万、定存365.055百万与短投105.091百万不扣债务地乘73.2%再除74百万股，额外上界仅约14.24美元，基准39.43加此宽松上界仍低于现价75.61；此上界不是可分配现金事实。','https://www.sec.gov/Archives/edgar/data/1680062/000168006226000021/acmr-20260630.htm'),
'DPC':('H1 CFO−34.0百万、设备支出19.8百万，FCF−53.8百万；D&A14.8百万。以2028 EBITDA350减持续激励25、折旧/维护资本代理55、利息8，税率25%、155百万股、28倍PE及13%折现2.25年交叉算得约26.96美元，与EV法27.93接近。以上均作者假设；净现金上下100百万只影响约0.49美元，不足以填补现价41.46与基准差距。','https://ir.doncasters.com/news-and-events/news/news-details/2026/Doncasters-Completes-Debt-Refinancing/default.aspx'),
'SIVE':('8月13日官方公告：权证行权新增1,659,015股，合计356,740,332股。2029模型390/430/480百万股包含未来融资，不是假称当前股数。即使强情景改为完全不新增股、仅使用356.740百万股，强价值约20.74SEK，仍低于31.86；有新量产订单/利润证据才能上修，12亿美元管道不能代替已签订单。','https://www.sivers-semiconductors.com/press/bootstrap-exercises-warrants-in-sivers-semiconductors/'),
'SOI':('已核5亿欧元ORNANE转换价206.46和潜在6.3%全股转换稀释。基准40百万股未给新债现金额外价值；即使宽松地把新增5亿全部当免费现金加在2029基准，现值也只增加约7.94欧元，104.00升至约111.94，仍低于155.50。排除依据为该估值情景过贵，而非债券条款缺证。','https://www.soitec.com/home/investors'),
'ESMT':('已核9月10日第二次有担保可转债转换价308.0台币、溢价102.44%。转换价不再属于未核项；发行总额、股数与最新现金/库存周转仍需合并复核，不把半年EPS翻倍年化。','https://www.esmt.com.tw/tw/press-room/2026091001?category=investor-Info'),
'ASMPT':('已读2026中报现金流：H1 CFO727.255百万港元，设备购置131.216百万及预付5.518百万；减另列融资流利息75.070百万、租赁109.088百万后约406.363百万。出售NEXX净收492.335百万在投资现金流，未计经营FCF。H1持续经营稀释EPS1.78，调整2.34不直接年化；当前净现金36.3亿港元。','https://www.asmpt.com/site/assets/files/85541/e_00522ir-20260827.pdf'),
'NVT':('Maverick2026收入估计700百万美元，17.5亿对11.5倍调整EBITDA隐含约152.17百万EBITDA；另有最高550百万现金或有对价。作者按800百万票息6.15%+600百万贷款6%+250百万循环6%测利息100.2百万，再减D&A20百万和25%税，增量利润约23.98百万，约0.15美元/股（160百万股假设），不能把全部EBITDA当EPS。正式归母模型及或有对价仍需对照交割披露。','https://investors.nvent.com/press-releases/press-release-details/2026/nVent-to-Acquire-Maverick-Power/default.aspx'),
'ON':('Synaptics交易为约70亿美元EV全股票交易，每SYNA股换1.350股ON；尚不能用单体Q2 EPS直接代表合并后股东权益。收购公告标题Acquires不代表已交割，仍核审批和换股。','https://investor.onsemi.com/news-releases/news-release-details/onsemi-acquire-synaptics-enable-next-generation-intelligent'),
'HSAI':('9月证券月报：A股215990888、B股1041146800，按1ADS=8普通股折合157.142百万ADS（含为激励预发给存托行股份，不能与期权全额重复相加）。未来175–190百万ADS留稀释。H1 CFO−15.115百万美元、设备和无形支出21.876百万，受限现金1.982百万；报告现金储备含短投/定存，并非全为银行现金。','https://www.sec.gov/Archives/edgar/data/1861737/000110465926108451/tm2625559d1_ex99-1.pdf')
}
for t,(text,url) in updates.items():
    old=c.get(t,{'text':'','urls':[]});old['text']+=' '+text
    # SEC paths come from stored manifests, never assume an accession number.
    if t in ['COHR','LITE','ACMR']:
        items=r('supplement_manifest.json');url=next(x['url'] for x in items if x['ticker']==t)
    old['urls'].append(url);c[t]=old
for t in ['COHR','LITE','ACMR','DPC','SIVE','SOI']:
    if t in d['incomplete']:del d['incomplete'][t]
    if t not in d['valuation_exclude']:d['valuation_exclude'].append(t)
d['incomplete']['ESMT']=['现金流与库存/采购质量','可转债总额到完全稀释股数和最新公司事件的桥']
d['incomplete']['HSAI']=['转盈经营利润率与当前估值的桥','最新IR未来事件核对']
d['incomplete']['ASMPT']=['最新证券变动及当地市场相对强度核对']
# Do not disguise a remaining single gap as conditional until every other gate is explicitly reviewed.
w('latest_material_corrections.json',c);w('final_decisions.json',d)
ss=r('supplement_status.json')
if not any(x.get('path')=='primary/300_ASMPT.txt' for x in ss):ss.append({'ticker':'ASMPT','url':updates['ASMPT'][1],'title':'2026 H1中报现金流及权益全文','path':'primary/300_ASMPT.txt','ok':True,'retrieved_utc':'2026-09-30T09:11:00Z'})
w('supplement_status.json',ss)
