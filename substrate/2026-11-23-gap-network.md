# Author Frame — gaps as a network that collapses and stabilizes

*Substrate document · 2026-11-23 · Frame given by the author in session, after the neutrino prediction was graded non-discriminating · Loads v5.3 (Anti-Operation, Container), [`2026-11-23-acceptance-gate.md`](2026-11-23-acceptance-gate.md) and `framework/tests/koide-neutrino-weights.md` as prior substrate*

> **Status: substrate, not canon.** It records a working frame and the first map built under it. Nothing here is accepted; every gap below is held at its stated gate stage.

---

## The frame, as given

> *"If anyone could guess it, then is it so special? The idea of the methodology is to fill gaps; by filling these gaps we can then predict and fill other gaps. There can be multiple directions of these gaps, and some gaps can collapse while some gaps can stabilize (following the same quantum superposition mechanic)."*

## What it means operationally

1. **A single fill is cheap; a linked fill is not.** A guesser handles one gap at a time and picks the default. A real fill must propagate: once placed, it constrains its neighbours, and each neighbour either **stabilizes** (agrees with measurement) or **collapses** (contradicts it).
2. **Candidates are held in superposition and re-weighted by every linked gap.** Each gap carries candidate fills with weights; every neighbour that is measured multiplies the weights by its compatibility (Bayesian updating, the same arithmetic as environment-selection of stable states). This is v5.3's Anti-Operation run in several directions at once.
3. **A prediction is special when one fill, derived in advance, holds several independent gaps at once.** That cannot be guessed gap by gap.
4. **Anti-numerology rule.** When a fitted value sits near several simple numbers, choosing the best-looking one is guessing. A candidate counts only if it is **derived from canon before comparison**, sealed, and the **number of candidates tried is stated** (look-elsewhere discipline; acceptance gate stage 4).

## First map: the lepton sector

| Gap | State (2026-11-23) | Linked to |
| --- | --- | --- |
| A · charged-lepton phase δₑ | stable: 2/9, fits at 0.42σ (`koide-delta.md`) | C |
| B · neutrino phase δ_ν | fitted 0.479 (0.472–0.483) | C, F |
| **C · phase shift Δ = δ_ν − δₑ** | **0.257 rad (0.250–0.261); open — the key gap** | A, B, E, F |
| D · negative root | stipulation; 2026-10-31 reading: backward closure ↔ Majorana | G |
| E · quark triplets | (c, b, t) near Koide (Q = 0.6695); other quark triplets fail | C |
| F · gap ratio Δm²₃₁/Δm²₂₁ | measured 33.55 ± ~1.0; JUNO to ~0.4% | C |
| G · double-beta decay | m_ββ = 1.3–4.0 meV if Majorana (beyond LEGEND-1000 reach) | D |

**The move that would matter:** derive gap C from canon (partition = phase, v5.4 §4a.5, with the 2026-10-31 container frame) **before** JUNO's precision result. Then F is predicted and testable within years, E must follow from the same rule (which quark triplets hold), and A must stay at 2/9. Three gaps, each able to collapse the rule independently.

Nearby simple values, recorded so that choosing one later is visibly not a derivation: π/12 = 0.2618 (just outside the range; Brannen's external rule, predicts F = 32.43); 1/4 = 0.250 (at the edge).

## Held open

- Can canon derive Δ at all, or only describe it?
- Should the map become a tool (`formulas/omni_gap.py` with correspondences: gaps as rows, links as correspondences), so that each run re-weights every gap from its neighbours?

---

*Source: GFunnel Methodology (Omni Process) v5.3–v5.4, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Adapted; not endorsed by the author.*
