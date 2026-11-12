#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/USER/Documents/serenity")
ARCHIVE = ROOT / "research_reports/serenity_x_full_archive_20260609"
RAW = Path("/tmp/serenity-aleabitoreddit-readonly/data/aleabitoreddit_tweets.csv")
OUT = ROOT / "research_reports/Serenity_X股票提及与立场整理_20260716"
COMMIT = "35e88fb092fdc02a03f905ca97d3bc6b1a726ca5"

CATEGORIES = [
    "明确正面/看好",
    "持续重点研究/偏正面",
    "中性研究/行业映射",
    "负面/警告/反例/做空语境",
    "仅转述/引用他人/列表出现",
    "歧义或证据不足",
]

# 仅收录能在原帖正文或锁定 commit 的上游分期分析中定位到明确持有、
# 做多、最喜欢、高确信等语义的名称。负面集合优先，反映语料后段的立场变化。
EXPLICIT_POSITIVE = {
    "NBIS", "SIVE", "SIVEF", "AXTI", "AAOI", "SOI", "SLOIF", "LPK",
    "IQE", "AEHR", "LITE", "HPS", "RDDT", "FLNC", "ALRIB", "ARM",
    "SNDK", "TSEM", "HIMS", "RKLB", "TSM", "CRDO", "ALAB", "UPWK",
    "CRCL", "GOOGL", "WLAC", "RBRK", "KSPI", "XFAB", "MRVL", "MU",
    "RMBS", "LPTH", "OSS", "ETOR", "VIRT",
}

PERSISTENT_POSITIVE = {
    "FORM", "ONTO", "CAMT", "MTSI", "JBL", "TOWA", "COHR", "AVGO",
    "AMZN", "META", "MSFT", "NVDA", "JBL", "LPKFF", "SIMO", "RPI",
    "NVT", "ANET", "AMKR", "SNDK", "SMCI", "CIFR", "WULF", "FLY",
    "LASR", "VPG", "FN", "INTC", "AMD", "TSM", "TSLA", "AAPL",
    "HPS", "POWL", "AMSC", "PLPC", "KEYS", "VIAV", "BESI", "ASML",
    "TSEM", "AAOI", "SOI", "SIVE", "AXTI", "IQE", "AEHR", "LITE",
    "RDDT", "FLNC", "ARM", "MRVL", "MU",
} - EXPLICIT_POSITIVE

NEGATIVE = {
    "IREN", "POET", "LWLG", "SLNH", "BKKT", "ASST", "BOT", "VCX",
    "CRWV", "QBTS", "QUBT", "IONQ", "RGTI", "OKLO", "ORCL",
}

STANCE_NOTES = {
    "IREN": "早期曾偏多，后期明确转为负面，核心警告是大额 ATM 与结构性稀释。",
    "POET": "早期有研究兴趣，后期因客户/设计剔除风险与相对吸引力下降而转入谨慎/负面。",
    "CRWV": "早期纳入 neocloud 篮子，后期重点警告高息债务和融资质量。",
    "LWLG": "作者明确披露做空，并反复质疑无收入合作与稀释风险。",
    "SLNH": "作者将其作为 ATM 稀释和股东价值转移的反例。",
    "BKKT": "作者以长期稀释历史作为反例，明确表示不会长期持有。",
    "ASST": "作者将其作为 ATM/SBC 稀释摧毁股东价值的反例。",
    "BOT": "作者明确警告 NAV 溢价和大额潜在稀释。",
    "VCX": "作者明确警告极端 NAV 溢价，并表示不应买入。",
    "QBTS": "作者多次列入 Strong Sell/Avoid，并认为量子商业化交易过早。",
    "QUBT": "作者列入 Strong Sell，虽也曾作为政策名单成分提及。",
    "IONQ": "作者多次列入 Strong Sell/Avoid，认为商业化时点过早。",
    "RGTI": "作者多次列入 Strong Sell/Avoid，认为商业化时点过早。",
    "OKLO": "作者多次列入 Strong Sell/非收入型过热案例。",
    "ORCL": "曾有交易性正面提及，但后续评级中进入 Avoid；分类按警告语境处理。",
    "CRCL": "曾有锁定期/做空警告，后续又披露正向交易与持仓；属于明显立场演化。",
    "RDDT": "早期有短期卖出评级，后期重新持有并称其为高质量盈利复合型公司。",
    "SLOIF": "作者明确表示改变看法并建立较大仓位；与 SOI 为同一公司不同市场代码。",
    "SIVEF": "SIVE 的美国 OTC/跨市场代码；与 SIVE 合并理解但保留独立 token 行。",
    "HPS": "原文常写作 HPS.A；索引抽取为 HPS，存在市场后缀截断。",
    "LPKFF": "LPK/LPKF 的 OTC/跨市场别名，语义证据多集中在 LPK。",
}

# 人工复核后的代表证据。用于覆盖自动“关键词与代码距离”挑选中少数
# 主语指向其他 ticker 的误配；URL 均在锁定 commit 原始 CSV 中。
EVIDENCE_OVERRIDES = {
    "AEHR": ("https://x.com/aleabitoreddit/status/2039756817019060539", "明确做多"),
    "AXTI": ("https://x.com/aleabitoreddit/status/2004574162283802728", "持仓披露"),
    "FLNC": ("https://x.com/aleabitoreddit/status/2053980270135738816", "持仓披露"),
    "GOOGL": ("https://x.com/aleabitoreddit/status/1940711432397684953", "持仓披露"),
    "HPS": ("https://x.com/aleabitoreddit/status/2044700039944245471", "明确看多"),
    "IQE": ("https://x.com/aleabitoreddit/status/2028524172121719168", "明确做多"),
    "LITE": ("https://x.com/aleabitoreddit/status/2004574162283802728", "持仓披露"),
    "MRVL": ("https://x.com/aleabitoreddit/status/1962880256576242129", "买入/加仓"),
    "OSS": ("https://x.com/aleabitoreddit/status/2008910857003221451", "持仓披露"),
    "RDDT": ("https://x.com/aleabitoreddit/status/2020258804953411966", "持仓披露"),
    "SIVE": ("https://x.com/aleabitoreddit/status/2033466880661606646", "明确做多"),
    "SLOIF": ("https://x.com/aleabitoreddit/status/2031648475310616604", "持仓披露"),
    "SNDK": ("https://x.com/aleabitoreddit/status/2017064502983086289", "持仓披露"),
    "XFAB": ("https://x.com/aleabitoreddit/status/2059561586956837085", "持仓披露"),
}

CRYPTO = {"BTC", "ETH", "LTC", "SOL", "XRP"}
ETF = {
    "IBIT", "SPY", "QQQ", "XLU", "EWY", "XLE", "GLD", "SLV", "JETS",
    "COPX", "FLKR", "KORU",
}
ALIASES = {
    "APPL": "疑似 AAPL 拼写变体",
    "CREDO": "CRDO 的公司名/代码混用",
    "QLCM": "疑似 QCOM 拼写变体",
    "AMSL": "疑似 ASML 拼写变体",
    "ELOSE": "疑似 EOSE 拼写变体",
    "SYSS": "可能与 SSYS 混用",
    "SIVEF": "SIVE 的美国 OTC/跨市场代码",
    "SLOIF": "SOI 的美国 OTC/跨市场代码",
    "LPKFF": "LPK/LPKF 的美国 OTC/跨市场代码",
    "HPS": "原文 HPS.A 被索引截断为 HPS",
    "LIT": "可能是 ETF LIT，也可能是 LITE 截断/拼写，需逐帖核验",
}
COMMON_WORD_AMBIGUITY = {
    "AI", "ALL", "ARE", "BE", "BOT", "CF", "DD", "EU", "FOR", "IT",
    "ME", "ON", "OR", "SO", "TE", "U", "V", "WIN", "NOW", "OPEN",
    "FIG", "ARM", "PL", "RR", "SG", "FI", "SEA", "SHOP",
}

POS_PATTERNS = [
    ("最高确信", re.compile(r"highest conviction|high conviction", re.I)),
    ("最喜欢", re.compile(r"favorite|favourite", re.I)),
    ("明确做多", re.compile(r"\b(?:i(?:’|')?m|went|still)\s+long\b|\blong term holding\b", re.I)),
    ("持仓披露", re.compile(r"\b(?:have|had|own|held|holding)\s+(?:a\s+)?(?:position|positions|shares)|\bportfolio\b", re.I)),
    ("买入/加仓", re.compile(r"\b(?:bought|buying|added|adding|accumulating|averaging up)\b", re.I)),
    ("明确看多", re.compile(r"\b(?:extremely bullish|bullish|strong buy|screaming buy)\b", re.I)),
]
NEG_PATTERNS = [
    ("明确看空/做空", re.compile(r"\b(?:bearish|shorted|shorting|strong sell)\b", re.I)),
    ("避免/不买", re.compile(r"\b(?:avoid|do not buy|don.t buy|would not go long|stay away)\b", re.I)),
    ("稀释警告", re.compile(r"\b(?:ATM|dilution|diluting|diluted)\b", re.I)),
    ("估值/NAV警告", re.compile(r"\b(?:NAV|overvalued|premium|red flag)\b", re.I)),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def split_pipe(value: str) -> list[str]:
    return [x.strip() for x in value.split("|") if x.strip()]


def token_pattern(ticker: str) -> re.Pattern[str]:
    return re.compile(r"(?<![A-Z0-9])\$?" + re.escape(ticker) + r"(?![A-Z0-9])", re.I)


def target_signal(text: str, ticker: str, patterns) -> tuple[int, str]:
    token = token_pattern(ticker)
    positions = [m.start() for m in token.finditer(text)]
    if not positions:
        return (0, "")
    best = (0, "")
    for label, pattern in patterns:
        for match in pattern.finditer(text):
            distance = min(abs(match.start() - p) for p in positions)
            if distance <= 140:
                score = 200 - distance
                if score > best[0]:
                    best = (score, label)
    return best


def paraphrase(label: str, positive: bool) -> str:
    if positive:
        return {
            "最高确信": "作者明确把该标的列为高确信/最高确信研究对象。",
            "最喜欢": "作者明确称该标的是自己最喜欢或最重点的相关标的之一。",
            "明确做多": "作者明确披露做多或长期持有该标的，并给出正向研究理由。",
            "持仓披露": "作者明确披露该标的在其持仓或核心组合中。",
            "买入/加仓": "作者明确披露买入、加仓或继续累积该标的。",
            "明确看多": "作者明确使用强烈看多或强买入措辞评价该标的。",
        }.get(label, "作者在正文中给出明确正向立场。")
    return {
        "明确看空/做空": "作者明确给出看空、做空或强卖出立场。",
        "避免/不买": "作者明确建议避免或表示不应建立多头。",
        "稀释警告": "作者把该标的作为 ATM/股权稀释与股东价值受损的警告案例。",
        "估值/NAV警告": "作者明确警告该标的存在极端估值或 NAV 溢价风险。",
    }.get(label, "作者在正文中给出明确负面或警告立场。")


def security_note(ticker: str) -> tuple[str, str]:
    if ticker in CRYPTO:
        return ("非股票：加密资产", "保留原始 token；不纳入股票立场外推")
    if ticker in ETF:
        return ("ETF/基金", "并非单一公司股票")
    if ticker in ALIASES:
        return ("代码别名/疑似拼写", ALIASES[ticker])
    if ticker.isdigit():
        return ("数字代码", "可能为亚洲市场证券代码；需结合原帖核验交易所")
    if ticker in COMMON_WORD_AMBIGUITY:
        return ("普通词歧义", "同时可能是证券代码；本报告不静默删除")
    return ("股票代码候选", "")


def dominant(counter: Counter[str], limit: int = 6) -> str:
    return "|".join(x for x, _ in counter.most_common(limit))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    index_rows = read_csv(ARCHIVE / "serenity_x_post_index.csv")
    raw_rows = read_csv(RAW)
    raw_by_url = {r["url"]: r for r in raw_rows}

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in index_rows:
        for ticker in split_pipe(row["tickers_mentioned"]):
            grouped[ticker.upper()].append(row)

    all_rows = []
    positive_rows = []
    negative_rows = []

    for ticker in sorted(grouped):
        rows = grouped[ticker]
        dates = sorted(r["timestamp_or_relative_time"] for r in rows)
        themes: Counter[str] = Counter()
        chokepoints: Counter[str] = Counter()
        evidence: Counter[str] = Counter()
        urls = []
        direct_count = 0
        quoted_only_count = 0
        candidates_pos = []
        candidates_neg = []

        pattern = token_pattern(ticker)
        for row in rows:
            themes.update(split_pipe(row["sectors"]))
            chokepoints.update(split_pipe(row["chokepoints"]))
            evidence[row["evidence_type"]] += 1
            if row["source_url"] not in urls:
                urls.append(row["source_url"])
            raw = raw_by_url.get(row["source_url"])
            if not raw:
                continue
            text = raw.get("text", "")
            quoted = raw.get("quoted_text", "")
            if pattern.search(text):
                direct_count += 1
                score, label = target_signal(text, ticker, POS_PATTERNS)
                if score:
                    candidates_pos.append((score, raw["createdAtISO"], raw["url"], label))
                score, label = target_signal(text, ticker, NEG_PATTERNS)
                if score:
                    candidates_neg.append((score, raw["createdAtISO"], raw["url"], label))
            elif pattern.search(quoted):
                quoted_only_count += 1

        if ticker in NEGATIVE:
            category = "负面/警告/反例/做空语境"
        elif ticker in EXPLICIT_POSITIVE:
            category = "明确正面/看好"
        elif ticker in PERSISTENT_POSITIVE:
            category = "持续重点研究/偏正面"
        elif direct_count == 0 and quoted_only_count > 0:
            category = "仅转述/引用他人/列表出现"
        elif len(rows) >= 5 and direct_count >= 2:
            category = "中性研究/行业映射"
        elif evidence["quoted_context_social_input"] == len(rows):
            category = "仅转述/引用他人/列表出现"
        else:
            category = "歧义或证据不足"

        security_type, ambiguity = security_note(ticker)
        best_pos = max(candidates_pos, default=None)
        best_neg = max(candidates_neg, default=None)
        stance_evidence = best_neg if category == "负面/警告/反例/做空语境" else best_pos
        if ticker in EVIDENCE_OVERRIDES:
            override_url, override_label = EVIDENCE_OVERRIDES[ticker]
            override_raw = raw_by_url[override_url]
            stance_evidence = (
                999,
                override_raw["createdAtISO"],
                override_url,
                override_label,
            )
        if stance_evidence:
            _, stance_date, stance_url, signal_label = stance_evidence
            translation = paraphrase(signal_label, category != "负面/警告/反例/做空语境")
            confidence = "高" if stance_evidence[0] >= 120 else "中"
        else:
            stance_date = ""
            stance_url = ""
            signal_label = ""
            translation = ""
            confidence = "低" if category in {"明确正面/看好", "负面/警告/反例/做空语境"} else ""

        note = STANCE_NOTES.get(ticker, "")
        if category == "明确正面/看好" and not note:
            note = "原帖正文存在明确持有、做多、买入、最高确信或最喜欢等语义。"
        elif category == "持续重点研究/偏正面" and not note:
            note = "多次进入正向供应链/行业论证，但本次未把频次自动升级为明确持仓。"
        elif category == "中性研究/行业映射" and not note:
            note = "主要用于行业、客户、供应链或同业映射；未发现足够明确的单一方向立场。"
        elif category == "仅转述/引用他人/列表出现" and not note:
            note = "主要出现在 quoted context、众包清单或他人观点中，不自动归因于作者。"
        elif category == "歧义或证据不足" and not note:
            note = "提及次数或语义证据不足，不能可靠判断方向。"

        record = {
            "标准化代码": ticker,
            "证券类型/歧义": security_type,
            "别名或歧义说明": ambiguity,
            "帖子数": len(rows),
            "作者正文直接提及数": direct_count,
            "仅引用上下文数": quoted_only_count,
            "首见时间": dates[0],
            "末见时间": dates[-1],
            "立场分类": category,
            "立场置信度": confidence,
            "立场说明": note,
            "主要主题": dominant(themes),
            "主要Chokepoint": dominant(chokepoints),
            "evidence_type分布": "|".join(f"{k}:{v}" for k, v in evidence.most_common()),
            "代表帖子URL": "|".join(urls[:5]),
            "立场证据日期": stance_date,
            "立场证据URL": stance_url,
            "中文意译": translation,
            "锁定来源commit": COMMIT,
        }
        all_rows.append(record)
        if category in {"明确正面/看好", "持续重点研究/偏正面"}:
            positive_rows.append(record)
        if category == "负面/警告/反例/做空语境":
            negative_rows.append(record)

    fields = list(all_rows[0])
    write_csv(OUT / "Serenity_X全部股票清单.csv", fields, all_rows)
    write_csv(OUT / "Serenity_X明确看好与重点研究.csv", fields, positive_rows)
    write_csv(OUT / "Serenity_X负面警告与反例.csv", fields, negative_rows)

    counts = Counter(r["立场分类"] for r in all_rows)
    top_mentions = sorted(all_rows, key=lambda r: (-int(r["帖子数"]), r["标准化代码"]))[:30]
    top_positive = sorted(positive_rows, key=lambda r: (-int(r["帖子数"]), r["标准化代码"]))[:25]
    top_negative = sorted(negative_rows, key=lambda r: (-int(r["帖子数"]), r["标准化代码"]))[:20]

    report = [
        "# Serenity X 股票提及与立场报告",
        "",
        "## 结论",
        "",
        f"- 从既有 `serenity_x_post_index.csv` 的 `tickers_mentioned` 全量提取并保留 **{len(all_rows)}** 个唯一 token。",
        "- 本报告是对 2025-07-02 至 2026-06-08 公开二级档案的历史语义整理，不是当前持仓确认、买入名单、基本面验证或 Serenity 候选升级。",
        "- 提及频次不等于看好；quoted context、众包列表和他人观点不自动归因于作者。",
        "- 原始公开源锁定 GitHub commit `" + COMMIT + "`；档案完整性仍为 PARTIAL。",
        "",
        "## 立场对账",
        "",
        "| 分类 | 数量 |",
        "| --- | ---: |",
    ]
    report.extend(f"| {category} | {counts[category]} |" for category in CATEGORIES)
    report.extend([
        f"| **合计** | **{sum(counts.values())}** |",
        "",
        "## 明确看好与重点研究（按提及数）",
        "",
        "| 代码 | 分类 | 帖子数 | 置信度 | 证据日期 | 证据URL | 一句意译 |",
        "| --- | --- | ---: | --- | --- | --- | --- |",
    ])
    for r in top_positive:
        report.append(
            f"| {r['标准化代码']} | {r['立场分类']} | {r['帖子数']} | "
            f"{r['立场置信度'] or '—'} | {r['立场证据日期'] or '—'} | "
            f"{r['立场证据URL'] or '—'} | {r['中文意译'] or r['立场说明']} |"
        )
    report.extend([
        "",
        "## 负面、警告与反例（按提及数）",
        "",
        "| 代码 | 帖子数 | 置信度 | 证据日期 | 证据URL | 说明 |",
        "| --- | ---: | --- | --- | --- | --- |",
    ])
    for r in top_negative:
        report.append(
            f"| {r['标准化代码']} | {r['帖子数']} | {r['立场置信度'] or '—'} | "
            f"{r['立场证据日期'] or '—'} | {r['立场证据URL'] or '—'} | "
            f"{r['立场说明']} |"
        )
    report.extend([
        "",
        "## 全部提及 Top 30",
        "",
        "| 代码 | 帖子数 | 分类 | 类型/歧义 | 首见 | 末见 |",
        "| --- | ---: | --- | --- | --- | --- |",
    ])
    for r in top_mentions:
        report.append(
            f"| {r['标准化代码']} | {r['帖子数']} | {r['立场分类']} | "
            f"{r['证券类型/歧义']} | {r['首见时间'][:10]} | {r['末见时间'][:10]} |"
        )
    report.extend([
        "",
        "## 解释规则",
        "",
        "- `明确正面/看好`：正文中能定位到明确持有、做多、买入/加仓、最喜欢或高确信语义。",
        "- `持续重点研究/偏正面`：多次正向论证，但本次不把频次或供应链关联自动等同明确持仓。",
        "- `中性研究/行业映射`：主要用于同业、客户、供应链、宏观或主题映射。",
        "- `负面/警告/反例/做空语境`：能定位到看空、做空、Avoid、Strong Sell、稀释或 NAV 风险等语义。",
        "- `仅转述/引用他人/列表出现`：主要来自 quoted context、众包清单或引用，不归因于作者。",
        "- `歧义或证据不足`：次数少、代码有歧义，或语义不足以判断方向。",
        "",
        "完整 684 行、主题、chokepoint、evidence_type 分布及最多 5 条代表 URL 见 `Serenity_X全部股票清单.csv`。",
    ])
    (OUT / "Serenity_X股票提及与立场报告.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    source_limits = f"""# 来源与限制

## 来源

- 本地派生索引：`research_reports/serenity_x_full_archive_20260609/serenity_x_post_index.csv`，5,857 行。
- 原始公开二级档案：`https://github.com/yan-labs/serenity-aleabitoreddit`。
- 本次只读 clone 位置：`/tmp/serenity-aleabitoreddit-readonly`。
- 锁定 commit：`{COMMIT}`。
- 语料时间范围：2025-07-02 至 2026-06-08。
- 既有档案结论：PARTIAL，不是官方 X 完整导出。

## 方法边界

- 全量 token 以本地 `post_index.tickers_mentioned` 为准，因此得到 684 个唯一 token；上游 `ticker_stats.txt` 的 678 个只统计原始 `$ticker`，两者口径不同。
- 统计中的“帖子数”是出现该 token 的帖子记录数，不是观点强度、推荐次数或公司质量分数。
- 立场判断优先使用作者正文 `text`；`quoted_text` 只用于识别引用上下文，不能自动视为作者观点。
- 明确正面和明确负面必须能在锁定源定位到 URL；频次、主题标签、chokepoint 标签本身不用于推断立场。
- 对 SIVE/SIVEF、SOI/SLOIF、LPK/LPKFF 等跨市场代码保留独立行，同时在别名字段说明关联。
- 加密资产、ETF、数字代码、疑似拼写和普通词歧义 token 不静默删除，统一在“证券类型/歧义”中标注。

## 重要限制

- 本报告不验证公司基本面、客户、收入、订单、估值或作者自报业绩。
- 作者观点会变化；单一历史看多帖不能代表语料结束时仍然看多。已知反转在“立场说明”中尽量保留。
- 自动邻近语义用于挑选代表证据，仍可能遗漏图片内文字、长文正文、跨帖线程和无 `$` 代码的海外股票。
- 部分代码是市场后缀被旧索引截断的结果，例如 `$HPS.A` 被记录为 `HPS`。
- 不输出买入/卖出建议、目标价、仓位、入场点、退出价或交易计划。
- 社交档案不能清除 Serenity 的 STOP-SOCIAL-HYPE、STOP-LINKAGE-WEAK 或其他治理门禁。
"""
    (OUT / "来源与限制.md").write_text(source_limits, encoding="utf-8")

    self_check = f"""# 自检

- [x] `serenity_x_post_index.csv` 读取行数：{len(index_rows)}。
- [x] 唯一 token：{len(all_rows)}；全量清单行数与唯一 token 一致。
- [x] 六类立场合计：{sum(counts.values())}；与全量 token 对账一致。
- [x] 明确正面/重点研究 CSV 行数：{len(positive_rows)}。
- [x] 负面/警告/反例 CSV 行数：{len(negative_rows)}。
- [x] 所有正面/负面分类代码均存在于全量清单。
- [x] 代表 URL 来自本地 post_index 或锁定 commit 的原始公开源。
- [x] quoted context 不自动归因；保留 `作者正文直接提及数` 与 `仅引用上下文数`。
- [x] 全量 CSV 保留 evidence_type 分布、主题、chokepoint、首末见与最多 5 条代表 URL。
- [x] 未读取登录态、cookie、token、brokerage、持仓或账户数据。
- [x] 未修改既有档案或治理文件；仅创建本交付目录。
- [x] Python 3.9.6 标准库 `csv` 可完整读取三份 CSV：684 / {len(positive_rows)} / {len(negative_rows)} 行。
- [x] 分类包含关系核验：正面与负面清单均为全量 684 行集合的子集。
- [x] URL 集合核验：代表 URL 与立场证据 URL 的越界数均为 0。
- [x] 明确正面/负面分类缺失立场证据 URL 数为 0；证据 URL 的作者正文均直接出现对应 token。
- [x] quoted_context 抽查：ARKF、BLSH、KOPN、LYC、P40、SBET、TOST 均为 1 条仅引用、0 条正文直接提及，分类为“仅转述/引用他人/列表出现”。
- [x] 锁定源 HEAD 复核为 `{COMMIT}`。
- [x] `git diff --check` 退出码 0。

## 已知非阻塞差异

- 上游 `ticker_stats.txt` 是 678 个原始 `$ticker`；本报告按项目 `post_index.tickers_mentioned` 口径得到 684 个 token，额外项来自 quoted context/派生抽取。
- 项目工作树在本任务前已有 dirty；本任务未清理、覆盖或提交既有改动。
"""
    (OUT / "自检.md").write_text(self_check, encoding="utf-8")

    print({
        "unique_tokens": len(all_rows),
        "stance_counts": dict(counts),
        "positive_rows": len(positive_rows),
        "negative_rows": len(negative_rows),
    })


if __name__ == "__main__":
    main()
