#!/usr/bin/env python3
"""
forecast.py — the two-arm forecast test, with every metric estimated and tagged.

Status: DERIVATION, not canon. Built for the kind of test a user ran: give an
AI a snapshot of a situation N months ago plus the goals, ask it to predict
what happened, and compare with and without the methodology.

The protocol (Estimate Protocol, substrate/2026-10-20-estimate-protocol.md):

  1. `new`    writes a sealed prediction sheet. EVERY metric in the situation
              file gets a row in BOTH arms. A row may not be left blank: it
              carries a value, a low–high range, a tag, and a falsifier.
  2. The sheet is committed to git BEFORE actuals are entered
              (audit/prediction/PROTOCOL.md: the commit is the seal).
  3. `score`  enters the actuals and scores each arm per metric:
                hit       actual inside the stated range
                miss      actual outside the stated range
                error     |predicted − actual| / scale  (scale = the metric's own
                          stated tolerance, so metrics with different units compare)
              and reports, per arm: hit rate vs. stated coverage, mean scaled
              error, and the tag-by-tag breakdown (do `estimate` rows hit more
              often than `assumption` rows? they should).

Tags (the only vocabulary allowed in the sheet):
  measured             the value was known at prediction time (not scored)
  forced               follows by necessity from known values
  estimate             calculated from stated evidence (prior, structure, analogue, trend),
                       with a calibrated range
  assumption           a value with no evidence base beyond judgement. ALLOWED — but it
                       must be tagged, must carry a range, and is scored separately
  held-open            the only tag that may omit a value, and only with a reason that
                       passes the test: no prior, no analogue, no structure, no trend.
                       "I don't know" is not a reason; a base rate always exists for
                       anything that has happened before.

Usage
  python3 formulas/forecast.py new  <situation.json> <sheet.json>
  python3 formulas/forecast.py score <sheet.json> <actuals.json>
  python3 formulas/forecast.py example          # writes an example situation file

The predictions themselves are written by the forecaster (human or model)
into the sheet; this tool enforces the format, the seal, and the scoring.
Standard library only.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys

TAGS = ("measured", "forced", "estimate", "assumption", "held-open")
ARMS = ("framework-free", "methodology")


def _load(p):
    with open(p) as f:
        return json.load(f)


def _dump(p, d):
    with open(p, "w") as f:
        json.dump(d, f, indent=1, ensure_ascii=False)
        f.write("\n")


def cmd_example(_):
    ex = {
        "subject": "a small business, snapshot taken 6 months before the scoring date",
        "snapshot_date": "2026-04-20",
        "horizon_months": 6,
        "facts_at_snapshot": {
            "monthly_revenue_usd": 18000,
            "clients": 9,
            "team_size": 2,
            "cash_runway_months": 4,
            "goal": "reach $30k MRR and hire one salesperson"
        },
        "metrics": [
            {"name": "monthly_revenue_usd", "unit": "USD/month", "tolerance": 3000,
             "note": "tolerance = the error size that would change a decision"},
            {"name": "clients", "unit": "count", "tolerance": 2},
            {"name": "team_size", "unit": "count", "tolerance": 1},
            {"name": "salesperson_hired", "unit": "0/1", "tolerance": 0.5},
            {"name": "cash_runway_months", "unit": "months", "tolerance": 1.5}
        ]
    }
    _dump("situation.example.json", ex)
    print("wrote situation.example.json")


def cmd_new(args):
    situation = _load(args[0])
    out = args[1]
    rows = {arm: [] for arm in ARMS}
    for m in situation["metrics"]:
        for arm in ARMS:
            rows[arm].append({
                "metric": m["name"], "unit": m.get("unit", ""), "tolerance": m["tolerance"],
                "value": None, "low": None, "high": None, "coverage": 0.9,
                "tag": None, "method": "", "falsifier": "",
                "next_measurement": ""
            })
    sheet = {
        "_protocol": "Estimate Protocol — every row must carry value, low, high, tag, falsifier "
                     "(held-open may omit value only with a reason). Commit this file before actuals exist.",
        "situation_file": args[0], "created": dt.date.today().isoformat(),
        "lookup_status": "withheld", "arms": rows, "actuals": None, "scores": None
    }
    _dump(out, sheet)
    print(f"wrote {out}: {len(situation['metrics'])} metrics × {len(ARMS)} arms. Fill every row, then commit.")


def validate(sheet):
    errors = []
    for arm, rows in sheet["arms"].items():
        for r in rows:
            where = f"{arm}/{r['metric']}"
            if r["tag"] not in TAGS:
                errors.append(f"{where}: tag must be one of {TAGS}")
                continue
            if r["tag"] == "held-open":
                if not r.get("method"):
                    errors.append(f"{where}: held-open needs a reason in 'method' (no prior, no analogue, no structure, no trend)")
                continue
            for k in ("value", "low", "high"):
                if r.get(k) is None:
                    errors.append(f"{where}: '{k}' is blank — a tagged estimate is allowed, a blank is not")
            if r["tag"] in ("estimate", "assumption") and not r.get("falsifier"):
                errors.append(f"{where}: needs a falsifier")
            if r.get("low") is not None and r.get("high") is not None and r["low"] > r["high"]:
                errors.append(f"{where}: low > high")
    return errors


def seal_hash(sheet):
    body = json.dumps(sheet["arms"], sort_keys=True)
    return hashlib.sha256(body.encode()).hexdigest()


def cmd_score(args):
    sheet = _load(args[0])
    actuals = _load(args[1])
    errs = validate(sheet)
    if errs:
        print("sheet is not valid; fix before scoring:\n  " + "\n  ".join(errs))
        sys.exit(1)
    sheet["phase_a_sha256"] = seal_hash(sheet)
    sheet["actuals"] = actuals
    sheet["lookup_status"] = "revealed"
    report = {}
    for arm, rows in sheet["arms"].items():
        scored = []
        for r in rows:
            a = actuals.get(r["metric"])
            if a is None or r["tag"] == "measured":
                continue
            if r["tag"] == "held-open":
                scored.append({**r, "actual": a, "result": "held-open", "scaled_error": None})
                continue
            hit = r["low"] <= a <= r["high"]
            scored.append({**r, "actual": a, "result": "hit" if hit else "miss",
                           "scaled_error": abs(r["value"] - a) / r["tolerance"]})
        n = [s for s in scored if s["result"] in ("hit", "miss")]
        by_tag = {}
        for s in n:
            d = by_tag.setdefault(s["tag"], {"n": 0, "hits": 0, "err": 0.0})
            d["n"] += 1; d["hits"] += s["result"] == "hit"; d["err"] += s["scaled_error"]
        for d in by_tag.values():
            d["hit_rate"] = d["hits"] / d["n"]; d["mean_scaled_error"] = d["err"] / d["n"]; del d["err"]
        report[arm] = {
            "n_scored": len(n),
            "hit_rate": sum(s["result"] == "hit" for s in n) / len(n) if n else None,
            "stated_coverage": sum(s["coverage"] for s in n) / len(n) if n else None,
            "mean_scaled_error": sum(s["scaled_error"] for s in n) / len(n) if n else None,
            "within_tolerance_rate": sum(s["scaled_error"] <= 1 for s in n) / len(n) if n else None,
            "held_open": sum(s["result"] == "held-open" for s in scored),
            "by_tag": by_tag, "rows": scored,
        }
    sheet["scores"] = report
    _dump(args[0], sheet)
    print(f"{'arm':<16}{'scored':>7}{'hit rate':>10}{'stated':>8}{'err/tol':>9}{'in-tol':>8}{'open':>6}")
    for arm, r in report.items():
        f = lambda v, pct=True: ("—" if v is None else (f"{100*v:.0f}%" if pct else f"{v:.2f}"))
        print(f"{arm:<16}{r['n_scored']:>7}{f(r['hit_rate']):>10}{f(r['stated_coverage']):>8}"
              f"{f(r['mean_scaled_error'], False):>9}{f(r['within_tolerance_rate']):>8}{r['held_open']:>6}")
    for arm, r in report.items():
        if r["by_tag"]:
            print(f"\n{arm} by tag: " + "; ".join(
                f"{t}: n={d['n']}, hit {100*d['hit_rate']:.0f}%, err/tol {d['mean_scaled_error']:.2f}" for t, d in r["by_tag"].items()))
    print("\nReading: the arm with the lower err/tol and a hit rate near its stated coverage wins. "
          "A held-open count above 0 is itself a finding: the forecaster declined to calculate.")


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(0)
    cmd, args = sys.argv[1], sys.argv[2:]
    {"new": cmd_new, "score": cmd_score, "example": cmd_example}[cmd](args)


if __name__ == "__main__":
    main()
