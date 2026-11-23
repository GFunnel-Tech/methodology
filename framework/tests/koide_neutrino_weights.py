#!/usr/bin/env python3
"""
Addendum to test 1b (koide_neutrino.py, run 2026-10-31): paired branches and weights.

This is the script sealed with PRED-005 on 2026-11-23 (then named koide_neutrino.py),
renamed so the 2026-10-31 run keeps its file. Run with no argument for current inputs
(NuFIT 6.0, DESI DR2); run with --pred005 for the inputs sealed in PRED-005
(NuFIT 5.3, DESI 2024).

v5.4 section 14, test 1, second half — "then neutrinos".

The charged-lepton run (koide_delta.py) left this step held open because absolute
neutrino masses are unmeasured. It is runnable anyway: the Brannen form fixes
Koide's Q = 2/3 for any delta, oscillation experiments measure the two mass gaps,
and three masses under two gaps plus Q = 2/3 have one free number left — m1 — which
the condition then fixes.

    sqrt(m_k) = mu * (1 + sqrt(2) * cos(2*pi*k/3 + delta))   =>   Q = 2/3 identically

A bracket can go negative, so a root may carry a sign. The script tries every sign
pattern and both orderings, and reports which admit a solution.

Standard library only. Run:  python3 koide_neutrino.py
"""
import cmath
import math
from itertools import product

import sys

INPUTS = {
    # NuFIT 6.0 (2024) splittings, DESI DR2 + CMB (2025) 95% cap — the 2026-10-31 run's inputs
    "current": dict(DM21=7.49e-5, DM31_NO=2.513e-3, DM32_IO=-2.484e-3, CAP=0.064),
    # NuFIT 5.3, DESI 2024 — the inputs sealed in PRED-005
    "pred005": dict(DM21=7.41e-5, DM31_NO=2.511e-3, DM32_IO=-2.498e-3, CAP=0.072),
}
_SET = INPUTS["pred005" if "--pred005" in sys.argv else "current"]
DM21, DM31_NO, DM32_IO = _SET["DM21"], _SET["DM31_NO"], _SET["DM32_IO"]
COSMO_SUM_LIMIT = _SET["CAP"]   # eV, 95% upper limit on the sum
TWO_THIRDS, TWO_NINTHS = 2 / 3, 2 / 9


def masses_no(m1):
    return m1, math.sqrt(m1**2 + DM21), math.sqrt(m1**2 + DM31_NO)


def masses_io(m3):
    m2 = math.sqrt(m3**2 - DM32_IO)
    m1 = math.sqrt(m2**2 - DM21)
    return m1, m2, m3


def q_signed(m, signs):
    roots = [s * math.sqrt(x) for s, x in zip(signs, m)]
    return sum(m) / sum(roots) ** 2


def scan(masses, signs, lo=1e-9, hi=1.0, steps=40000):
    """Every lightest-mass value where Q crosses 2/3, refined by bisection."""
    out, xs = [], [lo * (hi / lo) ** (i / steps) for i in range(steps + 1)]
    f = lambda x: q_signed(masses(x), signs) - TWO_THIRDS
    for a, b in zip(xs, xs[1:]):
        if (f(a) < 0) != (f(b) < 0):
            for _ in range(200):
                mid = (a + b) / 2
                a, b = (mid, b) if (f(a) < 0) == (f(mid) < 0) else (a, mid)
            out.append((a + b) / 2)
    return out


def brannen_delta(m, signs):
    """delta and mu of the signed roots, read as three phases 120 degrees apart."""
    r = [s * math.sqrt(x) for s, x in zip(signs, m)]
    mu = sum(r) / 3
    z = sum(rk * cmath.exp(-2j * math.pi * k / 3) for k, rk in enumerate(r, start=1))
    return cmath.phase(z / (1.5 * math.sqrt(2) * mu)), mu


def main():
    print(f"Signed Brannen form applied to neutrinos; inputs: {'PRED-005 (NuFIT 5.3, DESI 2024)' if '--pred005' in sys.argv else 'current (NuFIT 6.0, DESI DR2)'}\n")
    found = []
    for name, masses in (("normal", masses_no), ("inverted", masses_io)):
        for signs in product((1, -1), repeat=3):
            if signs[0] == signs[1] == signs[2] == -1 or sum(signs) < 0:
                continue  # overall sign is redundant
            for x in scan(masses, signs):
                m = masses(x)
                found.append((name, signs, m))
    if not found:
        print("No solution in either ordering for any sign pattern.")
        return
    for name, signs, m in found:
        d, mu = brannen_delta(m, signs)
        print(f"ordering={name:8s} signs={signs}")
        print(f"  m1={m[0]:.4e}  m2={m[1]:.4e}  m3={m[2]:.4e} eV")
        print(f"  sum={sum(m):.5f} eV   (cosmology limit {COSMO_SUM_LIMIT} eV: "
              f"{'allowed' if sum(m) < COSMO_SUM_LIMIT else 'EXCLUDED'})")
        print(f"  Q check={q_signed(m, signs):.10f}   delta={d:.5f} rad "
              f"(mod 2pi/3: {d % (2*math.pi/3):.5f}; 2/9={TWO_NINTHS:.5f})\n")
    floor = sum(masses_no(0.0))
    print(f"Normal-ordering floor (m1 = 0): sum = {floor:.5f} eV\n")
    branch_weights(found)


def branch_weights(found, osc_sigmas=(1.0, 1.5, 2.5)):
    """Weight the surviving branches against current measurements.

    Each measurement multiplies a branch's weight by how compatible the branch is
    with it, then the weights are renormalised (Bayesian updating; the same
    arithmetic as environment-selection of stable states). Inputs, all stated:
      - cosmology: one-sided 95% cap on the sum, read as a half-Gaussian at zero;
      - oscillation data: a preference for normal ordering of `osc_sigmas`, read
        as a likelihood ratio exp(s^2 / 2). The spread reflects the dataset dispute.
    """
    sigma = COSMO_SUM_LIMIT / 1.645
    like = lambda total: math.exp(-total**2 / (2 * sigma**2))
    sums = {name: sum(m) for name, _, m in found}
    if not {"normal", "inverted"} <= sums.keys():
        return
    cosmo_lr = like(sums["normal"]) / like(sums["inverted"])
    print(f"Branch weights (cosmology favours normal by {cosmo_lr:.1f}x):")
    for s in osc_sigmas:
        ratio = math.exp(s**2 / 2) * cosmo_lr
        print(f"  oscillation preference {s:.1f} sigma -> P(normal) = {ratio / (1 + ratio):.3f}")


if __name__ == "__main__":
    main()
