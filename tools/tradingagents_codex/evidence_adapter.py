"""Public-evidence dispatch. No network, account access or hidden fallbacks."""
import json, math, statistics

def indicators(rows):
    c=[r['close'] for r in rows]; n=len(c)
    if not c:return {}
    def ema(values,span):
        out=[values[0]]; alpha=2/(span+1)
        for x in values[1:]:out.append(alpha*x+(1-alpha)*out[-1])
        return out
    values={f'close_{k}_sma':statistics.mean(c[-k:]) if n>=k else None for k in [20,50,200]}
    for k in [10,50]:values[f'close_{k}_ema']=ema(c,k)[-1] if n>=k*3 else None
    if n>=78:
        macd=[a-b for a,b in zip(ema(c,12),ema(c,26))]; signal=ema(macd,9)
        values.update(macd=macd[-1],macds=signal[-1],macdh=macd[-1]-signal[-1])
    if n>=20:
        m=statistics.mean(c[-20:]);sd=statistics.pstdev(c[-20:])
        values.update(boll_ub=m+2*sd,boll_lb=m-2*sd,boll=m)
        volume=sum(r['volume'] for r in rows[-20:])
        values['vwma']=sum(r['close']*r['volume'] for r in rows[-20:])/volume if volume else None
    if n>=15:
        changes=[b-a for a,b in zip(c,c[1:])];up=statistics.mean(max(v,0) for v in changes[:14]);down=statistics.mean(max(-v,0) for v in changes[:14])
        for v in changes[14:]:up=(13*up+max(v,0))/14;down=(13*down+max(-v,0))/14
        values['rsi']=100-100/(1+up/down) if down else (100 if up else 50)
        tr=[max(r['high']-r['low'],abs(r['high']-c[i-1]),abs(r['low']-c[i-1])) for i,r in enumerate(rows) if i]
        atr=statistics.mean(tr[:14])
        for v in tr[14:]:atr=(13*atr+v)/14
        values['atr']=atr
    return values

class EvidenceAdapter:
    def __init__(self,packet):self.p=packet
    def respond(self,name,*args,**kwargs):
        p=self.p
        unknown=lambda why:{'status':'UNKNOWN','reason':why}
        data=unknown('No matching evidence collected')
        stock_tools={'get_fundamentals','get_balance_sheet','get_cashflow','get_income_statement','get_stock_data','get_verified_market_snapshot','get_indicators','get_news','get_insider_transactions'}
        if name in stock_tools and args and args[0]!=p['ticker']:
            data=unknown('Ticker outside frozen scope')
        elif name in ['get_balance_sheet','get_cashflow','get_income_statement']:
            freq=kwargs.get('freq',args[1] if len(args)>1 else 'quarterly')
            if freq!='quarterly':data=unknown('Annual statement not collected; do not relabel interim data as annual')
            else:data=p['statements'][name]
        elif name=='get_fundamentals':data=p['fundamentals']
        elif name in ['get_stock_data','get_verified_market_snapshot','get_indicators']:
            if name=='get_stock_data':
                start=kwargs.get('start_date',args[1] if len(args)>1 else '0000');end=kwargs.get('end_date',args[2] if len(args)>2 else p['as_of'])
            else:start='0000';end=kwargs.get('curr_date',args[2] if name=='get_indicators' and len(args)>2 else args[1] if len(args)>1 else p['as_of'])
            rows=[r for r in p['market']['rows'] if start<=r['date']<=end]
            if not rows:data=unknown('No bars in requested date range')
            elif name=='get_indicators':
                name_i=kwargs.get('indicator',args[1] if len(args)>1 else '')
                value=indicators(rows).get(name_i)
                data={'indicator':name_i,'value':value,'status':'computed' if value is not None else 'UNKNOWN','as_of':rows[-1]['date'],'bars_used':len(rows),'basis':'daily OHLC, SMA; EMA seeded first close >=3span warmup; RSI/ATR Wilder14; Bollinger20 population SD; VWMA20','source':p['market']['source']}
            else:
                cs=[r['close'] for r in rows];vol=[r['volume'] for r in rows]
                data={'rows':rows if name=='get_stock_data' else rows[-2:],'source':p['market']['source'],'as_of':rows[-1]['date'],'requested_end':end,'coverage_start':rows[0]['date'],'price_basis':p['market']['price_basis'],'indicators':indicators(rows),'last_volume_over_prior20_mean':vol[-1]/statistics.mean(vol[-21:-1]) if len(vol)>=21 else None,'return_20':cs[-1]/cs[-21]-1 if len(cs)>20 else None}
                if name=='get_verified_market_snapshot':data.update(benchmarks=p['benchmarks'],vix=p['vix'],verification='source-backed daily snapshot, not intraday entry confirmation')
        elif name=='get_news':data=p['company_events']
        elif name=='get_insider_transactions':data=unknown('SEC filing index is not parsed insider transactions')
        elif name=='get_macro_indicators':
            ind=kwargs.get('indicator',args[0] if args else '')
            data=p['vix'] if str(ind).lower()=='vix' else unknown('Requested macro series not collected; VIX cannot stand in for it')
        elif name in ['get_global_news','get_prediction_markets']:data=unknown('Not collected; company news is not global or prediction-market evidence')
        return json.dumps({'tool':name,'retrieved_utc':p['retrieved_utc'],'scope':'public evidence snapshot; provenance and date remain binding','data':data,'policy':p['policy']},ensure_ascii=False)
