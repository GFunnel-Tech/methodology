#!/usr/bin/env python3
"""
correspondence_test.py — does a relation learned in one system fill gaps in another?

Status: DERIVATION / variable evidence, not canon. Tests the Correspondence
channel (C) of formulas/omni_gap.py: fit the shape of a relation in a PARALLEL
system, remove the scale, apply it where the target system's own data is thin.

Five pairs. In each, the TARGET is made deliberately small (so its own
structure channel is weak), a share of its known values is hidden, and the
hidden truth is recovered three ways:

  own data only     omni with channels P, S, R from the target alone
  + correspondence  omni with the C channel from the source added
  naive transfer    the source's regression applied to the target in RAW units
                    (what "use the other system's formula" means without the
                    scale removal)

Pairs
  1  Mammal brain mass: small-bodied species -> the 20 largest-bodied species
     (log10 body, log10 brain; the Snell/Jerison power law). Same relation,
     three orders of magnitude apart in scale: the fractal case.
  2  Penguins: Adelie + Chinstrap -> Gentoo (a larger species), body mass.
  3  Cars: USA -> Japan, fuel economy.
  4  ARBITRARY MAPPING: cars (USA) onto penguins by column position. Written as
     a negative control, it is not one: the pairing happens to preserve the SIGN
     of the relations (bigger engine -> heavier car; longer flipper -> heavier
     penguin), and in standardized space that is most of what transfers. It is
     kept because it shows what Correspondence actually carries.
  5  TRUE NEGATIVE CONTROL: the same pairing with the sign reversed (penguin
     body mass mapped to fuel economy, which FALLS with size). Correspondence
     should earn ~zero weight, and the engine should say so.

Run:  python3 formulas/correspondence_test.py      (standard library only)
"""

from __future__ import annotations

import csv
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from omni_gap import OmniGap, Correspondence, _Ridge, _mean_sd  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def read(name):
    with open(os.path.join(HERE, "data", name), newline="") as f:
        return list(csv.DictReader(f))


def num(v):
    return None if v in ("", "NA", "nan") else float(v)


def table(recs, cols, where=lambda r: True, transform=None):
    out = []
    for r in recs:
        if not where(r):
            continue
        row = [num(r[c]) for c in cols]
        if transform:
            row = [None if v is None else transform(v) for v in row]
        out.append(row)
    return out


def pairs():
    log = math.log10
    mam = read("mammals.csv")
    mam.sort(key=lambda r: float(r["body"]))
    yield ("1 mammal brain mass, small-bodied -> 20 largest (log10)",
           ["body", "brain"], table(mam[:-20], ["body", "brain"], transform=log), "brain",
           ["body", "brain"], table(mam[-20:], ["body", "brain"], transform=log),
           {"body": "body", "brain": "brain"}, 20, 0.5)
    pen = read("penguins.csv")
    pc = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    yield ("2 penguins, Adelie+Chinstrap -> Gentoo (thin: 20 birds)",
           pc, table(pen, pc, lambda r: r["species"] != "Gentoo"), "body_mass_g",
           pc, table(pen, pc, lambda r: r["species"] == "Gentoo"),
           {c: c for c in pc}, 20, 0.5)
    mpg = read("mpg.csv")
    mc = ["mpg", "displacement", "horsepower", "weight", "acceleration"]
    yield ("3 cars, USA -> Japan (thin: 20 cars)",
           mc, table(mpg, mc, lambda r: r["origin"] == "usa"), "mpg",
           mc, table(mpg, mc, lambda r: r["origin"] == "japan"),
           {c: c for c in mc}, 20, 0.5)
    yield ("4 ARBITRARY MAPPING (sign preserved): cars (USA) onto penguins (Gentoo)",
           mc, table(mpg, mc, lambda r: r["origin"] == "usa"), "body_mass_g",
           pc, table(pen, pc, lambda r: r["species"] == "Gentoo"),
           {"body_mass_g": "weight", "flipper_length_mm": "displacement",
            "bill_length_mm": "horsepower", "bill_depth_mm": "acceleration"}, 20, 0.5)
    yield ("5 TRUE NEGATIVE CONTROL (sign reversed): penguin mass <- car mpg",
           mc, table(mpg, mc, lambda r: r["origin"] == "usa"), "body_mass_g",
           pc, table(pen, pc, lambda r: r["species"] == "Gentoo"),
           {"body_mass_g": "mpg", "flipper_length_mm": "weight",
            "bill_length_mm": "displacement", "bill_depth_mm": "horsepower"}, 20, 0.5)


def run(name, scols, srows, target_col, tcols, trows_all, mapping, n_target, frac, masks=20):
    tj = tcols.index(target_col)
    sd_t = _mean_sd([r[tj] for r in trows_all if r[tj] is not None])[1]
    co = Correspondence("source", scols, srows, mapping)
    # naive transfer: source regression in raw units on the mapped predictors
    mapped_t = [c for c in tcols if c in mapping and c != target_col]
    sp = [scols.index(mapping[c]) for c in mapped_t]
    sj = scols.index(mapping[target_col])
    T = [r for r in srows if r[sj] is not None and all(r[c] is not None for c in sp)]
    naive = _Ridge([[r[c] for c in sp] for r in T], [r[sj] for r in T])
    err = {"own data only": [], "+ correspondence": [], "naive transfer": []}
    weights, verdicts = [], {}
    for m in range(masks):
        rng = random.Random(500 + m)
        trows = rng.sample(trows_all, min(n_target, len(trows_all)))
        known = [i for i, r in enumerate(trows) if r[tj] is not None]
        hidden = set(rng.sample(known, max(1, int(frac * len(known)))))
        masked = [[None if (i == i2 and j == tj and i in hidden) else v for j, v in enumerate(r)]
                  for i2, r in enumerate(trows) for i in [i2]]
        for label, cos in (("own data only", ()), ("+ correspondence", (co,))):
            og = OmniGap(tcols, masked, correspondences=cos, seed=m, folds=min(5, len(trows)))
            fills = {(f.row, og.ci[f.column]): f for f in og.fill() if f.column in og.ci}
            for i in hidden:
                err[label].append(((fills[(i, tj)].center - trows[i][tj]) / sd_t) ** 2)
            if cos:
                c = og.calibration[tj]["correspondence"]
                weights.append(sum(c["weights"].values()))
                verdicts[c["verdict"]] = verdicts.get(c["verdict"], 0) + 1
        for i in hidden:
            x = [trows[i][tcols.index(c)] for c in mapped_t]
            if all(v is not None for v in x):
                err["naive transfer"].append(((naive.predict(x) - trows[i][tj]) / sd_t) ** 2)
    rms = lambda v: math.sqrt(sum(v) / len(v)) if v else float("nan")
    print(f"\n=== {name} ===  source {len(srows)} rows -> target {n_target} rows, {int(frac*100)}% of '{target_col}' hidden, {masks} masks")
    for k, v in err.items():
        print(f"  {k:<18} NRMSE {rms(v):.3f}")
    print(f"  correspondence weight (mean) {sum(weights)/len(weights):.2f}; engine verdict: "
          + ", ".join(f"{k} in {v}/{masks} runs" for k, v in verdicts.items()))
    return {k: rms(v) for k, v in err.items()}


def main():
    for args in pairs():
        run(*args)


if __name__ == "__main__":
    main()
