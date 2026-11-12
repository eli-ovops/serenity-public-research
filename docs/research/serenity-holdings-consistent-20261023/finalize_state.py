"""Integrate approved research into the sole current state; retain prior snapshots."""
import json, datetime
from pathlib import Path
P=Path(__file__).resolve().parent
STATE=P.parents[1]/'当前状态与开放循环.md'
data=json.loads((P/'DECISIONS.json').read_text())
for c in data['cards']:
 if c['symbol']=='POET':
  c['protection']['milestone_deadline']='公司Q2原文是2026剩余季度为资格认证交付实质生产单元，不是承诺全面商业量产。12/31窗口结束若仍无足以支持该实质出货的公开证据且无事前已承销的明确替代日期/现金安排，2027首个正常交易时点现剩10或5→0，属于有限等待/证据风险退出；不把查询不到说成确认未出货。新重大事实仍可更早退出。'
 if c['symbol']=='DPC':
  c['source_limits']='本轮SEC200无9/8后新增；发行人Q2完整经营/现金/股本表200实读。IR新闻索引为Loading动态壳，未称列表读全；发行人BusinessWire原声明经Yahoo分发页本轮200实读，原source链接https://www.businesswire.com/news/home/20261020704270/en/，明确11/12盘前及08ET。旧SEC10Q403未重取。不称新买事件门通过。'
 if c['symbol']=='SCTX':
  c['root_profit_execution_clarification']='原25–26无新人体证据的首批减1，在常规有效价达到25生效；跳空高开超过26且无新人体事实仍为同一首批，不因越过窄带遗漏。该执行澄清从本次前瞻生效，不回填历史。'
 for key in ['final_protection','protection','prospective_plan']:
  if isinstance(c.get(key),dict):c[key]['corporate_action_adjustment']='拆股/除权或重大财报/融资改变价量/估值口径时旧图相应维度过期，先调整同口径，不能直接将除权低价当跌破。SOXX11/5拆股提示待发行人核，不冒已核比例。'
(P/'DECISIONS.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
(P/'root_CARDS.json').write_text(json.dumps([c for c in data['cards'] if c['symbol'] in ['DPC','POET']],ensure_ascii=False,indent=2)+'\n')
old=STATE.read_text()
head='# 当前状态与开放循环\n\n'
active='''## 当前有效状态（2026-10-23 全8只同标准复核；确认成交事实仍至10/22）

- **当前决定唯一入口**：[全现仓报告](research/serenity-holdings-consistent-20261023/REPORT.md)、[冻结决定卡](research/serenity-holdings-consistent-20261023/DECISIONS.json)。冻结北京10/23 11:27:46，规则v1.3本轮与恢复后已全文实读。用户本轮只要求全部现仓，不是重新筛74家。所有下方旧RMBS清仓稿均已撤回，不能复活。
- **唯一持仓事实**：**NVDA2、TSM1、CLS1、RMBS1@86.52、RXRX20、DPC1、POET10、SCTX2**；FORM/INOD/TSLA/NVT/CAMT/TEM/AIP为0。未获用户确认NVDA减1或RMBS卖出，事实数量不变。当前NAV/现金/费用UNKNOWN，2760.53及1456是RMBS买前历史；不当当前资金、不查账户。
- **现在需处理**：➖NVDA **2→研究目标1**。10/22常规收212.21<原214，原首批已触发；与此前提前建议是同一股，若用户已卖该1则只留1，不再重复减第二股。不假设已执行。其余7只保留当前确认数量、不加；原承销取舍/同尺模型未因重读旧风险反向清仓。
- **新保护只从现在前瞻生效**：NVDA减后剩1、TSM1、CLS1，分别以股票前20日低212.77／407.13／286.35，且SOXX<489.70，**连续两未来常规收盘同时满足→对应剩余1退出**；从10/23计，不回填10/22，最早10/26收盘确认、下一实际可交易时点处置。DPC剩1两未来收盘<27.82且XLI<164.66→退出；POET10两未来收盘<5.30且SOXX<489.70→同一首批减5留5。不是把单日最低价抄成新硬止损，仍是未证明盈利优势的作者资本保护政策，可能卖飞、延迟确认也会多承受损失。生物医药保留既有阶段/数量与经济条件，不机械套SOXX。
- **反弹/盈利提前减仓**：NVDA剩1到320预警、≥327.48无新盈利/现金改善→卖1；TSM467.82预警、≥470无新每ADS改善→卖1；CLS320预警、≥355.54无新每股现金/利润改善→卖1；DPC28.12预警、≥29.52无新EBITDA/现金/股本改善→卖剩1；POET常规有效价≥5.75且无新付费出货/验收及每股兑现→10→5，剩5到8.20仍无上述改善→0。POET上下两条是同一首批5股，确认后退休，不重复。价格上跳越阈值仍算；重大新材料先到则同次替代图，不凭看多宣传抬价。
- **临床仓及RMBS保护**：RXRX20留20；新增常规价≥5.19且无10/15旧资料以外临床/注册改善→20→10，首批后不重复，重大安全/主要疗效/注册/现金失败时现剩全部→0。SCTX2留2；原常规收<16.70且同日XBI<145，或常规价≥25无新人体证据→同一首批2→1，跳空超过26不漏该批；10/22收17.96/XBI151.64未满足联合条件。RMBS原GARP1保留、常规有效价≤85退出不下移，昨低85.01未触；93.56重审/≥98无更强每股现金盈利→退出。旧无条件清仓已撤回，不因本轮再改口。
- **已知事件明确取舍**：CLS既有1及RMBS既有1允许跨10/26盘后（CLS另10/27 08ET会议/投资者日），均不加事件仓；若原经济/风险先触则退出。两未来收盘确认不能承诺避开10/26盘后跳空。RXRX现20（首批后10）允许跨11/2追加FAP数据，10/30先核；DPC1跨11/12盘前、11/11先核；POET10（首批后5）跨11/16 07ET、11/13先核。SCTX2（首批后1）承担2027H1首批人体数据，6/30后无资料/可信事前替代安排，7/1首个可交易时点剩余退出。POET原承诺是2026剩余季度为资格认证交付生产单元，非已承诺全面商业量产；12/31后无足以续持证据/事前替代日期及资金则2027首个正常交易时点剩余退出，不将查询失败当未出货事实。
- **经营/估值触发优先**：DPC原182m全年EBITDA下限、OEM量承诺/资格/铸造回报；POET认证/订单/现金稀释桥；CLS项目取消、2027加速/2028EPS19与每股现金；NVDA数据中心增长/毛利与客户取消融资；TSM Q4收入52.3bn/GM65%及每ADS现金；RXRX/SCTX安全/主要疗效/注册和关键里程碑资金，具体均在决定卡。新可信实质失败可早于价格条件退出，无新经营坏消息也不能覆盖已触发资本保护。
- **本轮补证与有限缺口**：TSM独立Q3完整FS/指引实读，纠正25,932m为加权稀释股数、债务至983.513bnNTD，原EPS模型没有另加净现金，不据此伪造估值下修。10/22具体6-K及精确期后outstanding仍UNKNOWN，临时留1不加；NVDA下一财报确日/动态日历未核全，剩1承担正常披露风险；TSM1允许跨已核11/10月营收。RXRX/SCTX当前IR列表受阻，复用已读原临床/财务与本轮SEC索引；不是8只全部资料逐字重读或新买门通过。下一指定21:30先补这些有限管线缺口，不取明确拒绝原文、不将工具故障当基本面失败。
- **市场截点**：10/22常规收QQQ704.47/−2.86%、SOXX475.69/−6.79%、SPY763.96/−1.18%、RSP218.22/+0.73%，医疗相对稳；科技重压不等于全宽度崩溃。Cboe延迟VIX19.03/+12.3489%，日高20.31、时间无时区，不冒同步tick。Treasury10/22日末2Y4.65%、10Y4.96%较前日降16/17bp。FOMC10/27–28、GDP/PCE10/29；不编今天CPI/非农或确定跌因。NasdaqSOXX11/5拆股提示待发行人核，除权前后阈值必须同口径调整，不能按旧原价直接触发。
- **验收与边界**：8只均有本次当前目标、原触发、新/旧事实、同尺估值、盈利/风险/事件条件；TSM等有限未知保留，未冒全74筛选完成。根目录34/34公共请求HTTP200，原件/sha/算术检查与独立只读逻辑复核已保存；不证明保护规则能赚钱。未访问账户/订单/秘密、未交易/外发/付费或加后台。ID20已授权工作日21:30一次公开复核保持，首次10/22真实触发已留证，送达/连续监控不冒称。

## 当前开放循环与下一业务顺序

1. 先接用户新的实际成交更正，尤其NVDA同一首批，未确认仍2；RMBS未确认卖出仍1，不自动买回。现有任何减仓均须记录确认后的终局，不能从建议自动减事实。
2. 今晚10/23 21:30指定运行先看全部8只已触发/预警和新披露；新结构条件从本日第一未来常规盘开始，开盘21:30尚不能拿未完成收盘作确认。金融/经济硬触发先处理，不等74池研究。
3. 补TSM精确期后股本/10/22未读6-K所涉及的独立发行人信息、NVDA具体财报日、RXRX/SCTX有限IR新增；若仍失败须标管线故障并换有限充分独立来源，不原样顺延“观察”。不重取安全/403拒绝的原文或借镜像/身份绕过。
4. 后续74池研究继续按既有范围增量；本轮用户只要求现仓没有假称74重筛。保存触发/告知/成交分别证据，未来复核卖飞、回吐、费用、右尾捕获；当前真实净收益归因仍缺完整主动成交/费用/资金流，不查账户。

'''
histmark='## 历史记录（以下均为当时快照，不作为当前持仓、规则或行情）'
if histmark not in old:raise ValueError('historical boundary missing; do not overwrite')
prior,rest=old.split(histmark,1)
prior=prior.removeprefix(head).replace('## 当前有效状态','#### 历史原标题：当前有效状态').replace('## 当前开放循环与下一业务顺序','#### 历史原标题：当前开放循环与下一业务顺序')
rest=rest.replace('## 当前有效状态','#### 历史原标题：当前有效状态')
STATE.write_text(head+active+histmark+'\n\n### 2026-10-23本轮复核前快照（完整保留，动作已由上方全8只决定替代）\n\n'+prior+'\n'+rest)
receipt={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'acceptance':'quantity/old_vs_new/trigger/prospective policy/source-limit integration accepted','independent_reviewer':'root/screen_photonics','reviewer_message':'Final counts, batch deduplication, future two-close rules, profit regular-session execution and event scale accepted; no blocking contradiction.','limitations':['New protection policy not validated as profitable; can sell rebounds.','CLS earliest two-future-close confirmation10/26 cannot ensure exit before after-close earnings.','Financial/IR access limits preserved; not74screen or newbuy approval.'],'source_sha_receipts':'public/*.receipt.json; compute/sources receipts; bio/public receipts','state_file':str(STATE),'no_real_fills_inferred':True,'no_account_access':True,'no_temp_deletion':'Raw extracts/scripts/receipts retained as research evidence, no asset cleanup performed.'}
(P/'FINAL_ACCEPTANCE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print('Updated sole current state; historical snapshots retained. Final decision quantities unchanged.')
