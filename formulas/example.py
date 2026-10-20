#!/usr/bin/env python3
"""
example.py — the formula run on gaps nobody created: the six cars whose
horsepower is genuinely missing from the UCI auto-mpg table, plus a P&L with
holes. Prints every RESPOND record in full.

Run:  python3 formulas/example.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from benchmark import load_csv  # noqa: E402
from omni_gap import OmniGap, summarize  # noqa: E402


def show(fills, label=None):
    for f in fills:
        head = f"row {f.row}" + (f" ({label(f.row)})" if label else "")
        val = f"{f.value:.4g}" if f.value is not None else "—  (conflict: measure this record)"
        print(f"\n{head} · {f.column}\n  tag       : {f.status}\n  value     : {val}"
              f"\n  range     : [{f.lo:.4g}, {f.hi:.4g}]   narrowing vs base rate: {100 * f.narrowing:.0f}%"
              f"\n  channels  : {f.channels}\n  falsifier : {f.falsifier}")
        if f.next_measurement:
            print(f"  next      : {f.next_measurement}")


def main():
    cols = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year"]
    rows = load_csv("mpg.csv", cols)
    names = []
    import csv
    with open(os.path.join(os.path.dirname(__file__), "data", "mpg.csv")) as fh:
        names = [r["name"] for r in csv.DictReader(fh)]
    og = OmniGap(cols, rows, tolerance={"horsepower": 10.0})   # decision tolerance: +/-10 hp
    print("=== auto-mpg: the six real gaps (horsepower never recorded) ===")
    show(og.fill(), label=lambda i: names[i])

    print("\n\n=== P&L with holes: identities revenue - cogs = gross, gross - opex = net ===")
    cols = ["headcount", "revenue", "cogs", "gross", "opex", "net"]
    from benchmark import synthetic_pnl
    _, full, ids = synthetic_pnl()
    holes = [r[:] for r in full]
    holes[0][3] = None                      # gross missing, revenue & cogs known  -> forced
    holes[1][3] = holes[1][5] = None        # gross and net missing                -> forced (cascade)
    holes[2][1] = holes[2][2] = None        # revenue and cogs both missing        -> one identity, two unknowns
    holes[3][0] = None                      # headcount: no identity covers it
    og = OmniGap(cols, holes, identities=ids, tolerance={"headcount": 5})
    fills = og.fill()
    show(fills)
    print("\nsummary:", summarize(fills))
    for f in fills:
        print(f"  row {f.row} {f.column:<9} truth {full[f.row][og.ci[f.column]]:>12.6g}   centre {f.center:>12.6g}")


if __name__ == "__main__":
    main()
