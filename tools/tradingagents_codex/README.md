# TradingAgents → Codex local adapter

Status (2026-09-30): **native full graph and research tool roundtrip passed with frozen public evidence; default live vendor stack not verified**.

This project-local adapter uses the installed `codex exec` command and Codex's
own ChatGPT login. It never extracts login tokens or puts them into an API key.
No API credits were purchased and no installed package, authentication file, or
global Codex configuration was modified.

## Evidence and limits

- `codex login status`: Logged in using ChatGPT.
- Installed CLI: 0.158.0-alpha.2.1; TradingAgents: 0.5.2.
- Seven offline contract tests passed: message/tool conversion and budget,
  rejection of unbound tools, rejection of incomplete turns, Pydantic parsing,
  timeout termination without automatic relaunch, local system-proxy inheritance,
  and preservation of explicit proxy settings / rejection of remote proxy substitution.
- The native TradingAgents market/fundamentals/news graph compiles with this
  adapter as both its quick and deep model. This is initialization, not research.
- Two bounded direct CLI probes returned no completed answer within 55 seconds.
  The isolated second probe reported `request timed out` and reconnect messages.
  Neither failure establishes an API balance problem. Actual responding model:
  UNKNOWN. These were the pre-fix results. After inheriting the existing local
  system proxy, the smoke request and a native AIP bear node both completed.

The connection prerequisite is now **passed**. The exact smoke answer was
`CODEX_BRIDGE_OK`; a native TradingAgents bear node produced
`AIP_RETROSPECTIVE_BEAR_REVIEW.md`. A later bounded AIP trial completed the native graph with 15 model calls and
24 native tool calls against frozen public evidence. Default live vendor data
acquisition remains unverified. See the full-trial review below. The retrospective
report was checked for scope and is not a refreshed buy/sell recommendation.
Structured tool calls are translated from a validated JSON envelope; this is a
local adaptation, not an upstream TradingAgents native Codex provider.

## Usage

Mount `/Volumes/EXTERNAL`. From the Serenity project root:

```sh
PYTHON_DOTENV_DISABLED=1 PYTHONDONTWRITEBYTECODE=1 \
  /Volumes/EXTERNAL/.codex-global-tools/uv-tools/tradingagents/bin/python \
  tools/tradingagents_codex/run.py check
```

`check` initializes the graph without making a model request. `smoke` requests one exact verification answer;
`aip-review` runs one real TradingAgents bear-research node against the public
company-research section of the September 29 report. It is explicitly a
retrospective review, not a refreshed investment recommendation. Each entry
point allows one model invocation, with a 55-second deadline; no silent retries.
Codex itself may reconnect within that deadline. Calls consume the applicable
Codex/ChatGPT allowance if processed; they are not unlimited free inference.

Offline checks:

```sh
PYTHON_DOTENV_DISABLED=1 PYTHONDONTWRITEBYTECODE=1 \
  /Volumes/EXTERNAL/.codex-global-tools/uv-tools/tradingagents/bin/python \
  -m unittest discover -s tools/tradingagents_codex -p 'test_bridge.py' -v
```

## Scope and generated files

- `bridge.py`: LangChain adapter, structured outputs and bound-tool translation.
- `run.py`: bounded startup/smoke/native-node trial; process-local factory hook.
- `test_bridge.py`: offline simulated subprocess tests, explicitly not live proof.
- `docs/research/tradingagents-codex-bridge-20260930/`: trial evidence and future
  per-call schema/status/response files. `check` created its empty `cache/` and
  `results/` directories. No global TradingAgents memory is read.
- Test temporary directories are created and removed by TemporaryDirectory.

No broker integration, order execution, service, scheduler or listening port.
Codex calls disable shell, apps, browser, plugin discovery and multi-agent tools,
use a read-only sandbox, skip global config, and run ephemerally. Research tool
requests return to the caller; this adapter never executes a requested function.

References: installed `codex exec --help`; installed TradingAgents source;
[official Codex integration documentation](https://developers.openai.com/siwc/token-sharing-open-source/codex-app-server).
The OAuth app-server route is a distinct alternative and was not implemented.

## Proxy inheritance fix (2026-09-30)

The adapter now supplies the already-enabled local macOS HTTPS proxy to its
Codex child process when no explicit process HTTPS/ALL proxy is present. It
preserves existing process settings, never logs or saves proxy addresses, and
does not change system settings. The changed route passed a bounded live smoke request and then a native
TradingAgents AIP retrospective bear-node call. Model identities in the logs
are requested models; the actual returned model identity remains UNKNOWN.

Live usage reported by Codex: smoke 18,211 input / 23 output tokens; native node
20,180 input / 775 output tokens (including 200 reasoning output tokens).
These calls use the applicable subscription allowance and are not cost-free
unlimited inference. The later full-graph trial is recorded separately below.

## Full native graph trial (2026-09-30)

`full_trial.py` runs the native graph with a 20-call budget and 90-second
per-call deadline, using the public packet in
`docs/research/tradingagents-aip-full-20260930/public_evidence.json`.
It completed in 15 model calls and 24 tool calls. The vendor functions are
replaced only in this process with snapshot readers; the native tool schemas
and ToolNodes remain in use. This does not validate the default live vendors.

The raw final rating was Hold, but research acceptance failed: the two-round
tool cap prevented the market node from requesting its mandatory verified
snapshot, and valuation/event inputs remained incomplete. Treat the output
as a workflow trial, not a buy/sell or holding recommendation. Review:
`docs/research/tradingagents-aip-full-20260930/REVIEW.md`.
