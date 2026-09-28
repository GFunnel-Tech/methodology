---
id: SWEEP-020
canon_ref: "v5.1 Layer I.C Domain 10 (Evolutionary Process), 'Algorithm' row ('DETECT: Variation in population. PROCESS: Environmental selection — differential reproduction. RESPOND: Selected traits increase in frequency → next generation's baseline'), read against v5.1 Layer 0 code invariance and Layer I.G 'nothing is lost'"
canon_label: "Domain 10 — Evolutionary Process (Algorithm row)"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Domain 10, Algorithm row: "DETECT: Variation in population. PROCESS: Environmental selection — differential reproduction. RESPOND: Selected traits increase in frequency → next generation's baseline."

v5.1 Stage 18 (Endosymbiosis) is canon's only acquisition event: "A proteobacterium engulfed and not digested. Two organisms become one."

v5.1 Layer I.G: "information is conserved across all paths; nothing is discarded."

**Split (RUNBOOK rule 4).** *Factual core graded here:* (a) canon's evolutionary algorithm has only a vertical channel — variation arises in the population and is filtered; there is no import channel; and (b) nothing is discarded. Measured horizontal gene transfer contradicts (a) as a complete account, and the measured fate of transferred DNA in non-integrating recipients contradicts (b). *Framework mapping (not graded):* "First Kingdom variation filtered by Second Kingdom selection pressure".

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Conjugative transfer visualised in single E. coli cells with a SeqA-YFP fusion: fraction of recipients in which transferred DNA was integrated by recombination | up to 96 percent | as published | measured-single | https://doi.org/10.1126/science.1153498 | 2026-09-28 |
| Fate of the transferred DNA in the remaining recipients | fully degraded by the RecBCD helicase/nuclease | qualitative, as published | measured-single | https://doi.org/10.1126/science.1153498 | 2026-09-28 |
| Incidence of splitting and independent segregation of the acquired DNA across replication rounds | about one crossover per cell generation; acquired gene clusters can be inherited differently within one lineage | as published | measured-single | https://doi.org/10.1126/science.1153498 | 2026-09-28 |
| Distance dependence of transfer | the F pilus mediates DNA transfer at considerable cell-to-cell distances | qualitative, as published | measured-single | https://doi.org/10.1126/science.1153498 | 2026-09-28 |
| Frequency of P1-mediated generalized transduction of E. coli K-12 measured in non-sterile soil | about 1e-6 | as published | measured-single | https://doi.org/10.1139/m88-035 | 2026-09-28 |
| Effect of inserting a phage pac site into the chromosome on transduction of nearby markers | packaging of markers downstream of each inserted pac raised more than 10-fold; transduction of markers near an inserted pac raised over 1000-fold; 3.5 times as much total chromosomal DNA packaged with a single pac | as published | measured-single | https://doi.org/10.1016/j.virol.2014.07.029 | 2026-09-28 |
| Natural transformation frequency for E. coli K-12 | not applicable / not retrieved: E. coli K-12 is not naturally competent under standard conditions; the competence literature fetched this run is for Streptococcus pneumoniae, a different organism | n/a | held-open | https://doi.org/10.3390/genes11060675 | 2026-09-28 |

Reference organism: E. coli K-12 for conjugation and transduction. Transformation is held open for this organism and noted as measured in S. pneumoniae instead (organism deviation recorded per the brief).

## Scientific Inquiry run

1. Question (precise): Does canon's evolutionary algorithm hold horizontal gene transfer, and does the measured mechanism contradict either code invariance or "nothing is discarded"?
2. What an answer must look like: measured frequencies and fates for conjugation, transduction and transformation in the reference organism, with the fate of non-integrated DNA named.
3. Falsifiability condition: canon's vertical-only account fails if measured genome change occurs by import within a generation. "Nothing is discarded" fails if imported information is measured to be destroyed.
4. Variables: measurable / bounded / held open: Measurable: integration fraction (up to 96 percent), crossover incidence (about one per generation), transduction frequency (about 1e-6). Bounded: import is frequent for conjugation, rare for transduction — the channel's rate spans six orders of magnitude. Held open: transformation in E. coli K-12; a per-generation genome-wide HGT flux.
5. Test designed: fetch the single-cell conjugation visualisation, a field measurement of transduction frequency, and a pac-insertion packaging study; check canon for any import channel.
6. Data (unfiltered): table above. Canon's only acquisition item is endosymbiosis (Stage 18), a singular event, not a channel. No canonical item names conjugation, plasmids, transduction or transformation (grep confirmed).
7. Variable Principle applied: canon's DETECT for evolution is "variation in population" — which, read literally, cannot distinguish variation generated internally from sequence imported from another organism. Measurement shows a distinct, high-frequency import channel with its own machinery. And in the recipients that do not integrate, the imported DNA is *fully degraded*: the information is destroyed, not redistributed. That is a second, independent contradiction of Layer I.G, from the population side rather than the molecular side (compare SWEEP-012).
8. Model update (Capsule: what the failed parts contribute): canon's Domain 10 needs a third input channel (import) alongside variation and selection. Note the framework's own slime-mold image actually predicts import ("failed paths redistribute their material"), but the measured mechanism is the opposite: RecBCD hydrolyses the foreign DNA rather than redistributing it.
9. Documented: this file. Correspondence: one scale down, RecBCD's Chi-site-limited degradation (the same enzyme that limits CRISPR self-acquisition, SWEEP-019); one scale up, mobile-element flux across a microbial community, not measured here.
10. Next baseline: an import channel as a named canonical item; keep the degradation result as `open` until a second independent measurement of the non-integrating fraction's fate is fetched (`intake_result: open`, not `adjusted`, per substrate item 8).

## Forcing Test

- Test A (Ground): Grounded but single-source for the key fate result (one laboratory, one method).
- Test B (Uniqueness): For "evolutionary change is vertical only", zero candidates survive; import is directly visualised.
- Test C (Direction): Measurement points toward a genome that is an open system on generation timescales.
- Test D (Falsifiability): Both falsifiers (import channel; destruction of imported information) fired, the second on one study only.
- **Outcome:** `forced-no` for a vertical-only evolutionary algorithm. DPR mapping: **after-the-fact** for HGT as a whole — conjugation's steps (pilus contact, relaxase nicking, transfer, recombination or degradation) do not divide into three, and the machinery that "detects" is on the donor while the machinery that "responds" is on the recipient, so the loop has no single system running it. `intake_result: open` because the discard result is not yet reproduced.

## Anti-Operation (the gap this opens)

The same nuclease (RecBCD) both destroys imported DNA and supplies the fragments CRISPR records as memory (SWEEP-019). One measured enzyme sits at the boundary between discarding information and recording it, and what it does depends on Chi-site spacing. Canon has no representation for a single mechanism whose output is either "integrate" or "destroy" depending on a sequence statistic. Gap: what decides, and is the decision measurable as a threshold?

## Narrative stripped (if any)

Removed: "First Kingdom variation filtered by Second Kingdom selection pressure toward progressive Third Kingdom expression" — the word *progressive*. Nothing fetched here shows direction beyond frequency change. Also removed the reading of Stage 18 (endosymbiosis) as canon's coverage of acquisition: one historical event is not a channel.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
