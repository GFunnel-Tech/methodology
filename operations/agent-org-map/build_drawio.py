#!/usr/bin/env python3
"""Build GFunnel-Agent-Operating-System.drawio — the agent org map as a multi-page draw.io file.

Pages: 1 Operating Model · 2 Org Chart (every agent) · 3 Reporting & Communication (by tier) ·
4 Work Suggestion Loop · 5 Team at Work (newsletter run) · 6 Instant Delivery (GFunnel).
Generated from agents_data.py so it never drifts from the workbook. DERIVATION, not canon.
"""
import os, sys
from xml.sax.saxutils import quoteattr, escape
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from agents_data import A, DEPTS, TEAMS

BY = {a[0]: a for a in A}
KIDS = defaultdict(list)
for a in A:
    KIDS[a[4]].append(a[0])
QUAD = {"STR":"yin","FIN":"yin","HRC":"yin","CON":"yin","MKT":"yang","SAL":"yang","OPS":"yang","TEC":"bridge","CS":"bridge","GOV":"gov","ORC":"orc"}
PAL = {"gov":("#E3E8F1","#2B3A55"),"orc":("#E6EBF1","#4D5F7A"),"yang":("#FBEEDF","#C26A12"),"yin":("#DDF0F3","#1F7A8C"),"bridge":("#EBF2DD","#5F7F22"),
       "owner":("#2B3A55","#2B3A55"),"gate":("#FFF2CC","#B8860B"),"note":("#FFFFFF","#9AA5B5"),"grey":("#F5F6F8","#9AA5B5")}
FONT = "fontFamily=Helvetica;"

class Page:
    def __init__(self, name, w=1700, h=1200):
        self.name, self.cells, self.n, self.w, self.h = name, [], 0, w, h
    def nid(self):
        self.n += 1; return f"c{self.n}"
    def v(self, label, x, y, w, h, style, parent="1", cid=None):
        cid = cid or self.nid()
        self.cells.append(f'<mxCell id="{cid}" value={quoteattr(label)} style={quoteattr(style)} vertex="1" parent="{parent}"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        return cid
    def e(self, s, t, label="", style="", parent="1"):
        cid = self.nid()
        st = "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#5B6678;fontSize=10;" + FONT + style
        self.cells.append(f'<mxCell id="{cid}" value={quoteattr(label)} style={quoteattr(st)} edge="1" parent="{parent}" source="{s}" target="{t}"><mxGeometry relative="1" as="geometry"/></mxCell>')
        return cid
    def model(self):
        return (f'<mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.w}" pageHeight="{self.h}" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
                + "".join(self.cells) + "</root></mxGraphModel>")

def box(kind, bold=False, dashed=False, font=11, rounded=1, white=False):
    f, s = PAL[kind]
    return (f"rounded={rounded};whiteSpace=wrap;html=1;fillColor={f};strokeColor={s};fontSize={font};{FONT}arcSize=8;"
            + ("fontStyle=1;" if bold else "") + ("dashed=1;" if dashed else "") + ("fontColor=#FFFFFF;" if white else "fontColor=#18202C;")
            + ("strokeWidth=2;" if bold else ""))
def kind(aid): return "owner" if aid == "G-00" else QUAD[BY[aid][3]]
def lab(aid, extra=""):
    a = BY[aid]
    return f"<b>{aid}</b> · {a[14]}<br>{escape(a[1])}" + (f"<br><i>{escape(extra)}</i>" if extra else "")
TITLE = "text;html=1;fontSize=20;fontStyle=1;" + FONT + "fontColor=#18202C;align=left;verticalAlign=top;"
SUB = "text;html=1;fontSize=11;" + FONT + "fontColor=#5B6678;align=left;verticalAlign=top;whiteSpace=wrap;"
FOOT = ("Derivation, not canon. Source: GFunnel Methodology (Omni Process) v5.1–v5.3, Cameron Garlick / GFunnel, "
        "github.com/GFunnel-Tech/methodology, CC BY 4.0. Adapted into an agent operating model; not endorsed by the author.")

def legend(p, x, y):
    p.v("<b>Legend</b>", x, y, 200, 20, "text;html=1;fontSize=11;" + FONT + "align=left;")
    items = [("owner","Owner (human)"),("gov","Governance"),("orc","Orchestration / Owner channel"),("yang","High-Yang hub (Mkt, Sales, Ops)"),
             ("yin","High-Yin hub (Strat, Fin, HR, Content)"),("bridge","Bridging hub (Tech, Client Success)"),("gate","Human Gate (Owner decides)")]
    for i, (k, t) in enumerate(items):
        p.v("", x, y + 26 + i * 24, 18, 16, box(k))
        p.v(t, x + 26, y + 22 + i * 24, 260, 24, "text;html=1;fontSize=10;" + FONT + "align=left;verticalAlign=middle;")
    p.v("Autonomy: A autonomous · H human-in-loop · L human-led · R human-reserved<br>Solid arrow = work / reporting flow · dashed = check, signal or dotted line",
        x, y + 26 + len(items) * 24, 420, 34, SUB)

pages = []

# ───────── Page 1 · Operating Model ─────────
p = Page("1 · Operating Model", 1720, 1180)
p.v("GFunnel Agent Operating System", 20, 10, 700, 30, TITLE)
p.v("Everything runs inside GFunnel and is delivered as close to instantly as possible. Every action is an event; the Owner hears it through one channel (O-23), tiered so only what needs the Owner interrupts. Every piece of work runs on one live board (O-25) and the Shepherd's Way.", 20, 42, 640, 40, SUB)
owner = p.v("<b>OWNER</b><br>G-00 · Founder / Operator<br><i>decides · names outcomes · supplies measurements</i>", 690, 20, 320, 76, box("owner", bold=True, font=12, white=True))
g07 = p.v(lab("G-07"), 1080, 30, 220, 56, box("gov", dashed=True, font=10))
p.e(g07, owner, "weekly time review", "dashed=1;")
liaison = p.v(lab("O-23", "instant push · one-tap decisions · digests on demand"), 690, 160, 320, 76, box("orc", bold=True))
p.e(owner, liaison, "requests · decisions", "exitX=0.3;exitY=1;entryX=0.3;entryY=0;")
p.e(liaison, owner, "push · inbox · digests", "exitX=0.7;exitY=0;entryX=0.7;entryY=1;")
gate = p.v("<b>Human Gates (21)</b><br>choice · naming · measurement · contracts · prices · hires · deploys", 1370, 100, 300, 130, "rhombus;whiteSpace=wrap;html=1;fontSize=10;" + FONT + f"fillColor={PAL['gate'][0]};strokeColor={PAL['gate'][1]};")
p.e(gate, liaison, "decision brief", "dashed=1;")
# governance column
gov = p.v("<b>Office of Governance</b> — checks every run", 20, 120, 240, 470, "swimlane;html=1;startSize=26;fontSize=11;" + FONT + f"fillColor={PAL['gov'][0]};strokeColor={PAL['gov'][1]};swimlaneFillColor=#FFFFFF;rounded=1;")
for i, gid in enumerate(["G-01","G-02","G-03","G-04","G-05","G-06"]):
    p.v(lab(gid), 12, 40 + i * 70, 216, 58, box("gov", font=10), parent=gov)
# routing row
intake = p.v(lab("O-01"), 300, 310, 220, 64, box("orc"))
router = p.v(lab("O-02", "chief of staff"), 560, 310, 220, 64, box("orc", bold=True))
board = p.v(lab("O-25", "one live board for all work"), 820, 310, 240, 64, box("orc", bold=True))
scout = p.v(lab("O-24", "proposes next work"), 1100, 310, 220, 64, box("orc", bold=True))
p.e(liaison, intake, "Owner requests", "exitX=0.1;exitY=1;entryX=0.5;entryY=0;")
p.e(intake, router, "named input")
p.e(router, board, "routed item")
p.e(scout, liaison, "proposals (instant, per signal)", "exitX=0.5;exitY=0;entryX=1;entryY=0.75;")
p.e(liaison, board, "approved work ↓ · status ↑", "exitX=0.8;exitY=1;entryX=0.5;entryY=0;")
# signals column
sig = p.v("<b>Project signals</b>", 1380, 270, 300, 380, "swimlane;html=1;startSize=26;fontSize=11;" + FONT + f"fillColor={PAL['grey'][0]};strokeColor={PAL['grey'][1]};swimlaneFillColor=#FFFFFF;rounded=1;")
for i, (sid, t) in enumerate([("O-04","lowest BEAS cell"),("O-08","stalled project / next gradient"),("SAL-12","lowest-conversion funnel step"),("CS-10","client's next Fibonacci step"),("STR-05","rising risk"),("O-20","recurring pattern"),("G-03","variable worth narrowing")]):
    p.v(f"<b>{sid}</b> — {t}", 12, 36 + i * 48, 276, 40, box(kind(sid), font=10), parent=sig)
p.e(sig, scout, "signals", "dashed=1;exitX=0;exitY=0.25;entryX=1;entryY=0.5;")
# execution container
ex = p.v("<b>Execution</b> — 9 hubs · 27 team leads · 79 task agents (full chart on page 2). Each team runs every item through the Shepherd's Way.", 300, 440, 1040, 300,
         "swimlane;html=1;startSize=30;fontSize=11;" + FONT + "fillColor=#F5F6F8;strokeColor=#5B6678;swimlaneFillColor=#FFFFFF;rounded=1;whiteSpace=wrap;")
hubs = ["STR","MKT","SAL","OPS","FIN","HRC","TEC","CS","CON"]
for i, h in enumerate(hubs):
    lead = h + "-00"; nteams = len([t for t in TEAMS.values() if t[1] == h])
    p.v(f"<b>{DEPTS[h][0]}</b><br>{nteams} team lead{'s' if nteams != 1 else ''}", 12 + i * 114, 42, 106, 62, box(QUAD[h], font=10), parent=ex)
steps = ["01 Direct","02 Guide","03 Gather","04 Organize","05 Create","06 Database","07 Repetition"]
sids = []
for i, s_ in enumerate(steps):
    sids.append(p.v(f"<b>{s_}</b>", 20 + i * 146, 150, 126, 44, box("grey", font=10), parent=ex))
for a_, b_ in zip(sids, sids[1:]):
    p.e(a_, b_, "", parent=ex)
p.e(sids[-1], sids[2], "next cycle / New Thought re-enters at Gather", "dashed=1;exitX=0.5;exitY=1;entryX=0.5;entryY=1;", parent=ex)
p.v("Team lead owns Direct, Guide, approval and closure · task agents do Gather → Create · O-15 does Database · O-03 blocks Create until Organize is done", 20, 240, 1000, 40, SUB, parent=ex)
p.e(gov, ex, "", "dashed=1;exitX=1;exitY=0.95;entryX=0;entryY=0.75;")
p.e(board, ex, "dispatch to team leads", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
p.e(ex, board, "live status · blockers", "dashed=1;exitX=0.62;exitY=0;entryX=0.9;entryY=1;")
# bottom row
db = p.v(lab("O-15", "instant recap"), 300, 790, 240, 64, box("orc"))
ctl = p.v(lab("O-03", "step gates"), 580, 790, 240, 64, box("orc"))
beas = p.v(lab("O-04", "monthly 45-point score"), 860, 790, 240, 64, box("orc"))
clients = p.v("<b>Clients &amp; market</b><br>deliverables · recaps · monthly results reports", 1140, 790, 240, 64, box("grey"))
p.e(ex, db, "finished work", "exitX=0.1;exitY=1;entryX=0.5;entryY=0;")
p.e(ctl, ex, "gates", "dashed=1;exitX=0.5;exitY=0;entryX=0.37;entryY=1;")
p.e(beas, ex, "scores hubs", "dashed=1;exitX=0.5;exitY=0;entryX=0.6;entryY=1;")
p.e(ex, clients, "delivery", "exitX=0.9;exitY=1;entryX=0.5;entryY=0;")
p.e(board, liaison, "", "dashed=1;exitX=0.3;exitY=0;entryX=0.62;entryY=1;")
p.e(beas, sig, "BEAS lowest cell", "dashed=1;exitX=0.5;exitY=1;entryX=0.5;entryY=1;")
legend(p, 20, 880)
p.v(FOOT, 20, 1130, 1200, 30, SUB)
pages.append(p)

# ───────── Page 2 · Org Chart (every agent) ─────────
ORDER = ["O-23","G-01","O-02","STR-00","MKT-00","SAL-00","OPS-00","FIN-00","HRC-00","TEC-00","CS-00","CON-00","G-07"]
direct = sorted(KIDS["G-00"], key=lambda k: ORDER.index(k) if k in ORDER else 99)
COLW, GAP, BH, VG, IND = 250, 26, 46, 10, 22
p = Page("2 · Org Chart", 20 + len(direct) * (COLW + GAP), 2200)
p.v(f"Org Chart — all {len(A)} agents", 20, 10, 700, 30, TITLE)
p.v("Solid lines are chain of command. Team leads (bold) are accountable for deliverables and manage the task agents below them. Dotted lines are listed in the workbook's Agent Roster.", 20, 42, 900, 30, SUB)
cx = (p.w - 320) // 2
ids = {"G-00": p.v(lab("G-00"), cx, 80, 320, 60, box("owner", bold=True, font=12, white=True))}
maxy = 0
def place(aid, x, y, w, depth):
    global maxy
    a = BY[aid]; mgr = bool(KIDS[aid])
    ids[aid] = p.v(lab(aid) + (f"<br><i>{len(KIDS[aid])} reports</i>" if mgr and depth > 0 else ""), x, y, w, BH + (12 if mgr and depth > 0 else 0), box(kind(aid), bold=mgr, font=10))
    y += BH + (12 if mgr and depth > 0 else 0) + VG
    for k in sorted(KIDS[aid], key=lambda k: 0 if KIDS[k] else 1):
        y = place(k, x + IND, y, w - IND, depth + 1)
        p.e(ids[aid], ids[k], "", "exitX=0.06;exitY=1;entryX=0;entryY=0.5;endArrow=none;")
    maxy = max(maxy, y); return y
for i, d in enumerate(direct):
    x = 20 + i * (COLW + GAP)
    place(d, x, 190, COLW, 0)
    p.e(ids["G-00"], ids[d], "", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;edgeStyle=elbowEdgeStyle;elbow=vertical;")
p.h = maxy + 80
p.v(FOOT, 20, maxy + 20, 1200, 30, SUB)
pages.append(p)

# ───────── Page 3 · Reporting & Communication ─────────
lanes = ["Task agents","Team leads (27)","Hub leads · offices · specialist agents","Owner Liaison (O-23)","OWNER","Clients"]
LW, X0 = 210, 170
R3 = [
 ("P0 · Interrupt (target ≤ 10 s)",[("Crisis alert (O-19) — stays until acknowledged",2,4),("Security incident (TEC-06)",2,4)]),
 ("P1 · Push now (target ≤ 60 s)",[("Human Gate → decision brief",2,3),("One-tap decision card in the Owner Inbox",3,4),("Owner request → receipt pushed back; item on the board",4,1),("Work proposal (O-24), the moment a signal changes",2,3),("Proposal card in the Owner Inbox: approve / defer / decline",3,4),("Blocked item that needs the Owner",1,3),("Closed Won deal / client's first result",2,4)]),
 ("P2 · Live feed (target ≤ 5 s)",[("Every item state change on the live board",0,1),("Team lead updates → board (O-25)",1,2),("Board, funnel and BEAS stream to the live dashboard",2,3),("Recap the moment a deliverable is finished (O-15)",2,5),("Zero-lag first response to every lead (SAL-01)",2,5)]),
 ("P3 · Rollups (on demand ≤ 60 s)",[("'Brief me now' digest — any time, plus daily",3,4),("Weekly rollup — on demand, plus weekly",3,4),("Monthly BEAS, financials, risk",2,3),("Client BEAS + results reports (CS-06)",2,5),("Quarterly plan, compliance, Immersion reviews",2,4)]),
]
rows = sum(len(r[1]) for r in R3)
p = Page("3 · Reporting & Communication", X0 + LW * len(lanes) + 40, 160 + rows * 46 + len(R3) * 30 + 140)
p.v("Reporting & Communication with the Owner", 20, 10, 800, 30, TITLE)
p.v("Event-driven inside GFunnel: each arrow fires the moment its event happens, from the sender's lane to the receiver's lane. Tiers decide what interrupts the Owner. Latency figures are targets until TEC-09 measures them.", 20, 42, 1100, 30, SUB)
for j, ln in enumerate(lanes):
    k_ = "owner" if ln == "OWNER" else ("orc" if "Liaison" in ln else "grey")
    p.v(f"<b>{ln}</b>", X0 + j * LW, 90, LW - 6, 40, box(k_, font=11, white=(ln == "OWNER")))
y = 140
for cad, items in R3:
    band_h = len(items) * 46 + 20
    p.v(f"<b>{cad}</b>", 20, y, 140, band_h, box("gate" if cad.startswith("P0") else ("orc" if cad.startswith("P1") else "grey"), font=11) + "verticalAlign=middle;")
    p.v("", X0, y, LW * len(lanes) - 6, band_h, "rounded=0;html=1;fillColor=none;strokeColor=#C9D1DC;dashed=1;")
    yy = y + 10
    for txt, a_, b_ in items:
        lo, hi = min(a_, b_), max(a_, b_)
        x1 = X0 + lo * LW + LW // 2 - 40; x2 = X0 + hi * LW + LW // 2 + 40
        direction = "east" if b_ > a_ else "west"
        p.v(escape(txt), x1, yy, x2 - x1, 38, f"shape=singleArrow;direction={direction};whiteSpace=wrap;html=1;arrowWidth=0.7;arrowSize=0.04;fontSize=10;{FONT}fillColor={PAL['orc'][0] if b_ in (3,4) else PAL['grey'][0]};strokeColor=#5B6678;")
        yy += 46
    y += band_h + 10
p.v(FOOT, 20, y + 20, 1200, 30, SUB)
pages.append(p)

# ───────── Page 4 · Work Suggestion Loop ─────────
p = Page("4 · Work Suggestion Loop", 1720, 1060)
p.v("Work Suggestion Loop — the team proposes work from project signals", 20, 10, 1000, 30, TITLE)
p.v("Agents never start unapproved work. They propose it the moment a signal changes, with an expected outcome and a falsifier; the Owner decides with one tap; afterwards the result is checked against the prediction and the gap feeds the next signal.", 20, 42, 1000, 30, SUB)
n_sig = p.v("<b>1 · Signal changes (events)</b><br>BEAS lowest cell (O-04) · stalls (O-08) · lowest funnel step (SAL-12) · clients' next step (CS-10) · risks (STR-05) · patterns (O-20) · open variables (G-03)", 60, 140, 300, 110, box("grey", font=10))
n_sc = p.v("<b>2 · O-24 Work Suggestion Agent</b><br>fires the moment a signal changes; writes the proposal card", 480, 140, 260, 80, box("orc", bold=True))
n_rk = p.v("<b>3 · O-T3 Intelligence &amp; Decision Lead</b><br>checks cards; ranks by dependency order; Four-Pillar check before any scale proposal", 860, 130, 300, 100, box("orc"))
n_li = p.v("<b>4 · O-23 Owner Liaison</b><br>pushes the card to the Owner Inbox (P1, instant)", 1160, 330, 260, 80, box("orc", bold=True))
n_ow = p.v("<b>5 · OWNER decides</b><br>one tap: approve · defer · decline", 1140, 500, 300, 120, "rhombus;whiteSpace=wrap;html=1;fontSize=11;" + FONT + f"fillColor={PAL['gate'][0]};strokeColor={PAL['gate'][1]};")
n_bd = p.v("<b>6 · O-25 Work Board</b><br>approval instantly becomes a board item, dispatched to its team lead", 860, 720, 300, 90, box("orc", bold=True))
n_tm = p.v("<b>7 · Team lead + team</b><br>runs the Shepherd's Way; daily status on the board", 480, 730, 280, 80, box("yang"))
n_cmp = p.v("<b>8 · O-16 Decision Support</b><br>actual vs expected outcome; did the falsifier fire?", 100, 600, 280, 80, box("orc"))
n_int = p.v("<b>9 · O-10 Capsule Integrator</b><br>integrates the gap; nothing is lost", 100, 400, 280, 80, box("orc"))
p.e(n_sig, n_sc); p.e(n_sc, n_rk); p.e(n_rk, n_li); p.e(n_li, n_ow)
p.e(n_ow, n_bd, "approve"); p.e(n_bd, n_tm); p.e(n_tm, n_cmp, "delivered"); p.e(n_cmp, n_int); p.e(n_int, n_sig, "next signal starts higher")
n_def = p.v("<b>Deferred</b><br>O-24 re-proposes it at a later scan", 1470, 470, 200, 60, box("grey", dashed=True, font=10))
n_dec = p.v("<b>Declined</b><br>reason logged; O-10 integrates it", 1470, 600, 200, 60, box("grey", dashed=True, font=10))
p.e(n_ow, n_def, "defer", "dashed=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
p.e(n_ow, n_dec, "decline", "dashed=1;exitX=0.75;exitY=0.75;entryX=0;entryY=0.5;")
card = ("<b>Work Proposal card</b><br><br>Project · Problem (which signal)<br>Proposed work<br>Owning team lead<br>Expected outcome (observable)<br>"
        "Falsifier: what would show it was wrong, and the threshold<br>Effort estimate (held as a range)<br>Dependency order / prerequisites<br>Open variables (named, not filled)<br>Human Gates it will need")
p.v(card, 470, 300, 380, 240, "rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=top;spacing=14;fontSize=11;" + FONT + "fillColor=#FFFFFF;strokeColor=#4D5F7A;strokeWidth=2;")
p.v("Canon anchors: Layer V step 5 (lowest cell first) · Layer I.E step 8 (anticipate the next gradient) · Layer VII step 6 (lowest-conversion step) · Client Onboarding step 9 (next Fibonacci step) · Decision-Making steps 7–10 · Layer I.G. The loop itself is a derivation.", 20, 880, 1100, 40, SUB)
p.v(FOOT, 20, 1000, 1200, 30, SUB)
pages.append(p)

# ───────── Page 5 · Team at Work — Editorial & Email ─────────
cols5 = ["Requested","01 Direct","02 Guide","03–04 Gather & Organize","05 Create","Review","06 Database","07 Repetition"]
lanes5 = ["G-00","O-23","O-25","CON-T1","CON-09","CON-06","CON-10","CON-11","CON-12","CON-13","CON-14","O-15"]
CW, RH, LX, TY = 165, 64, 230, 120
p = Page("5 · Team at Work — Newsletter", LX + CW * len(cols5) + 40, TY + 40 + RH * len(lanes5) + 160)
p.v("Team at Work — one newsletter issue through the Editorial & Email team", 20, 10, 1200, 30, TITLE)
p.v("Columns are live work-board states (the Shepherd's Way). Rows are agents. Numbered cards show the order; every move is an event on the live board. Speed comes from the standing newsletter blueprint, prepared in advance.", 20, 42, 1100, 30, SUB)
for j, c in enumerate(cols5):
    p.v(f"<b>{c}</b>", LX + j * CW, TY, CW - 6, 34, box("grey", font=10))
for i, aid in enumerate(lanes5):
    y_ = TY + 40 + i * RH
    p.v(lab(aid), 20, y_, LX - 30, RH - 8, box(kind(aid), bold=bool(KIDS[aid]) or aid == "G-00", font=9, white=(aid == "G-00")))
    p.v("", LX, y_, CW * len(cols5) - 6, RH - 8, "rounded=0;html=1;fillColor=none;strokeColor=#E1E6EE;")
def cell(n, aid, col, txt, k="note"):
    i = lanes5.index(aid)
    return p.v(f"<b>{n}</b> {escape(txt)}", LX + col * CW + 6, TY + 44 + i * RH, CW - 18, RH - 16, box(k, font=9))
s1 = cell(1, "O-25", 0, "Calendar slot opens: issue item on the board")
s2 = cell(2, "CON-T1", 1, "Set reader outcome + done-criterion")
s3 = cell(3, "CON-T1", 2, "Brief and assign the team")
s4 = cell(4, "CON-09", 3, "Plan issue; pull proof, University, research")
s5 = cell(5, "CON-06", 4, "Write feature section")
s6 = cell(6, "CON-10", 4, "Write emails, subject lines, CTAs")
s7 = cell(7, "CON-11", 5, "Subtractive edit; fact-check; read aloud")
s8 = cell(8, "CON-12", 5, "Brand voice + claims + attribution")
g_ = cell("G", "G-00", 5, "Only if a results claim needs approval", "gate")
s9 = cell(9, "CON-T1", 5, "Approve against done-criterion")
s10 = cell(10, "CON-13", 6, "Segment, test send, schedule in Lead Connector")
s11 = cell(11, "O-15", 6, "Document issue + send record")
s12 = cell(12, "CON-14", 7, "48 h / 7-day report; weakest step")
s13 = cell(13, "CON-T1", 7, "Retro; next issue starts higher")
r1 = cell("↑", "O-23", 7, "Results on the live feed; in the digest on demand", "orc")
p.e(s8, s9, "", "fontSize=9;exitX=0;exitY=0.5;entryX=0;entryY=0.75;")
for a_, b_ in [(s1,s2),(s2,s3),(s3,s4),(s4,s5),(s4,s6),(s5,s7),(s6,s7),(s7,s8),(s9,s10),(s10,s11),(s11,s12),(s12,s13)]:
    p.e(a_, b_, "", "fontSize=9;")
p.e(s8, g_, "claim gate (only if needed)", "dashed=1;exitX=1;exitY=0.3;entryX=1;entryY=0.5;")
p.e(g_, s9, "", "dashed=1;exitX=0;exitY=0.5;entryX=0;entryY=0.25;")
p.e(s13, r1, "", "dashed=1;")
p.e(s3, s1, "", "dashed=1;exitX=0.5;exitY=0;entryX=1;entryY=0.5;")
p.v("Writing Algorithm split: lead owns steps 1, 2, 9 · Newsletter Producer step 3 · Email Copywriter steps 4–6 · Editor steps 7–8 (v5.1 L3004–3023). The team layer is a derivation.", 20, TY + 50 + RH * len(lanes5), 1200, 30, SUB)
p.v(FOOT, 20, TY + 90 + RH * len(lanes5), 1200, 30, SUB)
pages.append(p)

# ───────── Page 6 · Instant Delivery Architecture ─────────
p = Page("6 · Instant Delivery (GFunnel)", 1760, 1120)
p.v("Instant Delivery inside GFunnel — how an event reaches the Owner, and a decision reaches the team", 20, 10, 1300, 30, TITLE)
p.v("Every agent action is an event. One bus, one router, four tiers. The Owner's tap is an event too, so decisions reach the board and the team the same way. Components marked 'verify' may already exist in GFunnel; anything missing gets built.", 20, 42, 1300, 30, SUB)
srcs = p.v("<b>Event sources</b>", 20, 110, 300, 600, "swimlane;html=1;startSize=26;fontSize=11;" + FONT + f"fillColor={PAL['grey'][0]};strokeColor={PAL['grey'][1]};swimlaneFillColor=#FFFFFF;rounded=1;")
for i_, (t_, k_) in enumerate([("Any agent — <b>gate.raised</b>","orc"),("O-24 — <b>proposal.created</b>","orc"),("Team leads + task agents — <b>item.state_changed / item.blocked</b>","yang"),("Team leads — <b>deliverable.completed</b>","yin"),("SAL-11 / CS-04 — <b>deal.won / result.first</b>","bridge"),("O-04, O-08, SAL-12, CS-10, STR-05, O-20 — <b>signal.changed</b>","orc"),("O-19 / TEC-06 — <b>crisis.confirmed / security.incident</b>","gate"),("O-23 — <b>owner.request.created</b>","orc")]):
    p.v(t_, 12, 36 + i_ * 68, 276, 58, box(k_, font=10), parent=srcs)
bus = p.v("<b>GFunnel Event Bus</b><br>typed events · stored in the Event Log<br><i>TEC-09 · n8n webhooks + Lead Connector triggers (verify)</i>", 380, 300, 250, 110, box("orc", bold=True))
router = p.v("<b>Notification Router</b><br>applies the Owner's tiers + noise rules<br>retries · fallback channel<br><i>TEC-09 + O-23 (verify)</i>", 690, 300, 250, 110, box("orc", bold=True))
p.e(srcs, bus, "events", "exitX=1;exitY=0.45;entryX=0;entryY=0.5;")
p.e(bus, router, "")
tiers = [("<b>P0 · Interrupt</b> ≤ 10 s<br>mobile push + alert that stays until acknowledged; second channel if unanswered","gate",120),
         ("<b>P1 · Push now</b> ≤ 60 s<br>mobile push + Owner Inbox card<br>one tap: approve · defer · decline","orc",250),
         ("<b>P2 · Live feed</b> ≤ 5 s<br>live dashboard + activity feed; no push","grey",380),
         ("<b>P3 · Rollup</b> ≤ 60 s on demand<br>'brief me now' digest, daily and weekly","grey",510)]
tids = []
for t_, k_, y_ in tiers:
    tids.append(p.v(t_, 1010, y_, 300, 100, box(k_, font=10, bold=(k_ != "grey"))))
for t_ in tids:
    p.e(router, t_, "", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
own = p.v("<b>OWNER</b><br>phone + GFunnel", 1400, 290, 220, 130, box("owner", bold=True, font=12, white=True))
for t_ in tids:
    p.e(t_, own, "", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;" + ("dashed=1;" if t_ in tids[2:] else ""))
tap = p.v("<b>Owner tap = event</b><br>gate.decided · proposal.decided · owner.request.created", 1400, 520, 220, 90, box("orc", font=10))
p.e(own, tap, "decides / asks", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
board = p.v("<b>O-25 Live Work Board</b><br>item created / unblocked at once<br><i>custom object or pipeline (verify)</i>", 690, 700, 250, 90, box("orc", bold=True))
team = p.v("<b>Team lead → task agents</b><br>dispatched instantly; Create runs on demand from the standing blueprint", 380, 700, 250, 90, box("yang", font=10))
p.e(tap, board, "via event bus", "exitX=0.5;exitY=1;entryX=1;entryY=0.5;")
p.e(board, team, "dispatch")
p.e(team, srcs, "every state change emits an event", "dashed=1;exitX=0;exitY=0.5;entryX=0.5;entryY=1;")
log = p.v("<b>Event Log (Database)</b><br>the bus stores every event — recaps, audits, digests<br><i>O-15 · TEC-09</i>", 380, 860, 250, 80, box("orc", font=10))
mon = p.v("<b>Latency Monitor</b><br>watches the router: event → device time per tier; alerts on breach<br><i>TEC-09 · TEC-08</i>", 690, 860, 250, 80, box("orc", font=10))
blue = p.v("<b>Standing blueprints</b><br>Gather + Organize done in advance per recurring deliverable, so speed never skips steps<br><i>CON-T3 + team leads</i>", 20, 860, 300, 80, box("yin", font=10))
p.e(blue, team, "", "dashed=1;exitX=0.5;exitY=0;entryX=0;entryY=0.75;")
p.v("Latency figures are design targets set from 'as close to instant as possible' — not measurements. Canon anchors: ACE 'zero lag' first response (v5.1 L1595); Communication step 5, density the receiver can hold; Shepherd's Way Step 05, speed comes from prior thoroughness; System Architecture steps 5 and 8. The architecture is a derivation.", 20, 980, 1300, 40, SUB)
p.v(FOOT, 20, 1050, 1200, 30, SUB)
pages.append(p)

out = os.path.join(HERE, "GFunnel-Agent-Operating-System.drawio")
with open(out, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net" type="device">')
    for i, pg in enumerate(pages):
        f.write(f'<diagram id="p{i+1}" name={quoteattr(pg.name)}>{pg.model()}</diagram>')
    f.write("</mxfile>")
if len(sys.argv) > 1 and sys.argv[1].startswith("--page"):
    print(pages[int(sys.argv[1][6:]) - 1].model())
else:
    print("wrote", out, [pg.name for pg in pages])
