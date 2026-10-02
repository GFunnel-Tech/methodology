#!/usr/bin/env python3
"""
Cell Atlas, membrane run 01 — Na+/K+ pump energy budget.

Checks the work the pump must do per cycle against the free energy one ATP
supplies, for the canonical 3 Na : 2 K stoichiometry and the 2 Na : 1 K
variant measured in brine shrimp. Standard library only.

Inputs are the values tabulated in Peluffo & Hernandez 2023,
doi:10.1007/s12551-023-01082-5 (mammalian cell, 37 C).
"""
import math

R = 8.314462618e-3      # kJ / (mol K), CODATA
F = 96.48533212         # kJ / (mol V), CODATA
T = 310.15              # K (37 C)
NA_IN, NA_OUT = 15.0, 140.0   # mM
K_IN, K_OUT = 120.0, 4.0      # mM
DG_ATP = 54.0           # kJ/mol available from ATP hydrolysis in the cell


def work(n_na, n_k, vm_volts):
    """Free energy (kJ/mol of cycles) to move n_na Na+ out and n_k K+ in.

    Each Na+ climbs its concentration gradient and, with the inside negative,
    the voltage too. Each K+ climbs its concentration gradient but the voltage
    helps it in. Net charge moved out per cycle is (n_na - n_k).
    """
    rt = R * T
    return (n_na * rt * math.log(NA_OUT / NA_IN)
            + n_k * rt * math.log(K_IN / K_OUT)
            - (n_na - n_k) * F * vm_volts)


def stall_voltage(n_na, n_k):
    """Membrane potential at which the cycle needs all of DG_ATP."""
    w0 = work(n_na, n_k, 0.0)
    net = n_na - n_k
    return None if net == 0 else -(DG_ATP - w0) / (net * F)


def main():
    print(f"RT = {R*T:.4f} kJ/mol;  dG_ATP = {DG_ATP} kJ/mol\n")
    print(f"{'stoich':>8} {'W(0 mV)':>9} {'W(-50 mV)':>10} {'W(-80 mV)':>10} {'eff(-80)':>9} {'stall Vm':>9}")
    for n_na, n_k in [(3, 2), (4, 3), (4, 2), (2, 1)]:
        w0, w50, w80 = (work(n_na, n_k, v) for v in (0.0, -0.050, -0.080))
        vs = stall_voltage(n_na, n_k)
        print(f"{n_na}Na:{n_k}K {w0:9.2f} {w50:10.2f} {w80:10.2f} {w80/DG_ATP:9.0%} {vs*1000:8.1f}mV")
    print("\nCheck against the source: 3:2 at 0 mV = 34.819, at -50 mV = 39.627 kJ/mol;")
    print("stall of 4:3 near -48.2 mV and 4:2 near -69.5 mV.")
    w = work(3, 2, 0.0)
    assert abs(w - 34.819) < 0.05, w
    assert abs(work(3, 2, -0.050) - 39.627) < 0.05
    assert abs(stall_voltage(4, 3) * 1000 + 48.2) < 0.5
    assert abs(stall_voltage(4, 2) * 1000 + 69.5) < 0.5
    print("All checks pass.")


if __name__ == "__main__":
    main()
