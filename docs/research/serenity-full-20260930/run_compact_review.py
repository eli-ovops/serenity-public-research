"""Finite native TradingAgents bull/bear reviews of public packets, no autonomous tools."""
import os,sys,json,re
from pathlib import Path
from datetime import datetime,timezone
os.environ['PYTHON_DOTENV_DISABLED']='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
P=Path(__file__).resolve().parent
ROOT=P.parents[2]
sys.path.insert(0,str(ROOT/'tools/tradingagents_codex'))
from bridge import CodexChatModel
from tradingagents.agents.researchers.bull_researcher import create_bull_researcher
from tradingagents.agents.researchers.bear_researcher import create_bear_researcher
from tradingagents.dataflows.config import set_config
set_config({'output_language':'简体中文'})
groups=[('packaging','FORM CAMT ONTO AMKR ASX AEHR ASMPT TER'),('optical_connectivity','TSEM CRDO AAOI CIEN COHR LITE FN'),('optical_emerging','POET SIVE LWLG NOK AXTI SOI IQE LASR'),('cooling','MOD AAON NVT VRT'),('servers','SMCI DELL HPE CLS Lenovo'),('cloud','ANET AMZN NBIS'),('power','PWR FLNC ETN GEV HWM DPC GNRC'),('compute','NVDA AVGO MRVL AIP ALAB'),('equipment','KLAC LRCX AMAT ASML ACMR ENTG'),('foundry','TSM INTC ON GFS'),('memory','MU WDC STX RMBS SKHY ESMT'),('medical_special','CCXI TSLA RXRX SCTX TEM'),('robotics','OUST HSAI INOD VPG RR SERV')]
snap=json.loads((P/'public_snapshot.json').read_text()); facts={x['ticker']:x for x in json.loads((P/'companyfacts.json').read_text())}
baseline={x['ticker']:x for x in json.loads((P/'baseline_public.json').read_text())}
statuses=[]
for fn in ['primary_status.json','supplement_status.json']:
 if (P/fn).exists():statuses+=json.loads((P/fn).read_text())
def excerpt(s):
 if len(s)<13000:return s
 # XBRL text starts with metadata. Include financial tables, management discussion, cash and risks; gaps remain explicitly incomplete.
 chunks=[s[:5000]]
 patterns=['Consolidated Statements of Operations','CONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS','CONSOLIDATED STATEMENTS OF CASH FLOWS','Liquidity and Capital Resources','Outlook','Business Outlook','stock-based compensation','customer concentration','customer advances','warrant']
 for pat in patterns:
  hits=list(re.finditer(re.escape(pat),s,re.I))
  if hits:
   m=hits[-1];chunks.append(s[max(0,m.start()-100):m.start()+900])
 return '\n[EXTRACT; NOT COMPLETE DOCUMENT]\n'.join(chunks)[:15000]
R=P/'tradingagents_compact';R.mkdir(exist_ok=True)
model=CodexChatModel(run_dir=str(R/'calls'),model_name='gpt-6.1-sol',effort='medium',max_calls=13,timeout_seconds=120,codex_binary='/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex')
log=[]
for group,names in groups:
 tickers=names.split();packet=[]
 for t in tickers:
  docs=[x for x in statuses if x['ticker']==t and x.get('ok') and x.get('characters',0)>1500]
  # Financial release and recent filing can coexist. Latest supplement first; max 2 bounded excerpts.
  docs=sorted(docs,key=lambda x:(x['index']>=200,x['index']),reverse=True)[:2]
  financial=facts.get(t,{}).get('facts',{})
  compact={k:{unit:[max(vals,key=lambda z:(z.get('end',''),z.get('start','')))] if vals else [] for unit,vals in v.items()} for k,v in financial.items()}
  packet.append({'ticker':t,'issuer':snap['sec'].get(t,{}).get('name',baseline[t].get('company_from_sec')),'price_metrics':snap['prices'].get(t,{'status':'overseas quote pending'}).get('metrics',{}),'xbrl':compact,'SEC_filings':snap['sec'].get(t,{}).get('filings',[]),'prior_specific_open_questions':baseline[t].get('remaining_work'),'documents':[{'source':x['url'],'text':excerpt((P/x['path']).read_text())[:2600]} for x in docs]})
 context='''这是同一产业内逐只研究，不得漏掉任何 ticker。只分析给定公开资料，无账户数据，无交易权。不得把旧年份或XBRL单季/累计期混淆。角色的看多/看空立场不能压倒事实。每只输出：1瓶颈/盈利捕获；2已证实财务事实和现金流/股数/预付款/非控股/融资风险；3压力/基准/强三情景的可复算估值模型、所有输入、期限、折现率、计价币种，作者假设必须显式区分公司指引。盈利公司用规范化EPS/现金流；亏损公司不能只套PS，检验最终利润率/融资稀释；生物药采用风险调整而非合作收入PE；SPAC看条款。必要输入缺失则标UNKNOWN，不能凑目标价。给出假设选择理由并算出价格，尽量每只250-400中文字符。4经济失效和重新确认路径；5列全部未闭合维度(基本面/估值/走势/公司事件/市场)，不能把多缺口包装单缺口观察。6明确研究优先级并非买入排名。SEC索引成功不等于已读正文或IR事件门通过，模型不能认证未核验门。数据截点2026-09-30，价格为9/29完成日；MU今晚Q4财报未发布，禁止编造Q4数据；CCXI是Churchill Capital Corp XI，非ChemoCentryx；SKHY需ADS换算，KLAC股票拆分不可混EPS。净现金缺少投资/债务时不得把现金一项当净现金。光通信机会pipeline不是订单。所有模型仅为待主线程核对的研究草稿，不是正式推荐。'''
 state={'company_of_interest':names,'trade_date':'2026-09-30','asset_type':'stock','instrument_context':context,'market_report':json.dumps({t:snap['prices'].get(t,{}).get('metrics',{}) for t in tickers+['QQQ','SOXX','RSP','XLV']},ensure_ascii=False),'sentiment_report':'无社交意见作为证据','news_report':'SEC截至9/30指数已读取，IR新闻/日历覆盖尚未全部闭合。MU9/30 16:30EDT重大二元事件。','fundamentals_report':json.dumps(packet,ensure_ascii=False),'investment_debate_state':{'history':'','bull_history':'','bear_history':'','current_response':'','count':0}}
 (R/(group+'_packet.json')).write_text(json.dumps(packet,ensure_ascii=False,indent=2))
 row={'group':group,'tickers':tickers,'started_utc':datetime.now(timezone.utc).isoformat()}
 try:
  state.update(create_bear_researcher(model)(state))
  (R/(group+'_bear.md')).write_text(state['investment_debate_state']['bear_history'])
  row['bear']='completed';print(group,'bear completed',flush=True)
 except Exception as e:
  row['error']=str(e);print(group,'ERROR',str(e),flush=True)
  log.append(row);(R/'status.json').write_text(json.dumps(log,indent=2));break
 log.append(row);(R/'status.json').write_text(json.dumps(log,indent=2))
print('FINISHED',len(log),'groups',flush=True)
