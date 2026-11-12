"""Finite public-data consolidation. No network, accounts, orders or background."""
import json,csv,datetime,statistics
from pathlib import Path
P=Path(__file__).resolve().parent
OLD=P.parent/'serenity-screen-all74-20261021'
def read(f):return json.loads(f.read_text())
def dump(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def num(x):
 if x is None:return None
 try:return float(str(x).replace('$','').replace(',','').replace('%','').replace('+',''))
 except ValueError:return None
prior=read(OLD/'ALL74_CARDS.json'); rows=[];qmap={}
for c in prior['cards']:
 t=c['symbol'];f=P/'shared/public'/('INFO_'+t+'.json');row={'symbol':t,'currency':c['currency'],'previous_research_status':c['status'],'previous_cap':c['participation_cap']}
 if f.exists():
  d=read(f).get('data')
  if d:
   a=d['primaryData'];b=d.get('secondaryData')
   row.update(latest_price=num(a['lastSalePrice']),latest_percent=a['percentageChange'],latest_time=a['lastTradeTimestamp'],latest_session=d['marketStatus'],regular_close=num(b['lastSalePrice']) if b else None,regular_percent=b['percentageChange'] if b else None,regular_time=b['lastTradeTimestamp'] if b else None,source=str(f),dayrange=d.get('keyStats',{}).get('dayrange') if d.get('keyStats') else None)
 else:
  f=P/'shared/public'/('OVER_'+t+'.json');d=read(f)['chart']['result'][0];m=d['meta']
  row.update(latest_price=m['regularMarketPrice'],latest_time=datetime.datetime.fromtimestamp(m['regularMarketTime'],datetime.timezone.utc).isoformat(),latest_session='local last regular; no synchronization claim',source=str(f),regular_close=m['regularMarketPrice'])
 row['price_vs_prior_research_cap']='within' if row.get('regular_close') is not None and row['regular_close']<=row['previous_cap'] else 'above_or_unverified'
 rows.append(row);qmap[t]=row
for t in ['QQQ','SOXX','SPY','RSP','XLI','XLV','XBI']:
 d=read(P/'shared/public'/('INFO_'+t+'.json'))['data'];a=d['primaryData'];b=d['secondaryData'];qmap[t]={'symbol':t,'regular_close':num(b['lastSalePrice']),'regular_percent':b['percentageChange'],'regular_time':b['lastTradeTimestamp'],'latest_price':num(a['lastSalePrice']),'latest_percent':a['percentageChange'],'latest_time':a['lastTradeTimestamp'],'latest_session':d['marketStatus']}
dump('QUOTES.json',{'collected_utc':'2026-10-22 about00:00–00:02Z','quotes':qmap,'all74_price_count':len(rows),'regular_and_afterhours_separate':True})
with (P/'ALL74_INCREMENT.csv').open('w',newline='') as f:
 fields=sorted(set().union(*(r.keys() for r in rows)));w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
# Compose new close-confirmed daily bar only where full OHLCV now exists from independent provider.
history=read(OLD/'shared/HISTORY_SOURCES.json'); metrics={};series={};bar_sources={}
for t,path in history.items():
 old=read(Path(path))['data']['tradesTable']['rows'];old=sorted(old,key=lambda r:datetime.datetime.strptime(r['date'],'%m/%d/%Y'))
 vals=[num(r['close']) for r in old];cl=qmap[t].get('regular_close');cf=P/'shared/public'/('CHART5_'+t+'.json')
 if cl is not None:vals.append(cl)
 if cf.exists():
  d=read(cf)['chart']['result'][0];i=len(d['timestamp'])-1;a=d['indicators']['quote'][0];date=datetime.datetime.fromtimestamp(d['timestamp'][i],datetime.timezone.utc).date().isoformat()
  assert date=='2026-10-21',(t,date)
  rawclose=a.get('close',[None]*(i+1))[i]
  bar_sources[t]={'date':date,'open':a['open'][i],'high':a['high'][i],'low':a['low'][i],'regular_volume':a['volume'][i],'regular_close':cl,'close_source':'Nasdaq INFO secondaryData explicit regular close','OHLC_volume_source':str(cf),'provider_last_daily_close':rawclose,'provider_meta_price':d['meta']['regularMarketPrice'],'limitation':'Yahoo finaldaily close field None; official explicit Nasdaq regularclose used, provider lasttrade minor differences retained; volume preliminary'}
  lows=[num(r['low']) for r in old]+[a['low'][i]];highs=[num(r['high']) for r in old]+[a['high'][i]];vol=[num(r['volume']) for r in old]+[a['volume'][i]]
 else:lows=highs=vol=None
 m={'asof':'2026-10-21','close':cl,'SMA20':sum(vals[-20:])/20,'SMA50':sum(vals[-50:])/50,'OHLCV_refreshed':cf.exists()}
 for n in [5,20,60]:m['return'+str(n)+'_pct']=(vals[-1]/vals[-1-n]-1)*100
 if lows is not None:m.update(low20=min(lows[-20:]),high20=max(highs[-20:]),volume_last=vol[-1],volume_ratio20=vol[-1]/(sum(vol[-20:])/20))
 metrics[t]=m;series[t]=vals
for t,m in metrics.items():
 for bench in ['QQQ','SOXX','XLI','XLV','XBI','SPY']:m['RS20_vs_'+bench+'_pp']=m['return20_pct']-metrics[bench]['return20_pct']
dump('TECHNICAL_INCREMENT.json',{'metrics':metrics,'composite_bar_sources':bar_sources,'limitations':'All75 US-path close series appended; fresh full OHLCV only19 prioritized names/ETFs, remaining price/close-based trend only. Nasdaq same-date history query application400, corrected dates stilllaggedOct20; not count either asOct21bar. No forecast/model refreshed merely fromAPI200.'})
# Freeze the old rebound-exit test before selecting any new stock.
look={t:{r['z']['dateTime']:r['y'] for r in read(P/'shared/public'/('INTRADAY_'+t+'.json'))['data']['chart']} for t in ['INOD','QQQ']}
hits=[]
for k,v in look['INOD'].items():
 try:tm=datetime.datetime.strptime(k.replace(' ET',''),'%I:%M %p').time()
 except ValueError:continue
 if datetime.time(10,20)<=tm<=datetime.time(16) and 61<=v<=65 and k in look['QQQ'] and look['QQQ'][k]<743:hits.append({'labeled_time_ET':k,'INOD':v,'QQQ':look['QQQ'][k]})
assert hits
trigger={'symbol':'INOD','date_US':'2026-10-21','old_rule':'61–65 and no new operating earnings improvement and QQQ<743 -> exit same1 share; mutuallyexclusive with close<52','matched_minute_samples':hits,'first_sample':'14:13ET / Beijing10/22 02:13 as labeled by provider, not first tick proof','current_assessment_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'announcement_review':'holdings/UPDATE.md: no new primary operating earnings improvement found within stated SEC/IR/issuersearch coverage','confirmed_qty':1,'research_target_qty':0,'execution_status':'NOT_CONFIRMED; user holdings remain1 until explicit fill confirmation','execution_reassessment':'next available regular session reduce1 to0; no guarantee of61 fill, no need to recover cost; new material primary counterevidence would require reunderwriting','data_quality':'Nasdaq chart rawx is4h inconsistent with labeledET clock; comparison uses bothseries same explicit z.dateTimeET field and chartdate, independently checked daily highs. QQQ headerlastSalePrice stale; finalclose from explicit INFOsecondary, not chartheader. Minute prints are samples not trade execution.'}
dump('INOD_TRIGGER.json',trigger)
plans=[]
for t,price,L,mechanism in [('AAON',75,71.19,'regularclose<L -> newshare target0 nextavailable regularsession; intradaytouch warning/stopnewentries'),('HPE',57.5,53.5,'regularsession touchL -> newshare target0; no pricefillguarantee'),('ONTO',220,213.5,'regularclose<L -> newshare target0 nextavailable regularsession')]:
 c=next(c for c in prior['cards'] if c['symbol']==t);risk=round(price-L,4)
 plans.append({'symbol':t,'research_status':'研究门通过，账户门待确认','mode':'基本面/GARP','limit':price,'tif':'DAY','activation_beijing':'2026-10-22 22:00 orlater (30minafterregularopen)','expires_beijing':'2026-10-23 04:00','valuation_unchanged':c['values'],'valuation_cap_unchanged':c['participation_cap'],'fixed_L_unchanged':L,'mechanism':mechanism,'planned_one_share_price_risk':risk,'minimum_NAV_one_share_before_fees':round(max(10*price,200*risk),4),'normal_8pct_amount_NAV':round(price/.08,4),'personal_quantity':'not assigned, current NAV/cash UNKNOWN','profit_review_and_exit':c['research_limit_plan'].get('profit_review_price'), 'profit_exit_if_no_stronger_evidence':c['research_limit_plan'].get('profit_exit_without_stronger_per_share_evidence'),'economic_invalidation':c['invalidation'],'new_fact_expiry':'earnings/guidance/financing/M&A/regulatory changes cancel research map; user must not activate or must cancel any unfilledactualorder; not automatic broker cancellation','entry_guard':'do not activate ifpricealreadybelowL or broadmarketisclearlyoutofcontrol; ordinaryred/green notveto','gap_risk':'DAY and capitalprotection do not cap gap/slippage/fee losses','correlation':'chooseonlyone of3; combinewithcurrentAIinfrastructure exposure'})
dump('PLANS.json',{'asof_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'priority':['AAON','HPE','ONTO'],'only_one_new_direction':True,'plans':plans})
print(json.dumps({'all74_prices':len(rows),'US_close_trend_series':len(metrics),'full_new_OHLCV':len(bar_sources),'INOD_hits':hits,'plans':[{k:p[k] for k in ['symbol','limit','fixed_L_unchanged','planned_one_share_price_risk','minimum_NAV_one_share_before_fees']} for p in plans]},ensure_ascii=False))
