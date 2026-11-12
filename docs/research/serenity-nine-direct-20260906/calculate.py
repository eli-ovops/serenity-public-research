"""Public-research scenario calculations; no account access, feeds or trading.

All cash forecasts are analyst assumptions, not company guidance.
Money and shares in millions, except HWM uses per-share FCFE.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FADE = [.15, .12, .09, .06, .04]

def dcf(cf, r, g, net, shares, fade=True):
    cf = list(cf)
    if fade:
        for rate in FADE:
            cf.append(cf[-1] * (1 + rate))
    operating_pv = sum(c / (1+r)**t for t, c in enumerate(cf, 1))
    terminal_pv = cf[-1]*(1+g)/(r-g)/(1+r)**len(cf)
    return dict(cash_flows=cf, discount_rate=r, terminal_growth=g,
                equity_bridge=net, model_shares=shares,
                value=(operating_pv+terminal_pv+net)/shares,
                terminal_fraction=terminal_pv/(operating_pv+terminal_pv))

# Stress / base / strong. Equity bridge deliberately reserves operating cash.
SPECS = {
 'FORM': [([140,154,169.4,186.34,204.974],.12,.03,200,80),
          ([180.2*1.2**i for i in range(5)],.10,.035,200,80),
          ([220*1.2**i for i in range(5)],.10,.035,200,80)],
 'AEHR': [([8,10,12,15,18],.13,.03,85,36),
          ([23,30,40,52,68],.11,.035,100,34),
          ([35,48,65,90,120],.10,.04,100,34)],
 'AXTI': [([-20,0,10,20,30],.13,.03,200,75),
          ([0,15,35,60,85],.105,.035,280,70),
          ([5,30,70,120,180],.10,.04,280,70)],
 'Soitec': [([0,30,60,90,120],.12,.03,-56,36),
            ([40,90,156,224,279],.10,.035,-56,36),
            ([60,125,210,300,380],.10,.035,-56,36)],
 'IQE': [([-8,-5,0,4,8],.14,.03,-15,1500),
         ([0,4,12,20,28],.12,.035,0,1450),
         ([2,10,25,40,60],.11,.04,0,1450)],
 'Sivers': [([-180,-120,-50,10,60],.15,.03,500,400),
            ([-170,-80,30,120,250],.13,.035,600,375),
            ([-150,-30,100,300,550],.12,.04,600,375)],
 'GEV': [([3000,3500,4200,5000,6000],.105,.03,3000,275),
         ([4500,6000,7500,9500,11500],.09,.035,5000,270),
         ([5500,7500,10000,13000,16000],.09,.035,5000,270)],
 # FCFE per share already after interest and reinvestment: no debt subtraction.
 'HWM': [([4,4.4,4.8,5.2,5.7],.11,.03,0,1),
         ([4.75,5.6,6.6,7.8,9.2],.095,.035,0,1),
         ([5,6.2,7.7,9.5,11.8],.09,.04,0,1)]
}

def main():
    out = {'method':'Analyst scenarios; 5 explicit years + 5 fading-growth years + terminal',
           'fade_growth':FADE, 'models':{}}
    for name, cases in SPECS.items():
        out['models'][name] = {label:dcf(*case) for label,case in zip(['stress','base','strong'],cases)}
    # ESMT uses through-cycle earnings, not peak month annualisation.
    out['models']['ESMT'] = {
        label:dict(revenue=rev, net_margin=margin, diluted_shares=320,
                   pe_multiple=pe, eps=rev*margin/320, value=rev*margin/320*pe)
        for label,rev,margin,pe in [('stress',22000,.12,10),('base',30000,.22,14),('strong',40000,.30,16)]}
    out['cross_checks'] = {
        'ESMT_H1_CFO_TWD_m':10585.892,
        'ESMT_H1_FCF_after_tangible_and_intangible_capex_TWD_m':10585.892-222.651-90.904,
        'ESMT_June_net_cash_excluding_leases_TWD_m':14527.171-1000-907.292,
        'ESMT_basic_market_cap_TWD_m':298.1278*278.5,
        'ESMT_CB_extra_shares_at_100_TWD_m':2000/100,
        'ESMT_CB_extra_shares_at_200_TWD_m':2000/200,
        'ESMT_CB_extra_shares_at_278_5_TWD_m':2000/278.5,
        'AEHR_price_to_FY27_midpoint_sales':86.26*32.480/140,
        'AXTI_price_to_Q2_revenue_times_four_NOT_FORECAST':61.64*65.570/(47.6*4),
        'Soitec_EV_to_FY26_trough_sales':(128.3*36+56)/592,
        'IQE_market_cap_GBP_m':.4745*1312.590972,
        'Sivers_market_cap_SEK_m':27.26*356.740332,
        'Sivers_EV_to_H1_sales_times_two_NOT_FORECAST':(27.26*356.740332-600)/(115.6*2),
        'GEV_reported_FCF_guide_yield_NOT_NORMALIZED':12000/(941.95*270),
        'HWM_price_to_FY26_guided_adjusted_EPS':259.27/5.27,
        'HWM_FY26_guided_FCF_yield':1900/(259.27*402),
        'VIX_September4_change_pct':(14.53/14.32-1)*100,
    }
    for name,cases in out['models'].items():
        assert cases['stress']['value'] < cases['base']['value'] < cases['strong']['value'], name
    (ROOT/'calculations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    for name,cases in out['models'].items():
        scale=100 if name=='IQE' else 1
        print(name, ' / '.join(f'{cases[k]["value"]*scale:.2f}' for k in ['stress','base','strong']))

if __name__ == '__main__': main()
