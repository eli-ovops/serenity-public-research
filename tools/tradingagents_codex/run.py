"""Bounded entry point. No installed packages or user configs are modified."""
import argparse
from copy import deepcopy
import json
import os
from pathlib import Path
from unittest.mock import patch

# Must precede any TradingAgents import; never load project .env files.
os.environ["PYTHON_DOTENV_DISABLED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

from bridge import CodexChatModel

ROOT = Path(__file__).resolve().parents[2]


def make_graph(model, directory, selected_analysts=None):
    """Inject this provider for graph construction only, restoring the factory.

    This process-local hook is for TradingAgents 0.5.2. It does not patch its
    installed source or start propagation. All nodes share the bounded model.
    """
    from tradingagents.default_config import DEFAULT_CONFIG
    from tradingagents.graph import trading_graph

    cfg = deepcopy(DEFAULT_CONFIG)
    cfg.update(llm_provider="codex_cli", deep_think_llm=model.model_name,
               quick_think_llm=model.model_name, max_debate_rounds=1,
               max_risk_discuss_rounds=1, max_tool_rounds=2, output_language="简体中文",
               checkpoint_enabled=False, results_dir=str(directory / "results"),
               data_cache_dir=str(directory / "cache"),
               memory_log_path=str(directory / "trial_memory.md"))

    class Client:
        def get_llm(self):
            return model

    with patch.object(trading_graph, "create_llm_client", return_value=Client()):
        return trading_graph.TradingAgentsGraph(
            selected_analysts if selected_analysts is not None else ["market", "fundamentals", "news"], config=cfg, debug=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["check", "smoke", "aip-review"])
    args = parser.parse_args()
    root = ROOT / "docs/research/tradingagents-codex-bridge-20260930"
    model = CodexChatModel(run_dir=str(root / "calls"), max_calls=1)
    if args.mode == "check":
        graph = make_graph(model, root)
        assert graph.quick_thinking_llm is model and graph.deep_thinking_llm is model
        print("PASS: TradingAgents graph compiled with the Codex adapter; no model request made")
        return
    if args.mode == "smoke":
        model.model_name = "gpt-6-luna"
        model.effort = "low"
        result = model.invoke("只回复 CODEX_BRIDGE_OK。这是连接验证，不需要任何数据或工具。")
        if result.content.strip() != "CODEX_BRIDGE_OK" or result.tool_calls:
            raise RuntimeError("Unexpected smoke-test response")
        print(result.content)
        return

    from tradingagents.agents.researchers.bear_researcher import create_bear_researcher
    from tradingagents.dataflows.config import set_config
    set_config({"output_language": "简体中文"})
    source = ROOT / "docs/research/serenity-daily-20260929/REPORT.md"
    # Explicit public company-research section only. Do not send the holdings
    # section or the whole daily report to the subprocess.
    report = source.read_text().split("## 三家小公司的新估值地图\n", 1)[1].split("\n## 已有持仓逐项", 1)[0]
    state = {
        "company_of_interest": "AIP", "trade_date": "2026-09-29", "asset_type": "stock",
        "instrument_context": "AIP = Arteris, Inc. This is a retrospective evidence review, not a current trading recommendation. Review only AIP facts. Do not invent current prices or refresh dates.",
        "market_report": "No fresh market data. Retrospective review only.",
        "news_report": "No fresh news or event verification.", "sentiment_report": "Not provided",
        "fundamentals_report": report,
        "investment_debate_state": {"history": "", "bull_history": "", "bear_history": "",
                                    "current_response": "", "count": 0},
    }
    result = create_bear_researcher(model)(state)
    output = root / "AIP_RETROSPECTIVE_BEAR_REVIEW.md"
    output.write_text("# Retrospective integration trial, not a current buy/sell decision\n\n"
                      + result["investment_debate_state"]["bear_history"])
    print(json.dumps({"output": str(output), "scope": "one native TradingAgents bear node"}))


if __name__ == "__main__":
    main()
