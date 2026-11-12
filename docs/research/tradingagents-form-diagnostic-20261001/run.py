import os,sys,json,time
from pathlib import Path
os.environ['PYTHON_DOTENV_DISABLED']='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
R=Path(__file__).resolve().parent
ROOT=R.parents[2]
sys.path.insert(0,str(ROOT/'tools/tradingagents_codex'))
from bridge import CodexChatModel
from tradingagents.agents.researchers.bull_researcher import create_bull_researcher
from tradingagents.agents.researchers.bear_researcher import create_bear_researcher
from tradingagents.dataflows.config import set_config
set_config({'output_language':'简体中文'})
source=(ROOT/'docs/research/serenity-full-20260930/DOSSIERS.md').read_text()
packet='## FORM'+source.split('## FORM',1)[1].split('\n## ',1)[0]
(R/'input.md').write_text(packet)
model=CodexChatModel(run_dir=str(R/'calls'),model_name='gpt-6.1-sol',effort='medium',max_calls=2,timeout_seconds=300,progress_interval_seconds=10,codex_binary='/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex')
state={'company_of_interest':'FORM','trade_date':'2026-09-30','asset_type':'stock','instrument_context':'仅做历史材料复核，不是今日买卖判断。材料是上轮研究摘要而非独立验证的一手正文。不要浏览或编造事实。用简体中文最多600字：检验估值算式，区分已有风险与新增发现，指出最重要的未证实假设和可证伪条件。已有通过标签不是证据，不得照抄为结论。','market_report':'仅材料内9月29日历史行情，未刷新。','news_report':'未刷新公司事件。','sentiment_report':'无','fundamentals_report':packet,'investment_debate_state':{'history':'','bull_history':'','bear_history':'','current_response':'','count':0}}
log=[]
for role,factory in [('bull',create_bull_researcher),('bear',create_bear_researcher)]:
 started=time.monotonic()
 try:
  state.update(factory(model)(state))
  (R/(role+'.md')).write_text(state['investment_debate_state'][role+'_history'])
  row={'role':role,'status':'completed','seconds':round(time.monotonic()-started,2)}
 except Exception as exc:
  row={'role':role,'status':'failed','error_type':type(exc).__name__,'seconds':round(time.monotonic()-started,2)}
 log.append(row);(R/'status.json').write_text(json.dumps(log,indent=2));print(json.dumps(row),flush=True)
 if row['status']!='completed':break
