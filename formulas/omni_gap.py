#!/usr/bin/env python3
"""
omni_gap.py — The Omni Gap Formula, as a runnable engine.

Status: DERIVATION, not canon (AGENTS.md rule 4). Derived from the Master
Meta-Algorithm, the Variable Principle, Layer I.G (Capsule), Layer II
(Correspondence), Layer ◇ and Layer ⊙ (Forcing Test, Anti-Operation), with the
Reality Audit's corrections carried (TERMINATE, F-066; operational falsifiers,
F-042/F-043; "no-signal" as its own outcome, VERDICT.md). See formulas/OMNI-GAP.md.

What it does, for every empty cell x[i][j] of a table:

  DETECT    the feasible set F: bounds and linear identities the record must obey
            ("map what IS measurable on either side").
  PROCESS   evidence channels, each a layer of the framework:
              P  Capsule prior        — every prior record of this variable
              S  Process structure    — the variable's measured relation to the
                                        other variables in the same record
              R  Analogue             — the nearest analogous records in the same system
              C  Correspondence       — the same relation fitted in a PARALLEL system,
                                        scale removed, applied here ("as above, so below":
                                        the fractal transfers, the scale does not)
            fused with weights learned by hiding values that ARE known and
            seeing which channel recovers them (the Capsule loop: every failed
            path is integrated), then conditioned on the identities in F.
  RESPOND   a value for EVERY open cell, with a calibrated interval
            (split-conformal, so the stated miss rate is the measured miss rate),
            a tag saying how the value was made, an operational falsifier, and
            the conjugate gap: the one measurement that would narrow it most.
  TERMINATE the engine never emits a value without its tag. When no channel beats
            the prior, the value is the base rate and the tag says so
            (assumption/prior-only). When the interval is wider than the
            decision tolerance, the tag says so (estimate/wide).

Two rules are enforced in code, not left to the operator:
  1. A fill is never used as an input to another fill (no assumption stacking).
     Only measured values feed the channels; filled cells interact only through
     explicit identities.
  2. Every output carries its tag. A filled value is never reported as
     measured, and an open variable is never left blank: it gets the best
     calculated value plus the tag and range that say how far to trust it.

Standard library only, matching the repository's convention.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from statistics import NormalDist

# Status vocabulary (Forcing Test outcome classes, framework/registers.md §2,
# plus the two the audit found missing: conflict and no-signal).
# Every open cell receives a value. What changes is the TAG that travels with it.
# (Estimate Protocol, substrate/2026-10-20-estimate-protocol.md: a calculated,
# tagged estimate is not an assumption; an untagged one is.)
MEASURED = "measured"
FORCED = "forced-fill"          # one value survives the identities: exact
FILL = "estimate"               # calibrated estimate, interval within the decision tolerance
OPEN = "estimate/wide"          # calibrated estimate, interval wider than the tolerance: act with care
NO_SIGNAL = "assumption/prior-only"  # nothing beats the base rate: the value IS the base rate, tagged as such
CONFLICT = "conflict"           # channels or identities disagree beyond calibration: the blocker


# --------------------------------------------------------------------------- #
# Small linear algebra (no numpy, by convention)
# --------------------------------------------------------------------------- #

def _solve(A, b):
    """Solve A x = b by Gaussian elimination with partial pivoting."""
    n = len(A)
    M = [list(A[r]) + [b[r]] for r in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        if abs(M[p][c]) < 1e-12:
            raise ZeroDivisionError("singular system")
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c:
                f = M[r][c] / M[c][c]
                if f:
                    for k in range(c, n + 1):
                        M[r][k] -= f * M[c][k]
    return [M[r][n] / M[r][r] for r in range(n)]


def _inv(A):
    n = len(A)
    cols = [_solve(A, [1.0 if r == c else 0.0 for r in range(n)]) for c in range(n)]
    return [[cols[c][r] for c in range(n)] for r in range(n)]


def _mean_sd(vals):
    n = len(vals)
    if n == 0:
        return 0.0, 1.0
    m = sum(vals) / n
    if n < 2:
        return m, 1.0
    sd = math.sqrt(sum((v - m) ** 2 for v in vals) / (n - 1))
    return m, (sd if sd > 0 else 1.0)


def _quantile(sorted_vals, q):
    if not sorted_vals:
        return float("inf")
    k = min(len(sorted_vals) - 1, max(0, math.ceil(q * (len(sorted_vals) + 1)) - 1))
    return sorted_vals[k]


# --------------------------------------------------------------------------- #
# Channels
# --------------------------------------------------------------------------- #

class _Ridge:
    """S channel: y ~ X on standardized predictors."""

    def __init__(self, X, y, lam=1.0):
        p = len(X[0]) if X else 0
        self.mx, self.sx = [], []
        for c in range(p):
            m, s = _mean_sd([r[c] for r in X])
            self.mx.append(m)
            self.sx.append(s)
        self.my = sum(y) / len(y)
        Z = [[(r[c] - self.mx[c]) / self.sx[c] for c in range(p)] for r in X]
        yc = [v - self.my for v in y]
        if p:
            A = [[sum(z[a] * z[b] for z in Z) + (lam if a == b else 0.0) for b in range(p)] for a in range(p)]
            rhs = [sum(z[a] * t for z, t in zip(Z, yc)) for a in range(p)]
            self.beta = _solve(A, rhs)
        else:
            self.beta = []
        res = [t - sum(b * zz for b, zz in zip(self.beta, z)) for z, t in zip(Z, yc)]
        dof = max(1, len(y) - p - 1)
        self.resid_sd = math.sqrt(sum(e * e for e in res) / dof)

    def predict(self, x):
        return self.my + sum(b * (v - m) / s for b, v, m, s in zip(self.beta, x, self.mx, self.sx))


@dataclass
class Fill:
    row: int
    column: str
    status: str
    value: float | None           # None only on conflict (the record itself is the question)
    center: float                 # best estimate, always present
    lo: float
    hi: float
    narrowing: float              # 1 - width / prior width (0 = no information gained)
    channels: dict = field(default_factory=dict)
    falsifier: str = ""
    next_measurement: str | None = None
    note: str = ""


@dataclass
class Correspondence:
    """A parallel system whose relations may transfer to the target.

    columns / rows   the source system's table (floats or None)
    mapping          {target column: source column} — which variables correspond
    name             label used in reports

    Transfer is scale-free: the relation is fitted on the source's own
    standardized coordinates (each column centred and scaled within the source)
    and applied to the target's standardized coordinates. Same shape, different
    scale. Whether the shape really transfers is not assumed: the channel earns
    weight only by recovering hidden known values in the target, like every
    other channel, and the calibration reports whether Correspondence held.
    Log-transform columns beforehand when the relation is a power law.
    """
    name: str
    columns: list
    rows: list
    mapping: dict

    def __post_init__(self):
        self.ci = {c: i for i, c in enumerate(self.columns)}
        self.stats = [_mean_sd([r[j] for r in self.rows if r[j] is not None]) for j in range(len(self.columns))]
        self._models = {}

    def model(self, src_j, src_preds):
        key = (src_j, src_preds)
        if key not in self._models:
            T = [r for r in self.rows if r[src_j] is not None and all(r[c] is not None for c in src_preds)]
            if len(T) < max(12, 3 * len(src_preds) + 5):
                self._models[key] = None
            else:
                Z = [[(r[c] - self.stats[c][0]) / self.stats[c][1] for c in src_preds] for r in T]
                zy = [(r[src_j] - self.stats[src_j][0]) / self.stats[src_j][1] for r in T]
                self._models[key] = _Ridge(Z, zy)
        return self._models[key]


# --------------------------------------------------------------------------- #
# The engine
# --------------------------------------------------------------------------- #

class OmniGap:
    """
    columns     list of column names
    rows        list of rows; each a list of float or None (None = the gap)
    identities  list of (coeffs, b): sum(coeffs[col] * x[col]) == b in every row
    bounds      {col: (lo, hi)}; either side may be None
    tolerance   {col: max acceptable interval half-width}; default 0.5 * column sd
    alpha       stated miss rate of every interval (0.10 -> 90% intervals)
    """

    def __init__(self, columns, rows, identities=(), bounds=None, tolerance=None,
                 alpha=0.10, k=7, folds=5, calib_per_column=300, seed=0, correspondences=(), memory=None):
        self.correspondences = list(correspondences)
        self.memory = memory          # formulas/memory.py Memory, or None
        self.cols = list(columns)
        self.ci = {c: i for i, c in enumerate(self.cols)}
        self.rows = [list(r) for r in rows]
        self.n, self.p = len(self.rows), len(self.cols)
        self.identities = [({self.ci[c]: a for c, a in coeffs.items()}, b) for coeffs, b in identities]
        self.bounds = {self.ci[c]: v for c, v in (bounds or {}).items()}
        self.alpha, self.k, self.folds = alpha, k, folds
        self.calib_per_column = calib_per_column
        self.rng = random.Random(seed)
        self.z = NormalDist().inv_cdf(1 - alpha / 2)
        self.stats = [_mean_sd([r[j] for r in self.rows if r[j] is not None]) for j in range(self.p)]
        self.tol = {j: 0.5 * self.stats[j][1] for j in range(self.p)}
        for c, v in (tolerance or {}).items():
            self.tol[self.ci[c]] = v
        self.fold_of = [i % folds for i in range(self.n)]
        self.rng.shuffle(self.fold_of)
        self._models = {}
        self.calibration = {}

    # ---- channel evaluation for one cell, training only on rows in `fold != hold`

    def _train_rows(self, j, preds, hold):
        return [r for i, r in enumerate(self.rows)
                if self.fold_of[i] != hold and r[j] is not None and all(r[c] is not None for c in preds)]

    def _model(self, j, preds, hold):
        key = (j, preds, hold)
        if key not in self._models:
            T = self._train_rows(j, preds, hold)
            if len(T) < max(12, 3 * len(preds) + 5):
                self._models[key] = None
            else:
                X = [[r[c] for c in preds] for r in T]
                y = [r[j] for r in T]
                self._models[key] = (_Ridge(X, y), T)
        return self._models[key]

    def _channels(self, i, j, hold=None):
        row = self.rows[i]
        mean_j = _mean_sd([r[j] for k_, r in enumerate(self.rows)
                           if r[j] is not None and self.fold_of[k_] != hold])[0]
        out = {"P": mean_j}
        known = tuple(c for c in range(self.p) if c != j and row[c] is not None)
        # C: the relation from each parallel system, on standardized coordinates
        if self.correspondences:
            sd_j = _mean_sd([r[j] for k_, r in enumerate(self.rows)
                             if r[j] is not None and self.fold_of[k_] != hold])[1]
            for n_, co in enumerate(self.correspondences):
                tj = self.cols[j]
                if tj not in co.mapping:
                    continue
                mapped = tuple(c for c in known if self.cols[c] in co.mapping)
                if not mapped:
                    continue
                src_j = co.ci[co.mapping[tj]]
                src_preds = tuple(co.ci[co.mapping[self.cols[c]]] for c in mapped)
                m = co.model(src_j, src_preds)
                if m is None:
                    continue
                zx = [(row[c] - self.stats[c][0]) / self.stats[c][1] for c in mapped]
                out[f"C{n_ + 1}"] = mean_j + m.predict(zx) * sd_j
        preds = known
        # drop predictors until there is enough shared data to fit (fewest-missing kept)
        while preds and self._model(j, preds, hold) is None:
            miss = {c: sum(r[c] is None for r in self.rows) for c in preds}
            preds = tuple(c for c in preds if c != max(preds, key=lambda c: miss[c]))
        if not preds:
            return out, preds
        model, T = self._model(j, preds, hold)
        x = [row[c] for c in preds]
        out["S"] = model.predict(x)
        # R: nearest analogous records on the same measured coordinates
        sd = [self.stats[c][1] for c in preds]
        dist = []
        for r in T:
            d = math.sqrt(sum(((r[c] - v) / s) ** 2 for c, v, s in zip(preds, x, sd)))
            dist.append((d, r[j]))
        dist.sort(key=lambda t: t[0])
        nn = dist[: self.k]
        w = [1.0 / (d + 1e-6) for d, _ in nn]
        out["R"] = sum(wi * v for wi, (_, v) in zip(w, nn)) / sum(w)
        return out, preds

    # ---- the Capsule loop: hide known values, learn what recovers them

    def calibrate(self):
        for j in range(self.p):
            known = [i for i in range(self.n) if self.rows[i][j] is not None]
            self.rng.shuffle(known)
            known = known[: self.calib_per_column]
            recs = []
            for i in known:
                ch, _ = self._channels(i, j, hold=self.fold_of[i])
                recs.append((ch, self.rows[i][j]))
            w = self._stack_weights(recs)
            corr = None
            if self.correspondences:
                cn = [n for n in w if n.startswith("C")]
                w0 = self._stack_weights(recs, exclude=[f"C{k_ + 1}" for k_ in range(len(self.correspondences))])
                sse = lambda ww: sum((y - self._combine(ch, ww)) ** 2 for ch, y in recs)
                gain = 1 - math.sqrt(sse(w) / max(sse(w0), 1e-300))
                corr = {"weights": {n: round(w[n], 3) for n in cn}, "error_reduction": gain,
                        "verdict": "held" if cn and gain > 0.02 else "not supported here"}
            chan_counts = {}
            for ch, _ in recs:
                key = "+".join(sorted(ch))
                chan_counts[key] = chan_counts.get(key, 0) + 1
            expression = max(chan_counts, key=chan_counts.get) if chan_counts else "P"
            res, prior_res, disagree = [], [], []
            for ch, y in recs:
                res.append(abs(y - self._combine(ch, w)))
                prior_res.append(abs(y - ch["P"]))
                if "S" in ch and "R" in ch:
                    disagree.append(abs(ch["S"] - ch["R"]))
            res.sort(); prior_res.sort(); disagree.sort()
            q = _quantile(res, 1 - self.alpha)
            q0 = _quantile(prior_res, 1 - self.alpha)
            self.calibration[j] = {
                "weights": w,
                "halfwidth": q,
                "prior_halfwidth": q0,
                "conflict_threshold": _quantile(disagree, 0.995) if len(disagree) > 50 else float("inf"),
                "n": len(recs),
                "rmse": math.sqrt(sum(e * e for e in res) / max(1, len(res))),
                "no_signal": q >= 0.95 * q0,
                "correspondence": corr,
                "cases": known,
                "source": "this run",
                "expression": expression,
            }
            self._pool_with_memory(j)
        if self.identities:
            self._calibrate_identities()
        self._remember()
        return self.calibration

    # ---- memory: the Capsule. Prior runs on the same variable pool their calibration
    # into this one when this run's own calibration rests on few cases. Memory never
    # replaces a measurement: the pooled width is weighted by cases, the source is named.

    POOL_BELOW = 30   # pool when this run calibrated on fewer cases than this

    def _pool_with_memory(self, j):
        if not self.memory:
            return
        cal = self.calibration[j]
        if cal["n"] >= self.POOL_BELOW:
            return
        # pool only with runs that used the SAME expression on this variable: a width
        # learned with structure+analogue channels does not describe a prior-only estimate
        past = self.memory.recall(self.cols[j], cal["expression"], cal["n"])
        if not past:
            cal["source"] = "this run (memory holds no run with the same expression and size regime)"
            return
        sd = self.stats[j][1]
        n_now, n_past = cal["n"], past["cases"]
        pooled = (cal["halfwidth"] / sd * n_now + past["halfwidth_sd"] * n_past) / (n_now + n_past)
        cal["halfwidth_own"] = cal["halfwidth"]
        cal["halfwidth"] = pooled * sd
        if n_now < 12:                       # too few to have learned weights worth keeping
            cal["weights"] = dict(past["weights"])
            cal["no_signal"] = past["no_signal"]
        cal["source"] = f"pooled with memory ({past['runs']} prior run(s), {n_past} cases, same expression and size regime)"

    def _remember(self):
        if not self.memory:
            return
        from memory import fingerprint
        cols = {}
        for j, c in enumerate(self.cols):
            cal = self.calibration[j]
            cols[c] = {"weights": {k: round(v, 4) for k, v in cal["weights"].items()},
                       "halfwidth_sd": round(cal.get("halfwidth_own", cal["halfwidth"]) / self.stats[j][1], 4),
                       "n": cal["n"], "no_signal": cal["no_signal"], "expression": cal["expression"],
                       "correspondence": ({"verdict": cal["correspondence"]["verdict"],
                                           "error_reduction": round(cal["correspondence"]["error_reduction"], 4)}
                                          if cal.get("correspondence") else None),
                       "source": "this run" if cal["source"].startswith("this run") else cal["source"]}
        self._memory_record = {"columns": cols, "identities": len(self.identities), "alpha": self.alpha,
                               "correspondences": [c.name for c in self.correspondences]}
        self._fingerprint = fingerprint(self.cols, self.rows)

    def _calibrate_identities(self):
        """Second pass of the Capsule loop: run the WHOLE pipeline, identities
        included, on hidden known values. Cells that an identity narrows but does
        not force get their own interval width, measured rather than assumed
        (conditioning alone would assume their errors are independent)."""
        for j in range(self.p):
            res = []
            for i in self.calibration[j]["cases"]:
                truth = self.rows[i][j]
                self.rows[i][j] = None
                gaps = [c for c in range(self.p) if self.rows[i][c] is None]
                mu, h, _, forced, touched = self._estimate_row(i, gaps, hold=self.fold_of[i])
                self.rows[i][j] = truth
                if j in touched and not forced.get(j):
                    res.append(abs(truth - mu[j]))
            res.sort()
            cal = self.calibration[j]
            cal["n_identity"] = len(res)
            # split-conformal is valid from (1-alpha)/alpha cases; below that the width
            # cannot be measured, so fall back to the base-rate width (no narrowing claimed)
            n_min = math.ceil((1 - self.alpha) / self.alpha)
            cal["halfwidth_identity"] = (_quantile(res, 1 - self.alpha) if len(res) >= n_min
                                         else cal["prior_halfwidth"])

    @staticmethod
    def _stack_weights(recs, exclude=()):
        """Non-negative least squares over channel subsets (exact: all subsets tried)."""
        names = sorted({n for ch, _ in recs for n in ch} - set(exclude), key=lambda n: (n[0] != "P", n))
        best, best_sse = {"P": 1.0}, float("inf")
        for mask in range(1, 1 << len(names)):
            sub = [n for b, n in enumerate(names) if mask >> b & 1]
            data = [(ch, y) for ch, y in recs if all(n in ch for n in sub)]
            if len(data) < len(sub) + 5:
                continue
            A = [[sum(ch[a] * ch[b] for ch, _ in data) for b in sub] for a in sub]
            rhs = [sum(ch[a] * y for ch, y in data) for a in sub]
            try:
                coef = _solve(A, rhs)
            except ZeroDivisionError:
                continue
            if any(c < 0 for c in coef):
                continue
            # score on ALL records, falling back to the prior where a channel is absent
            w = dict(zip(sub, coef))
            sse = sum((y - OmniGap._combine(ch, w)) ** 2 for ch, y in recs)
            if sse < best_sse:
                best, best_sse = w, sse
        return best

    @staticmethod
    def _combine(ch, w):
        avail = {n: c for n, c in w.items() if n in ch}
        missing = sum(c for n, c in w.items() if n not in ch)
        # mass of an unavailable channel is redistributed to the prior
        return sum(c * ch[n] for n, c in avail.items()) + missing * ch["P"]

    # ---- the conjugate gap: which missing measurement would narrow this cell most

    def _next_measurement(self, i, j, preds):
        row = self.rows[i]
        base = self._model(j, preds, None) if preds else None
        base_sd = base[0].resid_sd if base else self.stats[j][1]
        best = None
        for c in range(self.p):
            if c == j or row[c] is not None:
                continue
            m = self._model(j, tuple(sorted(preds + (c,))), None)
            if m is None:
                continue
            gain = 1 - m[0].resid_sd / base_sd
            if best is None or gain > best[1]:
                best = (c, gain)
        if best and best[1] > 0.05:
            return f"measure {self.cols[best[0]]} (expected to shrink this interval ~{100 * best[1]:.0f}%)"
        return None

    # ---- RESPOND

    def fill(self):
        if not self.calibration:
            self.calibrate()
        fills = []
        for i, row in enumerate(self.rows):
            gaps = [j for j in range(self.p) if row[j] is None]
            if not gaps:
                self._check_measured_identities(i, fills)
                continue
            mu, h, info, forced, touched = self._estimate_row(i, gaps)
            for j in gaps:
                if j in touched and not forced.get(j):
                    h[j] = self.calibration[j]["halfwidth_identity"]
                fills.append(self._respond(i, j, mu[j], h[j], info[j], forced.get(j, False)))
        if self.memory:
            tags = {}
            nxt = {}
            for f in fills:
                tags[f.status] = tags.get(f.status, 0) + 1
                if f.next_measurement:
                    nxt[f.next_measurement] = nxt.get(f.next_measurement, 0) + 1
            conj = max(nxt, key=nxt.get) if nxt else None
            self.memory.record("omni-gap", self._fingerprint, self._memory_record,
                               {"cells": len(fills), "tags": tags,
                                "mean_narrowing": round(sum(f.narrowing for f in fills) / max(1, len(fills)), 4)},
                               conjugate=conj)
        return fills

    def _estimate_row(self, i, gaps, hold=None):
        mu, h, info = {}, {}, {}
        for j in gaps:
            cal = self.calibration[j]
            ch, preds = self._channels(i, j, hold=hold)
            mu[j] = self._combine(ch, cal["weights"])
            h[j] = cal["halfwidth"]
            flag = ("S" in ch and "R" in ch and abs(ch["S"] - ch["R"]) > cal["conflict_threshold"])
            info[j] = (ch, preds, flag)
        forced, touched = self._condition(i, gaps, mu, h)
        return mu, h, info, forced, touched

    def _condition(self, i, gaps, mu, h):
        """Condition the per-cell Gaussians on the row's linear identities."""
        row = self.rows[i]
        A, b = [], []
        for coeffs, rhs in self.identities:
            unk = [j for j in coeffs if row[j] is None]
            if not unk:
                continue
            A.append([coeffs.get(j, 0.0) for j in gaps])
            b.append(rhs - sum(a * row[j] for j, a in coeffs.items() if row[j] is not None))
        if not A:
            return {}, set()
        sig2 = [(h[j] / self.z) ** 2 for j in gaps]
        x = [mu[j] for j in gaps]
        # Keep only independent identities: a redundant one adds no information
        # (and would make the system singular).
        kept, kept_b, all_A, all_b = [], [], A, b
        for r_, b_ in zip(all_A, all_b):
            trial = kept + [r_]
            M = [[sum(p[g] * sig2[g] * q[g] for g in range(len(gaps))) for q in trial] for p in trial]
            try:
                _inv(M)
            except ZeroDivisionError:
                continue
            kept.append(r_)
            kept_b.append(b_)
        A, b = kept, kept_b
        touched = {j for g, j in enumerate(gaps) if any(abs(r_[g]) > 0 for r_ in A)}
        SAt = [[sig2[g] * A[r][g] for r in range(len(A))] for g in range(len(gaps))]
        ASAt = [[sum(A[r][g] * SAt[g][s] for g in range(len(gaps))) for s in range(len(A))] for r in range(len(A))]
        inv = _inv(ASAt)
        resid = [b[r] - sum(A[r][g] * x[g] for g in range(len(gaps))) for r in range(len(A))]
        K = [[sum(SAt[g][s] * inv[s][r] for s in range(len(A))) for r in range(len(A))] for g in range(len(gaps))]
        forced = {}
        for g, j in enumerate(gaps):
            mu[j] = x[g] + sum(K[g][r] * resid[r] for r in range(len(A)))
            post = sig2[g] - sum(K[g][r] * SAt[g][r] for r in range(len(A)))
            forced[j] = post <= 1e-9 * sig2[g]
            h[j] = 0.0 if forced[j] else self.z * math.sqrt(max(post, 0.0))
        # A redundant identity the conditioned values do not satisfy = the identities
        # contradict each other on this record's measurements.
        for coeffs, rhs in self.identities:
            vals = [mu[j] if row[j] is None else row[j] for j in coeffs]
            lhs = sum(a * v for a, v in zip(coeffs.values(), vals))
            if abs(lhs - rhs) > 1e-6 * max(1.0, abs(rhs), *(abs(v) for v in vals)):
                for j in coeffs:
                    if row[j] is None:
                        forced[j] = "conflict"
        return forced, touched

    def _respond(self, i, j, mu, h, info, forced):
        ch, preds, flag = info
        cal = self.calibration[j]
        lo, hi = mu - h, mu + h
        blo, bhi = self.bounds.get(j, (None, None))
        if blo is not None:
            lo, mu = max(lo, blo), max(mu, blo)
        if bhi is not None:
            hi, mu = min(hi, bhi), min(mu, bhi)
        prior_w = 2 * cal["prior_halfwidth"]
        narrowing = max(0.0, 1 - (hi - lo) / prior_w) if prior_w > 0 else 0.0
        name = self.cols[j]
        if forced == "conflict":
            status, value = CONFLICT, None
            fals = "The record's measured values make its identities contradict each other: the data or an identity is wrong."
        elif forced:
            status, value = FORCED, mu
            fals = f"Refuted if the identities do not hold for this record (a measured {name} != {mu:.6g})."
        elif flag:
            status, value = CONFLICT, None
            lo = min(ch["S"], ch["R"]) - h
            hi = max(ch["S"], ch["R"]) + h
            fals = "Structure and analogues disagree beyond anything seen in calibration: this record is unlike the rest. Measure it."
        elif cal["no_signal"]:
            status, value = NO_SIGNAL, mu
            fals = (f"Base rate only: nothing in the record predicts {name} better than its average. "
                    f"Refuted if measured {name} falls outside [{lo:.6g}, {hi:.6g}] ({100 * (1 - self.alpha):.0f}%).")
        elif h <= self.tol[j]:
            status, value = FILL, mu
            fals = (f"Refuted if measured {name} falls outside [{lo:.6g}, {hi:.6g}]; "
                    f"stated miss rate {100 * self.alpha:.0f}% (measured on {cal['n']} hidden known values).")
        else:
            status, value = OPEN, mu
            fals = (f"Wide: the range exceeds the decision tolerance. Refuted if measured {name} falls outside "
                    f"[{lo:.6g}, {hi:.6g}] ({100 * (1 - self.alpha):.0f}%).")
        nxt = None if status in (FORCED, FILL) else self._next_measurement(i, j, preds)
        note = "" if cal["source"] == "this run" else f"calibration {cal['source']}"
        return Fill(i, name, status, value, mu, lo, hi, narrowing,
                    {k: round(v, 6) for k, v in ch.items()}, fals, nxt, note)

    def _check_measured_identities(self, i, fills):
        row = self.rows[i]
        for coeffs, rhs in self.identities:
            lhs = sum(a * row[j] for j, a in coeffs.items())
            scale = max(1.0, abs(rhs), *(abs(a * row[j]) for j, a in coeffs.items()))
            if abs(lhs - rhs) > 1e-6 * scale:
                names = "+".join(self.cols[j] for j in coeffs)
                fills.append(Fill(i, names, CONFLICT, None, lhs, lhs, lhs, 0.0, {},
                                  "Measured values violate a stated identity: the data or the identity is wrong.",
                                  None, "reality vs structure: reality wins (substrate item 1)"))


def summarize(fills):
    counts = {}
    for f in fills:
        counts[f.status] = counts.get(f.status, 0) + 1
    return counts
