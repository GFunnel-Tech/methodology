#!/usr/bin/env python3
"""What did it cost to build the reality log this audit reads?

Reads the sourced data in this directory (facilities.json, rd_series.json, cpi_us.json,
fx.json — every figure there carries its URL and retrieval date) and computes totals in
constant US dollars of the latest full CPI year.

Standard library only. Every CHOICE this script makes (which figure is the headline for a
facility, which year a nominal figure is priced in) is declared in HEADLINE below with its
reason. Choices are conventions, not measurements; change them and re-run.

Usage:  python3 audit/cost/compute_cost.py            # prints the tables
        python3 audit/cost/compute_cost.py --json     # also writes results.json
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
load = lambda name: json.load(open(os.path.join(HERE, name), encoding="utf-8"))

CPI = {int(y): v for y, v in load("cpi_us.json")["annual"].items()}
FX = {k: {int(y): v for y, v in s.items()} for k, s in load("fx.json")["series"].items()}
BASE = max(CPI)                                   # latest full CPI year

# ---- Headline choices (convention, declared) ------------------------------------------
# Each item: facility id -> list of (low, high) components. A component is
#   (figure_index, price_year, note). price_year = the year whose dollars the figure is in:
#   the source's stated price year if it gives one; otherwise the completion / report year
#   of the figure (a convention: nominal multi-year totals inflated from their END year
#   understate the real cost, so those totals are LOWER bounds).
HEADLINE = {
    "wmap":   {"low": [(0, 1995, "1995 proposed budget — not a final cost")],
               "high": [(0, 1995, "same")]},
    "planck": {"low": [(0, 2009, "ESA total, launch year 2009")], "high": [(0, 2009, "same")]},
    "hubble": {"low": [(0, 2021, "NASA lifetime, 2021 $, excludes shuttle operations")],
               "high": [(0, 2021, "lifetime"), (2, 2004, "+ SM4 shuttle mission, high estimate"),
                        (4, 1999, "+ SM3A")]},
    "lhc":    {"low": [(0, 2008, "CERN materials cost, machine + CERN detector share + computing (primary)")],
               "high": [(4, 2012, "cost to Higgs discovery incl. operations and experiments (secondary)")]},
    "rhic":   {"low": [(0, 1999, "construction budget")],
               "high": [(0, 1999, "budget"), (1, 1999, "+ overrun"), (2, 1999, "+ overhead absorbed")]},
    "ligo":   {"low": [(0, 2001, "initial LIGO construction"), (2, 2015, "+ Advanced LIGO")],
               "high": [(1, 2001, "initial LIGO incl. R&D and ops to FY2001"), (2, 2015, "+ Advanced LIGO")]},
    "osiris-rex": {"low": [(0, 2016, "program excl. launch"), (1, 2016, "+ launch")],
                   "high": [(2, 2023, "lifetime, nominal")]},
    "hgp":    {"low": [(0, 1991, "US cost at completion, FY1991 $")], "high": [(0, 1991, "same")]},
    "super-kamiokande": {"low": [(0, 1991, "construction, JPY, 1991")],
                         "high": [(2, 1991, "total approved funding (Wikipedia)")]},
    "kamland": {"low": [(0, 2002, "Japan share"), (1, 2002, "+ US DOE share")],
                "high": [(0, 2002, "Japan share"), (1, 2002, "+ US DOE share")]},
    "desi":   {"low": [(0, 2020, "DOE construction")], "high": [(0, 2020, "DOE"), (1, 2020, "+ in-kind")]},
    "cassini": {"low": [(2, 2017, "total per Wikipedia breakdown")], "high": [(0, 2017, "NASA full life incl. ESA/ASI")]},
    "iss":    {"low": [(0, 2014, "US investment to 2014 (nominal over 21 years)")],
               "high": [(0, 2014, "same")]},
}
EXCLUDED = {
    "cobe": "held open — only a $30M approval cap was sourced, not an actual cost",
    "borexino": "held open — no cost found",
    "jwst": "not yet used by the audit (future Phase 9 re-audits)",
    "nist": "an annual budget, not a facility total — reported separately",
}


def to_usd(amount, currency, year):
    if currency == "USD":
        return amount
    key = {"EUR": "EURUSD", "CHF": "CHFUSD", "JPY": "JPYUSD"}[currency]
    return amount * FX[key][year]


def to_base(usd, year):
    return usd * CPI[BASE] / CPI[year]


def facilities():
    fac = {f["id"]: f for f in load("facilities.json")}
    rows, tot = [], {"low": 0.0, "high": 0.0}
    tot_ex_iss = {"low": 0.0, "high": 0.0}
    for fid, spec in HEADLINE.items():
        f = fac[fid]
        vals = {}
        for bound in ("low", "high"):
            v = 0.0
            for idx, year, _ in spec[bound]:
                g = f["figures"][idx]
                v += to_base(to_usd(g["amount"], g["currency"], year), year)
            vals[bound] = v
        # the two readings are ranges of scope; after deflation either can be larger
        vals = {"low": min(vals.values()), "high": max(vals.values())}
        for bound in ("low", "high"):
            tot[bound] += vals[bound]
            if fid != "iss":
                tot_ex_iss[bound] += vals[bound]
        rows.append((f["name"], f["audit_use"], vals["low"], vals["high"], f["source_type"]))
    return rows, tot, tot_ex_iss


def series_sum(values, first=None, last=None, deflate=True):
    s = 0.0
    years = []
    for y, v in values.items():
        y = int(y)
        if (first and y < first) or (last and y > last) or y not in CPI:
            continue
        s += to_base(v, y) if deflate else v
        years.append(y)
    return s, min(years), max(years)


def macro():
    r = load("rd_series.json")
    out = {}
    g = r["global_gerd"]["values"]
    out["global_gerd"] = series_sum(g)
    share = {int(y): v for y, v in r["basic_share"]["values"].items()}
    basic = {y: v * share[int(y)] for y, v in g.items() if int(y) in share}
    out["global_basic_proxy"] = series_sum(basic)
    out["us_federal_rd"] = series_sum(r["us_federal_rd"]["values"])
    out["nih"] = series_sum(r["nih_appropriations"]["values"])
    return out


def fmt(x):
    return f"${x / 1e12:,.2f} T" if x >= 1e12 else f"${x / 1e9:,.1f} B" if x >= 1e9 else f"${x / 1e6:,.0f} M"


if __name__ == "__main__":
    rows, tot, tot_ex = facilities()
    print(f"All amounts in constant {BASE} US dollars (CPI-U).\n")
    print("LEVEL 1 — facilities the audit read")
    for name, use, lo, hi, src in sorted(rows, key=lambda r: -r[3]):
        rng = fmt(lo) if abs(hi - lo) < 1e6 else f"{fmt(lo)} – {fmt(hi)}"
        print(f"  {name[:44]:44} {rng:>22}  ({src})")
    print(f"  {'TOTAL':44} {fmt(tot['low']) + ' – ' + fmt(tot['high']):>22}")
    print(f"  {'TOTAL excluding ISS':44} {fmt(tot_ex['low']) + ' – ' + fmt(tot_ex['high']):>22}")
    for k, why in EXCLUDED.items():
        print(f"  excluded: {k} — {why}")
    m = macro()
    print("\nLEVEL 2 — the research enterprise underneath (sums of annual spending)")
    labels = {
        "global_gerd": "World R&D (all R&D, PPP $)",
        "global_basic_proxy": "World basic research (US share as proxy)",
        "us_federal_rd": "US federal R&D outlays",
        "nih": "US NIH appropriations",
    }
    for k, (s, y0, y1) in m.items():
        print(f"  {labels[k]:44} {y0}–{y1}  {fmt(s):>12}")
    if "--json" in sys.argv:
        res = {"base_year": BASE,
               "level1": {"rows": [dict(name=r[0], audit_use=r[1], low=r[2], high=r[3], source_type=r[4]) for r in rows],
                          "total": tot, "total_excluding_iss": tot_ex, "excluded": EXCLUDED},
               "level2": {k: {"sum": s, "from": y0, "to": y1} for k, (s, y0, y1) in m.items()}}
        json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=2)
        print("\nwrote results.json")
