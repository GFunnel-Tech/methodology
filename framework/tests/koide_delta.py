#!/usr/bin/env python3
"""
v5.4 section 14, test 1 — the Koide / delta = 2/9 prediction run.

Brannen parametrization (v5.4 section 6):
    sqrt(m_k) = mu * (1 + sqrt(2) * cos(2*pi*k/3 + delta)),  k = 1,2,3

v5.4 claims the trefoil fixes delta = 2/9. This script tests that claim.
Standard library only. Run:  python3 koide_delta.py
"""
import math

# PDG 2024 charged-lepton pole masses (MeV)
M_E, M_MU, M_TAU, M_TAU_U = 0.51099895069, 105.6583755, 1776.93, 0.09
M_TAU_V54 = 1776.86          # value cited in v5.4 section 6
S2, TWO_NINTHS = math.sqrt(2), 2 / 9
NAMES = {1: "m_e", 2: "m_mu", 3: "m_tau"}


def bracket(k, delta):
    """The Brannen bracket. k=1 -> electron, 2 -> muon, 3 -> tau."""
    return 1 + S2 * math.cos(2 * math.pi * k / 3 + delta)


def koide_q(a, b, c):
    return (a + b + c) / (math.sqrt(a) + math.sqrt(b) + math.sqrt(c)) ** 2


def solve(f, lo, hi, iters=200):
    """Bisect f on a bracket known to contain one sign change."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        if (f(lo) < 0) == (f(mid) < 0):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def fit_delta(m_tau, m_mu=M_MU):
    """Fit delta from the (mu, tau) pair -- the well-conditioned pair."""
    return solve(lambda d: bracket(3, d) / bracket(2, d) - math.sqrt(m_tau / m_mu),
                 0.15, 0.35)


def predict(anchor_k, anchor_m, delta=TWO_NINTHS):
    """Fix delta, set the scale mu from one mass, return all three."""
    mu = math.sqrt(anchor_m) / bracket(anchor_k, delta)
    return {k: (mu * bracket(k, delta)) ** 2 for k in (1, 2, 3)}


def main():
    obs = {1: M_E, 2: M_MU, 3: M_TAU}

    print("=" * 68)
    print("1. Koide Q from measured masses")
    print("=" * 68)
    for lbl, mt in (("PDG 2024 (tau=1776.93)", M_TAU), ("v5.4 cites (tau=1776.86)", M_TAU_V54)):
        q = koide_q(M_E, M_MU, mt)
        print(f"  {lbl:28s} Q = {q:.12f}   |Q-2/3|/(2/3) = {abs(q - 2/3)/(2/3):.3e}")
    print("\n  NOTE: Q = 2/3 is IDENTICALLY TRUE for the Brannen form at any delta.")
    print("  The 6 ppm Koide agreement is therefore built into the form, not evidence for it.")
    print("  All testable content sits in the value of delta.")

    print("\n" + "=" * 68)
    print("2. delta fitted from data, vs the trefoil claim delta = 2/9")
    print("=" * 68)
    d0 = fit_delta(M_TAU)
    sigma = (abs(fit_delta(M_TAU + M_TAU_U) - d0) + abs(fit_delta(M_TAU - M_TAU_U) - d0)) / 2
    print(f"  delta (fitted)  = {d0:.10f} +/- {sigma:.10f}   (1 sigma, from tau mass +/-{M_TAU_U})")
    print(f"  2/9             = {TWO_NINTHS:.10f}")
    print(f"  difference      = {d0 - TWO_NINTHS:+.3e}  =  {(d0 - TWO_NINTHS)/sigma:+.2f} sigma")
    print(f"  v5.4 quotes delta = 0.22224; this fit gives {d0:.5f} (PDG 2024)"
          f" / {fit_delta(M_TAU_V54):.5f} (tau=1776.86)")

    print("\n" + "=" * 68)
    print("3. THE PREDICTION RUN: fix delta = 2/9 exactly, one free scale mu")
    print("=" * 68)
    for k in (1, 2, 3):
        pred = predict(k, obs[k])
        others = [j for j in (1, 2, 3) if j != k]
        print(f"\n  Anchored on {NAMES[k]}:")
        for j in others:
            err = 100 * (pred[j] - obs[j]) / obs[j]
            print(f"    {NAMES[j]:6s} predicted {pred[j]:13.7f}  observed {obs[j]:13.7f}  error {err:+8.4f} %")

    print("\n" + "=" * 68)
    print("4. Conditioning -- why the anchor choice matters")
    print("=" * 68)
    sens = {}
    for k in (1, 2, 3):
        sens[k] = -2 * S2 * math.sin(2 * math.pi * k / 3 + TWO_NINTHS) / bracket(k, TWO_NINTHS)
        print(f"  d ln({NAMES[k]}) / d delta = {sens[k]:+10.4f}")
    print(f"\n  m_e is {abs(sens[1]/sens[3]):.0f}x more sensitive to delta than m_tau.")
    print("  m_e is therefore the SHARPEST probe of delta, not the safest anchor.")
    print("  With delta fixed there is 1 free parameter (mu) for 3 masses -> 2 real predictions.")


if __name__ == "__main__":
    main()
