#!/usr/bin/env python3
"""
v5.4 section 14, test 5 — D1 Lamina Shield first engineering estimate.

v5.4 section 8 states: "rifle round ~3 kJ -> hundreds of tesla if field-only;
plasma is the cheaper route." This script checks that number and identifies
which criterion actually produces it. Standard library only.
"""
import math

MU0, K_B = 4 * math.pi * 1e-7, 1.380649e-23
SOLID_N = 1e29          # ~ number density of a solid, m^-3
PLASMA_WINDOW_P = 1e5   # Hershcovitch plasma window operates near 1 atm

ROUNDS = [  # label, density kg/m^3, velocity m/s
    ("5.56 NATO", 10000, 940),
    ("7.62 NATO", 10000, 840),
    ("12.7 mm AP", 7850, 900),
    ("APFSDS (tungsten)", 18000, 1600),
]


def b_for_pressure(p):
    """Field whose magnetic pressure B^2/(2 mu0) equals p."""
    return math.sqrt(2 * MU0 * p)


def main():
    print("=" * 72)
    print("A. The ENERGY-DENSITY criterion (what 'a 3 kJ round' invites) -- WRONG")
    print("=" * 72)
    print("   u * V = KE gives a field that merely STORES the round's energy.\n")
    print(f"   {'interaction volume':>20s} {'u (J/m^3)':>12s} {'B (T)':>9s}")
    for v, lbl in ((1.0, "1 m^3"), (1e-3, "1 L"), (1e-7, "0.1 cm^3")):
        u = 3000.0 / v
        print(f"   {lbl:>20s} {u:12.3e} {b_for_pressure(u):9.2f}")
    print("\n   This reaches 'hundreds of tesla' only at ~0.1 cm^3, and it is the wrong")
    print("   criterion anyway: storing 3 kJ nearby does not decelerate anything.")

    print("\n" + "=" * 72)
    print("B. The PRESSURE criterion (correct) -- P_shield >= P_dyn = (1/2) rho v^2")
    print("=" * 72)
    print(f"\n   {'projectile':>20s} {'P_dyn (Pa)':>12s} {'B required (T)':>15s}")
    for lbl, rho, v in ROUNDS:
        p = 0.5 * rho * v * v
        print(f"   {lbl:>20s} {p:12.3e} {b_for_pressure(p):15.1f}")
    print("\n   -> v5.4's 'hundreds of tesla' is CONFIRMED, via this criterion.")
    print("      Records: ~45 T continuous, ~100 T pulsed non-destructive, ~1200 T destructive.")
    print("      So a small-arms shield is at the edge of pulsed-magnet practice;")
    print("      a tungsten long rod (241 T) is beyond non-destructive practice.")

    print("\n" + "=" * 72)
    print("C. Why plasma is FORCED, not merely cheaper")
    print("=" * 72)
    print("   A neutral projectile has no charge and no current: B exerts no force on it.")
    print("   The field can only act on a medium that carries charge. So the momentum must")
    print("   be taken by plasma, and the field's job is to confine that plasma.\n")
    p = 0.5 * 10000 * 940 ** 2
    print(f"   Required stagnation pressure: {p:.3e} Pa")
    print(f"   {'T (K)':>10s} {'n required (m^-3)':>20s} {'% of solid density':>20s}")
    for t in (1e4, 1e5, 1e6, 1e7):
        n = p / (K_B * t)
        print(f"   {t:10.0e} {n:20.3e} {100 * n / SOLID_N:19.3f} %")
    print(f"\n   Plasma-window precedent runs at ~{PLASMA_WINDOW_P:.0e} Pa — a factor of"
          f" {p / PLASMA_WINDOW_P:.0f} below requirement.")
    print("   VERDICT: no physics prohibition; the binding constraint is confinement of a")
    print("   dense plasma at ~4 GPa. That is a materials-and-power problem, matching v5.4's")
    print("   own 'physics-permitted, energy-bound' status for D1.")


if __name__ == "__main__":
    main()
