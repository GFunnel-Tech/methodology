#!/usr/bin/env python3
"""
benchmark.py — does the Omni Gap Formula beat known gap-filling methods?

Status: DERIVATION / variable evidence, not canon.

Protocol: take real tables, hide 20% of the MEASURED cells at random, fill them
with each method, then compare against the hidden truth. Five random masks per
dataset. Nothing the methods see contains a hidden value.

Methods compared
  mean      column mean (the "fill with the average" default)
  knn       k-nearest records on the measured coordinates (k=7)
  ridge     regression on the measured coordinates of the same record
  chained   MICE-style iterative regression: every gap starts at the mean and is
            re-predicted from all other columns, including other fills, 10 rounds
            (the standard statistical imputation method)
  omni      formula/omni_gap.py

Scores
  NRMSE     root-mean-square error / column sd, averaged over columns (lower = better;
            1.0 = no better than knowing nothing but the column's spread)
  coverage  share of hidden truths inside omni's stated 90% interval
  fill%     share of gaps omni was willing to fill (live-fill or forced-fill)
  filled vs held open  error on the cells omni agreed to fill, vs each baseline
            on the SAME cells; and how wrong it would have been on the cells it refused

Run:  python3 formula/benchmark.py            (standard library only, ~1-2 min)
"""

from __future__ import annotations

import csv
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from omni_gap import OmniGap, _Ridge, _mean_sd, FILL, FORCED  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def load_csv(name, cols):
    rows = []
    with open(os.path.join(HERE, "data", name), newline="") as f:
        for rec in csv.DictReader(f):
            rows.append([float(rec[c]) if rec[c] not in ("", "NA", "nan") else None for c in cols])
    return rows


def synthetic_pnl(n=300, seed=7):
    """Synthetic P&L with two exact identities. Labelled synthetic: it exists to
    test the identity channel, not to stand in for real data."""
    rng = random.Random(seed)
    rows = []
    for _ in range(n):
        head = rng.randint(3, 120)
        rev = head * rng.lognormvariate(math.log(150_000), 0.35)
        cogs = rev * rng.uniform(0.25, 0.65)
        opex = head * rng.lognormvariate(math.log(60_000), 0.3)
        gross = rev - cogs
        rows.append([head, rev, cogs, gross, opex, gross - opex])
    cols = ["headcount", "revenue", "cogs", "gross", "opex", "net"]
    ids = [({"revenue": 1, "cogs": -1, "gross": -1}, 0.0),
           ({"gross": 1, "opex": -1, "net": -1}, 0.0)]
    return cols, rows, ids


DATASETS = [
    ("auto-mpg (UCI, real)",
     ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year"],
     lambda c: (load_csv("mpg.csv", c), [])),
    ("palmer penguins (real)",
     ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
     lambda c: (load_csv("penguins.csv", c), [])),
]


# ----------------------------------------------------------------- baselines

def m_mean(rows, p):
    st = [_mean_sd([r[j] for r in rows if r[j] is not None])[0] for j in range(p)]
    return lambda i, j: st[j]


def m_ridge_knn(rows, p, which):
    sds = [_mean_sd([r[j] for r in rows if r[j] is not None])[1] for j in range(p)]
    means = [_mean_sd([r[j] for r in rows if r[j] is not None])[0] for j in range(p)]
    cache = {}

    def pred(i, j):
        preds = tuple(c for c in range(p) if c != j and rows[i][c] is not None)
        key = (j, preds)
        if key not in cache:
            T = [r for r in rows if r[j] is not None and all(r[c] is not None for c in preds)]
            cache[key] = (T, _Ridge([[r[c] for c in preds] for r in T], [r[j] for r in T]) if preds and len(T) > 12 else None)
        T, model = cache[key]
        if not preds or model is None:
            return means[j]
        x = [rows[i][c] for c in preds]
        if which == "ridge":
            return model.predict(x)
        d = sorted((math.sqrt(sum(((r[c] - v) / sds[c]) ** 2 for c, v in zip(preds, x))), r[j]) for r in T)[:7]
        w = [1 / (dd + 1e-6) for dd, _ in d]
        return sum(wi * v for wi, (_, v) in zip(w, d)) / sum(w)
    return pred


def m_chained(rows, p, rounds=10):
    mask = [[r[j] is None for j in range(p)] for r in rows]
    means = [_mean_sd([r[j] for r in rows if r[j] is not None])[0] for j in range(p)]
    cur = [[means[j] if r[j] is None else r[j] for j in range(p)] for r in rows]
    for _ in range(rounds):
        for j in range(p):
            if not any(m[j] for m in mask):
                continue
            others = [c for c in range(p) if c != j]
            T = [i for i in range(len(rows)) if not mask[i][j]]
            model = _Ridge([[cur[i][c] for c in others] for i in T], [cur[i][j] for i in T])
            for i in range(len(rows)):
                if mask[i][j]:
                    cur[i][j] = model.predict([cur[i][c] for c in others])
    return lambda i, j: cur[i][j]


# ----------------------------------------------------------------- run

def run(name, cols, rows, ids, reps=5, frac=0.20):
    p = len(cols)
    sd = [_mean_sd([r[j] for r in rows if r[j] is not None])[1] for j in range(p)]
    agg = {m: [] for m in ("mean", "knn", "ridge", "chained", "omni")}
    cover_nf, n_nf, cover, filled, total, fill_err, fill_best, open_err, status_tot = 0, 0, 0, 0, 0, [], {}, [], {}
    for rep in range(reps):
        rng = random.Random(100 + rep)
        cells = [(i, j) for i in range(len(rows)) for j in range(p) if rows[i][j] is not None]
        hidden = set(rng.sample(cells, int(frac * len(cells))))
        masked = [[None if (i, j) in hidden else rows[i][j] for j in range(p)] for i in range(len(rows))]
        preds = {
            "mean": m_mean(masked, p),
            "knn": m_ridge_knn(masked, p, "knn"),
            "ridge": m_ridge_knn(masked, p, "ridge"),
            "chained": m_chained(masked, p),
        }
        og = OmniGap(cols, masked, identities=ids, seed=rep)
        fills = {(f.row, og.ci[f.column]): f for f in og.fill() if f.column in og.ci}
        preds["omni"] = lambda i, j: fills[(i, j)].center
        err = {m: [[] for _ in range(p)] for m in preds}
        for (i, j) in hidden:
            truth = rows[i][j]
            for m, f in preds.items():
                err[m][j].append((f(i, j) - truth) / sd[j])
            fo = fills[(i, j)]
            status_tot[fo.status] = status_tot.get(fo.status, 0) + 1
            total += 1
            eps = 1e-9 * max(1.0, abs(truth))  # float round-off on exact (forced) fills
            inside = fo.lo - eps <= truth <= fo.hi + eps
            cover += inside
            if fo.status != FORCED:
                cover_nf, n_nf = cover_nf + inside, n_nf + 1
            if fo.status in (FILL, FORCED):
                filled += 1
                fill_err.append(((fo.value - truth) / sd[j]) ** 2)
                for m in ("knn", "ridge", "chained"):
                    fill_best.setdefault(m, []).append(((preds[m](i, j) - truth) / sd[j]) ** 2)
            else:
                open_err.append(((fo.center - truth) / sd[j]) ** 2)
        for m in preds:
            agg[m].append(sum(math.sqrt(sum(e * e for e in ej) / len(ej)) for ej in err[m] if ej) / p)

    print(f"\n=== {name}: {len(rows)} records x {p} variables, {int(frac*100)}% hidden, {reps} masks ===")
    print(f"{'method':<10}{'NRMSE':>8}")
    for m, v in agg.items():
        print(f"{m:<10}{sum(v)/len(v):>8.3f}")
    print(f"omni 90% interval coverage : {100*cover/total:.1f}% all cells, "
          f"{100*cover_nf/max(1, n_nf):.1f}% excluding exact forced fills   (stated: 90%)")
    print(f"omni statuses              : " + ", ".join(f"{k} {100*v/total:.1f}%" for k, v in sorted(status_tot.items())))
    rms = lambda v: math.sqrt(sum(v) / len(v))
    if fill_err:
        print(f"cells omni FILLED ({100*filled/total:.1f}%)  : omni RMS error {rms(fill_err):.3f} sd   | same cells: "
              + ", ".join(f"{m} {rms(v):.3f}" for m, v in fill_best.items()))
    if open_err:
        print(f"cells omni HELD OPEN       : its centre would have erred {rms(open_err):.3f} sd (why it refused to fill them)")
    return {m: sum(v) / len(v) for m, v in agg.items()}


def main():
    results = {}
    for name, cols, loader in DATASETS:
        rows, ids = loader(cols)
        results[name] = run(name, cols, rows, ids)
    cols, rows, ids = synthetic_pnl()
    results["synthetic P&L with identities"] = run("synthetic P&L with 2 identities (synthetic)", cols, rows, ids)
    return results


if __name__ == "__main__":
    main()
