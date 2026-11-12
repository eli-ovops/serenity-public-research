import json,re
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parent;ROOT=R.parents[2]
s=(ROOT/'docs/research/serenity-full-20260930/primary/200_FORM.txt').read_text()
sec_url='https://www.sec.gov/Archives/edgar/data/1039399/000103939926000033/form-20260627.htm'
def section(a,b):
 start=s.index(a);end=s.index(b,start+len(a));return s[start:end]
statements={
 'get_balance_sheet':section('CONDENSED CONSOLIDATED BALANCE SHEETS','CONDENSED CONSOLIDATED STATEMENTS OF INCOME'),
 'get_income_statement':section('CONDENSED CONSOLIDATED STATEMENTS OF INCOME','CONDENSED CONSOLIDATED STATEMENTS OF COMPREHENSIVE INCOME'),
 'get_cashflow':section('CONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS','NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS')}
statements={k:{'source':sec_url,'period_end':'2026-06-27','filed':'2026-08-04','units':'USD thousands unless per share','period_basis':'Cashflow H1 cumulative; income Q2 and H1 columns; balance at period end','text':v} for k,v in statements.items()}
market={}
for t in ['FORM','QQQ','SOXX','RSP']:
 raw=json.loads((R/(t+'_yahoo.json')).read_text());chart=raw['data']['chart']['result'][0];q=chart['indicators']['quote'][0]
 rows=[]
 for i,ts in enumerate(chart['timestamp']):
  day=datetime.fromtimestamp(ts,timezone.utc).date().isoformat()
  if day>'2026-09-30' or any(q[k][i] is None for k in ['open','high','low','close','volume']):continue
  rows.append({'date':day,**{k:q[k][i] for k in ['open','high','low','close','volume']}})
 market[t]={'rows':rows,'source':raw['source'],'price_basis':'Yahoo daily OHLC, not adjusted close; actions not independently reconciled'}
vraw=json.loads((R/'vix.json').read_text());vr=[x for x in vraw['rows'] if datetime.strptime(x['DATE'],'%m/%d/%Y').date().isoformat()<='2026-09-30'];vix={'source':vraw['source'],'as_of':'2026-09-30','session':'completed regular session','last':vr[-1],'prior':vr[-2],'change_pct':(float(vr[-1]['CLOSE'])/float(vr[-2]['CLOSE'])-1)*100}
policy='研究层和账户层分开。缺账户事实不否决研究层。缺放量突破、ATR、RSI、完美回踩、深度安全边际不单独否决合理价格首股。不强制技术止损替代经济失效。合理参与区不同于深度价值价。大盘失控须指数与宽度同步恶化，QQQ/VIX单项红绿不否决。研究通过须基本面/估值/公司事件/市场/经济失效闭合；两项以上缺口=研究未完成，仅一项才条件观察(Owner及期限)，有硬反证才排除。HOLD不是持仓指令，不提供股数或新增配置0。旧价格地图不能自动续期。'
now=datetime.now(timezone.utc).isoformat()
newsurl='https://investors.formfactor.com/news-releases/news-release-details/formfactor-announces-participation-18th-annual-ceo-investor'
events={'as_of_utc':now,'method':'SEC latest index retrieved directly + IR press/event pages read through web tool','SEC':json.loads((R/'sec.json').read_text()),'IR_sources':['https://investors.formfactor.com/press-releases','https://investors.formfactor.com/events-and-presentations',newsurl],'news':[{'published':'2026-09-30 16:01 EDT','event_date':'2026-10-13','type':'investor conference participation','source':newsurl}],'event_gate':'No known scheduled material binary company event found in next24h after 2026-10-01 08:20 UTC; undisclosed residual risk remains. Review expires24h later or on new disclosure. Ordinary Oct13 conference is outside24h; not classified binary.','IR_conflict':'Event index says upcoming details unavailable, but Sep30 news explicitly lists Oct13 conference. Do not interpret blank calendar as no events.'}
notes=[]
for term in ['SK hynix Inc.','Provision for Income Taxes','Capital Resources']:
 pos=s.find(term,51000);notes.append({'section':term,'text':s[max(0,pos-150):pos+1900] if pos>=0 else 'UNKNOWN','source':sec_url})
packet={'ticker':'FORM','as_of':'2026-10-01','retrieved_utc':now,'statements':statements,'market':market['FORM'],'benchmarks':{k:v for k,v in market.items() if k!='FORM'},'vix':vix,'company_events':events,'policy':policy,'fundamentals':{'source':sec_url,'company':'FormFactor semiconductor test and probe card supplier','notes':notes,'company_guidance':{'source':'https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2026-second-quarter-results','published':'2026-07-29','Q3_revenue_USDm':[260,280],'Q3_GAAP_EPS':[0.66,0.84],'Q3_adjusted_EPS':[0.77,0.95]},'prior_author_assumptions':{'date':'2026-09-30','method':'2028 EPS x PE /1.12^2.25','EPS':[2.8,5.8,7.5],'PE':[22,30,36],'not_company_guidance':True,'status':'unvalidated future EPS bridge, do not auto-approve old140cap'},'derived_checks':{'H1_CFO_minus_cash_capex_USDm':81.973,'H1_increase_unpaid_capex_USDm':15.817,'H1_cashFCF_minus_unpaid_capex_increase_USDm':66.156,'caveat':'Timing sensitivity, not reported FCF, not automatically next-period payment. SBC dilution and equity-award withholding separate, avoid double counting.','H1_tax_rate_pct':8.9,'Q2_tax_rate_pct':11.1,'future_normal_tax_rate':'author assumption needed, not repeat low rate forever'}}}
(R/'packet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2))
print('packet built',len(json.dumps(packet)), 'bars',len(market['FORM']['rows']))
