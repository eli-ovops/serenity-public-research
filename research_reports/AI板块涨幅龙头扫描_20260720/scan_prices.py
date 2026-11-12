#!/usr/bin/env python3
import csv
import json
import math
import time
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

END = "2026-07-20"
START = "2026-03-01"
SECTORS = {
    "AI存储/HBM": ["MU", "WDC", "STX"],
    "高速光互连/光器件": ["CRDO", "AAOI", "CIEN", "COHR", "LITE", "MRVL", "FN"],
    "先进封装与测试": ["CAMT", "ONTO", "FORM", "AMKR", "ASX", "TER"],
    "半导体设备/量测": ["KLAC", "LRCX", "AMAT", "ASML", "ACMR", "ENTG"],
    "AI服务器/散热/电源": ["VRT", "MOD", "AAON", "NVT", "ETN", "GEV", "DELL", "HPE", "SMCI", "PWR"],
}
BENCHMARKS = ["SOXX", "QQQ"]
OUT = Path(__file__).parent

def n(v):
    if v is None:
        return None
    return float(str(v).replace("$", "").replace(",", ""))

def get(symbol, assetclass="stocks"):
    url = ("https://api.nasdaq.com/api/quote/" + symbol + "/historical?assetclass=" + assetclass
           + "&fromdate=" + START + "&todate=" + END + "&limit=5000")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (public research; no cookies)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        blob = json.load(r)
    rows = blob.get("data", {}).get("tradesTable", {}).get("rows") or []
    parsed=[]
    for x in rows:
        try:
            parsed.append({"date": x["date"], "close": n(x["close"]), "high": n(x["high"]), "low": n(x["low"]), "volume": n(x["volume"])})
        except (KeyError, TypeError, ValueError):
            continue
    return list(reversed(parsed))

def metrics(rows):
    if len(rows) < 61:
        return None
    last=rows[-1]
    # Latest close versus close 20/60 completed trading sessions before it.
    r5=last["close"]/rows[-6]["close"]-1
    r20=last["close"]/rows[-21]["close"]-1
    r60=last["close"]/rows[-61]["close"]-1
    window=rows[-21:]
    peak=-math.inf; mdd=0
    for r in window:
        peak=max(peak, r["close"])
        mdd=min(mdd, r["close"]/peak-1)
    av20=sum(r["volume"]*r["close"] for r in rows[-20:])/20
    avprev=sum(r["volume"] for r in rows[-40:-20])/20
    avnow=sum(r["volume"] for r in rows[-20:])/20
    return {"latest_date":last["date"], "latest_close":last["close"], "r5":r5, "r20":r20, "r60":r60, "mdd20":mdd, "adv20":av20, "volume_ratio20":avnow/avprev if avprev else None, "days":len(rows)}

allrows={}; results={}; excluded={}
universe=[(s, sec) for sec, symbols in SECTORS.items() for s in symbols]
with ThreadPoolExecutor(max_workers=6) as pool:
    jobs={pool.submit(get, s): (s, sec) for s, sec in universe}
    for job in as_completed(jobs):
        s, sec=jobs[job]
        try:
            rows=job.result()
            allrows[s]=rows
            m=metrics(rows)
            if m:
                m["sector"]=sec; results[s]=m
            else:
                excluded[s]={"sector":sec,"reason":"不足61个交易日或公开端点缺少完整历史", "days":len(rows)}
        except Exception as e:
            excluded[s]={"sector":sec,"reason":f"公开行情端点失败: {type(e).__name__}"}

bench={}
for s in BENCHMARKS:
    try:
        rows=get(s, "etf")
        if not rows: rows=get(s, "stocks")
        bench[s]=metrics(rows)
    except Exception as e:
        bench[s]={"error":type(e).__name__}

with (OUT/"行情原始与指标.json").open("w") as f:
    json.dump({"as_of":END,"source":"Nasdaq public historical API", "stocks":results, "benchmarks":bench, "excluded":excluded}, f, ensure_ascii=False, indent=2)
with (OUT/"个股指标.csv").open("w", newline="") as f:
    cols=["ticker","sector","latest_date","latest_close","r5","r20","r60","mdd20","adv20","volume_ratio20","days"]
    w=csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for s,x in sorted(results.items(), key=lambda a:(a[1]["sector"],-a[1]["r20"])):
        w.writerow({"ticker":s, **x})

def med(x):
    x=sorted(x); return x[len(x)//2] if len(x)%2 else (x[len(x)//2-1]+x[len(x)//2])/2
summary=[]
soxx=bench.get("SOXX",{}).get("r20")
qqq=bench.get("QQQ",{}).get("r20")
for sec in SECTORS:
    a=[(s,x) for s,x in results.items() if x["sector"]==sec]
    if not a: continue
    row={"sector":sec,"n":len(a),"median_r20":med([x["r20"] for _,x in a]),"median_r60":med([x["r60"] for _,x in a]),"up_ratio":sum(x["r20"]>0 for _,x in a)/len(a),"raw_leader":max(a,key=lambda t:t[1]["r20"])[0]}
    row["excess_soxx20"]=row["median_r20"]-soxx if soxx is not None else None
    row["excess_qqq20"]=row["median_r20"]-qqq if qqq is not None else None
    # Comparable leader: liquid > $10m 20d dollar volume, volume ratio >= .6, MDD no worse than -25%; excludes SMCI due governance BLOCKED, applies quality comparison filter only.
    comparable=[(s,x) for s,x in a if x["adv20"]>=10_000_000 and x["volume_ratio20"]>=.6 and x["mdd20"]>=-.25 and s != "SMCI"]
    row["comparable_leader"]=max(comparable,key=lambda t:t[1]["r20"])[0] if comparable else None
    row["comparable_count"]=len(comparable)
    summary.append(row)
summary.sort(key=lambda x:(x["median_r20"], x["up_ratio"], x["median_r60"]), reverse=True)
with (OUT/"板块汇总.json").open("w") as f: json.dump({"benchmarks":bench,"ranked":summary},f,ensure_ascii=False,indent=2)
print(json.dumps({"benchmarks":bench,"ranked":summary,"excluded":excluded}, ensure_ascii=False,indent=2))
