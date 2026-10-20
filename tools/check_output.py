#!/usr/bin/env python3
"""
check_output.py — lint an AI answer against the Estimate Protocol.

Status: derivation tooling (not canon). Standard library only.

Two uses:

  1. Claude Code hooks (configured in .claude/settings.json)
       SessionStart : prints the mode rule so it is in context before the first task
       Stop         : reads the transcript, lints the last assistant message, and
                      BLOCKS the turn (exit 2 + reason) when it emits numbers that
                      read as estimates with no tag. Claude is re-prompted with the
                      reason, so the fix happens before the user sees the answer.
  2. Any AI, any vendor — lint a saved answer by hand:
       python3 tools/check_output.py --file answer.md

What it checks (CLAUDE.md §1–§2; substrate/2026-10-20-estimate-protocol.md):

  BLOCKING  an "estimate-shaped" answer (several numbers + forecasting language)
            that carries no tag token at all. Tags: measured · forced · estimate ·
            assumption · held-open · conflict, written as [tag: …], `tag: …`,
            or "(estimate)" style markers.
  BLOCKING  the phrase "held open" / "cannot be estimated" / "no way to know" used
            on a quantity while the answer gives it no value and no four-part
            reason (no prior / structure / analogue / trend).
  WARNING   no "Mode:" line (Answer / Diagnose / Estimate / Both / Contribute).

It is a linter, not a judge: it catches the failure the user's test exposed
(numbers refused or given untagged) and cannot verify that a tag is honest.
A Stop hook that already blocked once lets the turn through (stop_hook_active),
so a disagreement never loops.
"""

from __future__ import annotations

import argparse
import json
import re
import sys

MODE_RULE = """\
GFunnel Methodology — operating rule (CLAUDE.md §1–2). Before reading anything else, pick the MODE and say it:
  Answer  (a concept)  ·  Diagnose  (something stuck → full methodology, every step)  ·
  Estimate  (a number not yet in the record → instruments only, formulas/, workflows/estimate.md)  ·  Both  ·  Contribute.
Every quantity you emit carries a tag — measured · forced · estimate · assumption · held-open · conflict — with a
range and a falsifier on every estimate/assumption. A value may be omitted only when no prior, no structure, no
analogue and no trend exists. Refusing to estimate where a base rate exists fails the protocol. Outputs are linted
on Stop (tools/check_output.py): untagged estimate-shaped answers are sent back."""

TAG_RE = re.compile(
    r"(\[\s*tag\s*:\s*(measured|forced|estimate|assumption|held-open|conflict)[^\]]*\]"
    r"|\btag\s*:\s*(measured|forced|estimate|assumption|held-open|conflict)\b"
    r"|\((measured|forced|estimate|assumption|held-open|conflict)\)"
    r"|`(measured|forced|estimate|assumption|held-open|conflict)`"
    r"|\*\*(measured|forced|estimate|assumption|held-open|conflict)\*\*)",
    re.I,
)
MODE_RE = re.compile(r"^\s*\**\s*mode\s*\**\s*:\s*\**\s*(answer|diagnose|estimate|both|contribute)", re.I | re.M)
FORECAST_WORDS = re.compile(
    r"\b(estimate[sd]?|predict(s|ed|ion)?|forecast(s|ed)?|expect(s|ed)?|likely|probably|projected|"
    r"will (be|reach|hit|grow|fall|drop|rise)|should (be|reach)|around|roughly|approximately|about)\b", re.I)
NUMBER_RE = re.compile(r"(?<![\w.])[-+]?\$?\d[\d,]*(\.\d+)?\s*(%|k|m|bn|b|x|×|usd|eur|gbp|s|ms|kg|g|mpc|mev|gev|hz|km|mi|days?|weeks?|months?|years?|hp|clients?|users?)?\b", re.I)
REFUSAL_RE = re.compile(
    r"\b(held open|hold(ing)? (it|this|that|these) open|cannot be (estimated|predicted|known|calculated)|"
    r"no way to (know|estimate|predict)|impossible to (estimate|predict|know)|can'?t (estimate|predict|know))\b", re.I)
REASON_RE = re.compile(r"\b(no prior|no structure|no analogue|no analog|no trend|four-part test|boundary gap|proven-open)\b", re.I)


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", " ", text, flags=re.S)


def lint(text: str) -> tuple[list[str], list[str]]:
    """Return (blocking, warnings)."""
    body = strip_code(text)
    blocking, warnings = [], []
    numbers = [m for m in NUMBER_RE.finditer(body) if not re.fullmatch(r"[-+]?\d{1,2}", m.group(0).strip())]
    forecasty = len(FORECAST_WORDS.findall(body))
    tags = len(TAG_RE.findall(body))
    estimate_shaped = len(numbers) >= 3 and forecasty >= 2
    if estimate_shaped and tags == 0:
        blocking.append(
            f"Estimate-shaped answer ({len(numbers)} quantities, {forecasty} forecasting terms) with no tag on any of them. "
            "Tag every quantity: measured · forced · estimate · assumption · held-open · conflict, "
            "and give each estimate/assumption a range and a falsifier (CLAUDE.md §2).")
    if REFUSAL_RE.search(body) and not REASON_RE.search(body) and tags == 0:
        blocking.append(
            "A quantity is declined ('held open' / 'cannot be estimated') without the four-part reason "
            "(no prior, no structure, no analogue, no trend). Anything that has happened before has a prior: "
            "give the best value with a tag and a range, or state which of the four is absent.")
    if (estimate_shaped or tags) and not MODE_RE.search(body):
        warnings.append("No 'Mode:' line. Say which mode you chose (Answer / Diagnose / Estimate / Both / Contribute) "
                        "and what you did not load (CLAUDE.md §1).")
    return blocking, warnings


def last_assistant_text(transcript_path: str) -> str:
    """Last assistant message's text from a Claude Code JSONL transcript."""
    text = ""
    try:
        with open(transcript_path, encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("type") != "assistant":
                    continue
                msg = rec.get("message", {})
                content = msg.get("content", [])
                parts = []
                if isinstance(content, str):
                    parts.append(content)
                else:
                    for c in content:
                        if isinstance(c, dict) and c.get("type") == "text":
                            parts.append(c.get("text", ""))
                if parts:
                    text = "\n".join(parts)   # keep the latest
    except OSError:
        return ""
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--session-start", action="store_true", help="print the mode rule (SessionStart hook)")
    ap.add_argument("--file", help="lint this text file and exit 1 on blocking findings")
    ap.add_argument("--stop-hook", action="store_true", help="read Claude Code Stop-hook JSON on stdin")
    args = ap.parse_args()

    if args.session_start:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": MODE_RULE}}))
        return

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
        blocking, warnings = lint(text)
        for b in blocking:
            print("BLOCKING:", b)
        for w in warnings:
            print("warning :", w)
        if not blocking and not warnings:
            print("ok: passes the Estimate Protocol lint")
        sys.exit(1 if blocking else 0)

    # Stop hook
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        payload = {}
    if payload.get("stop_hook_active"):
        return  # already sent back once this turn: let it through
    text = last_assistant_text(payload.get("transcript_path", "")) if payload.get("transcript_path") else ""
    if not text:
        return
    blocking, warnings = lint(text)
    if blocking:
        reason = "Estimate Protocol lint (tools/check_output.py):\n- " + "\n- ".join(blocking + warnings) + \
                 "\nRevise the answer so every quantity is tagged, then finish."
        print(json.dumps({"decision": "block", "reason": reason}))
        sys.exit(0)
    if warnings:
        print(json.dumps({"systemMessage": "Estimate Protocol lint: " + " ".join(warnings)}))


if __name__ == "__main__":
    main()
