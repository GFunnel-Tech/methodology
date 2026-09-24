#!/usr/bin/env python3
"""
Reality Audit, Phase 4 — supporting derivations for v5.1 Appendix D,
CONSERVATION LAWS and DYNAMICAL LAWS tables. Standard library only.

Every input number below was fetched during the run (2026-09-24); the URL is
next to it. Outputs are `derived` rows in the audit files that cite this script.

Run:  python3 audit/constants/check_law_derivations.py
"""
import math

# ---- CODATA 2022, https://physics.nist.gov/cuu/Constants/Table/allascii.txt (retrieved 2026-09-24) ----
G = 6.67430e-11              # m^3 kg^-1 s^-2
E_CHARGE = 1.602176634e-19   # C (exact)
M_E = 9.1093837139e-31       # kg
M_P = 1.67262192595e-27      # kg
EPS0 = 8.8541878188e-12      # F m^-1
MU0 = 1.25663706127e-6       # N A^-2

# 1. Kepler row: ratio of gravitational to Coulomb attraction between proton and electron
#    (distance cancels: both are 1/r^2).
ratio = (G * M_E * M_P) / (E_CHARGE ** 2 / (4 * math.pi * EPS0))
print(f"[DERIVED] F_grav/F_coulomb (proton-electron) = {ratio:.3e}")

# 2. pi row / Maxwell: after the 2019 SI redefinition mu0 is measured, not 4*pi*1e-7 exactly.
print(f"[DERIVED] mu0/(4*pi*1e-7) - 1 = {MU0 / (4 * math.pi * 1e-7) - 1:.2e}")

# 3. Le Chatelier row: N2 + 3 H2 <=> 2 NH3, ideal gas, constant T and P.
#    Q = x_NH3^2 / (x_N2 x_H2^3) * P^-2. Add dn of N2 at equilibrium (Q = K):
#    d ln Q / d n_N2 = -1/n_N2 + 2/n_tot   (the 2 = -(sum of stoichiometric coefficients) = -(2-1-3)).
#    Q rises above K (reaction shifts LEFT, producing more N2) when x_N2 > 1/2.
def dlnQ_dnN2(n_n2, n_h2, n_nh3):
    n_tot = n_n2 + n_h2 + n_nh3
    return -1 / n_n2 + 2 / n_tot


for n_n2, n_h2, n_nh3 in [(1.0, 3.0, 0.5), (6.0, 2.0, 1.0)]:
    x = n_n2 / (n_n2 + n_h2 + n_nh3)
    d = dlnQ_dnN2(n_n2, n_h2, n_nh3)
    direction = "right (opposes addition)" if d < 0 else "LEFT (produces more N2)"
    print(f"[DERIVED] x_N2 = {x:.3f}: d lnQ/d n_N2 = {d:+.3f} -> shift {direction}")

# 4. Hardy-Weinberg: one generation of random mating from arbitrary genotype frequencies.
AA, Aa, aa = 0.5, 0.1, 0.4
p = AA + Aa / 2
q = 1 - p
nxt = (p * p, 2 * p * q, q * q)
p2 = nxt[0] + nxt[1] / 2
print(f"[DERIVED] start (AA,Aa,aa)=({AA},{Aa},{aa}) p={p:.3f}; after 1 generation {tuple(round(v, 4) for v in nxt)}, p={p2:.3f}")

# 5. Newton's third law row: magnetic forces between two moving charges (low-velocity Biot-Savart
#    field of a point charge, B = mu0/(4 pi) q v x R / |R|^3). Charge 1 at origin moving +x,
#    charge 2 at (0, d, 0) moving +y. Units: q = 1 C, v = 1 m/s, d = 1 m (only the directions matter).
def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def mag_force_on(q_t, v_t, r_t, q_s, v_s, r_s):
    R = tuple(rt - rs for rt, rs in zip(r_t, r_s))
    n = math.sqrt(sum(c * c for c in R))
    B = tuple(MU0 / (4 * math.pi) * q_s * c / n ** 3 for c in cross(v_s, R))
    return tuple(q_t * c for c in cross(v_t, B))


r1, v1 = (0.0, 0.0, 0.0), (1.0, 0.0, 0.0)
r2, v2 = (0.0, 1.0, 0.0), (0.0, 1.0, 0.0)
F_on_2 = mag_force_on(1.0, v2, r2, 1.0, v1, r1)
F_on_1 = mag_force_on(1.0, v1, r1, 1.0, v2, r2)
total = tuple(a + b for a, b in zip(F_on_1, F_on_2))
print(f"[DERIVED] magnetic force on 1 = {F_on_1}, on 2 = {F_on_2}; sum = {total} (nonzero -> not equal and opposite)")
