#!/usr/bin/env python3
"""Reality Audit, Phase 4 — v5.1 Appendix D physical constants vs. measurement.

Compares every value canon states with the primary source, at canon's own stated
precision: a canon value passes if it equals the measured value rounded to the digits
canon quotes (|canon - measured| <= half a unit in canon's last digit, plus the
measured 1-sigma uncertainty).

Standard library only. Every reference value is declared below with its source.
Sources retrieved 2026-09-24:
  CODATA 2022  https://physics.nist.gov/cuu/Constants/Table/allascii.txt
  Planck 2018  https://arxiv.org/abs/1807.06209   (abstract: H0, Omega_m)
  SH0ES 2022   https://arxiv.org/abs/2112.04510   (abstract: H0, q0)
"""

from decimal import Decimal
import math

# ---- Canon (v5.1 Appendix D, "PHYSICAL CONSTANTS") — as written -----------------------
CANON = {
    "c":             "299792458",
    "G":             "6.674e-11",
    "hbar":          "1.0546e-34",
    "k_B":           "1.381e-23",
    "alpha_inv":     "137.036",      # canon: 1/137.036…
    "m_e":           "9.109e-31",
    "m_p":           "1.673e-27",
    "e":             "1.602e-19",
    "planck_length": "1.616e-35",
    "planck_time":   "5.391e-44",
    "mp_over_me":    "1836",         # canon: "Ratio m_p/m_e ≈ 1836"
}
CANON_LAMBDA_TEXT = "~1.1×10⁻µ² m⁻²"   # not a number as written (see CONST-cosmological-constant)
CANON_H0_RANGE = (67.0, 73.0)          # canon: "~67-73 km/s/Mpc"

# ---- CODATA 2022 (value, 1-sigma uncertainty; 0 = exact by SI definition) --------------
CODATA = {
    "c":             ("299792458", "0"),
    "G":             ("6.67430e-11", "0.00015e-11"),
    "hbar":          ("1.054571817e-34", "0"),        # exact (h exact); listed truncated
    "k_B":           ("1.380649e-23", "0"),
    "alpha_inv":     ("137.035999177", "0.000000021"),
    "m_e":           ("9.1093837139e-31", "0.0000000028e-31"),
    "m_p":           ("1.67262192595e-27", "0.00000000052e-27"),
    "e":             ("1.602176634e-19", "0"),
    "planck_length": ("1.616255e-35", "0.000018e-35"),
    "planck_time":   ("5.391247e-44", "0.000060e-44"),
    "mp_over_me":    ("1836.152673426", "0.000000032"),
}

# ---- Cosmology (Planck 2018 abstract; SH0ES 2022 abstract) -----------------------------
H0_PLANCK, H0_PLANCK_ERR = 67.4, 0.5       # km/s/Mpc, base-LCDM inferred
OMEGA_M, OMEGA_M_ERR = 0.315, 0.007        # Planck 2018
H0_SHOES, H0_SHOES_ERR = 73.04, 1.04       # km/s/Mpc, distance ladder
C_M_S = 299792458.0
AU_M = 149597870700.0                      # IAU 2012 exact
MPC_M = 1e6 * AU_M * 648000 / math.pi      # parsec = 648000/pi au (IAU 2015)


def half_ulp(s):
    """Half a unit in the last quoted digit of a canon string."""
    d = Decimal(s)
    return Decimal(1).scaleb(d.as_tuple().exponent) / 2


def check_values():
    ok_all = True
    print(f"{'quantity':15} {'canon':>12} {'measured (CODATA 2022)':>24}  verdict")
    for key, canon in CANON.items():
        val, err = (Decimal(x) for x in CODATA[key])
        tol = half_ulp(canon) + err
        diff = abs(Decimal(canon) - val)
        ok = diff <= tol
        ok_all &= ok
        print(f"{key:15} {canon:>12} {str(val):>24}  {'consistent' if ok else 'CONFLICT'}")
    return ok_all


def lambda_derived():
    """Lambda = 3 * Omega_L * H0^2 / c^2, flat base-LCDM (Omega_L = 1 - Omega_m)."""
    h0 = H0_PLANCK * 1000 / MPC_M                     # s^-1
    omega_l = 1 - OMEGA_M
    lam = 3 * omega_l * h0 ** 2 / C_M_S ** 2
    rel = math.hypot(OMEGA_M_ERR / omega_l, 2 * H0_PLANCK_ERR / H0_PLANCK)
    return lam, lam * rel


if __name__ == "__main__":
    ok = check_values()
    lam, lam_err = lambda_derived()
    print(f"\nLambda (derived, Planck 2018 base-LCDM): {lam:.3e} ± {lam_err:.1e} m^-2")
    print(f"Canon writes: {CANON_LAMBDA_TEXT!r} — exponent unreadable; "
          f"'~1.1×10⁻⁵² m⁻²' would be consistent: {abs(1.1e-52 - lam) <= 0.05e-52 + lam_err}")
    lo, hi = CANON_H0_RANGE
    for name, v, e in (("Planck 2018", H0_PLANCK, H0_PLANCK_ERR), ("SH0ES 2022", H0_SHOES, H0_SHOES_ERR)):
        inside = lo - e <= v <= hi + e
        print(f"H0 {name}: {v} ± {e} km/s/Mpc — within canon's ~{lo:g}-{hi:g}: {inside}")
    sigma = abs(H0_SHOES - H0_PLANCK) / math.hypot(H0_PLANCK_ERR, H0_SHOES_ERR)
    print(f"H0 tension (Planck vs SH0ES): {sigma:.1f} sigma")
    print("\nall stated values consistent" if ok else "\nCONFLICTS FOUND")
