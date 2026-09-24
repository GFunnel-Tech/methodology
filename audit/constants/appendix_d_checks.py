#!/usr/bin/env python3
"""Reality Audit, Phase 4: stdlib checks for v5.1 Appendix D
(Information & Computation, Biological & Scaling, Economic/Network/Social,
Hermetic & Framework Invariants).

Status: derivation. Standard library only. Constants are declared at the top.
Retrieved 2026-09-24. Run:  python3 audit/constants/appendix_d_checks.py
Network access is needed only for sections 6 and 7 (Gutenberg text, Rupp data).
"""
import math
import re
import urllib.request
from collections import Counter

# --- CODATA 2018 exact SI values (https://physics.nist.gov/cgi-bin/cuu/Value?c / ?h / ?k) ---
C = 299_792_458.0          # m s^-1, exact
H = 6.626_070_15e-34       # J Hz^-1, exact
K_B = 1.380_649e-23        # J K^-1, exact

# --- Hinkle 2005 (PMID 15620362) mechanistic P/O ratios ---
PO_NADH, PO_SUCC = 2.5, 1.5        # "about 2.5 ... and 1.5"
PO_NADH_ALT, PO_SUCC_ALT = 2.3, 1.4  # H+/ATP = 10/3 alternative in same abstract
# --- Per-glucose reducing equivalents, counted from KEGG reactions (R01061 GAPDH x2,
#     R00209 PDH x2, TCA R00709/R08549/R00342 NADH x3 per turn x2, R02164 SDH x1 per turn x2,
#     substrate-level: R01512 PGK x2 + R00200 PK x2 - R00299 HK - R04779 PFK + R00405/R00432 x2)
NADH_CYTO, NADH_MITO, SUCC = 2, 2 + 6, 2
SUBSTRATE_ATP = 2 + 2 - 1 - 1 + 2

GUTENBERG_URL = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"
RUPP_URL = ("https://raw.githubusercontent.com/karlrupp/microprocessor-trend-data/"
            "master/50yrs/transistors.dat")


def s1_bremermann():
    v = C ** 2 / H
    print(f"[1] Bremermann c^2/h = {v:.4e} bit s^-1 kg^-1")


def s2_landauer():
    for t in (300.0, 293.15):
        e = K_B * t * math.log(2)
        print(f"[2] Landauer kT ln2 at {t} K = {e:.4e} J = {e / 1.602176634e-19 * 1e3:.2f} meV")


def s3_atp():
    def y(po_n, po_s, shuttle_po):
        return NADH_MITO * po_n + SUCC * po_s + NADH_CYTO * shuttle_po + SUBSTRATE_ATP
    print(f"[3] ATP/glucose, P/O 2.5/1.5, malate-aspartate shuttle: {y(PO_NADH, PO_SUCC, PO_NADH):.1f}")
    print(f"[3] ATP/glucose, P/O 2.5/1.5, glycerol-phosphate shuttle: {y(PO_NADH, PO_SUCC, PO_SUCC):.1f}")
    print(f"[3] ATP/glucose, P/O 2.3/1.4, malate-aspartate: {y(PO_NADH_ALT, PO_SUCC_ALT, PO_NADH_ALT):.1f}")
    print(f"[3] ATP/glucose, P/O 2.3/1.4, glycerol-phosphate: {y(PO_NADH_ALT, PO_SUCC_ALT, PO_SUCC_ALT):.1f}")


def s4_pareto_share():
    # Pareto(alpha) with alpha>1: top fraction p of population holds share p^(1-1/alpha).
    for a in (1.1, 1.161, 1.5, 2.0, 3.0):
        print(f"[4] Pareto alpha={a}: top 20% hold {0.2 ** (1 - 1 / a) * 100:.1f}%")
    # alpha that gives exactly 80/20: solve 0.2^(1-1/a)=0.8
    a = 1 / (1 - math.log(0.8) / math.log(0.2))
    print(f"[4] alpha giving exactly 80/20 = {a:.4f}")


def s5_lindy():
    # Pareto survival S(t)=(t0/t)^alpha: E[T - t | T > t] = t/(alpha-1) for alpha>1.
    for a in (1.5, 2.0, 3.0):
        print(f"[5] Lindy: alpha={a}: expected remaining life = {1 / (a - 1):.2f} x current age")


def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def ols(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs); sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    ss_res = sum((y - (my + b * (x - mx))) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys)
    return b, 1 - ss_res / ss_tot


def s6_zipf():
    t = fetch(GUTENBERG_URL)
    s = t.find("*** START"); e = t.find("*** END")
    words = re.findall(r"[a-z]+", t[s:e].lower())
    c = Counter(words); f = sorted(c.values(), reverse=True)
    n_tok, n_typ = len(words), len(f)
    # fit ranks 1..1000 (avoid the hapax tail)
    xs = [math.log(r) for r in range(1, 1001)]; ys = [math.log(f[r - 1]) for r in range(1, 1001)]
    b, r2 = ols(xs, ys)
    top = sum(f[: max(1, n_typ // 5)]) / n_tok
    print(f"[6] Moby-Dick tokens={n_tok} types={n_typ}")
    print(f"[6] Zipf OLS slope ranks 1-1000 = {b:.3f} (R^2={r2:.4f})")
    print(f"[6] share of tokens from top 20% of word types = {top * 100:.1f}%")
    print(f"[6] f(1)/f(10) = {f[0] / f[9]:.2f}, f(1)/f(100) = {f[0] / f[99]:.2f}")


def s7_moore():
    rows = []
    for line in fetch(RUPP_URL).splitlines():
        p = line.split()
        if len(p) >= 2:
            try:
                rows.append((float(p[0]), float(p[1])))
            except ValueError:
                pass
    print(f"[7] Rupp transistor-count rows={len(rows)}, years {min(r[0] for r in rows):.1f}-{max(r[0] for r in rows):.1f}")
    for lo, hi in ((1971, 2022), (1971, 1990), (1990, 2005), (2005, 2022), (2010, 2022)):
        sub = [(y, v) for y, v in rows if lo <= y < hi]
        b, r2 = ols([y for y, _ in sub], [math.log2(v) for _, v in sub])
        print(f"[7] {lo}-{hi}: n={len(sub)} doubling time = {1 / b:.2f} yr (R^2={r2:.3f})")


def s8_departments():
    # v5.1 Layer V "Nine GFunnel Departments" table, 3K column, as transcribed.
    k = ["3rd", "2nd→1st", "2nd→1st", "1st", "1st→2nd", "2nd", "2nd→1st", "1st→2nd", "2nd"]
    print(f"[8] 3K column distribution: {dict(Counter(k))}")


if __name__ == "__main__":
    s1_bremermann(); s2_landauer(); s3_atp(); s4_pareto_share(); s5_lindy()
    s6_zipf(); s7_moore(); s8_departments()
