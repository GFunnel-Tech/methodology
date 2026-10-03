#!/usr/bin/env python3
"""What did it cost to gain the knowledge the methodology contains — and how much did it produce?

Combines the sourced inputs in this directory:
  knowledge_map.json    248 items -> the research programs / studies their knowledge rests on
  facilities.json       costs of the large facilities (via compute_cost.HEADLINE)
  programs_extra.json   costs of 17 further programs
  unit_costs.json       cost per research paper, by field (see unit_costs.md)
  cpi_us.json, fx.json  inflation and exchange rates

Rules (declared; change and re-run):
  * Each program is counted ONCE, however many items rely on it.
  * Each cited primary study (paper) is priced at its field's cost-per-paper range
    (unit_costs.md, "Proposed per-field ranges", 2025 $). One paper = one study (k = 1):
    a declared convention — unit_costs.md holds k open.
  * Reference compilations (NIST, PDG) are counted at ONE YEAR of operating budget: a floor.
    The experiments they compile are only partly captured by the facility list.
  * Held-open programs (no usable cost) are excluded and listed.

Standard library only.  Usage:  python3 audit/cost/knowledge_value.py [--json]
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import compute_cost as cc  # noqa: E402  (HEADLINE, to_usd, to_base, BASE, fmt)

load = cc.load

# Deutsche Mark per euro, irrevocably fixed 1 Jan 1999.
# Source: ECB, https://www.ecb.europa.eu/euro/intro/html/index.en.html (retrieved 2026-09-27):
#   "1 | DEM 1.95583 (Deutsche Mark)"
DEM_PER_EUR = 1.95583

# Cost per paper, 2025 $, (low, high), from unit_costs.md "Proposed per-field ranges".
PER_PAPER = {
    "physics": (0.14e6, 0.18e6), "chemistry": (0.14e6, 0.18e6),
    "astronomy": (0.14e6, 0.83e6),                      # university lab .. flagship telescope
    "biochemistry": (0.20e6, 0.35e6), "cell-biology": (0.20e6, 0.35e6),
    "neuroscience": (0.20e6, 0.35e6), "genetics-evolution": (0.20e6, 0.35e6),
    "other": (0.20e6, 0.35e6),                          # physiology, agronomy, clinical
    "earth-science": (0.25e6, 0.34e6),
    "psychology": (0.09e6, 0.10e6), "social-science": (0.09e6, 0.10e6), "economics": (0.09e6, 0.10e6),
    "mathematics": (0.09e6, 0.12e6), "computer-science": (0.09e6, 0.12e6),
}

# Headline choices for programs_extra.json: (low components, high components),
# each component (figure_index, price_year, note). Price year = stated, else report year.
EXTRA = {
    "pdg":   ([(0, 2008, "one year, FY2008 budget")], [(1, 2009, "one year, FY2009 plan")]),
    "bicep-keck": ("sum", 2015, "NSF awards named in BK18 only — partial"),
    "eso-vlt": ([(0, 1998, "VLT/VLTI total to 2003, DEM 1998")], [(0, 1998, "same")]),
    "messenger": ([(0, 2004, "at launch")], [(1, 2015, "at end of mission")]),
    "alma":  ([(1, 2013, "NRAO construction")], [(0, 2013, "ESO/ALMA construction")]),
    "darpa-hafnium-isomer": ([(0, 2004, "FY04"), (1, 2005, "FY05")], [(0, 2004, "FY04"), (1, 2005, "FY05")]),
    "exa-cel-clinical-program": ("exa", None, "CRISPR 40% share 2021–23; high = /0.4 (derived total)"),
    "fermi": ([(0, 2008, "mission at launch")], [(0, 2008, "same")]),
    "nustar": ([(1, 2012, "lifecycle low")], [(0, 2012, "lifecycle high")]),
    "pew-global-religion": ("sum", 2018, "Templeton grants only"),
}
REFERENCE_FLOOR = {  # facilities.json ids counted at one year of budget
    "nist": ([(1, 2024, "FY2024 measurement-lab account (STRS)")], [(0, 2024, "FY2024 total NIST")]),
}


def usd(g, year):
    cur, amt = g["currency"], g["amount"]
    if cur == "DEM":                              # DEM -> EUR (fixed) -> USD at 1999 rate (first euro year)
        return amt / DEM_PER_EUR * cc.FX["EURUSD"][1999], 1999 if year < 1999 else year
    return cc.to_usd(amt, cur, year), year


def component_sum(figs, comps):
    total = 0.0
    for idx, year, _ in comps:
        v, y = usd(figs[idx], year)
        total += cc.to_base(v, y)
    return total


def program_costs():
    fac = {f["id"]: f for f in load("facilities.json")}
    ext = {f["id"]: f for f in load("programs_extra.json")}
    costs, notes = {}, {}
    for pid, spec in cc.HEADLINE.items():
        figs = fac[pid]["figures"]
        vals = [component_sum(figs, spec["low"]), component_sum(figs, spec["high"])]
        costs[pid] = (min(vals), max(vals))
        notes[pid] = fac[pid]["source_type"]
    if "jwst" in fac:                              # used by one mapped item
        g = fac["jwst"]["figures"][0]
        v = cc.to_base(g["amount"], 2021)
        costs["jwst"] = (v, v); notes["jwst"] = "price tag as of May 2021"
    for pid, (lo, hi) in REFERENCE_FLOOR.items():
        figs = fac[pid]["figures"]
        costs[pid] = (component_sum(figs, lo), component_sum(figs, hi)); notes[pid] = "ONE YEAR only (floor)"
    for pid, spec in EXTRA.items():
        figs = ext[pid]["figures"]
        if spec[0] == "sum":
            v = sum(cc.to_base(g["amount"], spec[1]) for g in figs if g["currency"] == "USD")
            costs[pid] = (v, v)
        elif spec[0] == "exa":
            share = sum(cc.to_base(g["amount"], g["price_year"]) for g in figs)
            costs[pid] = (share, share / 0.4)
        else:
            v = (component_sum(figs, spec[0]), component_sum(figs, spec[1]))
            costs[pid] = (min(v), max(v))   # readings differ in scope; after deflation either can be larger
        notes[pid] = spec[-1] if isinstance(spec[-1], str) else ""
    notes["pdg"] = "ONE YEAR only (floor)"
    return costs, notes


def main():
    kmap = load("knowledge_map.json")
    costs, notes = program_costs()
    used = sorted({p for k in kmap for p in (k.get("programs") or [])})
    counted = [p for p in used if p in costs]
    held = [p for p in used if p not in costs]

    prog_lo = sum(costs[p][0] for p in counted)
    prog_hi = sum(costs[p][1] for p in counted)
    iss_lo, iss_hi = costs.get("iss", (0, 0)) if "iss" in counted else (0, 0)

    st_lo = st_hi = 0.0
    by_field = {}
    for k in kmap:
        n, f = k.get("n_studies") or 0, k.get("field")
        if n and f in PER_PAPER:
            lo, hi = PER_PAPER[f]
            st_lo += n * lo; st_hi += n * hi
            a = by_field.setdefault(f, [0, 0.0, 0.0]); a[0] += n; a[1] += n * lo; a[2] += n * hi

    basis = {}
    for k in kmap:
        basis[k["knowledge_basis"]] = basis.get(k["knowledge_basis"], 0) + 1

    fmt = cc.fmt
    print(f"Knowledge the methodology CONTAINS — cost to gain it (constant {cc.BASE} US $)\n")
    print(f"Items: {len(kmap)}  by basis: {basis}\n")
    print("A. Programs and facilities (each counted once)")
    for p in sorted(counted, key=lambda p: -costs[p][1]):
        n_items = sum(1 for k in kmap if p in (k.get("programs") or []))
        lo, hi = costs[p]
        rng = fmt(lo) if abs(hi - lo) < 1e6 else f"{fmt(lo)} – {fmt(hi)}"
        print(f"  {p:28} {n_items:3} items  {rng:>22}  {notes.get(p, '')}")
    print(f"  {'subtotal':28}            {fmt(prog_lo) + ' – ' + fmt(prog_hi):>22}")
    print(f"  held open (no usable cost): {', '.join(held)}")
    print("\nB. Individual studies (cited papers x field cost per paper)")
    for f, (n, lo, hi) in sorted(by_field.items(), key=lambda x: -x[1][2]):
        print(f"  {f:28} {n:3} papers {fmt(lo) + ' – ' + fmt(hi):>22}")
    print(f"  {'subtotal':28}            {fmt(st_lo) + ' – ' + fmt(st_hi):>22}")
    tot_lo, tot_hi = prog_lo + st_lo, prog_hi + st_hi
    print(f"\nTOTAL knowledge contained           {fmt(tot_lo)} – {fmt(tot_hi)}")
    print(f"TOTAL excluding the ISS (one fact)  {fmt(tot_lo - iss_lo)} – {fmt(tot_hi - iss_hi)}")
    print("\nKnowledge the methodology PRODUCED (confirmed by a later measurement): $0 to date")
    print("  see README — v5.4 states zero novel predictions; open tests are listed there.")

    if "--json" in sys.argv:
        out = {"base_year": cc.BASE, "items": len(kmap), "by_basis": basis,
               "programs": {p: {"low": costs[p][0], "high": costs[p][1], "note": notes.get(p, "")} for p in counted},
               "programs_held_open": held,
               "studies_by_field": {f: {"papers": v[0], "low": v[1], "high": v[2]} for f, v in by_field.items()},
               "subtotal_programs": [prog_lo, prog_hi], "subtotal_studies": [st_lo, st_hi],
               "total": [tot_lo, tot_hi], "total_excluding_iss": [tot_lo - iss_lo, tot_hi - iss_hi],
               "produced_confirmed": 0}
        json.dump(out, open(os.path.join(HERE, "knowledge_value.json"), "w"), indent=2)
        print("\nwrote knowledge_value.json")


if __name__ == "__main__":
    main()
