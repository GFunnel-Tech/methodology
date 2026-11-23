#!/usr/bin/env python3
"""
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

# NuFIT 5.3 (2024) best fits, eV^2. Normal ordering: m1 < m2 < m3.
DM21 = 7.41e-5
DM31_NO = 2.511e-3          # m3^2 - m1^2, normal ordering
DM32_IO = -2.498e-3         # m3^2 - m2^2, inverted ordering (m3 lightest)
COSMO_SUM_LIMIT = 0.072     # eV, DESI 2024 + CMB, 95% upper limit
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
    print("Koide Q = 2/3 applied to neutrinos, oscillation gaps from NuFIT 5.3\n")
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
    print(f"Normal-ordering floor (m1 = 0): sum = {floor:.5f} eV")


if __name__ == "__main__":
    main()
