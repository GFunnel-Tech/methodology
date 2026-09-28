---
id: SWEEP-014
canon_ref: "v5.1 Layer I.C Domain 9, 'DNA as Base Code' row: 'Gene expression is the universal algorithm at molecular level: signal → transcription/translation → expressed protein'"
canon_label: "Domain 9 — DNA as Base Code"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Domain 9, DNA as Base Code row: "DNA is Second Kingdom compressed into First Kingdom form. **Gene expression is the universal algorithm at molecular level: signal → transcription/translation → expressed protein.**"

v5.1 Layer 0, Cross-Domain Convergence Table, Biological row: "DETECT: Homeostatic deviation or threat. PROCESS: Cellular signaling cascade + gene expression. RESPOND: Adapted equilibrium."

**Split (RUNBOOK rule 4).** *Factual core graded here:* canon places transcription and translation together inside one PROCESS operation, and names no promoter-recognition step, no sigma factor, and no rate. *Framework mapping (not graded):* "Second Kingdom compressed into First Kingdom form."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Sigma factors encoded by E. coli | 7 | exact count as published | measured-reproduced | https://doi.org/10.1007/s13353-024-00870-3 | 2026-09-28 |
| In vivo targets of sigma-32 identified genome-wide; estimated total sigma-32 promoters; fraction inside coding regions | 87 targets identified; 120-150 promoters estimated; 25 percent within coding regions | as published | measured-single | https://doi.org/10.1038/nsmb1130 | 2026-09-28 |
| Overlap of promoter recognition between sigma factors | majority of sigma-32 targets also sigma-70 targets; RNAP-sigma70 and RNAP-sigma32 initiate in vitro with similar efficiency from identical positions | qualitative, as published | measured-single | https://doi.org/10.1038/nsmb1130 | 2026-09-28 |
| E. coli RNA polymerase transcription elongation rate, real-time surface plasmon resonance with a flux-flow model | 20 nt/s | ± 7 nt/s | measured-single | https://doi.org/10.1021/acsomega.3c04754 | 2026-09-28 |
| Literature range of measured bacterial transcription elongation rates collected by the same study | 10 to 55 nt/s, depending on method and conditions | range as published | measured-single | https://doi.org/10.1021/acsomega.3c04754 | 2026-09-28 |
| Coupling: overall transcription elongation rate in vivo is controlled by the rate of translation; accelerating or decelerating the ribosome changes RNAP speed correspondingly; rare-codon content is inversely correlated with transcription rate | qualitative relation, as published | as published | measured-single | https://doi.org/10.1126/science.1184939 | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold transcription as a distinct operation — RNA polymerase, promoter recognition, sigma factors, elongation rate — and does DPR fit its measured mechanism?
2. What an answer must look like: a canonical item naming transcription separately from translation, with any rate or specificity statement; and measured values for elongation rate and promoter discrimination.
3. Falsifiability condition: the gap claim fails if canon anywhere separates transcription from translation as two operations, or names a sigma factor or a rate.
4. Variables: measurable / bounded / held open: Measurable: sigma factor count, promoter target counts, elongation rate. Bounded: promoter specificity is not a clean partition (sigma overlap measured). Held open: whether sigma-factor selection is a DETECT event in the framework's sense; canon has no item to compare.
5. Test designed: search canon for sigma / promoter / transcription rate; fetch measured sigma factor count, genome-wide promoter assignment, and elongation rates.
6. Data (unfiltered): table above. Canon names "transcription" only inside the compound "transcription/translation" and states no rate and no specificity mechanism.
7. Variable Principle applied: promoter recognition is the one place in transcription where a genuine detection boundary exists — and measurement shows it is *leaky* (sigma factors share promoters, 25 percent of sigma-32 targets lie inside coding regions). Canon's collapsed "transcription/translation" cannot represent this, and the framework's assertion that the loop applies "with zero exceptions" is not tested at this resolution.
8. Model update (Capsule: what the failed parts contribute): if the DPR parse is retained, DETECT = holoenzyme-promoter recognition and open-complex formation, PROCESS = processive RNA chain elongation, RESPOND = termination and release of the transcript. The DETECT/PROCESS boundary is real (promoter escape is a measured, separable transition); the RESPOND boundary is real (termination). But canon assigns the whole of transcription to PROCESS, so canon's own assignment is one scale coarser than the mechanism, and the finer parse is a derivation, not canon.
9. Documented: this file. Correspondence: one scale up, transcription-translation coupling means the two loops are not independent, which contradicts treating each as a self-contained DETECT-PROCESS-RESPOND cycle; one scale down, single-nucleotide addition cycles.
10. Next baseline: candidate PRED test on the measured speed ordering replication (653 nt/s) vs transcription (20 nt/s) vs translation, which canon nowhere states.

## Forcing Test

- Test A (Ground): Reality side grounded; canon side has no item at this resolution.
- Test B (Uniqueness): Not unique. Canon's parse puts transcription inside PROCESS; the finer parse puts a full loop inside transcription alone. Both are consistent with measurement, so measurement does not force either.
- Test C (Direction): Measurement points toward *nested and coupled* loops (RNAP speed set by ribosome speed), not toward one loop per molecular process.
- Test D (Falsifiability): The gap claim's falsifier (a canonical line naming a sigma factor or a transcription rate) did not fire.
- **Outcome:** `stipulation` — canon's placement of transcription inside a single PROCESS operation is a presentation choice. The DPR fit at the transcription scale is **after-the-fact** as canon states it, though a finer derived parse would fit measured boundaries (promoter escape, termination).

## Anti-Operation (the gap this opens)

Measured transcription-translation coupling means two of canon's supposedly separate molecular loops share a rate. The framework has no representation for two loops whose speeds are locked. What would "one algorithm, zero exceptions" predict about which of two coupled loops sets the pace? Canon supplies no answer.

## Narrative stripped (if any)

Removed: "DNA is Second Kingdom compressed into First Kingdom form" as a factual claim. It is a Kingdom mapping; no measurement fetched here forces or contradicts it.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
