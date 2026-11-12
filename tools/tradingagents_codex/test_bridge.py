"""Offline contract tests. Never start Codex or make a network request."""
import json
import subprocess
import tempfile
import unittest
from unittest.mock import patch, MagicMock

from langchain_core.messages import HumanMessage, ToolMessage
from pydantic import BaseModel

from bridge import CodexBridgeError, CodexChatModel, inherit_system_proxy


class BridgeTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.model = CodexChatModel(run_dir=self.directory.name, max_calls=1, use_system_proxy=False)

    def process(self, envelope, completed=True):
        process = MagicMock()
        process.returncode = 0
        events = [{"type": "item.completed", "item": {
            "type": "agent_message", "text": json.dumps(envelope)}}]
        if completed:
            events.append({"type": "turn.completed", "usage": {"input_tokens": 1}})
        process.communicate.return_value = ("\n".join(json.dumps(e) for e in events), "")
        return process

    def test_message_tool_result_roundtrip_and_budget(self):
        tool = {"type": "function", "function": {"name": "get_public_fact",
                "description": "Read a public fact", "parameters": {"type": "object",
                "properties": {"ticker": {"type": "string"}}, "required": ["ticker"]}}}
        envelope = {"content": "", "tool_calls": [
            {"name": "get_public_fact", "arguments_json": '{"ticker":"AIP"}'}]}
        process = self.process(envelope)
        with patch("bridge.subprocess.Popen", return_value=process) as start:
            output = self.model.bind_tools([tool]).invoke([
                HumanMessage("Research AIP"), ToolMessage(content="public evidence", tool_call_id="prior")])
            self.assertEqual(output.tool_calls[0]["args"], {"ticker": "AIP"})
            self.assertIn("public evidence", process.communicate.call_args.args[0])
            self.assertIn("--ephemeral", start.call_args.args[0])
            with self.assertRaises(CodexBridgeError):
                self.model.invoke("another request")
            self.assertEqual(start.call_count, 1)

    def test_progress_poll_does_not_resend_prompt_or_log_raw_text(self):
        self.model.progress_interval_seconds = 1
        process = self.process({"content": "ok", "tool_calls": []})
        final = process.communicate.return_value
        process.communicate.side_effect = [subprocess.TimeoutExpired("codex", 1,
            output=b'{"type":"turn.started"}\n', stderr=b'reconnecting SENSITIVE_SENTINEL'), final]
        with patch("bridge.subprocess.Popen", return_value=process) as start:
            self.model.invoke("public evidence")
        self.assertEqual(start.call_count, 1)
        self.assertIsNone(process.communicate.call_args_list[1].args[0])
        from pathlib import Path
        log = next(Path(self.directory.name).rglob("progress.jsonl")).read_text()
        self.assertNotIn("SENSITIVE_SENTINEL", log)
        self.assertIn("reconnecting", log)
        self.assertIn("turn.started", log)

    def test_reject_unbound_tool(self):
        with self.assertRaises(CodexBridgeError):
            self.model._decode('{"content":"","tool_calls":[{"name":"shell","arguments_json":"{}"}]}', [])

    def test_reject_partial_response(self):
        with patch("bridge.subprocess.Popen", return_value=self.process({"content": "ok", "tool_calls": []}, False)):
            with self.assertRaises(CodexBridgeError):
                self.model.invoke("hello")

    def test_pydantic_structured_response(self):
        class Verdict(BaseModel):
            missing_evidence: bool
        envelope = {"content": '{"missing_evidence":true}', "tool_calls": []}
        with patch("bridge.subprocess.Popen", return_value=self.process(envelope)):
            value = self.model.with_structured_output(Verdict).invoke("Review supplied evidence")
            self.assertTrue(value.missing_evidence)

    def test_timeout_terminates_process_group_without_retry(self):
        process = MagicMock()
        process.pid = 999999
        process.communicate.side_effect = [subprocess.TimeoutExpired("codex", 55), ("", "")]
        with patch("bridge.subprocess.Popen", return_value=process) as start, patch("bridge.os.killpg") as terminate:
            with self.assertRaises(CodexBridgeError):
                self.model.invoke("hello")
            self.assertEqual(start.call_count, 1)
            terminate.assert_called_once()

    def test_system_proxy_inheritance_does_not_modify_parent(self):
        parent = {"PATH": "/bin"}
        result, route = inherit_system_proxy(parent, "HTTPSEnable : 1\nHTTPSProxy : 127.0.0.1\nHTTPSPort : 8888")
        self.assertEqual(result["HTTPS_PROXY"], "http://127.0.0.1:8888")
        self.assertEqual(route, "existing_system_loopback_proxy")
        self.assertNotIn("HTTPS_PROXY", parent)

    def test_preserve_explicit_proxy_and_reject_remote_system_proxy(self):
        parent = {"HTTPS_PROXY": "http://localhost:9999"}
        result, route = inherit_system_proxy(parent, "")
        self.assertEqual(result, parent)
        self.assertEqual(route, "existing_process_proxy")
        with self.assertRaises(CodexBridgeError):
            inherit_system_proxy({}, "HTTPSEnable : 1\nHTTPSProxy : [REDACTED_HOST]\nHTTPSPort : 8888")


if __name__ == "__main__":
    unittest.main()
