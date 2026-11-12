"""Native TradingAgents graph, Codex inference, explicitly frozen public data.

Original analyst tool schemas and ToolNodes are retained. Vendor reads are
replaced process-locally with timestamped public evidence; no cookies or keys.
No position input, trading, reflection memory or installed-package changes.
"""
import json
import os
from pathlib import Path
import threading
from datetime import datetime, timezone
from unittest.mock import patch

os.environ["PYTHON_DOTENV_DISABLED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

from bridge import CodexChatModel
from run import make_graph, ROOT
from tradingagents.agents import tools as research_tools
from tradingagents.dataflows.config import run_config


def main():
    root = ROOT / "docs/research/tradingagents-aip-full-20260930"
    packet = json.loads((root / "public_evidence.json").read_text())
    model = CodexChatModel(run_dir=str(root / "calls"), max_calls=20, timeout_seconds=90)
    graph = make_graph(model, root)
    log_lock = threading.Lock()

    def respond(name, *args, **kwargs):
        row = {"time_utc": datetime.now(timezone.utc).isoformat(), "name": name,
               "args": args, "kwargs": kwargs, "source": "frozen_public_evidence"}
        with log_lock:
            with (root / "tool_calls.jsonl").open("a") as handle:
                handle.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
        if name in {"get_fundamentals", "get_balance_sheet", "get_cashflow", "get_income_statement"}:
            section = packet["fundamentals"]
        elif name in {"get_stock_data", "get_verified_market_snapshot"}:
            section = packet["market"]
        elif name == "get_indicators":
            closes = [r[4] for r in packet["market"]["rows"]]
            section = {"calculated_sma20": sum(closes) / len(closes), "n": len(closes),
                       "as_of": "2026-09-29", "source": packet["market"]["source"],
                       "requested_indicator": args[1] if len(args) > 1 else None,
                       "caveat": "Only SMA20 calculated. RSI/MACD/EMA/50-200 day averages/ATR UNKNOWN. Do not invent them."}
        elif name in {"get_news", "get_global_news", "get_insider_transactions"}:
            section = packet["news"]
        elif name == "get_macro_indicators":
            section = {"vix": packet["market"]["vix"], "other_macro": "UNKNOWN"}
        else:
            section = {"status": "UNKNOWN", "reason": "Not collected in the bounded public-source trial"}
        return json.dumps({"tool": name, "cutoff_utc": packet["cutoff_utc"],
                           "data": section, "scope": "Snapshot tool, not a live vendor API; do not claim absent fields were retrieved."}, ensure_ascii=False)

    context = (
        "AIP is Arteris, Inc., Nasdaq-listed semiconductor NoC IP supplier. "
        "This is a bounded research trial as of 2026-09-30 05:20 UTC. Latest completed US session: 2026-09-29. "
        "Public sources have been frozen for audit. Call the supplied tools to obtain them. "
        "Missing evidence is UNKNOWN, not negative evidence. No account facts are supplied. "
        "No personalized share sizing, shorting or instructions to liquidate an assumed holding. "
        "Source snapshots may disagree; disclose rather than invent reconciliation. "
        "Valuation assumptions must be reproducible and distinguished from company disclosures. "
        "Be concise: each analyst/debater at most 500 Chinese characters plus essential tables."
    )
    state = graph.propagator.create_initial_state("AIP", "2026-09-30", instrument_context=context)
    status = {"status": "running", "max_model_calls": 20, "scope": "one native graph with frozen public-evidence tools", "portfolio": "not supplied"}
    (root / "RUN_STATUS.json").write_text(json.dumps(status, ensure_ascii=False, indent=2))
    with patch.object(research_tools, "route_to_vendor", side_effect=respond), \
         patch.object(research_tools, "build_verified_market_snapshot", side_effect=lambda *a, **k: respond("get_verified_market_snapshot", *a, **k)), \
         run_config(graph.config):
        try:
            for update in graph.graph.stream(state, config={"recursion_limit": 70, "max_concurrency": 1}, stream_mode="values"):
                state = update
                (root / "state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2, default=str))
                reports = [k for k in ["market_report", "fundamentals_report", "news_report", "investment_plan", "trader_investment_plan", "final_trade_decision"] if state.get(k)]
                print(json.dumps({"reports_completed": reports, "model_invocations_started": model._calls}), flush=True)
            status.update(status="workflow_completed", final_rating=state.get("final_rating"), model_invocations_started=model._calls)
            sections = ["# AIP TradingAgents 原生流程试跑\n\n公开资料快照 + Codex；不是完整买入验收。"]
            for key in ["market_report", "fundamentals_report", "news_report", "investment_debate_state", "investment_plan", "trader_investment_plan", "risk_debate_state", "final_trade_decision"]:
                value = state.get(key)
                if isinstance(value, dict): value = value.get("history", json.dumps(value, ensure_ascii=False))
                sections.append("## " + key + "\n\n" + str(value or "UNKNOWN"))
            (root / "RAW_REPORT.md").write_text("\n\n".join(sections))
        except Exception as exc:
            status.update(status="workflow_incomplete", exception_type=type(exc).__name__, model_invocations_started=model._calls)
            print(json.dumps(status), flush=True)
            raise
        finally:
            (root / "RUN_STATUS.json").write_text(json.dumps(status, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
