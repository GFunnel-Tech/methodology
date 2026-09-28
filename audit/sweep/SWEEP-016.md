---
id: SWEEP-016
canon_ref: "v5.1 Layer I.C Domain 9, 'DNA as Base Code' row ('signal → transcription/translation → expressed protein') and v5.1 Appendix A Stage 23 ('ribosomes' among ATP-consuming molecular machines)"
canon_label: "Domain 9 — DNA as Base Code / Stage 23 ATP Hydrolysis / Cellular Work"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Domain 9: "Gene expression is the universal algorithm at molecular level: signal → transcription/translation → expressed protein."

v5.1 Appendix A, Stage 23: "Energy captured by molecular machines: motor proteins, ion pumps, **ribosomes**, polymerases."

**Split (RUNBOOK rule 4).** *Factual core graded here:* translation is one operation within a single molecular-scale loop, with no stated rate and no stated error rate. *Framework mapping (not graded):* "gene expression is the universal algorithm".

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Translational elongation rate in E. coli under good growth conditions (doubling rate above 1 per hour) | 16 to 17 amino acids per second | as published | measured-single | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5346290/ | 2026-09-28 |
| Translational elongation rate maintained close to zero growth (doubling time 20 hours) | above 9 amino acids per second | as published | measured-single | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5346290/ | 2026-09-28 |
| Dependence of elongation rate on the abundance of the translational apparatus | Michaelis-Menten dependence; active-ribosome fraction falls sharply at slow growth while elongation rate is maintained | as published | measured-single | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5346290/ | 2026-09-28 |
| Missense (misreading) error rate per codon in E. coli | 1e-3 to 1e-4, varying widely by codon and by competing tRNA abundance | range as published | measured-single | https://doi.org/10.1261/rna.294907 | 2026-09-28 |
| Amino-acid selection by tyrosyl-tRNA synthetase: preferential activation of tyrosine over phenylalanine, and the resulting misactivation rate in vivo | 1e5 to 2e5 fold discrimination; about 5e-4 misactivation, with no editing mechanism found | as published | measured-single | https://doi.org/10.1021/bi00565a009 | 2026-09-28 |
| Translation elongation rate in an E. coli cell-free system (for contrast with the in vivo value) | 1.5 amino acids per second per ribosome | ± 0.2 | measured-single | https://doi.org/10.1002/bit.20529 | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold translation — ribosome, tRNA charging, elongation rate, error rate — and does DPR fit the measured elongation cycle?
2. What an answer must look like: a canonical item naming translation as an operation with a rate or fidelity, and measured values for both.
3. Falsifiability condition: the gap claim fails if canon states any translation rate or error rate. The DPR claim fails if codon recognition, peptide-bond formation and translocation are not separable measured events.
4. Variables: measurable / bounded / held open: Measurable: elongation rate in vivo and in vitro, misreading rate per codon, synthetase discrimination. Bounded: error rate is bounded between about 1e-4 and 1e-3 per codon and is codon-dependent, so no single fidelity number exists. Held open: whether the ribosome's proofreading step and the synthetase's selection step are one "operation" or two in framework terms.
5. Test designed: fetch in vivo elongation rates across growth rates, a systematic per-codon misreading measurement, and an aminoacylation-fidelity measurement.
6. Data (unfiltered): table above. Canon states no rate and no error rate for translation. Measured fidelity is two to three orders of magnitude *worse* than replication fidelity, and varies by codon.
7. Variable Principle applied: canon's single compound "transcription/translation" implies one uniform process; measurement shows two processes with different speeds (about 20 nt/s of RNA vs about 50 nt of mRNA read per second at 16-17 aa/s) and very different error rates. No canonical number is contradicted, because canon states none — that absence is the gap.
8. Model update (Capsule: what the failed parts contribute): the parse that fits measured boundaries is DETECT = codon-anticodon recognition and kinetic proofreading in the A site (a separable, measurable discrimination step); PROCESS = peptidyl transfer; RESPOND = EF-G-driven translocation, which sets the next codon as the next input — the closest thing in this sweep to canon's "the response becomes the next cycle's input". Each boundary is separable by measurement (antibiotics and ribosomal mutations shift discrimination without abolishing transfer).
9. Documented: this file. Correspondence: one scale down, single-turnover GTPase steps; one scale up, tRNA charging is a *separate upstream* loop whose error (5e-4) enters the ribosome as an undetectable input — a detection blind spot canon's DETECT does not model.
10. Next baseline: a PRED candidate on the relation error-rate vs competing-tRNA abundance (Kramer and Farabaugh's central result), a relation canon nowhere states.

## Forcing Test

- Test A (Ground): Grounded. Rate and error rate are measured; the three sub-steps are separable.
- Test B (Uniqueness): Nearly forced at this scale: the elongation cycle is conventionally and measurably three-phase (selection, transfer, translocation). Competing parses exist (initiation / elongation / termination), so uniqueness is not established.
- Test C (Direction): Measurement points one way: selection precedes transfer precedes translocation, and the product of one cycle is the substrate of the next.
- Test D (Falsifiability): Falsifier named (non-separability); it did not fire.
- **Outcome:** `live-hypothesis`. DPR **fits** the measured elongation cycle, with the falsifier that a mischarged tRNA carries an error the DETECT step provably cannot see (no editing found for Tyr/Phe), so the loop is not self-correcting as Layer 0 implies. Canon's own item is still coarser than the mechanism: `methodology-gap` stands.

## Anti-Operation (the gap this opens)

Translation's measured error rate is 1e-3 to 1e-4 per codon, six or seven orders of magnitude worse than replication's per-base rate — yet canon asserts a single invariant code with no error terms anywhere. Open question the framework cannot yet answer: why is the framework's "code invariance" defended at the DNA level while the expression steps that actually produce the phenotype are the noisiest stage of the whole pipeline?

## Narrative stripped (if any)

Removed: "signal → transcription/translation → expressed protein" presented as the universal algorithm *at molecular level*. As a description it is accurate; as evidence for universality it is circular, since the three slots were chosen to match. Reality neither forces nor contradicts the universality mapping.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
