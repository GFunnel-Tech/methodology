#!/usr/bin/env python3
"""
memory.py — memory as the by-product of running the formula.

Status: DERIVATION, not canon. Standard library only.

There is no memory layer to fill. Every run of a formula emits one RECORD:

    fingerprint   a hash of the inputs' shape and summary (never the raw data)
    expression    what the formula did: channels, learned weights, identities,
                  correspondence verdicts, calibration widths in sd units
    output        what came out: tags, narrowing, sealed ranges, scores
    conjugate     the gap the run opened (the next measurement it named)

Records are appended to formulas/memory/runs.jsonl, content-addressed, so the
same inputs produce the same record and nothing is stored twice. That log IS
the memory (Layer VI step 6: if it isn't written, it isn't real). Anything the
system "remembers" is recomputed from it on demand (Layer I.G: the present is
the integration of every prior path):

    recall(variable)   the calibration earned on this variable across all prior
                       runs — weights per channel, interval width in sd units,
                       correspondence verdicts — so a run on a table too thin to
                       calibrate itself can warm-start from what earlier runs
                       learned, tagged as such.
    reliability(tag)   how often each tag has been right, across every scored
                       forecast and sealed prediction: the learned widening.
    show()             what the system knows, and from how many runs.

Two rules:
  1. No raw data enters memory. A record holds a fingerprint and statistics.
  2. Memory never overrides measurement. A warm-start is used only where the
     current run cannot calibrate itself, and the output says it came from
     memory and from how many runs.

    python3 formulas/memory.py show
    python3 formulas/memory.py recall horsepower
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PATH = os.path.join(HERE, "memory", "runs.jsonl")


def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)


def fingerprint(columns, rows):
    """Shape + per-column summary. Same data → same fingerprint; raw values never leave."""
    summary = []
    for j, c in enumerate(columns):
        vals = [r[j] for r in rows if r[j] is not None]
        n = len(vals)
        if n:
            m = sum(vals) / n
            sd = math.sqrt(sum((v - m) ** 2 for v in vals) / (n - 1)) if n > 1 else 0.0
        else:
            m = sd = 0.0
        summary.append([c, n, round(m, 6), round(sd, 6)])
    return hashlib.sha256(_canon({"rows": len(rows), "cols": summary}).encode()).hexdigest()[:16]


class Memory:
    def __init__(self, path=DEFAULT_PATH):
        self.path = path
        self._records = None

    # ---- the log

    def records(self):
        if self._records is None:
            self._records = []
            if os.path.exists(self.path):
                with open(self.path, encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            self._records.append(json.loads(line))
        return self._records

    def record(self, kind, fingerprint_, expression, output, conjugate=None, note=""):
        body = {"kind": kind, "fingerprint": fingerprint_, "expression": expression}
        rid = hashlib.sha256(_canon(body).encode()).hexdigest()[:16]
        if any(r["id"] == rid for r in self.records()):
            return rid, False
        rec = {"id": rid, "date": dt.date.today().isoformat(), **body, "output": output,
               "conjugate": conjugate, "note": note}
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(_canon(rec) + "\n")
        self.records().append(rec)
        return rid, True

    # ---- what is recomputed from the log

    @staticmethod
    def regime(n):
        """Size regime of a calibration: log2 bucket of its cases. A width learned
        from 300 cases does not describe an estimator trained on 20 (memory_test.py
        regime B: 71% coverage at a stated 90% when that was allowed)."""
        return int(math.log2(max(1, n)))

    def recall(self, variable, expression=None, n=None):
        """Calibration earned on `variable` across prior omni-gap runs.

        `expression` is the channel set the current run can use for this
        variable (e.g. "P+R+S"). Only records with the SAME expression are
        pooled: calibration is a property of the calculation, not of the
        variable. (Keyed by variable alone, memory made thin runs over-
        confident: 66% coverage at a stated 90%. memory_test.py keeps that
        failed path as the control.)"""
        hits = [r for r in self.records() if r["kind"] == "omni-gap" and variable in r["expression"].get("columns", {})]
        if not hits:
            return None
        cals = [r["expression"]["columns"][variable] for r in hits]
        cals = [c for c in cals if c.get("n", 0) >= 9 and c.get("source", "this run") == "this run"]  # only self-calibrated runs teach
        if expression is not None:
            cals = [c for c in cals if c.get("expression") == expression]
        if n is not None:
            cals = [c for c in cals if self.regime(c["n"]) == self.regime(n)]
        if not cals:
            return None
        tot = sum(c["n"] for c in cals)
        weights = {}
        for c in cals:
            for k, w in c["weights"].items():
                weights[k] = weights.get(k, 0.0) + w * c["n"] / tot
        hw = sum(c["halfwidth_sd"] * c["n"] for c in cals) / tot
        corr = [c["correspondence"] for c in cals if c.get("correspondence")]
        return {"variable": variable, "expression": expression, "regime": None if n is None else self.regime(n),
                "runs": len(cals), "cases": tot, "weights": weights,
                "halfwidth_sd": hw, "no_signal": sum(c["no_signal"] for c in cals) > len(cals) / 2,
                "correspondence_held": sum(1 for c in corr if c["verdict"] == "held"), "correspondence_runs": len(corr)}

    def reliability(self):
        """Hit rate and required widening per tag, over every scored prediction in the log."""
        by = {}
        for r in self.records():
            for s in r.get("output", {}).get("scored", []):
                d = by.setdefault(s["tag"], {"n": 0, "hits": 0, "ratios": []})
                d["n"] += 1
                d["hits"] += s["hit"]
                if s.get("ratio") is not None:
                    d["ratios"].append(s["ratio"])
        out = {}
        for t, d in by.items():
            rs = sorted(d["ratios"])
            k = min(len(rs) - 1, math.ceil(0.9 * (len(rs) + 1)) - 1) if rs else None
            out[t] = {"n": d["n"], "hit_rate": d["hits"] / d["n"],
                      "widening_for_90pct": max(1.0, rs[k]) if rs else None,
                      "valid": len(rs) >= 9}
        return out

    def show(self):
        recs = self.records()
        kinds = {}
        for r in recs:
            kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
        print(f"{len(recs)} records in {os.path.relpath(self.path)}  " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())))
        vars_ = sorted({v for r in recs if r["kind"] == "omni-gap" for v in r["expression"].get("columns", {})})
        if vars_:
            print("\nvariables with earned calibration (self-calibrated runs only):")
            for v in vars_:
                exprs = sorted({r["expression"]["columns"][v].get("expression", "?") for r in recs
                                if r["kind"] == "omni-gap" and v in r["expression"].get("columns", {})})
                for ex in exprs:
                    regs = sorted({self.regime(r["expression"]["columns"][v]["n"]) for r in recs
                                   if r["kind"] == "omni-gap" and r["expression"]["columns"].get(v, {}).get("expression") == ex})
                    for rg in regs:
                        c = self.recall(v, ex, 2 ** rg)
                        if not c:
                            continue
                        v_ = f"{v} [{ex}, n~2^{rg}]"
                        w = ", ".join(f"{k} {x:.2f}" for k, x in sorted(c["weights"].items()))
                        corr = f"; correspondence held {c['correspondence_held']}/{c['correspondence_runs']}" if c["correspondence_runs"] else ""
                        print(f"  {v_:<34} {c['runs']} run(s), {c['cases']} cases · 90% half-width {c['halfwidth_sd']:.2f} sd · weights {w}{corr}")
        rel = self.reliability()
        if rel:
            print("\ntag reliability (every scored prediction):")
            for t, d in sorted(rel.items()):
                wid = f"{d['widening_for_90pct']:.2f}x" if d["widening_for_90pct"] else "—"
                print(f"  {t:<12} n={d['n']:<4} hit {100*d['hit_rate']:.0f}%  widening needed for 90%: {wid}" + ("" if d["valid"] else "  (not yet valid: <9 cases)"))
        conj = [r["conjugate"] for r in recs if r.get("conjugate")]
        if conj:
            print(f"\n{len(conj)} conjugate gaps named by past runs; latest: {conj[-1]}")


def main():
    m = Memory()
    if len(sys.argv) < 2 or sys.argv[1] == "show":
        m.show()
    elif sys.argv[1] == "recall" and len(sys.argv) > 2:
        print(json.dumps(m.recall(sys.argv[2]), indent=1))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
