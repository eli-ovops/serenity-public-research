#!/usr/bin/env python3
"""Project entry to the pinned suoha skill; public research, no account access.

The upstream research lens and the project's portfolio decisions remain separate.
All upstream subprocesses get a literal credential-free environment. Values are
future scenario values until an explicit discount rate is supplied here.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
SKILL = PROJECT / ".agents/skills/suoha-serenity-skill"
COMMIT = "8391ab7b1bf44000dd99bf69664b8f2e03267d16"


def clean_environment() -> dict[str, str]:
    # Do not copy or inspect os.environ, optional API keys, cookies, or profiles.
    return {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "PYTHONNOUSERSITE": "1",
            "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUTF8": "1", "LC_ALL": "en_US.UTF-8"}


def project_path(raw: str, *, must_exist: bool = False) -> Path:
    p = Path(raw)
    p = (p if p.is_absolute() else PROJECT / p).resolve()
    private_names = {".git", ".ssh", ".aws", ".codex", "credentials", "secrets", "cookies", "profiles",
                     "auth.json", "credentials.json", "secrets.json", "api_keys.json"}
    if (not p.is_relative_to(PROJECT) or any(x.startswith(".env") or x.lower() in private_names for x in p.parts[len(PROJECT.parts):])):
        raise ValueError("Input/output must stay inside the project and must not be an environment file")
    if must_exist and (not p.is_file() or p.suffix != ".json"):
        raise ValueError("Input must be an existing project JSON research file")
    return p


def validate_snapshot_reference(lens: dict, lens_path: Path) -> None:
    """Check every path the upstream validator may read, before launching it."""
    raw = (lens.get("live_data") or {}).get("snapshot_path")
    if not isinstance(raw, str) or not raw.strip():
        return  # the upstream schema still checks whether the field is required
    ref = Path(raw)
    if ".." in ref.parts:
        raise ValueError("Snapshot reference traversal is forbidden; use an explicit project JSON path")
    candidates = [ref] if ref.is_absolute() else [
        PROJECT / ref, SKILL / ref, lens_path.parent / ref,
        lens_path.parent / "snapshots" / ref.name, lens_path.parent / ref.name]
    safe = [project_path(str(p)) for p in candidates]
    if any(p.suffix != ".json" for p in safe):
        raise ValueError("Snapshot references must be public research JSON files")
    if not any(p.is_file() for p in safe):
        raise ValueError("Referenced snapshot unavailable: provenance remains unverified")


def fresh_output(raw: str) -> Path:
    p = project_path(raw)
    if p.exists():
        raise ValueError("Output already exists; choose a new run path instead of overwriting evidence")
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def run_upstream(script: str, argv: list[str], receipt: Path) -> int:
    command = [sys.executable, str(SKILL / script), *argv]
    started = datetime.now(timezone.utc).isoformat()
    try:
        r = subprocess.run(command, cwd=PROJECT, env=clean_environment(),
                           capture_output=True, text=True, timeout=180)
        out = {"started_at_utc": started, "finished_at_utc": datetime.now(timezone.utc).isoformat(),
               "upstream_commit": COMMIT, "command": command, "exit_code": r.returncode,
               "environment": "literal public-only allowlist; no ambient secrets", "stdout": r.stdout,
               "stderr": r.stderr, "process_success_is_not_research_completion": True}
        receipt.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(r.stdout, end="")
        print(r.stderr, end="", file=sys.stderr)
        return r.returncode
    except subprocess.TimeoutExpired as exc:
        receipt.write_text(json.dumps({"started_at_utc": started, "exit_code": None,
                           "status": "bounded_timeout_180s", "command": command}) + "\n")
        print("Finite run timed out; inspect saved evidence, do not silently retry", file=sys.stderr)
        return 124


def discounted_scenarios(lens: dict, rate: float) -> dict:
    if not math.isfinite(rate) or not 0 <= rate <= 1:
        raise ValueError("An explicit annual discount rate in [0,1] is required")
    rows = []
    for scenario in lens["valuation"]["scenarios"]:
        years = scenario.get("horizon_years")
        terminal = scenario.get("implied_per_share")
        if not isinstance(years, (float, int)) or years < 0 or not math.isfinite(years):
            raise ValueError("Each scenario needs its own finite, nonnegative horizon_years")
        if not isinstance(terminal, (float, int)) or not math.isfinite(terminal):
            raise ValueError("Upstream computed terminal value missing or invalid")
        rows.append({"name": scenario["name"], "terminal_per_share": terminal,
                     "horizon_years": years, "annual_discount_rate": rate,
                     "present_value_per_share": terminal / (1 + rate) ** years,
                     "formula": "terminal_per_share / (1 + annual_discount_rate) ** horizon_years"})
    return {"kind": "explicit_discount_bridge_not_buy_limit", "upstream_commit": COMMIT,
            "currency": lens["valuation"]["current"].get("currency"), "scenarios": rows,
            "limitations": ["author assumptions are not company guidance", "discount rate is explicit author input",
                            "not an entry or exit instruction", "does not replace project financial/market/event/risk gates"]}


def check_valuation_inputs(lens: dict) -> None:
    warnings = (lens.get("live_data") or {}).get("warnings_addressed") or []
    unknown_debt = any("net_debt_unknown" in str(w.get("warning", ""))
                       for w in warnings if isinstance(w, dict))
    for sc in lens["valuation"]["scenarios"]:
        if sc.get("assumptions", {}).get("multiple_basis") == "ev_sales":
            if lens["valuation"]["current"].get("net_debt") is None or unknown_debt:
                raise ValueError("EV-sales requires verified net debt; an unknown-debt zero placeholder is not valid")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="action", required=True)
    pack = sub.add_parser("pack", help="one public ticker, no private ledger or parallel peer expansion")
    pack.add_argument("ticker"); pack.add_argument("--out-dir", required=True)
    health = sub.add_parser("health", help="run upstream financial check on a public snapshot JSON")
    health.add_argument("snapshot"); health.add_argument("--out-dir", required=True)
    value = sub.add_parser("value", help="recompute upstream scenario terminal values and explicit present values")
    value.add_argument("lens"); value.add_argument("--discount-rate", type=float, required=True)
    value.add_argument("--out-dir", required=True)
    val = sub.add_parser("validate", help="upstream research validation; does not validate trade decisions")
    val.add_argument("lens"); val.add_argument("--out-dir", required=True)
    args = ap.parse_args()
    out = fresh_output(args.out_dir); out.mkdir()
    if args.action == "pack":
        if not re.fullmatch(r"[A-Za-z0-9.^=-]{1,24}", args.ticker):
            raise ValueError("Use an explicit public ticker")
        code = run_upstream("connectors/live_data.py", ["--cache-dir", str(out / "cache"), "pack",
                            args.ticker, "--peers", "none", "--out-dir", str(out)], out / "RUN.json")
    elif args.action == "health":
        source = project_path(args.snapshot, must_exist=True)
        code = run_upstream("scripts/company_check.py", [str(source), "--json", str(out / "health.json"),
                            "--md", str(out / "health.md")], out / "RUN.json")
    elif args.action == "value":
        source = project_path(args.lens, must_exist=True)
        raw = json.loads(source.read_text(encoding="utf-8"))
        check_valuation_inputs(raw)
        code = run_upstream("scripts/serenity_lens.py", ["compute", str(source), "--out", str(out / "terminal.json")], out / "RUN.json")
        if code == 0:
            result = discounted_scenarios(json.loads((out / "terminal.json").read_text()), args.discount_rate)
            result["input_source"] = str(source)
            (out / "present-values.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    else:
        source = project_path(args.lens, must_exist=True)
        validate_snapshot_reference(json.loads(source.read_text(encoding="utf-8")), source)
        code = run_upstream("scripts/serenity_lens.py", ["validate", str(source)], out / "RUN.json")
    print(f"Research artifact: {out}")
    return code


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
