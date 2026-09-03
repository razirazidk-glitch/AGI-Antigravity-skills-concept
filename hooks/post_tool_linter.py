#!/usr/bin/env python3
"""
Post-Tool Linter & Telemetry Hook for agi-antigravity-core.

Inspects tool execution results after execution in the Antigravity agent loop.
Captures errors, performs telemetry logging, triggers auto-formatting on modified files,
and returns an empty JSON object as mandated by the Antigravity PostToolUse lifecycle specification.
"""

import json
import sys
from typing import Any, Dict


def process_post_tool_event(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Inspect post-tool execution payload, auto-format code, and log telemetry."""
    if not isinstance(payload, dict):
        return {}

    step_idx = payload.get("stepIdx", 0)
    error = payload.get("error", "")
    conversation_id = payload.get("conversationId", "")
    tool_name = payload.get("toolName", "")
    args = payload.get("args", {})

    if tool_name in ("write_to_file", "replace_file_content") and isinstance(args, dict):
        target_file = args.get("TargetFile")
        if target_file and isinstance(target_file, str):
            try:
                import subprocess
                subprocess.run(
                    ["/home/razirazi/.gemini/antigravity/bin/auto-format", target_file],
                    capture_output=True,
                    timeout=5,
                )
            except Exception:
                pass

    if error:
        sys.stderr.write(
            f"[POST_TOOL_LINTER] Warning: Tool step {step_idx} in conversation {conversation_id} reported error: {error}\n"
        )
        sys.stderr.flush()

    return {}


def main() -> None:
    """Main hook entry point reading JSON from stdin and writing JSON to stdout."""
    raw_input = sys.stdin.read().strip()
    if not raw_input:
        sys.stdout.write(json.dumps({}))
        sys.stdout.flush()
        return

    try:
        payload = json.loads(raw_input)
        result = process_post_tool_event(payload)
    except Exception as exc:
        sys.stderr.write(f"[POST_TOOL_LINTER] Error parsing post-tool payload: {exc}\n")
        result = {}

    sys.stdout.write(json.dumps(result))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
