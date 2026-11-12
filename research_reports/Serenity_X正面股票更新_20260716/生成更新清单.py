#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

RAW = Path("/tmp/serenity-x-20260716-10712/data/aleabitoreddit_tweets.csv")
OUT = Path("/Users/USER/Documents/serenity/research_reports/Serenity_X正面股票更新_20260716")
COMMIT = "8f99c7aa7e6578fe7d951fd8d880401902387d69"

EXPLICIT = {
    "AAOI", "ACMR", "AEHR", "ALAB", "ALRIB", "ARM", "AXTI", "CBRS", "CCXI",
    "CRCL", "CRDO", "ETOR", "FLNC", "GOOGL", "HIMS", "HPS", "IQE", "KSPI",
    "LITE", "LPK", "LPTH", "MRVL", "MU", "NBIS", "OSS", "RBRK", "RDDT",
    "RKLB", "RMBS", "SIVE", "SIVEF", "SLOIF", "SNDK", "SOI", "TSEM", "TSM",
    "UPWK", "VIRT", "WLAC", "XFAB",
}

PERSISTENT = {
    "AAPL", "AMD", "AMKR", "AMSC", "AMZN", "ANET", "AOSL", "ASML", "ASTS",
    "AVGO", "BESI", "CAMT", "CIFR", "COHR", "FLY", "FN", "FORM", "INTC",
    "JBL", "KEYS", "LASR", "LPKFF", "META", "MSFT", "MTSI", "NVDA", "NVT",
    "ONTO", "OUST", "PLPC", "POET", "POWI", "POWL", "RPI", "SIMO", "SMCI",
    "TOWA", "TSLA", "VIAV", "VPG", "WULF",
}

SPECIAL = [
    {
        "ticker": "3231.TW",
        "name": "Wistron（纬创）",
        "category": "明确正面/看好",
        "count": 0,
        "latest": "2026-06-20",
        "confidence": "高",
        "summary": "称其为自 SIVE 以来见过的最佳 NAV 折价加 AI 增长标的之一，并表示计划提高集中度。",
        "url": "https://x.com/aleabitoreddit/status/2068180134667182470",
        "note": "当前原始CSV存在6月9日至21日缺口；本项来自锁定仓库的增量theses记录。",
    },
    {
        "ticker": "2316.HK/WUS",
        "name": "WUS",
        "category": "明确正面/看好",
        "count": 0,
        "latest": "2026-06-20",
        "confidence": "中",
        "summary": "披露为既有核心持仓，并把H股子公司上市、NAV折价及激进股东介入列为潜在重估路径。",
        "url": "https://x.com/aleabitoreddit/status/2068180134667182470",
        "note": "代码/公司映射沿用锁定仓库theses；原始CSV缺少对应日期记录，需二次核实。",
    },
    {
        "ticker": "138080.KQ",
        "name": "OE Solutions",
        "category": "持续重点研究/偏正面",
        "count": 0,
        "latest": "2026-06-23",
        "confidence": "中",
        "summary": "认为其在稀缺EML/CW激光IP与较小市值背景下，是较合理的潜在并购目标。",
        "url": "https://x.com/aleabitoreddit/status/2069230221388333366",
        "note": "上游theses注明原帖长文本存在截断，属于研究线索而非已确认交易。",
    },
    {
        "ticker": "未给代码",
        "name": "Harmonic Drive",
        "category": "明确正面/看好",
        "count": 0,
        "latest": "2026-06-30",
        "confidence": "高",
        "summary": "在机器人上游部件敞口中明确披露当前持有Harmonic Drive。",
        "url": "https://x.com/aleabitoreddit/status/2071730699363881241",
        "note": "原帖未给证券代码，本清单不擅自补代码。",
    },
]

SPECIFIC = {
    "CCXI": "明确披露做多，并称通过CCXI获得Agility Robotics敞口、为其机器人方向最高集中度；但交易结构/上市仍需核验。",
    "CBRS": "披露为Cerebras的试探性、谨慎仓位；看好稀缺高速推理容量，但明确提示仓位与论点仍会演化。",
    "ACMR": "锁定仓库增量研究记录显示其为既有核心持仓，并计划提高集中度；原始CSV缺口导致计数可能偏低。",
    "AMZN": "称Amazon是当前最喜欢的hyperscaler，并认为其是实体AI/机器人采用的清晰受益者。",
    "SIVE": "反复披露大额持仓、方向性确信，并称其为当前最喜欢的股票之一及潜在下一只LITE。",
    "AAOI": "仍属正面光通信篮子，但最新明确校准：主要收入来自可插拔产品，尚无CPO design win，商业时间待定。",
    "POET": "由此前谨慎/负面语境转为建设性研究：最新用其AGM信息强化激光供给短缺延续至2029的判断；未见新增持仓披露。",
    "IREN": "不纳入：认可资产/并购潜力，但仍因ATM和SBC融资结构表示难以看多。",
    "ASTS": "长期方向仍偏正面，并用于LEO卫星网络产业验证；最新也提示相对瓶颈股存在机会成本。",
    "WULF": "把Anthropic相关大型数据中心租约视为neocloud/colo板块的积极验证，但不是对所有neocloud的笼统背书。",
    "AOSL": "作为美国功率半导体主题受益者之一被正向提及，属于产业映射而非持仓披露。",
    "POWI": "作为美国功率半导体主题受益者之一被正向提及，属于产业映射而非持仓披露。",
    "OUST": "被视为中国激光雷达厂商受限后可能填补西方市场空缺的受益者，属于事件驱动研究映射。",
}

POS_RE = re.compile(
    r"\b(bought|buying|added|adding|long|bullish|favorite|favourite|conviction|"
    r"position|holding|own|best|love|clear winner|buying opportunity|benefit)\b",
    re.I,
)

EVIDENCE_OVERRIDE = {
    "AAOI": "https://x.com/aleabitoreddit/status/2076763334930812936",
    "AMZN": "https://x.com/aleabitoreddit/status/2069655980456149142",
    "AOSL": "https://x.com/aleabitoreddit/status/2070304723262210194",
    "ASTS": "https://x.com/aleabitoreddit/status/2071545016007467486",
    "AXTI": "https://x.com/aleabitoreddit/status/2074007618046345249",
    "CBRS": "https://x.com/aleabitoreddit/status/2070758710599954450",
    "CCXI": "https://x.com/aleabitoreddit/status/2072636916173066624",
    "IQE": "https://x.com/aleabitoreddit/status/2074007618046345249",
    "LITE": "https://x.com/aleabitoreddit/status/2072726120706007465",
    "MU": "https://x.com/aleabitoreddit/status/2073793206408667392",
    "OUST": "https://x.com/aleabitoreddit/status/2074587024959709419",
    "POET": "https://x.com/aleabitoreddit/status/2071488272245944399",
    "POWI": "https://x.com/aleabitoreddit/status/2070304723262210194",
    "SIVE": "https://x.com/aleabitoreddit/status/2074504394608193799",
    "SNDK": "https://x.com/aleabitoreddit/status/2073793206408667392",
    "TSEM": "https://x.com/aleabitoreddit/status/2077039373711970804",
    "TSM": "https://x.com/aleabitoreddit/status/2069422448345518346",
    "WULF": "https://x.com/aleabitoreddit/status/2074109998544846954",
    "XFAB": "https://x.com/aleabitoreddit/status/2074063175293809150",
}


def pattern(ticker: str) -> re.Pattern[str]:
    return re.compile(r"(?<![A-Z0-9])\$" + re.escape(ticker) + r"(?![A-Z0-9])", re.I)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with RAW.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    selected = EXPLICIT | PERSISTENT
    for row in rows:
        text = row["text"]
        for ticker in selected:
            if pattern(ticker).search(text):
                grouped[ticker].append(row)

    output = []
    for ticker in sorted(selected):
        mentions = grouped[ticker]
        latest = max((r["createdAtLocal"][:10] for r in mentions), default="")
        positive_candidates = [r for r in mentions if POS_RE.search(r["text"])]
        evidence = max(positive_candidates or mentions, key=lambda r: r["createdAtISO"]) if mentions else None
        category = "明确正面/看好" if ticker in EXPLICIT else "持续重点研究/偏正面"
        confidence = "高" if category == "明确正面/看好" else "中"
        summary = SPECIFIC.get(
            ticker,
            "作者曾给出明确正向立场、持仓/做多披露或持续以正面框架跟踪。"
            if category == "明确正面/看好"
            else "作者持续作为重点产业链或公司研究对象，整体语境偏正面，但不等同于当前持仓。",
        )
        note = ""
        if ticker == "ACMR":
            latest = "2026-06-20"
            evidence_url = "https://x.com/aleabitoreddit/status/2068180134667182470"
            note = "最新信号来自锁定仓库theses；原始CSV存在6月9日至21日缺口。"
        else:
            evidence_url = EVIDENCE_OVERRIDE.get(ticker, evidence["url"] if evidence else "")
        if ticker == "SIVEF":
            note = "SIVE的美国OTC/跨市场代码，独立保留。"
        elif ticker == "SLOIF":
            note = "SOI的美国OTC/跨市场代码，独立保留。"
        elif ticker == "LPKFF":
            note = "LPK/LPKF的美国OTC/跨市场代码，独立保留。"
        elif ticker == "HPS":
            note = "原文常写HPS.A，抽取时保留为HPS。"
        output.append(
            {
                "ticker": ticker,
                "name": "",
                "category": category,
                "count": len(mentions),
                "latest": latest,
                "confidence": confidence,
                "summary": summary,
                "url": evidence_url,
                "note": note,
            }
        )

    output.extend(SPECIAL)
    order = {"明确正面/看好": 0, "持续重点研究/偏正面": 1}
    output.sort(key=lambda x: (order[x["category"]], -int(x["count"]), x["ticker"]))

    fields = ["分类", "代码", "名称", "原始正文提及次数", "最近提及日期", "置信度", "立场简述", "代表证据URL", "备注"]
    with (OUT / "Serenity_X正面看好股票全清单_截至20260716.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for x in output:
            w.writerow(
                {
                    "分类": x["category"],
                    "代码": x["ticker"],
                    "名称": x["name"],
                    "原始正文提及次数": x["count"],
                    "最近提及日期": x["latest"],
                    "置信度": x["confidence"],
                    "立场简述": x["summary"],
                    "代表证据URL": x["url"],
                    "备注": x["note"],
                }
            )

    explicit = [x for x in output if x["category"] == "明确正面/看好"]
    persistent = [x for x in output if x["category"] == "持续重点研究/偏正面"]
    lines = [
        "# Serenity X 正面看好股票全清单（截至2026-07-16）",
        "",
        f"- 锁定上游 commit：`{COMMIT}`",
        f"- 原始公开帖子记录：{len(rows):,} 条",
        f"- 语料实际最新时间：{max(r['createdAtLocal'] for r in rows)}（北京时间）",
        f"- 明确正面/看好：{len(explicit)} 项",
        f"- 持续重点研究/偏正面：{len(persistent)} 项",
        f"- 合计：{len(output)} 项",
        "",
        "> 这是历史公开观点索引，不是当前持仓确认或买入清单。原始CSV在2026-06-09至2026-06-21存在覆盖缺口，见《来源与限制》。",
        "",
        "## 明确正面/看好",
        "",
        "| 代码/名称 | 次数 | 最近提及 | 置信度 | 简述 | 证据 |",
        "|---|---:|---|---|---|---|",
    ]
    for x in explicit:
        label = x["ticker"] + (f" / {x['name']}" if x["name"] else "")
        lines.append(f"| {label} | {x['count']} | {x['latest']} | {x['confidence']} | {x['summary']} | [原帖]({x['url']}) |")
    lines += [
        "",
        "## 持续重点研究/偏正面",
        "",
        "| 代码/名称 | 次数 | 最近提及 | 置信度 | 简述 | 证据 |",
        "|---|---:|---|---|---|---|",
    ]
    for x in persistent:
        label = x["ticker"] + (f" / {x['name']}" if x["name"] else "")
        lines.append(f"| {label} | {x['count']} | {x['latest']} | {x['confidence']} | {x['summary']} | [原帖]({x['url']}) |")
    (OUT / "Serenity_X正面看好股票全清单_截至20260716.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
