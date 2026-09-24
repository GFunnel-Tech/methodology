#!/usr/bin/env python3
"""
Reality Audit, Phase 4 — v5.1 Appendix D, MATHEMATICAL CONSTANTS table.

Checks every numeric / structural value the canonical table states, using the
Python standard library only (audit/SCHEMA.md §2; framework/tests/ convention).
These objects are defined or proven, not measured: a pass means "the canonical
string matches the computed value", graded `derived` in the audit files.

Run:  python3 audit/constants/check_math_constants.py
Exit status 0 if every check passes.
"""
from decimal import Decimal, getcontext
import cmath

# ---- Canonical strings, copied from versions/v5.1/GFunnel-Methodology-v5.1.md, Appendix D ----
CANON_PI = "3.14159265358979"          # "3.14159265358979…"
CANON_PHI = "1.61803398874989"         # "1.61803398874989…"
CANON_E = "2.71828182845904"           # "2.71828182845904…"
CANON_SQRT2 = "1.41421356"             # "1.41421356…"
CANON_FIB = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
CANON_LUCAS = [2, 1, 3, 4, 7, 11, 18, 29, 47]
CANON_LIFE = {"survive": {2, 3}, "birth": {3}}   # "2 or 3 ... survives", "exactly 3 ... becomes alive"
CANON_SQRT2_GAP_YEARS = 3000           # "a foretaste of incompleteness, three thousand years early"

# ---- Dates used for the "three thousand years" check (fetched, see CONST-sqrt-2.md) ----
GODEL_YEAR = 1931                      # Monatshefte 38:173-198 (1931), doi:10.1007/BF01700692 (Crossref)
PYTHAGORAS_BIRTH_BC = 570              # MacTutor: born "about 570 BC", died "about 490 BC"
PYTHAGORAS_DEATH_BC = 490

# ---- Sunflower data (Swinton et al. 2016, doi:10.1098/rsos.160091, abstract via Crossref) ----
SUNFLOWER_PARASTICHIES = 768
SUNFLOWER_FIBONACCI = 565
SUNFLOWER_FIB_STRUCTURE = 67

DIGITS = 60
getcontext().prec = DIGITS + 10

results = []


def check(name, ok, detail):
    results.append((name, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def truncate(d, places):
    s = format(d, "f")
    whole, frac = s.split(".")
    return whole + "." + frac[:places]


def pi_machin():
    """pi = 16 arctan(1/5) - 4 arctan(1/239)."""
    def arctan_inv(x):
        x = Decimal(x)
        total, term, n, sign = Decimal(0), 1 / x, 1, 1
        x2 = x * x
        while term > Decimal(10) ** -(DIGITS + 5):
            total += sign * term / n
            term /= x2
            n += 2
            sign = -sign
        return total
    return 16 * arctan_inv(5) - 4 * arctan_inv(239)


def e_series():
    total, term, n = Decimal(1), Decimal(1), 1
    while term > Decimal(10) ** -(DIGITS + 5):
        term /= n
        total += term
        n += 1
    return total


def seq(a, b, n):
    out = [a, b]
    while len(out) < n:
        out.append(out[-1] + out[-2])
    return out


def life_step(cells, rule):
    counts = {}
    for (x, y) in cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx or dy:
                    counts[(x + dx, y + dy)] = counts.get((x + dx, y + dy), 0) + 1
    return {c for c, k in counts.items()
            if (c in cells and k in rule["survive"]) or (c not in cells and k in rule["birth"])}


def mandel_bounded(c, iters=1000):
    z = 0
    for _ in range(iters):
        z = z * z + c
        if abs(z) > 2:
            return False
    return True


# 1. pi
pi = pi_machin()
check("pi digits", truncate(pi, 14) == CANON_PI, f"computed {truncate(pi, 20)}…, canon {CANON_PI}…")

# 2. phi, and the defining ratio (a+b)/a = a/b
phi = (1 + Decimal(5).sqrt()) / 2
check("phi digits", truncate(phi, 14) == CANON_PHI, f"computed {truncate(phi, 20)}…, canon {CANON_PHI}…")
a, b = phi, Decimal(1)
check("phi defining ratio (a+b)/a == a/b", abs((a + b) / a - a / b) < Decimal(10) ** -DIGITS,
      f"|diff| = {abs((a + b) / a - a / b):.2E}")

# 3. e, and d/dx e^x = e^x (numerical derivative at x=1)
e = e_series()
check("e digits", truncate(e, 14) == CANON_E, f"computed {truncate(e, 20)}…, canon {CANON_E}…")


def exp_series(x):
    total, term, n = Decimal(1), Decimal(1), 1
    while abs(term) > Decimal(10) ** -(DIGITS + 5):
        term = term * x / n
        total += term
        n += 1
    return total


h = Decimal(10) ** -25
deriv = (exp_series(1 + h) - exp_series(1 - h)) / (2 * h)   # central difference, independent series
check("d/dx e^x at x=1 equals e", abs(deriv - e) < Decimal(10) ** -20, f"|diff| = {abs(deriv - e):.2E}")

# 4. i
check("i^2 == -1", (1j) ** 2 == -1, f"(1j)**2 = {(1j) ** 2}")
check("multiplication by i rotates by 90 degrees", abs(cmath.phase(1j) - float(pi) / 2) < 1e-15,
      f"arg(i) = {cmath.phase(1j)}")

# 5-7. infinity / 0 / 1 carry no numeric value to check (see audit files).

# 8. sqrt 2
s2 = Decimal(2).sqrt()
check("sqrt2 digits", truncate(s2, 8) == CANON_SQRT2, f"computed {truncate(s2, 20)}…, canon {CANON_SQRT2}…")
gap_lo, gap_hi = GODEL_YEAR + PYTHAGORAS_DEATH_BC - 1, GODEL_YEAR + PYTHAGORAS_BIRTH_BC - 1  # no year 0
check("'three thousand years' Pythagoreans->Godel", gap_lo <= CANON_SQRT2_GAP_YEARS <= gap_hi,
      f"Pythagoras lifetime to 1931 spans {gap_lo}-{gap_hi} years; canon says {CANON_SQRT2_GAP_YEARS}")

# 9. Fibonacci
fib = seq(1, 1, 40)
check("Fibonacci terms", fib[:10] == CANON_FIB, f"computed {fib[:10]}")
ratio_err = abs(Decimal(fib[-1]) / Decimal(fib[-2]) - phi)
check("F(n+1)/F(n) -> phi", ratio_err < Decimal("1e-15"), f"|F40/F39 - phi| = {ratio_err:.2E}")

# 10. Lucas
luc = seq(2, 1, 40)
check("Lucas terms", luc[:9] == CANON_LUCAS, f"computed {luc[:9]}")
check("L(n+1)/L(n) -> phi", abs(Decimal(luc[-1]) / Decimal(luc[-2]) - phi) < Decimal("1e-15"),
      f"|L40/L39 - phi| = {abs(Decimal(luc[-1]) / Decimal(luc[-2]) - phi):.2E}")
# Canon: "the recursion itself, not the starting point, produces the phi attractor". Test the exception:
psi = (1 - Decimal(5).sqrt()) / 2          # the other root of x^2 = x + 1
x = [Decimal(1), psi]
for _ in range(30):
    x.append(x[-1] + x[-2])
exc_ratio = x[-1] / x[-2]
check("seed (1, psi) does NOT approach phi (canon's 'not the starting point' has an exception)",
      abs(exc_ratio - psi) < Decimal("1e-6"),
      f"ratio after 30 steps = {exc_ratio:.12f} (psi = {psi:.12f}); also seed (0,0) gives no ratio")

# 11. Conway's Game of Life (B3/S23)
blinker = {(0, 0), (1, 0), (2, 0)}
check("Life: blinker has period 2", life_step(life_step(blinker, CANON_LIFE), CANON_LIFE) == blinker
      and life_step(blinker, CANON_LIFE) != blinker, "canon rules reproduce the standard period-2 oscillator")
block = {(0, 0), (1, 0), (0, 1), (1, 1)}
check("Life: block is a still life", life_step(block, CANON_LIFE) == block, "block unchanged")
glider = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
g = glider
for _ in range(4):
    g = life_step(g, CANON_LIFE)
check("Life: glider translates (1,1) every 4 generations", g == {(x + 1, y + 1) for (x, y) in glider},
      "standard glider reproduced")

# 12. Mandelbrot z_{n+1} = z_n^2 + c, z_0 = 0
inside = [0, -1, -2, 1j, 0.25]
outside = [1, 0.26, 2j, -2.1]
check("Mandelbrot membership of reference points",
      all(mandel_bounded(c) for c in inside) and not any(mandel_bounded(c) for c in outside),
      f"bounded: {inside}; escaping: {outside}")

# Supporting arithmetic for CONST-fibonacci-sequence (not a canonical string)
fib_share = (SUNFLOWER_FIBONACCI + SUNFLOWER_FIB_STRUCTURE) / SUNFLOWER_PARASTICHIES
print(f"[INFO] sunflower parastichy numbers Fibonacci or Fibonacci-structured: "
      f"{SUNFLOWER_FIBONACCI + SUNFLOWER_FIB_STRUCTURE}/{SUNFLOWER_PARASTICHIES} = {fib_share:.3f}; "
      f"non-Fibonacci: {SUNFLOWER_PARASTICHIES - SUNFLOWER_FIBONACCI - SUNFLOWER_FIB_STRUCTURE} "
      f"({1 - fib_share:.3f})")

failed = [n for n, ok in results if not ok]
print(f"\n{len(results) - len(failed)}/{len(results)} checks pass")
if failed:
    print("FAILED:", ", ".join(failed))
raise SystemExit(1 if failed else 0)
