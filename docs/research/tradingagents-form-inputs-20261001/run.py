"""Native TradingAgents graph, Codex inference, explicitly frozen public data.

Original analyst tool schemas and ToolNodes are retained. Vendor reads are
replaced process-locally with timestamped public evidence; no cookies or keys.
No position input, trading, reflection memory or installed-package changes.
"""
import json
import os
from pathlib import Path
import threading
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/"tools/tradingagents_codex"))
from datetime import datetime, timezone
from unittest.mock import patch

os.environ["PYTHON_DOTENV_DISABLED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

from bridge import CodexChatModel
from evidence_adapter import EvidenceAdapter
from run import make_graph, ROOT
from tradingagents.agents import tools as research_tools
from tradingagents.dataflows.config import run_config


def main():
    root = ROOT / "docs/research/tradingagents-form-inputs-20261001"
    packet = json.loads((root / "packet.json").read_text())
    started = time.monotonic()
    class BoundedModel(CodexChatModel):
        def _generate(self, *args, **kwargs):
            remaining = int(900 - (time.monotonic() - started))
            if remaining <= 0:
                raise RuntimeError("Aggregate 900 second budget exhausted")
            self.timeout_seconds = min(300, remaining)
            return super()._generate(*args, **kwargs)
    model = BoundedModel(run_dir=str(root / "calls"), max_calls=20, timeout_seconds=300,
        progress_interval_seconds=10, model_name="gpt-6.1-sol", effort="medium",
        codex_binary="/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex")
    graph = make_graph(model, root)
    log_lock = threading.Lock()

    def respond(name, *args, **kwargs):
        row = {"time_utc": datetime.now(timezone.utc).isoformat(), "name": name,
               "args": args, "kwargs": kwargs, "source": "typed_public_evidence_snapshot"}
        with log_lock:
            with (root / "tool_calls.jsonl").open("a") as handle:
                handle.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
        return EvidenceAdapter(packet).respond(name,*args,**kwargs)

    context = ("FORM FormFactor. Research date 2026-10-01; latest completed session 2026-09-30. "
        "Tools serve newly refreshed public data plus precise 10-Q statement sections. Annual statements not collected. "
        "Use supported tools only. Unknown global news/macros are not company hard-gate failures. "
        "All source dates and gap labels remain binding. No accounts, holdings, sizing, execution or imagined positions. "
        "Native Hold label cannot replace the project research status. Final body must list each of fundamental, valuation, event, market, economic invalidation gates; then research status separately from account unknown. "
        "Do not mechanically carry prior WAIT/HOLD or140cap. 2028 EPS and PE require a defensible bridge. Do not treat ordinary investor conference as binary. "
        "Analysis <=600 Chinese characters per node plus essential table. Identify incremental evidence and counterevidence, no invented facts. " + packet['policy'])

    state = graph.propagator.create_initial_state("FORM", "2026-10-01", instrument_context=context)
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
            sections = ["# FORM TradingAgents 原生流程试跑\n\n公开资料快照 + Codex；不是完整买入验收。"]
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
