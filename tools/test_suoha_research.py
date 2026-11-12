import sys
import json
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import suoha_research as S


class ValueAndBoundary(unittest.TestCase):
    def test_future_value_not_relabelled_current(self):
        lens = {"valuation": {"current": {"currency": "USD"}, "scenarios": [
            {"name": "base", "implied_per_share": 121, "horizon_years": 2}]}}
        value = S.discounted_scenarios(lens, .10)
        self.assertAlmostEqual(value["scenarios"][0]["present_value_per_share"], 100)
        self.assertEqual(value["scenarios"][0]["terminal_per_share"], 121)

    def test_missing_horizon_rejected(self):
        with self.assertRaises(ValueError):
            S.discounted_scenarios({"valuation": {"current": {}, "scenarios": [{"name": "x", "implied_per_share": 50}]}}, .1)

    def test_secrets_not_in_subprocess_environment(self):
        env = S.clean_environment()
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertNotIn("EDINET_API_KEY", env)
        self.assertNotIn("GH_TOKEN", env)
        self.assertNotIn("HOME", env)

    def test_outside_and_environment_paths_rejected(self):
        with self.assertRaises(ValueError): S.project_path("/tmp/outside.json")
        with self.assertRaises(ValueError): S.project_path(".env")

    def test_nested_snapshot_cannot_escape_or_read_credentials(self):
        for path in ["/tmp/outside.json", "../outside.json", "secrets.json", ".env"]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                S.validate_snapshot_reference({"live_data": {"snapshot_path": path}}, S.PROJECT / "lens.json")

    def test_missing_nested_snapshot_not_silently_skipped(self):
        with self.assertRaises(ValueError):
            S.validate_snapshot_reference({"live_data": {"snapshot_path": "missing-snapshot-for-regression.json"}}, S.PROJECT / "lens.json")

    def test_existing_project_snapshot_accepted(self):
        with tempfile.TemporaryDirectory(dir=S.PROJECT / "tools", prefix="suoha-path-test-") as tmp:
            path = Path(tmp) / "snapshot.json"
            path.write_text(json.dumps({"warnings": []}))
            S.validate_snapshot_reference({"live_data": {"snapshot_path": str(path)}}, path.parent / "lens.json")

    def test_zero_debt_placeholder_cannot_pass_EV_sales(self):
        lens = {"valuation": {"current": {"net_debt": 0}, "scenarios": [{"assumptions": {"multiple_basis": "ev_sales"}}]},
                "live_data": {"warnings_addressed": [{"warning": "net_debt_unknown: awaiting report"}]}}
        with self.assertRaises(ValueError): S.check_valuation_inputs(lens)

    def test_explicit_zero_debt_without_unknown_warning_allowed(self):
        S.check_valuation_inputs({"valuation": {"current": {"net_debt": 0},
                                 "scenarios": [{"assumptions": {"multiple_basis": "ev_sales"}}]}})


if __name__ == "__main__": unittest.main()
