#!/usr/bin/env python3
"""Build omni-gap-formula.drawio (+ an SVG preview of each page) from one layout.

Pages
  1  The Formula        DETECT → PROCESS (P·S·R·C, weights, Π_F) → RESPOND (tags) → TERMINATE/LEARN
  2  The Router         which mode, which tool, for which input (what CLAUDE.md says in prose)
  3  The Output Card    the anatomy of one tagged estimate, and what each tag permits
  4  The Living Asset   the Gap Ledger loop: evidence → run → movement → seal → score → widen

Generated from this file so the diagram never drifts from the code it describes.
DERIVATION, not canon. Standard library only.

  python3 formulas/diagrams/build_diagram.py
"""
import os
from xml.sax.saxutils import quoteattr, escape

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "fontFamily=Helvetica;"
PAL = {  # kind: (fill, stroke)
    "detect": ("#DDF0F3", "#1F7A8C"), "process": ("#FBEEDF", "#C26A12"), "respond": ("#EBF2DD", "#5F7F22"),
    "learn": ("#E3E8F1", "#2B3A55"), "tag": ("#FFF2CC", "#B8860B"), "stop": ("#F8DCDC", "#A33A3A"),
    "note": ("#FFFFFF", "#9AA5B5"), "grey": ("#F5F6F8", "#9AA5B5"), "dark": ("#2B3A55", "#2B3A55"),
}
FOOT = ("Derivation, not canon. Source: GFunnel Methodology (Omni Process) v5.1–v5.4, Cameron Garlick / GFunnel, "
        "github.com/GFunnel-Tech/methodology, CC BY 4.0. The formula is an adaptation; not endorsed by the author.")


class Page:
    def __init__(self, name, w=1600, h=1000):
        self.name, self.w, self.h = name, w, h
        self.boxes, self.edges, self.n = [], [], 0

    def nid(self):
        self.n += 1
        return f"c{self.n}"

    def v(self, label, x, y, w, h, kind="note", bold=False, font=11, dashed=False, white=False, align="center"):
        cid = self.nid()
        self.boxes.append(dict(id=cid, label=label, x=x, y=y, w=w, h=h, kind=kind, bold=bold, font=font,
                               dashed=dashed, white=white, align=align))
        return cid

    def text(self, label, x, y, w, h, font=11, bold=False, color="#18202C", align="left"):
        cid = self.nid()
        self.boxes.append(dict(id=cid, label=label, x=x, y=y, w=w, h=h, kind=None, bold=bold, font=font,
                               dashed=False, white=False, align=align, color=color))
        return cid

    def e(self, s, t, label="", dashed=False):
        self.edges.append(dict(id=self.nid(), s=s, t=t, label=label, dashed=dashed))

    # ---- draw.io
    def drawio(self):
        cells = []
        for b in self.boxes:
            if b["kind"] is None:
                st = (f"text;html=1;fontSize={b['font']};{FONT}fontColor={b.get('color', '#18202C')};align={b['align']};"
                      f"verticalAlign=top;whiteSpace=wrap;" + ("fontStyle=1;" if b["bold"] else ""))
            else:
                f, s = PAL[b["kind"]]
                st = (f"rounded=1;whiteSpace=wrap;html=1;fillColor={f};strokeColor={s};fontSize={b['font']};{FONT}arcSize=8;"
                      f"align={b['align']};" + ("fontStyle=1;strokeWidth=2;" if b["bold"] else "") + ("dashed=1;" if b["dashed"] else "")
                      + ("fontColor=#FFFFFF;" if b["white"] else "fontColor=#18202C;") + ("spacingLeft=6;" if b["align"] == "left" else ""))
            cells.append(f'<mxCell id="{b["id"]}" value={quoteattr(b["label"])} style={quoteattr(st)} vertex="1" parent="1">'
                         f'<mxGeometry x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" as="geometry"/></mxCell>')
        for e in self.edges:
            st = ("edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#5B6678;fontSize=10;"
                  + FONT + ("dashed=1;" if e["dashed"] else ""))
            cells.append(f'<mxCell id="{e["id"]}" value={quoteattr(e["label"])} style={quoteattr(st)} edge="1" parent="1" '
                         f'source="{e["s"]}" target="{e["t"]}"><mxGeometry relative="1" as="geometry"/></mxCell>')
        return (f'<diagram name={quoteattr(self.name)} id={quoteattr(self.name.replace(" ", "-"))}>'
                f'<mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
                f'fold="1" page="1" pageScale="1" pageWidth="{self.w}" pageHeight="{self.h}" math="0" shadow="0">'
                f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(cells) + "</root></mxGraphModel></diagram>")

    # ---- SVG preview (straight edges, centre to centre, clipped at box borders)
    def svg(self):
        by = {b["id"]: b for b in self.boxes}
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" '
               f'font-family="Helvetica, Arial, sans-serif">', f'<rect width="{self.w}" height="{self.h}" fill="#FFFFFF"/>',
               '<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
               '<path d="M0,0 L8,4 L0,8 z" fill="#5B6678"/></marker></defs>']
        for e in self.edges:
            a, b = by[e["s"]], by[e["t"]]
            ax, ay = a["x"] + a["w"] / 2, a["y"] + a["h"] / 2
            bx, by_ = b["x"] + b["w"] / 2, b["y"] + b["h"] / 2
            x1, y1 = _clip(ax, ay, bx, by_, a)
            x2, y2 = _clip(bx, by_, ax, ay, b)
            dash = ' stroke-dasharray="6,4"' if e["dashed"] else ""
            out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#5B6678" stroke-width="1.5" marker-end="url(#a)"{dash}/>')
            if e["label"]:
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                t = _plain(e["label"])
                out.append(f'<rect x="{mx - 3.2 * len(t):.0f}" y="{my - 9:.0f}" width="{6.4 * len(t):.0f}" height="16" fill="#FFFFFF" opacity="0.9"/>')
                out.append(f'<text x="{mx:.0f}" y="{my + 3:.0f}" font-size="10" text-anchor="middle" fill="#5B6678">{escape(t)}</text>')
        for b in self.boxes:
            if b["kind"] is not None:
                f, s = PAL[b["kind"]]
                dash = ' stroke-dasharray="6,4"' if b["dashed"] else ""
                sw = 2 if b["bold"] else 1
                out.append(f'<rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="8" fill="{f}" stroke="{s}" stroke-width="{sw}"{dash}/>')
            color = "#FFFFFF" if b["white"] else b.get("color", "#18202C")
            out.extend(_svg_text(b, color))
        out.append("</svg>")
        return "\n".join(out)


def _clip(cx, cy, tx, ty, b):
    """Point on b's border along the ray from its centre toward (tx, ty)."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (b["w"] / 2) / abs(dx) if dx else float("inf")
    sy = (b["h"] / 2) / abs(dy) if dy else float("inf")
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


def _plain(html):
    return (html.replace("<br>", " / ").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "")
            .replace("&nbsp;", " "))


def _svg_text(b, color):
    """Very small HTML-ish renderer: <br> splits lines, <b> bolds a whole line, wraps on width."""
    lines_raw = b["label"].split("<br>")
    size = b["font"]
    maxc = max(4, int(b["w"] / (size * 0.56)))
    lines = []
    for raw in lines_raw:
        bold = "<b>" in raw or b["bold"]
        txt = _plain(raw).strip()
        if not txt:
            lines.append(("", bold))
            continue
        words, cur = txt.split(" "), ""
        for w in words:
            if len(cur) + len(w) + 1 > maxc and cur:
                lines.append((cur, bold))
                cur = w
            else:
                cur = (cur + " " + w).strip()
        lines.append((cur, bold))
    lh = size * 1.3
    total = lh * len(lines)
    if b["kind"] is None:
        y0 = b["y"] + size
    else:
        y0 = b["y"] + b["h"] / 2 - total / 2 + size
    anchor = "middle" if b["align"] == "center" else "start"
    x = b["x"] + b["w"] / 2 if b["align"] == "center" else b["x"] + 8
    out = []
    for i, (t, bold) in enumerate(lines):
        fw = ' font-weight="bold"' if bold else ""
        out.append(f'<text x="{x:.0f}" y="{y0 + i * lh:.0f}" font-size="{size}" text-anchor="{anchor}" fill="{color}"{fw}>{escape(t)}</text>')
    return out


# --------------------------------------------------------------------------- pages

def page_formula():
    p = Page("1 The Formula", 1600, 980)
    p.text("<b>The Omni Gap Formula</b> — x* = Π_F [ Σ_k w_k · μ_k(x | E) ],  I = x* ± q₁₋α,  tag = FT(F, I, τ)", 30, 20, 1540, 30, font=18, bold=True)
    p.text("One run of DETECT → PROCESS → RESPOND on one empty cell. Every path is tagged; nothing leaves blank. Code: formulas/omni_gap.py", 30, 52, 1540, 20, color="#5B6678")

    # DETECT column
    d0 = p.v("<b>DETECT</b><br>the gap x and what surrounds it", 40, 110, 230, 60, "detect", bold=True, font=12)
    d1 = p.v("E — the measured values in the same record<br><i>only measured values; never another fill</i>", 40, 190, 230, 60, "detect")
    d2 = p.v("F — the feasible set<br>bounds + identities the record must obey<br>(revenue − cogs = gross)", 40, 270, 230, 70, "detect")
    d3 = p.v("τ — decision tolerance<br>the error size that would change a decision", 40, 360, 230, 60, "detect")
    d4 = p.v("Parallel system(s) + mapping<br>which variables correspond (optional)", 40, 440, 230, 60, "detect", dashed=True)
    for a, b in ((d0, d1), (d1, d2), (d2, d3), (d3, d4)):
        p.e(a, b)

    # PROCESS: channels
    p.text("<b>PROCESS</b> — four evidence channels, one layer each", 330, 110, 500, 24, font=13, bold=True)
    cP = p.v("<b>P · Capsule prior</b><br>what this variable looks like across every prior record<br><i>Layer I.G — all prior paths</i>", 330, 150, 250, 80, "process")
    cS = p.v("<b>S · Process structure</b><br>the variable's measured relation to the other values in this record (ridge)<br><i>Layer 0 / I.C</i>", 330, 250, 250, 80, "process")
    cR = p.v("<b>R · Analogue</b><br>the nearest comparable records in the same system (k-NN)<br><i>Layer I.G / II</i>", 330, 350, 250, 80, "process")
    cC = p.v("<b>C · Correspondence</b><br>the relation fitted in a PARALLEL system on its own standardized coordinates, applied here: the shape transfers, the scale does not<br><i>Layer II, Axiom 10</i>", 330, 450, 250, 100, "process", dashed=True)
    p.e(d1, cP); p.e(d1, cS); p.e(d1, cR); p.e(d4, cC)

    w = p.v("<b>w · weights</b><br>learned by hiding values that ARE known and measuring which channel recovers them (non-negative least squares)<br><i>Capsule loop — every failed path integrated</i>", 640, 250, 250, 110, "process", bold=True)
    for c in (cP, cS, cR, cC):
        p.e(c, w)
    pi = p.v("<b>Π_F · condition on F</b><br>Gaussian conditioning on the identities; when one value survives the cell is FORCED (exact)", 950, 250, 230, 110, "process", bold=True)
    p.e(w, pi, "x*")
    p.e(d2, pi)
    q = p.v("<b>q₁₋α · calibrated width</b><br>the (1−α) quantile of the errors on those hidden known values (split-conformal): the stated miss rate IS the measured miss rate", 640, 400, 250, 100, "process")
    p.e(w, q, "residuals")
    p.e(q, pi)

    # RESPOND
    p.text("<b>RESPOND</b> — a value for every open cell, with its tag", 1230, 110, 340, 24, font=13, bold=True)
    tags = [("forced-fill", "identities leave one value: exact", "respond"),
            ("estimate", "range within τ; act on it", "respond"),
            ("estimate/wide", "range wider than τ; act with care; next measurement named", "respond"),
            ("assumption/prior-only", "nothing beats the base rate; the value IS the base rate, tagged", "tag"),
            ("conflict", "the record contradicts itself — no value; measure this record", "stop")]
    tids = []
    for i, (t, d, k) in enumerate(tags):
        tids.append(p.v(f"<b>{t}</b><br>{d}", 1230, 150 + i * 78, 330, 64, k, align="left"))
    p.e(pi, tids[0]); p.e(pi, tids[1]); p.e(pi, tids[2]); p.e(pi, tids[3]); p.e(pi, tids[4])
    card = p.v("<b>Every output carries</b><br>value · 90% range · tag · falsifier (observation + threshold) · the one measurement that would narrow it most", 1230, 560, 330, 90, "learn", bold=True)
    p.e(tids[2], card, dashed=True)

    # TERMINATE / LEARN
    t1 = p.v("<b>TERMINATE</b> (audit correction F-066)<br>never emit a value without its tag; never use a fill as an input to another fill", 330, 640, 400, 80, "stop", bold=True)
    t2 = p.v("<b>LEARN · restart at a higher baseline</b> (MMA step 12)<br>every measurement later revealed joins the calibration set; sealed predictions are scored and the learned widening is applied once n ≥ 9", 760, 640, 440, 80, "learn", bold=True)
    p.e(card, t2)
    p.e(t2, w, "re-weight", dashed=True)
    p.e(t2, q, "re-calibrate", dashed=True)

    # measured box
    p.v("<b>Measured on real tables</b> (formulas/benchmark.py)<br>Auto-MPG error 0.426 vs best standard method 0.448 · penguins 0.561 vs 0.584 · P&L 0.234 vs 0.256<br>90% ranges held the truth 91–93% of the time · Correspondence: mammal brain mass across 3 orders of magnitude 1.04 → 0.60; sign-reversed control: weight 0, 'not supported'", 40, 760, 1140, 90, "grey", align="left")
    p.v("<b>What it does not do</b><br>produce a number from a canon layer (the audit found zero such cases) · beat the best possible inference from the same information · fill a boundary gap (t → 0) where no prior, structure, analogue or trend exists", 1230, 700, 330, 150, "note", align="left")
    p.text(FOOT, 30, 900, 1540, 40, font=9, color="#5B6678")
    return p


def page_router():
    p = Page("2 The Router", 1600, 1000)
    p.text("<b>When to run what</b> — the decision an AI makes before loading anything (CLAUDE.md §1, §3)", 30, 20, 1540, 30, font=18, bold=True)
    q0 = p.v("<b>What does the user want?</b>", 40, 110, 260, 60, "dark", bold=True, white=True, font=13)
    m1 = p.v("<b>Understand</b> a concept, layer, term", 380, 80, 260, 50, "detect")
    m2 = p.v("<b>Diagnose</b> why something is stuck or failing; run a named algorithm", 380, 160, 260, 70, "detect", bold=True)
    m3 = p.v("<b>Estimate</b> — a number not yet in the record: fill gaps, forecast, compare, narrow, calculate one system from another", 380, 270, 260, 90, "detect", bold=True)
    m4 = p.v("<b>Both</b>: diagnose, then put numbers on it", 380, 400, 260, 50, "detect")
    m5 = p.v("<b>Contribute / audit / integrate</b>", 380, 470, 260, 60, "detect")
    for m in (m1, m2, m3, m4, m5):
        p.e(q0, m)
    a1 = p.v("<b>Answer mode</b><br>load the one section (SECTIONS.md)<br>workflows/answer.md", 720, 75, 280, 60, "respond")
    a2 = p.v("<b>Full methodology</b><br>v5.1 by framework/algorithms.md → layer → algorithm, run literally, every step<br>workflows/run-algorithm.md (derive.md if none fits)", 720, 150, 280, 90, "process", bold=True)
    a3 = p.v("<b>Instruments only</b><br>Variable Principle · Forecasting Algorithm · Layer ◇ step 2 · Forcing Test outcomes · Estimate Protocol<br>workflows/estimate.md<br><i>do NOT load Layers I–VII content: 3–4× the time, no accuracy</i>", 720, 255, 280, 120, "process", bold=True)
    a4 = p.v("run-algorithm.md, then estimate.md for every number the diagnosis leaves open", 720, 400, 280, 50, "process")
    a5 = p.v("CONTRIBUTING.md · audit/ · docs/ai-integration.md<br>workflows/iterate.md · reality-audit.md · integrate.md", 720, 465, 280, 70, "respond")
    for m, a in ((m1, a1), (m2, a2), (m3, a3), (m4, a4), (m5, a5)):
        p.e(m, a)
    p.e(a4, a2, dashed=True); p.e(a4, a3, dashed=True)

    p.text("<b>Estimate mode → which tool, by the shape of the input</b> (all in formulas/, standard library)", 40, 580, 1000, 24, font=13, bold=True)
    tools = [("a table with empty cells", "omni_gap.py — OmniGap(cols, rows, identities, bounds, tolerance).fill()", "per cell: value · range · tag · falsifier · next measurement"),
             ("one quantity, several measurements that may disagree", "ledger.py — new / add / run / seal", "per gap: narrowed · conflict · held-open; the witness whose removal restores agreement; the precision a decisive measurement needs"),
             ("a situation and a request to predict its metrics", "forecast.py — new → fill every row → commit (the seal) → score", "two arms, every metric tagged; later: hit rate vs stated coverage, error per tag"),
             ("two systems that may correspond, one thin", "OmniGap(..., correspondences=[Correspondence(name, cols, rows, mapping)]) — pattern in correspondence_test.py", "estimates in the thin system from the rich one; per column: held / not supported here"),
             ("a question in conversation, no file", "the protocol by hand — estimate.md §3", "the same card, written out")]
    for i, (inp, tool, outp) in enumerate(tools):
        y = 615 + i * 62
        a = p.v(inp, 40, y, 280, 50, "detect", align="left")
        b = p.v(tool, 350, y, 560, 50, "process", align="left")
        c = p.v(outp, 940, y, 620, 50, "respond", align="left")
        p.e(a, b); p.e(b, c)
    p.v("<b>Rule on every output</b> (rule 5, amended 2026-10-20): never fill a variable silently; never refuse to fill one that has a prior, structure, analogue or trend. Tag: measured · forced · estimate · assumption · held-open · conflict. 'held-open' without a value only when all four are absent.", 1040, 75, 520, 110, "tag", align="left")
    p.v("<b>Diagnose mode</b> loads what the Estimate mode skips: Three Kingdoms, Hermetic principles, dynamic middle, gradient. They locate <i>why</i> a process is stuck. They do not produce numbers.", 1040, 205, 520, 80, "note", align="left")
    p.text(FOOT, 30, 945, 1540, 40, font=9, color="#5B6678")
    return p


def page_card():
    p = Page("3 The Output Card", 1600, 900)
    p.text("<b>The anatomy of one tagged estimate</b> — what every number the system emits looks like, and what each tag permits", 30, 20, 1540, 30, font=18, bold=True)
    card = p.v("<b>monthly_revenue_usd: 22 000 USD/month   [tag: estimate]</b><br><br>range     : 17 500 – 27 500  (90%)<br>method    : prior (base rate for firms of this size) · structure (clients × average contract) · analogue (3 comparable firms) · trend (two earlier readings)<br>falsifier : refuted if the measured value falls outside 17 500 – 27 500<br>next      : measure the client count — expected to shrink this range ~40%", 40, 80, 720, 190, "learn", align="left", font=12)
    parts = [("value", "the best number the evidence supports. Always present unless the tag is conflict (or held-open after the four-part test).", "respond"),
             ("tag", "how the value was made. One of six; see right.", "tag"),
             ("range + coverage", "calibrated where there is history (the stated miss rate is the measured miss rate); judged where there is not, and it says which.", "respond"),
             ("method", "which of the four channels fed it: prior · structure · analogue · trend (Forecasting Algorithm steps 3–6).", "process"),
             ("falsifier", "the observation and threshold that would prove it wrong (Layer ◇ step 2). Without it, it is a belief, not an estimate.", "stop"),
             ("next", "the one measurement that would narrow it most (the Anti-Operation's conjugate gap).", "learn")]
    for i, (k, d, kind) in enumerate(parts):
        p.v(f"<b>{k}</b><br>{d}", 40 + (i % 3) * 245, 300 + (i // 3) * 100, 230, 85, kind, align="left")

    p.text("<b>The six tags</b> and what each one permits", 820, 80, 700, 24, font=13, bold=True)
    tags = [("measured", "taken from a source, with uncertainty", "cite source and date", "respond"),
            ("forced", "follows by necessity from measured values (one candidate survives)", "state the identities used", "respond"),
            ("estimate", "calculated from stated evidence (prior · structure · analogue · trend), range calibrated where possible", "value + range + method + falsifier", "respond"),
            ("assumption", "a value from judgement alone. PERMITTED — an unstated assumption is worse. Scored separately so its reliability is learned", "value + range + falsifier + the word 'assumption'", "tag"),
            ("held-open", "NO value — allowed only when no prior, no structure, no analogue and no trend exists. 'I don't know' is not a reason; anything that has happened before has a prior", "the reason, and what would narrow it", "stop"),
            ("conflict", "the evidence disagrees with itself beyond its stated errors", "the witnesses, and which one restores agreement if removed", "stop")]
    for i, (t, m, must, kind) in enumerate(tags):
        y = 115 + i * 92
        p.v(f"<b>{t}</b>", 820, y, 130, 78, kind, bold=True, font=12)
        p.v(m, 960, y, 360, 78, "note", align="left")
        p.v(f"<i>must carry:</i> {must}", 1330, y, 230, 78, "grey", align="left", font=10)
    p.v("<b>Before 2026-10-20</b> the protocol had three statuses (measured · derived · held open) and gave the AI no permitted form for a calculated estimate. Rule 5 read as 'refuse'; a user's forecast test showed the cost (missed numbers, 3–4× slower). The Estimate Protocol (substrate/2026-10-20-estimate-protocol.md) added the tags and the four-part test.", 40, 520, 720, 110, "note", align="left")
    p.v("<b>The four-part test</b> for omitting a value: 1 no prior · 2 no structure · 3 no analogue · 4 no trend. All four absent → held-open. Any one present → a value can be calculated and must be. The Big Bang's first moment passes. Next quarter's revenue does not.", 40, 650, 720, 100, "tag", align="left")
    p.text(FOOT, 30, 850, 1540, 40, font=9, color="#5B6678")
    return p


def page_ledger():
    p = Page("4 The Living Asset", 1600, 820)
    p.text("<b>The Gap Ledger</b> — the formula run continuously on open questions (formulas/ledger.py, LEDGER.md)", 30, 20, 1540, 30, font=18, bold=True)
    steps = [("<b>add evidence</b><br>value · σ · independent method · source URL · publication date", "detect"),
             ("<b>run</b><br>group by independent method (one witness each) · combine by precision · χ² consistency test", "process"),
             ("<b>status per gap</b><br>held-open (no evidence) · live (single witness) · narrowed (corroborated) · conflict", "respond"),
             ("<b>on conflict</b><br>tension in σ · which witness, removed, restores agreement · the precision a decisive measurement needs", "stop"),
             ("<b>movement logged</b><br>history.jsonl → REPORT.md: the Iteration Ledger written by the formula", "learn")]
    ids = []
    for i, (t, k) in enumerate(steps):
        ids.append(p.v(t, 40 + i * 310, 90, 280, 90, k, bold=(k != "note")))
    for a, b in zip(ids, ids[1:]):
        p.e(a, b)
    s1 = p.v("<b>seal</b><br>freeze the current range as a prediction (date + hash); commit before adding evidence", 350, 260, 280, 80, "tag", bold=True)
    s2 = p.v("<b>score</b><br>later measurements (publication date after the seal; never theory) score hit / miss", 660, 260, 280, 80, "tag", bold=True)
    s3 = p.v("<b>learn</b><br>every scored case says how wide the range should have been; the widening factor is applied once n ≥ 9", 970, 260, 280, 80, "learn", bold=True)
    p.e(ids[2], s1); p.e(s1, s2); p.e(s2, s3); p.e(s3, ids[1], "re-calibrate", dashed=True)
    p.v("<b>Seeded gaps (verified against the primary papers)</b><br>G-001 Hubble constant — conflict 4.9σ; removing either the CMB value or the Cepheid ladder restores agreement<br>G-002 neutron lifetime — conflict 4.4σ, beam vs bottle<br>G-003 primordial lithium-7 — conflict 4.0σ, theory vs halo stars<br>G-004 W boson mass — conflict 7.2σ; removing CDF alone restores agreement (p = 0.65)<br>G-005 the Big Bang's first moment — held-open by the four-part test (v5.4 Gap 1, proven-open)", 40, 400, 760, 150, "grey", align="left")
    p.v("<b>What the replay measured</b><br>Backtest seals at past dates held only 17% of later results against a stated 90%: published uncertainties at these frontiers understate real error by ~3.3× so far (6 cases). Real seals placed 2026-10-19; predictive power stays held open until they are scored.", 830, 400, 730, 150, "note", align="left")
    p.v("<b>Boundary gaps</b> (no prior, no structure, no analogue, no trend) are narrowed only from their measurable side. The ledger never fills them. That is the one place 'held-open' without a value is the correct output.", 40, 580, 760, 80, "tag", align="left")
    p.v("<b>Keeping it alive</b>: ledger.py add … → run → seal → commit. Evidence date = publication date. Theory never scores a seal. One witness = one independent method.", 830, 580, 730, 80, "learn", align="left")
    p.text(FOOT, 30, 760, 1540, 40, font=9, color="#5B6678")
    return p


def main():
    pages = [page_formula(), page_router(), page_card(), page_ledger()]
    xml = ('<?xml version="1.0" encoding="UTF-8"?><mxfile host="app.diagrams.net" type="device">'
           + "".join(pg.drawio() for pg in pages) + "</mxfile>")
    with open(os.path.join(HERE, "omni-gap-formula.drawio"), "w") as f:
        f.write(xml)
    for i, pg in enumerate(pages, 1):
        with open(os.path.join(HERE, f"page-{i}.svg"), "w") as f:
            f.write(pg.svg())
    print(f"wrote omni-gap-formula.drawio ({len(pages)} pages) + page-1..{len(pages)}.svg")


if __name__ == "__main__":
    main()
