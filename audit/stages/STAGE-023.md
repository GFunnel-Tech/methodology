---
id: STAGE-023
canon_ref: v5.1 Appendix A, Stage 23
canon_label: "ATP Hydrolysis / Cellular Work"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, table "Stages 23–49", row 23 (line 1769):

> | 23 | ATP Hydrolysis / Cellular Work | Energy captured by molecular machines: motor proteins, ion pumps, ribosomes, polymerases. Universal currency. |

**Factual core (graded):** (a) free energy of ATP hydrolysis drives molecular machines, naming motor proteins, ion pumps, ribosomes and polymerases; (b) ATP is a universal energy currency.
**Framework mapping (not graded):** none beyond its place in the stage sequence ("Universal currency" is a standard biochemical description, graded in (b)).

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| In-vivo Gibbs free energy of ATP hydrolysis, Atlantic cod white muscle (31P-NMR), rest → exhaustion | −55.6 → −49.8 kJ/mol | ±1.4 ; ±0.7 kJ/mol | measured-single | doi:10.1242/jeb.008763 (PubMed 17951415), via https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17951415 | 2026-09-24 |
| ATP-driven rotation of F1-ATPase (a rotary motor) | torque >40 pN·nm; reproduced in E. coli F1 | as published | measured-reproduced | doi:10.1038/386299a0 (PubMed 9069291); doi:10.1006/bbrc.1999.0885 (PubMed 10403811) | 2026-09-24 |
| Ion pump: Na+,K+-ATPase ions moved per ATP hydrolysis cycle | 3 Na+ out, 2 K+ in | stoichiometric | measured-single | doi:10.1038/nature06419 (PubMed 18075585), via efetch id=18075585 | 2026-09-24 |
| Ribosome translocation energy source | GTP hydrolysis by EF-G | n/a | measured-single | doi:10.1038/s41467-021-26133-x (PubMed 34635670, PMC8505512), via https://www.ebi.ac.uk/europepmc/webservices/rest/search | 2026-09-24 |
| Amino-acid activation for translation (aminoacyl-tRNA synthetases) | ATP consumed, forming aminoacyl-adenylate + PPi | n/a | measured-reproduced | doi:10.1002/2211-5463.13903 (PubMed 39344714, PMC11961388; describes the standard assay used since the 1960s), via Europe PMC REST search | 2026-09-24 |
| Energy source of nucleic-acid polymerases | none | n/a | held-open | Not fetched in this run. | 2026-09-24 |
| Universality of ATP as energy currency across all domains | none | n/a | held-open | No source fetched in this run that measures this across all domains. | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does ATP hydrolysis power motor proteins, ion pumps, ribosomes and polymerases, and how much free energy does it release in cells?
2. What an answer must look like: in-vivo ΔG measurement; measured ATP coupling for each named machine class.
3. Falsifiability condition: falsified for a named machine if its work is shown to be powered by something other than ATP.
4. Variables: measurable: ΔG in vivo; coupling stoichiometries. Held open: polymerase energetics and cross-domain universality (not fetched).
5. Test designed: fetch in-vivo ΔG, rotary-motor, ion-pump and translation papers.
6. Data (unfiltered): table above. ΔG in vivo about −50 to −56 kJ/mol in one fish muscle. Ion pump and rotary motor are ATP-driven. The ribosome's translocation is powered by GTP (EF-G); ATP enters translation upstream via aminoacyl-tRNA synthetases.
7. Variable Principle applied: motors and pumps = measured. Ribosome = measured, but via GTP at the ribosome and ATP upstream. Polymerases and universality = held open in this run.
8. Model update (Capsule): accounted, with a refinement: canon's list mixes machines powered directly by ATP (pumps, F1) with the ribosome, whose own motor step uses GTP. "Nucleoside triphosphate hydrolysis" is the accurate class; ATP is the main but not the only currency.
9. Documented: this file.
10. Next baseline: fetch polymerase energetics and a cross-domain survey of ATP use.

## Forcing Test
- Test A (Ground): Grounded for pumps and motors; partly for ribosomes.
- Test B (Uniqueness): One reading survives for pumps and motors (ATP-driven).
- Test C (Direction): Forced: hydrolysis releases free energy (ΔG negative in vivo).
- Test D (Falsifiability): Yes (step 3).
- **Outcome:** forced-fill (for ATP-driven pumps and motors). The ribosome item is refined, not contradicted.

## Anti-Operation (the gap this opens)
In-vivo ΔG is condition-dependent (it fell by ~6 kJ/mol at exhaustion in the cod study). Canon's "universal currency" treats the payment as fixed; the measured value varies with cell state. Also opened: GTP as a second currency at the ribosome, which canon does not hold.

## Narrative stripped (if any)
None graded. "Universal currency" is a standard biochemical description, not a framework mapping. The label is observational; no new label proposed.
