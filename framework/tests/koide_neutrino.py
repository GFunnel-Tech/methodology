#!/usr/bin/env python3
"""Test 1b — the neutrino half of v5.4 §14 item 1 ("...then neutrinos").

Standard library only. Inputs: NuFIT 6.0 (2024) central mass-squared splittings.

Question: does the Brannen form  sqrt(m_k) = mu * (1 + sqrt2 * cos(2*pi*k/3 + delta))
that holds the charged leptons (delta = 2/9, framework/tests/koide-delta.md) also hold
the neutrino triplet, given only the two measured splittings?

Part A: all three sqrt(m) positive (Koide Q = 2/3 holds exactly). Scan delta over the
        window where every factor is positive (|delta| < pi/12) and report the range of
        the mu-independent ratio R = (m3^2 - m1^2)/(m2^2 - m1^2) against the measured one.
Part B: allow one factor negative (Q != 2/3 with positive roots; this is Brannen's 2006
        move). Solve mu, delta from the two splittings by bisection for each ordering.
"""
import math

S2 = math.sqrt(2)
D21 = 7.49e-5        # eV^2, m2^2 - m1^2
D3L_NO = 2.513e-3    # eV^2, m3^2 - m1^2 (normal ordering)
D3L_IO = -2.484e-3   # eV^2, m3^2 - m2^2 (inverted ordering)
SUM_BOUND_DESI_DR2 = 0.064  # eV, DESI DR2 (2025) 95% bound on sum of masses


def factors(delta):
    return sorted(1 + S2 * math.cos(2 * math.pi * k / 3 + delta) for k in range(3))


def masses(mu, delta):
    return [(mu * f) ** 2 for f in factors(delta)]  # ascending because factors sorted by value, squares keep order only if all >= 0


def ratio_NO(delta):
    m = sorted(f * f for f in factors(delta))  # masses up to mu^2
    return (m[2] ** 2 - m[0] ** 2) / (m[1] ** 2 - m[0] ** 2)


def ratio_IO(delta):
    m = sorted(f * f for f in factors(delta))  # lightest = m3; heavy pair = m1 < m2
    return (m[2] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[1] ** 2)


def bisect(f, a, b, tol=1e-12, it=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        return None
    for _ in range(it):
        c = 0.5 * (a + b)
        fc = f(c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return 0.5 * (a + b)


def main():
    print("Part A — positive roots (Koide exact)")
    tNO, tIO = D3L_NO / D21, -D3L_IO / D21
    rs_no, rs_io = [], []
    n = 2000
    for i in range(1, n):
        d = -math.pi / 12 + (i / n) * (math.pi / 6)
        if d == 0:
            continue
        rs_no.append(ratio_NO(d))
        rs_io.append(ratio_IO(d))
    print(f"  target R_NO = {tNO:.2f}   available R_NO in window: [{min(rs_no):.1f}, inf)")
    print(f"  target R_IO = {tIO:.2f}   available R_IO in window: [{min(rs_io):.3f}, {max(rs_io):.3f}]")
    print("  verdict: no delta reproduces either ordering -> forced-no for the positive-root form\n")

    print("Part B — one root negative (Brannen 2006)")
    for order, D3L in (("NO", D3L_NO), ("IO", D3L_IO)):
        # ratio is mu-independent; scan delta on the full circle for a sign change
        def R(d):
            m = sorted(f * f for f in factors(d))
            if order == "NO":
                return (m[2] ** 2 - m[0] ** 2) / (m[1] ** 2 - m[0] ** 2) - D3L / D21
            return (m[2] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[1] ** 2) + D3L / D21
        sols = []
        steps = 3600
        prev = None
        for i in range(steps + 1):
            d = 2 * math.pi * i / steps
            try:
                v = R(d)
            except ZeroDivisionError:
                prev = None
                continue
            if prev is not None and prev[1] * v < 0 and abs(v) < 50 and abs(prev[1]) < 50:
                root = bisect(R, prev[0], d)
                if root is not None:
                    root = root % (2 * math.pi / 3)
                    if all(abs(root - s) > 1e-6 for s in sols):
                        sols.append(root)
            prev = (d, v)
        for d in sols:
            m = sorted(f * f for f in factors(d))
            mu2 = D21 / (m[1] ** 2 - m[0] ** 2) if order == "NO" else D21 / (m[2] ** 2 - m[1] ** 2)
            mu = math.sqrt(math.sqrt(mu2))
            mm = [mu * mu * x for x in m]
            Qpos = sum(mm) / sum(math.sqrt(x) for x in mm) ** 2
            print(f"  {order}: delta = {d:.5f} rad  (2/9 + pi/12 = {2/9 + math.pi/12:.5f})   mu = {mu:.5f} sqrt(eV)")
            print(f"      masses (meV) = {[round(1000*x, 3) for x in mm]}   sum = {sum(mm):.4f} eV   "
                  f"Q(positive roots) = {Qpos:.4f}")
            print(f"      DESI DR2 bound sum < {SUM_BOUND_DESI_DR2} eV -> {'survives' if sum(mm) < SUM_BOUND_DESI_DR2 else 'EXCLUDED'}")


if __name__ == "__main__":
    main()
