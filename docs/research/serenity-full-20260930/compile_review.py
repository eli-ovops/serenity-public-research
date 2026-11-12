import csv,json,math,datetime,re
from pathlib import Path
P=Path(__file__).resolve().parent
def read(n): return json.loads((P/n).read_text())
def dump(n,v): (P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2))
scope=read('SCOPE.json'); snap=read('public_snapshot.json')
models={}
for line in (P/'valuation_assumptions.psv').read_text().splitlines():
    t,eps,pe,cur,basis=line.split('|')
    e=list(map(float,eps.split(','))); m=list(map(float,pe.split(',')))
    r=.15 if t=='ACMR' else .12; fx=1.10 if cur=='EUR' else 1
    models[t]={'method':'2028 EPS x exit PE / (1+r)^2.25','eps':e,'pe':m,'rate':r,'years':2.25,'fx':fx,'currency':('USD' if cur=='EUR' else cur),'input_currency':cur,'basis':basis,'values':[a*b*fx/(1+r)**2.25 for a,b in zip(e,m)]}
early=read('early_valuation_inputs.json')
for t,a in early['models'].items():
    models[t]={**a,'method':early['method'],'currency':'USD','rate':.15,'years':3.25,'values':[(a['revenue'][i]*a['net_margin'][i]*a['pe'][i]+a['net_cash'][i])/a['shares'][i]/1.15**3.25 for i in range(3)]}
a=early['INOD']; models['INOD']={**a,'currency':'USD','values':[a['revenue'][i]*a['net_margin'][i]*a['pe'][i]/a['shares'][i] for i in range(3)]}
a=early['RR']; models['RR']={**a,'currency':'USD','values':[(a['cash_and_investments']-a['liabilities']-a['burn'][i]+a['operating_option'][i])/a['shares'][i]/1.15 for i in range(3)]}
for t,a in read('complex_models.json').items():
    if a['method']=='EV_EBITDA': vals=[(a['ebitda_m'][i]*a['multiple'][i]+a['net_cash_m'][i])/a['shares_m'][i]/(1+a['rate'])**a['years'] for i in range(3)]
    else: vals=[(max(0,a['revenue_m'][i]*a['net_margin'][i]*a['pe'][i])+a['net_cash_m'][i])/a['shares_m'][i]/(1+a['rate'])**a['years']*a.get('quote_multiplier',1) for i in range(3)]
    models[t]={**a,'values':vals,'currency':{'IQE':'GBX','Lenovo':'HKD'}.get(t,a['currency'])}
prices={t:{**d.get('metrics',{}),'source':d.get('source'),'retrieved_utc':d.get('retrieved_utc'),'rows':d.get('rows',[])} for t,d in snap['prices'].items() if d.get('metrics')}
for d in read('overseas_history.json'):
    rows=[]
    for x in d.get('rows',[]):
        dt=datetime.datetime.strptime(x[0],'%b %d, %Y').date().isoformat()
        if dt>'2026-09-29': continue
        def num(s): return float(s.replace(',','').replace('$',''))
        try: rows.append(dict(date=dt,open=num(x[1]),high=num(x[2]),low=num(x[3]),close=num(x[4]),volume=num(x[7])))
        except ValueError: continue
    rows.sort(key=lambda x:x['date'])
    if not rows: continue
    c=rows[-1]['close']; window=rows[-20:]
    a={'last_date':rows[-1]['date'],'close':c,'bars':len(rows),'source':d['source'],'rows':rows,'sma_20':sum(x['close'] for x in window)/len(window),'sma_50':sum(x['close'] for x in rows[-50:])/50 if len(rows)>=50 else None,'low20':min(x['low'] for x in window),'high20':max(x['high'] for x in window),'volume_ratio':rows[-1]['volume']/(sum(x['volume'] for x in window)/len(window))}
    for n in [5,20,60]: a['return_'+str(n)]=c/rows[-n-1]['close']-1 if len(rows)>n else None
    prices[d['ticker']]=a
for t,a in prices.items():
    rr=a['rows']; a['return_1']=rr[-1]['close']/rr[-2]['close']-1 if len(rr)>1 else None
    a['volume_ratio']=rr[-1]['volume']/(sum(x['volume'] for x in rr[-20:])/20) if len(rr)>=20 and sum(x['volume'] for x in rr[-20:]) else None
dump('valuation_results.json',models)
dump('closed_session_prices.json',prices)
with (P/'valuation_results.csv').open('w') as f:
    w=csv.writer(f);w.writerow(['ticker','currency','close','stress','base','bull','price_over_base','status_of_model','basis'])
    for t in scope['universe']:
        m=models.get(t); q=prices.get(t,{}).get('close')
        w.writerow([t,m['currency'] if m else '',q,*([round(v,4) for v in m['values']] if m else ['','','']),round(q/m['values'][1],4) if m and q and m['values'][1] else '', '作者敏感性，不能自动用作买价' if m else 'UNKNOWN',m['basis'] if m else '尚未建立可校准模型'])
if __name__=='__main__':
    for t in scope['universe']:
        m=models.get(t);q=prices.get(t,{}).get('close')
        print(t,q, '/'.join(f'{v:.2f}' for v in m['values']) if m else 'NO_MODEL')
