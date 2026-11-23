# Workflow — The Acceptance Gate (the cell filter before transcription)

Use **before anything new is written into the methodology as its own**: a filled gap, a new result, a prediction, a correction, a new layer or construct. Use it on your own output and on anyone else's. It is the last step of every other workflow that produces a claim (`run-algorithm.md`, `derive.md`, `estimate.md`, `iterate.md`).

> **Status:** operating protocol, adopted on the author's instruction 2026-11-23 ([`substrate/2026-11-23-acceptance-gate.md`](../../../substrate/2026-11-23-acceptance-gate.md)). It is not canon. It implements v5.3's Container (⊙) — *classify → generate → converge-on-the-unforceable*, with the Perfection Criterion (zero hidden gaps) — as a filter a person or an AI can run.

## The rule

> **The whole methodology has to prove a fill before it is accepted. Nothing enters as a random layer.**

A cell does not transcribe what it has not filtered. Replication reaches about one error in 10⁹–10¹⁰ bases only because base selection, proofreading and mismatch repair are **separate mechanisms** in series (audit finding F-067). The gate copies that design.

## The stages (run in order; a fill stops at the first stage it fails)

| # | Cell stage | Gate stage | Pass condition | If it fails |
| --- | --- | --- | --- | --- |
| 1 | **Membrane** | Intake | Only **measurements** and **canon** enter. Outside theories are stripped to their measured quantities, uncertainty and source (reality filter items 4–5). | Strip the narrative; keep the number |
| 2 | **Receptor** | Placement | The fill binds to a **Kingdom**, a **layer** and a **domain**, named explicitly | Unplaceable: hold as a note, do not transcribe |
| 3 | **Self / non-self** | Origin | The fill is **derived from canon** (self). Anything imported — a formula, a constant, a rule from outside — is **non-self** and is labelled so | **Quarantine:** keep it, publish it if wanted, label it *borrowed*; it does not enter the methodology |
| 4 | **Checkpoint (G1/S)** | Derivation | The **Master Meta-Algorithm**, all 12 steps run literally (v5.1), including the Three Kingdoms (step 2) and the dynamic middle (step 5); then the **Forcing Test** A → B → C → D with each step shown (v5.3 §1) | Stop at the failed step; the blocker is the work |
| 5 | **Proofreading** | Falsifier | A falsifier is stated **and run** where it can be (a script, a measurement, a prediction sealed under `audit/prediction/PROTOCOL.md`) | Live hypothesis at most |
| 6 | **Mismatch repair** | Consistency | No conflict with any entry in `framework/registers.md`, the gap register or `formulas/README.md` §10; **Correspondence** checked one scale up and one scale down | Log the conflict; resolve before transcribing |
| 7 | **Folding QC** | Rework or recycle | Half-derived fills are held and reworked. Failed fills are logged as **forced-no** with the reason, so the parts are reusable (Layer I.G: nothing is lost) | Recycle into the ledger |
| 8 | **Transcription** | Entry | Only now does the fill enter a new version, declared by the author. Until then it lives in `substrate/`, `framework/tests/` or `audit/` with its gate result | — |

## Independence (the rule the cell enforces and AI runs tend to break)

Filters multiply only if they are **independent** (PRED-004: correlated stages fail together). One reasoner running every stage is one filter counted eight times. A fill is accepted only after it has passed **at least three different kinds** of filter:

1. **Reality** — a measurement or a script that can disagree with the claim.
2. **A different reasoner** — the author, another person, or an independent review that did not produce the fill.
3. **The canon's own consistency** — stage 6 run against the registers.

An AI may run stages 1–7 and report the result. It may not mark a fill *accepted* on its own.

## Report format

```
Gate run: <fill, one line>                       date: <YYYY-MM-DD>
1 Intake        pass | stripped: <what>
2 Placement     <Kingdom> · <layer> · <domain>
3 Origin        self | non-self: <what was imported, from whom>
4 Derivation    Master Meta steps 1–12: <stopped at #, or complete> · Forcing Test A/B/C/D: <each>
5 Falsifier     <stated> · run: <script / measurement / sealed PRED-###, or not yet>
6 Consistency   conflicts: <none | register row / §10 row> · Correspondence up/down: <held / not>
7 Disposition   accepted-pending-author | held for rework | quarantined (borrowed) | recycled (forced-no)
Independent filters passed: <reality / other reasoner / canon consistency>
```

## Worked example (2026-11-23): the neutrino-mass prediction

| Component | Stage reached | Disposition |
| --- | --- | --- |
| Masses from the two measured oscillation gaps | 1 (measurement) | passes intake |
| The Koide/Brannen form | **3: non-self** (imported; the trefoil reading was added after the fit; v5.4 §6 Test B unmet) | **quarantined** |
| The negative root | 3: non-self; the 2026-10-31 backward-closure reading is a candidate self-derivation | held for rework at stage 4 |
| Brannen's π/12 phase rule | **3: non-self** | **quarantined**; not sealed as a methodology prediction |

Result: the prediction is public and dated (PRED-005) **as a borrowed prediction**. It enters the methodology only if canon derives the form, the sign and the phase.

## Before you finish

- Every new claim in your output carries its gate disposition.
- Nothing quarantined is described as the methodology's own.
- The independent filters passed are named; if only one kind was used, say so.
