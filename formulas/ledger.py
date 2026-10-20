#!/usr/bin/env python3
"""
ledger.py — the Gap Ledger: the Omni Gap Formula run as a living asset.

Status: DERIVATION, not canon. See formulas/LEDGER.md.

Each gap is one quantity science has not settled. Evidence arrives over time.
Each piece of evidence is a measurement or a theory prediction, with an
uncertainty and a source. Every `run` re-applies the formula to every gap, in
this order:

  DETECT     group the evidence by independent method (one channel per method)
  PROCESS    combine the channels by precision weighting, then test whether they
             are consistent with each other (chi-square)
  RESPOND    status, interval, tension in sigma, the channel whose removal
             restores consistency, and the precision the next measurement needs
             to decide the question
  TERMINATE  with no evidence, the range stays held open; it is never filled

The run then compares the new state with the last recorded state. Every
movement (narrowed, widened, status change) is appended to history.jsonl and
becomes a row in the generated REPORT.md. That is the Iteration Ledger, written
by the formula itself.

Predictions are sealed before the data. `seal` records the current interval of
a gap as a prediction for its next measurement. Any evidence dated after the
seal is scored against it, so the ledger keeps a running hit rate to set
against the 90% it claims.

Standard library only.

  python3 formulas/ledger.py run                     # recompute, log movements, write REPORT.md
  python3 formulas/ledger.py run --as-of 2019-12-31  # replay: only evidence known by that date
  python3 formulas/ledger.py add G-001 --value 70.4 --sigma 1.9 --method "TRGB (JWST)" \
        --source "Author et al. 2026" --url https://... --date 2026-10-19
  python3 formulas/ledger.py seal G-001              # freeze a prediction for the next measurement
  python3 formulas/ledger.py new G-006 "question" --quantity "..." --unit "..."
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import os
from statistics import NormalDist

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "ledger")
GAPS = os.path.join(DIR, "gaps.json")
HISTORY = os.path.join(DIR, "history.jsonl")
REPORT = os.path.join(DIR, "REPORT.md")

ALPHA = 0.10                  # stated miss rate of every interval
P_CONFLICT = 0.01             # channels are in conflict below this p-value
Z = NormalDist().inv_cdf(1 - ALPHA / 2)


# --------------------------------------------------------------------------- #
# statistics (no scipy)
# --------------------------------------------------------------------------- #

def _gammainc_upper_reg(a, x):
    """Q(a, x), regularized upper incomplete gamma (Numerical Recipes)."""
    if x <= 0:
        return 1.0
    if x < a + 1:
        ap, s, d = a, 1.0 / a, 1.0 / a
        for _ in range(500):
            ap += 1
            d *= x / ap
            s += d
            if abs(d) < abs(s) * 1e-14:
                break
        return 1.0 - s * math.exp(-x + a * math.log(x) - math.lgamma(a))
    b, c, d = x + 1 - a, 1e300, 1 / (x + 1 - a)
    h = d
    for i in range(1, 500):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        d = 1e-300 if abs(d) < 1e-300 else d
        c = b + an / c
        c = 1e-300 if abs(c) < 1e-300 else c
        d = 1 / d
        h *= d * c
        if abs(d * c - 1) < 1e-14:
            break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h


def chi2_sf(chi2, dof):
    return _gammainc_upper_reg(dof / 2, chi2 / 2) if dof > 0 else 1.0


def combine(points):
    """Inverse-variance combination. points: [(value, sigma)]."""
    w = [1 / s ** 2 for _, s in points]
    mu = sum(wi * v for wi, (v, _) in zip(w, points)) / sum(w)
    sig = math.sqrt(1 / sum(w))
    chi2 = sum(((v - mu) / s) ** 2 for v, s in points)
    return mu, sig, chi2


def p_to_sigma(p):
    return NormalDist().inv_cdf(1 - p / 2) if p > 0 else float("inf")


# --------------------------------------------------------------------------- #
# the formula, one gap
# --------------------------------------------------------------------------- #

def channels(gap, until=None):
    """DETECT: one channel per independent method. Repeat results from the same
    method are combined first: they share systematics, so they are one witness."""
    by = {}
    for e in gap.get("evidence", []):
        if until and e["date"] > until:
            continue
        by.setdefault(e["method"], []).append((e["value"], e["sigma"], e))
    out = []
    for m, pts in by.items():
        mu, sig, _ = combine([(v, s) for v, s, _ in pts])
        kinds = {e.get("kind", "measurement") for _, _, e in pts}
        out.append({"method": m, "value": mu, "sigma": sig, "n": len(pts),
                    "kind": "theory" if kinds == {"theory"} else "measurement"})
    return out


def evaluate(gap, until=None):
    ch = channels(gap, until)
    lo_b, hi_b = (gap.get("bounds") or [None, None])
    res = {"channels": ch, "n_channels": len(ch)}
    if not ch:
        res.update(status="held-open", interval=[lo_b, hi_b], value=None,
                   note="No evidence. The range is held open, not filled.")
        return res
    if len(ch) == 1:
        c = ch[0]
        res.update(status="live (single witness)", value=c["value"],
                   interval=[c["value"] - Z * c["sigma"], c["value"] + Z * c["sigma"]],
                   note="One independent method only: nothing can cross-check it.")
        return res
    pts = [(c["value"], c["sigma"]) for c in ch]
    mu, sig, chi2 = combine(pts)
    dof = len(ch) - 1
    p = chi2_sf(chi2, dof)
    # the most discrepant pair, in sigma
    pair = max(((a, b) for i, a in enumerate(ch) for b in ch[i + 1:]),
               key=lambda ab: abs(ab[0]["value"] - ab[1]["value"]) / math.hypot(ab[0]["sigma"], ab[1]["sigma"]))
    tension = abs(pair[0]["value"] - pair[1]["value"]) / math.hypot(pair[0]["sigma"], pair[1]["sigma"])
    res.update(combined=mu, combined_sigma=sig, chi2=chi2, dof=dof, p=p, tension=tension,
               pair=[pair[0]["method"], pair[1]["method"]])
    if p >= P_CONFLICT:
        res.update(status="narrowed (corroborated)", value=mu,
                   interval=[mu - Z * sig, mu + Z * sig],
                   note=f"{len(ch)} independent methods agree (p = {p:.2f}).")
        return res
    # conflict: honest range is the PDG-style scaled error; no point value
    scale = math.sqrt(chi2 / dof)
    res.update(status="conflict", value=None, scale_factor=scale,
               interval=[mu - Z * sig * scale, mu + Z * sig * scale],
               note=f"Independent methods disagree: {tension:.1f} sigma between "
                    f"{pair[0]['method']} and {pair[1]['method']} (p = {p:.1e}).")
    # which single channel, removed, restores consistency? that names the location of the work
    culprits = []
    for c in ch:
        rest = [x for x in ch if x is not c]
        if len(rest) < 2:
            continue
        m2, s2, x2 = combine([(x["value"], x["sigma"]) for x in rest])
        p2 = chi2_sf(x2, len(rest) - 1)
        if p2 >= P_CONFLICT:
            culprits.append({"method": c["method"], "p_without": p2, "value_without": m2, "sigma_without": s2})
    culprits.sort(key=lambda c: -c["p_without"])
    res["restores_consistency_if_removed"] = culprits
    # the decisive next measurement: precision that separates the two camps at 3 sigma
    a, b = pair
    gapw = abs(a["value"] - b["value"])
    res["next_measurement"] = (f"An independent method with sigma <= {gapw / 3 / math.sqrt(2):.3g} {gap.get('unit', '')} "
                               f"would separate {a['method']} from {b['method']} at 3 sigma.")
    return res


# --------------------------------------------------------------------------- #
# the living part: history, movements, sealed predictions
# --------------------------------------------------------------------------- #

def load():
    with open(GAPS) as f:
        return json.load(f)


def save(data):
    with open(GAPS, "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


def last_states():
    states = {}
    if os.path.exists(HISTORY):
        with open(HISTORY) as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    states[r["gap"]] = r
    return states


def width(iv):
    return None if iv[0] is None or iv[1] is None else iv[1] - iv[0]


def required_widening(pr, e):
    """How much the sealed interval would have had to widen to contain e."""
    lo, hi = pr["interval"]
    mid, half = (lo + hi) / 2, (hi - lo) / 2
    return abs(e["value"] - mid) / math.hypot(half, Z * e["sigma"])


def learned_factor(data):
    """The Capsule loop: every scored prediction, hit or miss, says how wide the
    ledger's intervals should have been. Split-conformal over those ratios gives
    the factor that would have made 90% of them hits. It is applied only once
    there are enough cases for the quantile to be valid; until then it is
    reported, not used."""
    ratios = sorted(pr["ratios"][k] for g in data["gaps"] for pr in g.get("predictions", [])
                    for k in pr.get("ratios", {}))
    n_min = math.ceil((1 - ALPHA) / ALPHA)
    if not ratios:
        return None, 0, False
    k = min(len(ratios) - 1, math.ceil((1 - ALPHA) * (len(ratios) + 1)) - 1)
    return max(1.0, ratios[k]), len(ratios), len(ratios) >= n_min


def score_predictions(gap, until=None):
    """Score every sealed prediction against evidence dated after the seal."""
    for pr in gap.get("predictions", []):
        later = [e for e in gap.get("evidence", []) if e["date"] > pr["sealed"] and e.get("kind") != "theory"
                 and (until is None or e["date"] <= until) and e["id"] not in pr.get("scored", {})]
        for e in later:
            lo, hi = pr["interval"]
            mid, half = (lo + hi) / 2, (hi - lo) / 2
            # allow for the new measurement's own error: |x - mid| <= sqrt(half^2 + (Z*sigma)^2)
            r = required_widening(pr, e)
            pr.setdefault("scored", {})[e["id"]] = "hit" if r <= 1 else "miss"
            pr.setdefault("ratios", {})[e["id"]] = round(r, 4)


def cmd_run(args):
    data = load()
    prev = last_states()
    today = args.as_of or dt.date.today().isoformat()
    moves = []
    with open(HISTORY, "a") as hist:
        for gap in data["gaps"]:
            score_predictions(gap, args.as_of)
            r = evaluate(gap, args.as_of)
            f, n, valid = learned_factor(data)
            if valid and r["value"] is not None and None not in r["interval"]:
                mid = r["value"]
                half = (r["interval"][1] - r["interval"][0]) / 2 * f
                r["interval_raw"] = r["interval"]
                r["interval"] = [mid - half, mid + half]
                r["note"] += f" Range widened x{f:.2f}, learned from {n} scored predictions."
            gap["state"] = r
            w = width(r["interval"])
            p = prev.get(gap["id"])
            n_ev = len([e for e in gap.get("evidence", []) if not args.as_of or e["date"] <= args.as_of])
            changed = (p is None or p["status"] != r["status"] or
                       (w is not None and p.get("width") is not None and abs(w - p["width"]) > 1e-12 * max(1, abs(w))) or
                       p.get("n_evidence") != n_ev)
            if changed:
                row = {"date": today, "gap": gap["id"], "status": r["status"], "interval": r["interval"],
                       "width": w, "n_evidence": n_ev,
                       "tension": r.get("tension"), "prev_status": p["status"] if p else None,
                       "prev_width": p.get("width") if p else None}
                hist.write(json.dumps(row) + "\n")
                moves.append(row)
    save(data)
    write_report(data)
    # memory: scored ledger ranges become records (formulas/memory.py)
    try:
        from memory import Memory
        mem = Memory()
        for gap in data["gaps"]:
            scored = [{"metric": gap["id"], "tag": "ledger-range", "hit": v == "hit", "ratio": pr.get("ratios", {}).get(k)}
                      for pr in gap.get("predictions", []) if not pr.get("backtest")
                      for k, v in pr.get("scored", {}).items()]
            if scored:
                mem.record("ledger", gap["id"], {"gap": gap["id"], "status": gap["state"]["status"]}, {"scored": scored})
    except Exception as e:
        print(f"(memory not updated: {e})")
    for m in moves:
        print(describe_move(m))
    if not moves:
        print("No movement: no gap changed since the last run.")


def describe_move(m):
    if m["prev_status"] is None:
        return f"{m['date']} {m['gap']}: opened as {m['status']}"
    s = f"{m['date']} {m['gap']}: {m['prev_status']} -> {m['status']}"
    if m["width"] and m["prev_width"]:
        ch = 1 - m["width"] / m["prev_width"]
        s += f", range {100 * ch:.0f}% narrower" if ch >= 0 else f", range widened {100 * -ch:.0f}% (the witnesses disagree)"
    return s


def cmd_add(args):
    data = load()
    gap = next(g for g in data["gaps"] if g["id"] == args.gap)
    eid = f"{args.gap}-E{len(gap.setdefault('evidence', [])) + 1:02d}"
    gap["evidence"].append({"id": eid, "value": args.value, "sigma": args.sigma, "method": args.method,
                            "kind": args.kind, "source": args.source, "url": args.url,
                            "date": args.date or dt.date.today().isoformat(), "grade": args.grade})
    save(data)
    print(f"added {eid}; run `ledger.py run` to apply the formula")


def cmd_seal(args):
    data = load()
    gap = next(g for g in data["gaps"] if g["id"] == args.gap)
    r = evaluate(gap, args.as_of)
    if None in r["interval"]:
        raise SystemExit("cannot seal: the gap has no finite interval yet (held open)")
    real_today = dt.date.today().isoformat()
    today = args.as_of or real_today
    body = json.dumps({"gap": gap["id"], "interval": r["interval"], "sealed": today}, sort_keys=True)
    gap.setdefault("predictions", []).append({
        "sealed": today, "interval": r["interval"], "status_at_seal": r["status"],
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
        # a seal dated in the past is a BACKTEST: the later evidence was already known
        "backtest": today < real_today})
    save(data)
    print(f"sealed {gap['id']} {r['interval']} on {today}; commit before any new evidence is added")


def cmd_new(args):
    data = load()
    data["gaps"].append({"id": args.gap, "question": args.question, "quantity": args.quantity,
                         "unit": args.unit, "kind": args.kind, "route": args.route,
                         "bounds": None, "evidence": [], "predictions": []})
    save(data)
    print(f"opened {args.gap}")


# --------------------------------------------------------------------------- #
# report
# --------------------------------------------------------------------------- #

def fmt(x, unit=""):
    if x is None:
        return "—"
    return f"{x:.6g}" + (f" {unit}" if unit else "")


def write_report(data):
    L = ["# Gap Ledger — Report", "",
         "> Generated by `python3 formulas/ledger.py run`. Do not edit by hand. **Derivation, not canon.**",
         "> Intervals are 90%. Evidence values carry their source and retrieval date in `gaps.json`.", ""]
    L += ["| Gap | Question | Status | Range (90%) | Tension | Witnesses |", "| --- | --- | --- | --- | --- | --- |"]
    for g in data["gaps"]:
        r = g["state"]
        iv = r["interval"]
        rng = "held open" if None in iv else f"{iv[0]:.5g} – {iv[1]:.5g} {g.get('unit', '')}"
        t = f"{r['tension']:.1f}σ" if r.get("tension") is not None else "—"
        L.append(f"| {g['id']} | {g['question']} | **{r['status']}** | {rng} | {t} | {r['n_channels']} |")
    for g in data["gaps"]:
        r = g["state"]
        L += ["", f"## {g['id']} · {g['question']}", "",
              f"*Quantity:* {g.get('quantity', '')} · *Route:* {g.get('route', '')}", "",
              f"**{r['status']}** — {r['note']}", ""]
        if r["channels"]:
            L += ["| Witness (independent method) | Kind | Value | σ |", "| --- | --- | --- | --- |"]
            for c in r["channels"]:
                L.append(f"| {c['method']} | {c['kind']} | {fmt(c['value'])} | {fmt(c['sigma'])} |")
            L.append("")
        if r.get("restores_consistency_if_removed"):
            L.append("**Where the gap is (the location of the work):** removing any one of these makes the rest agree —")
            for c in r["restores_consistency_if_removed"]:
                L.append(f"- *{c['method']}*: the rest then give {fmt(c['value_without'])} ± {fmt(c['sigma_without'])} (p = {c['p_without']:.2f})")
            L.append("")
        if r.get("next_measurement"):
            L += [f"**Decisive next measurement:** {r['next_measurement']}", ""]
        if g.get("narrowing_routes"):
            L += ["**What would narrow it:** " + "; ".join(g["narrowing_routes"]), ""]
        if g.get("held_open"):
            L += ["**Held open (not filled):** " + "; ".join(g["held_open"]), ""]
        for pr in g.get("predictions", []):
            sc = pr.get("scored", {})
            tag = "Backtest seal (later evidence was already known)" if pr.get("backtest") else "Sealed prediction"
            L.append(f"*{tag} {pr['sealed']}:* [{pr['interval'][0]:.5g}, {pr['interval'][1]:.5g}] "
                     f"— scored: {', '.join(f'{k} {v}' for k, v in sc.items()) or 'awaiting new evidence'}")
    # calibration of the ledger itself
    L += ["", "## Calibration of the ledger itself", ""]
    f, n, valid = learned_factor(data)
    if f is None:
        L.append("- Learned widening factor: no scored predictions yet.")
    else:
        L.append(f"- Learned widening factor: **x{f:.2f}** from {n} scored predictions — "
                 + ("applied to every range above." if valid else
                    f"**not yet applied** (needs {math.ceil((1 - ALPHA) / ALPHA)} for a valid 90% quantile). "
                    "Until then the ranges above are the raw combination and are likely too narrow."))
    for label, bt in (("Real sealed predictions", False), ("Backtests (not evidence of foresight)", True)):
        hits = [v for g in data["gaps"] for pr in g.get("predictions", []) if bool(pr.get("backtest")) == bt
                for v in pr.get("scored", {}).values()]
        if hits:
            rate = sum(v == "hit" for v in hits) / len(hits)
            L.append(f"- {label}: {len(hits)} scored, hit rate {100 * rate:.0f}% (stated 90%).")
        else:
            L.append(f"- {label}: none scored yet." + (" Predictive power stays **held open** until real ones are." if not bt else ""))
    # movements
    L += ["", "## Movements (the Iteration Ledger, written by the formula)", "",
          "| Date | Gap | Movement |", "| --- | --- | --- |"]
    if os.path.exists(HISTORY):
        with open(HISTORY) as f:
            for line in f:
                if line.strip():
                    m = json.loads(line)
                    L.append(f"| {m['date']} | {m['gap']} | {describe_move(m).split(': ', 1)[1]} |")
    L += ["", "```", "Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,",
          "https://github.com/GFunnel-Tech/methodology, CC BY 4.0.",
          "Adapted: derivation, not endorsed by the author.", "```", ""]
    with open(REPORT, "w") as f:
        f.write("\n".join(L))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("--as-of", help="use only evidence dated on or before this day (replay)")
    r.set_defaults(fn=cmd_run)
    a = sub.add_parser("add"); a.add_argument("gap"); a.add_argument("--value", type=float, required=True)
    a.add_argument("--sigma", type=float, required=True); a.add_argument("--method", required=True)
    a.add_argument("--kind", default="measurement", choices=["measurement", "theory"])
    a.add_argument("--source", required=True); a.add_argument("--url", required=True)
    a.add_argument("--date"); a.add_argument("--grade", default="measured-single"); a.set_defaults(fn=cmd_add)
    s = sub.add_parser("seal"); s.add_argument("gap"); s.add_argument("--as-of", help="backtest seal (labelled as such)")
    s.set_defaults(fn=cmd_seal)
    n = sub.add_parser("new"); n.add_argument("gap"); n.add_argument("question")
    n.add_argument("--quantity", default=""); n.add_argument("--unit", default="")
    n.add_argument("--kind", default="measurement"); n.add_argument("--route", default="")
    n.set_defaults(fn=cmd_new)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
