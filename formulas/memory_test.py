#!/usr/bin/env python3
"""
memory_test.py — does memory-as-by-product improve the next run?

Status: DERIVATION / variable evidence, not canon.

The claim under test: a formula run leaves a record (calibration in sd units,
channel weights, verdicts), and a LATER run on a THIN table of the same
variables, which cannot calibrate itself well, is better calibrated when it
pools with that record than when it stands alone.

Protocol
  1. A fresh, temporary memory (nothing carried in from the repo's log).
  2. TEACH: run the formula once on the full Auto-MPG table (398 rows). The
     run's record enters memory; no raw data does.
  3. TEST: 40 thin tables of 16 rows drawn from Auto-MPG with 30% of cells
     hidden. Each is filled twice: without memory, and with memory. Score the
     90% intervals against the hidden truth.

What a pass looks like: with memory, measured coverage is closer to the stated
90% and less erratic across tables, at similar or smaller width. Accuracy of
the point estimate should NOT change much: memory pools calibration, it does
not supply values.

Run:  python3 formulas/memory_test.py      (standard library only)
"""

from __future__ import annotations

import math
import os
import random
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from benchmark import load_csv  # noqa: E402
from memory import Memory  # noqa: E402
from omni_gap import OmniGap, _mean_sd  # noqa: E402


def main():
    cols = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year"]
    full = load_csv("mpg.csv", cols)
    p = len(cols)
    sd = [_mean_sd([r[j] for r in full if r[j] is not None])[1] for j in range(p)]
    tmp = tempfile.mkdtemp()
    mem = Memory(os.path.join(tmp, "runs.jsonl"))

    # 1. teach
    OmniGap(cols, full, memory=mem, seed=0).fill()
    print(f"taught from the full table: {len(mem.records())} record(s), no raw data stored")

    # 2. test in two regimes
    for regime, nrows, frac in (("A · thin (16 rows, 30% hidden): expression differs from the taught run → must not pool", 16, 0.30),
                                ("B · small (28 rows, 15% hidden): same expression, different size regime → must not pool", 28, 0.15)):
        res = {"without memory": [], "with memory": []}
        run_regime(regime, nrows, frac, full, cols, p, sd, mem, res)
    # C. the legitimate regime: many small tables of the same variables (monthly reports,
    #    repeated lab runs). Teach from 40 OTHER small tables, test on 40 new ones.
    mem2 = Memory(os.path.join(tmp, "runs2.jsonl"))
    for t in range(40):
        rng = random.Random(5000 + t)
        rows = rng.sample(full, 28)
        OmniGap(cols, rows, memory=mem2, seed=t, folds=4).fill()
    res = {"without memory": [], "with memory": []}
    run_regime("C · small (28 rows, 15% hidden) after 40 prior small tables: same expression AND size regime → pools",
               28, 0.15, full, cols, p, sd, mem2, res)


def run_regime(regime, nrows, frac, full, cols, p, sd, mem, res):
    print(f"\n=== regime {regime} ===")
    for t in range(40):
        rng = random.Random(900 + t)
        rows = rng.sample(full, nrows)
        cells = [(i, j) for i in range(nrows) for j in range(p) if rows[i][j] is not None]
        hidden = set(rng.sample(cells, int(frac * len(cells))))
        masked = [[None if (i, j) in hidden else rows[i][j] for j in range(p)] for i in range(nrows)]
        for label, m in (("without memory", None), ("with memory", mem)):
            og = OmniGap(cols, masked, memory=m, seed=t, folds=4)
            og.POOL_BELOW = 60
            fills = {(f.row, og.ci[f.column]): f for f in og.fill() if f.column in og.ci}
            cov = wid = err = n = 0
            pooled = 0
            for (i, j) in hidden:
                f = fills[(i, j)]
                truth = rows[i][j]
                cov += f.lo <= truth <= f.hi
                wid += (f.hi - f.lo) / sd[j]
                err += ((f.center - truth) / sd[j]) ** 2
                pooled += "pooled" in (f.note or "")
                n += 1
            res[label].append((cov / n, wid / n, math.sqrt(err / n), pooled / n))
    print(f"{'':<16}{'coverage':>10}{'|cov-90%|':>11}{'spread':>8}{'width(sd)':>11}{'NRMSE':>8}{'pooled':>8}")
    for label, v in res.items():
        covs = [x[0] for x in v]
        mc = sum(covs) / len(covs)
        dev = sum(abs(c - 0.9) for c in covs) / len(covs)
        spread = math.sqrt(sum((c - mc) ** 2 for c in covs) / len(covs))
        print(f"{label:<16}{100*mc:>9.1f}%{100*dev:>10.1f}%{100*spread:>7.1f}%{sum(x[1] for x in v)/len(v):>11.2f}"
              f"{sum(x[2] for x in v)/len(v):>8.3f}{100*sum(x[3] for x in v)/len(v):>7.0f}%")
    print("coverage: share of hidden truths inside the stated 90% range (closer to 90% is better)\n"
          "|cov-90%|: mean miscalibration per table · spread: sd of coverage across tables (lower = steadier)\n"
          "pooled: share of cells whose width was pooled with memory. NRMSE should be ~unchanged: memory pools calibration, not values.")


if __name__ == "__main__":
    main()
