---
id: SWEEP-025
canon_ref: "v5.1 Appendix A, Stages 15, 16, 17 and 21 (the ordered progression Glycolysis → Fermentation/Anaerobic Respiration → Oxygenic Photosynthesis → Electron Transport Chain)"
canon_label: "Fermentation / Anaerobic Respiration (Stage 16) as a low-yield predecessor superseded by the oxygen-using Electron Transport Chain (Stage 21)"
proposed_label: "Terminal reductase repertoire: simultaneously encoded aerobic and anaerobic electron acceptors under regulatory choice"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, Stages 15–17 and 21, in this order:

> "15 | Glycolysis | Most ancient metabolic pathway. Glucose split anaerobically. Universal across nearly all life."
> "16 | Fermentation / Anaerobic Respiration | Pyruvate processed without oxygen. Low-yield, but functional. Dynamic middle of pre-oxygen metabolism."
> "17 | Oxygenic Photosynthesis (~2.4 Bya) | Great Oxygenation Event. Yang-extreme intervention."
> "21 | Electron Transport Chain | NADH and FADH₂ donate electrons. Cascade through Complexes I → III → IV pumps protons. Polarity created. Same logic as alkaline vents 4 Bya, now internalized."

**Split (RUNBOOK rule 4).** *Factual core graded here:* fermentation and anaerobic respiration are one low-yield stage belonging to "pre-oxygen metabolism", which the oxygen-using electron transport chain of Stage 21 supersedes; the sequence is a progression in which each stage is the substrate of the next.

*Framework mapping (not graded; see Narrative stripped):* "Dynamic middle of pre-oxygen metabolism"; "Yang-extreme intervention"; "Same logic ... now internalized."

Canon merges fermentation with anaerobic respiration into a single item, and places both before oxygen in a numbered order. No stage holds nitrate, fumarate, DMSO or TMAO respiration; no stage holds the simultaneous carriage of alternatives.

## Reality shows

Reference organism: *Escherichia coli* (the best-characterised organism for terminal-reductase choice).

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Composition of *E. coli* electron transport chains | many different dehydrogenases and terminal reductases/oxidases linked by three quinones (ubiquinone, menaquinone, demethylmenaquinone); isoenzymes present for both acceptors (O₂, nitrate) and donors (formate, H₂, NADH, glycerol-3-P); **no bc₁ complex** | review synthesis of primary data | derived | https://pubmed.ncbi.nlm.nih.gov/9230919/ | 2026-09-28 |
| Range of H⁺/e⁻ for the overall chain, depending on which enzymes and isoenzymes are used | 0 to 4 H⁺/e⁻ | as published range | derived | https://pubmed.ncbi.nlm.nih.gov/9230919/ | 2026-09-28 |
| Rank order of energy conservation by acceptor | "maximal with O₂ and lowest with fumarate"; nitrate intermediate | as published | derived | https://pubmed.ncbi.nlm.nih.gov/9230919/ | 2026-09-28 |
| Regulatory hierarchy of acceptor use | O₂ represses the terminal reductases of anaerobic respiration; in anaerobic respiration nitrate represses fumarate and DMSO reductases | as published | derived | https://pubmed.ncbi.nlm.nih.gov/9230919/ | 2026-09-28 |
| O₂ concentration range over which FNR switches | 1–5 mbar | as published | derived | https://pubmed.ncbi.nlm.nih.gov/9230919/ | 2026-09-28 |
| Direction of dehydrogenase selection under oxygen | "In aerobic growth, non-coupling dehydrogenases are expressed and used preferentially, whereas in fumarate or DMSO respiration coupling dehydrogenases are essential"; hence "the rationale for expression of the dehydrogenases is not maximal energy yield, but could be maximal flux or growth rates" | as published | derived | https://pubmed.ncbi.nlm.nih.gov/9230919/ | 2026-09-28 |
| Sensing architecture | two-component nitrate/nitrite sensors NarX/NarQ with response regulators NarL/NarP; ArcB/ArcA for oxygen; cytoplasmic FNR carrying a 4Fe4S cluster oxidised directly by O₂ | as published | derived | https://pubmed.ncbi.nlm.nih.gov/9230919/ | 2026-09-28 |
| Fully respiratory metabolism on galactose depends *exclusively* on the PEP–glyoxylate cycle, in contrast to respiro-fermentative glucose metabolism; *E. coli* "actively limits its galactose catabolism at the expense of otherwise possible faster" growth | as stated; 91 regulator mutants, ¹³C flux | measured-single | https://pubmed.ncbi.nlm.nih.gov/21451587/ | 2026-09-28 |
| Measured molar growth yields (g biomass per mol substrate) side by side for O₂, nitrate and fumarate respiration in one *E. coli* study | not retrieved | n/a | held-open | no single primary study reached this run reports all three yields under matched conditions; the qualitative rank order above is recorded instead, and no numbers are supplied from memory | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does canon's ordered placement of fermentation/anaerobic respiration before the oxygen-using electron transport chain survive the measured metabolic flexibility of *E. coli*, and does DETECT → PROCESS → RESPOND fit the measured acceptor-choice mechanism?
2. What an answer must look like: canon's stage order quoted; evidence on whether a single organism carries aerobic and anaerobic chains at once and how it chooses; and a DPR assignment with its boundary test.
3. Falsifiability condition: canon's progression reading fails if one organism is measured to carry, simultaneously and under regulatory control, terminal reductases for oxygen and for several anaerobic acceptors, choosing among them rather than having replaced one with the next. This is exactly what is measured.
4. Variables: measurable / bounded / held open: **Measurable** — H⁺/e⁻ per chain configuration, O₂ switching range, regulator identities and their binding sites. **Bounded** — H⁺/e⁻ between 0 and 4. **Held open** — matched molar growth yields for the three acceptors.
5. Test designed: fetch the standard measurement review for *E. coli* alternative respiratory pathways; fetch a large-scale flux study for evidence on whether flux is set to maximise yield; then attempt the DPR assignment.
6. Data (unfiltered): the table above. The decisive rows are the regulatory hierarchy (O₂ ⊳ nitrate ⊳ fumarate/DMSO) and the dehydrogenase row, which states directly that expression is *not* organised for maximal energy yield.
7. Variable Principle applied: canon fills the variable "how does an organism relate to oxygen" with a historical order. Measurement replaces the order with a repertoire plus a switch. The switch's set-points are measurable (1–5 mbar O₂); the relative yields are held open and are not filled.
8. Model update (Capsule: what the failed parts contribute): Stage 16 must be split — fermentation (substrate-level phosphorylation, no chain) and anaerobic respiration (a full chain with a non-oxygen acceptor) are different mechanisms, and the second is not "pre-oxygen": it runs in a modern organism alongside the aerobic chain. The failed part contributes the strongest structural finding of this sweep: canon's Appendix A order is a *presentational* sequence being read as a causal and temporal one. Stage 21's "Same logic ... now internalized" is correct as physics and wrong as history for anaerobic respiration, which was never superseded.
9. Documented: this file. Attempted DPR assignment: here, unusually, the assignment has a real boundary. **DETECT** → FNR's 4Fe4S cluster oxidised by O₂ at 1–5 mbar, or NarX/NarQ binding nitrate: these are identifiable sensor molecules with a measured stimulus range. **PROCESS** → phosphorelay and transcription-factor-mediated repression/activation at characterised promoters. **RESPOND** → altered terminal-reductase composition of the membrane. The three steps are separated by physically distinct molecules, and a change at the DETECT step (an FNR cluster mutant) leaves the others intact. **DPR mapping: fits.** But note what this costs canon: the fit is with Domain 9's regulatory algorithm, not with Appendix A's progression, and the same measurement that makes DPR fit is the measurement that breaks the stage order.
10. Next baseline: matched molar growth yields for O₂ / nitrate / fumarate. Re-review 2027-09-24.

## Forcing Test

- Test A (Ground): Grounded for the repertoire and the regulatory hierarchy; the yield ranking is grounded qualitatively only.
- Test B (Uniqueness): Canon's ordering is not unique. At least two orderings fit the same facts (a historical sequence; a co-existing repertoire under regulation), and the measured evidence selects the second.
- Test C (Direction): Measured direction runs against canon's implied one. Anaerobic respiration is not a superseded predecessor; it is a maintained option, and the organism does not select for maximum energy yield.
- Test D (Falsifiability): Falsifiable, and the progression reading fails.
- **Outcome:** `stipulation` for the numbered order — a presentation choice, not a forced result — with `forced-no` for the specific factual reading that Stage 16 belongs only to "pre-oxygen metabolism". The record is graded `conflict` on the factual core.

## Anti-Operation (the gap this opens)

If Appendix A's numbers are presentational rather than causal, then every "Per Cause and Effect: all later X caused at this moment" note attached to a stage inherits that weakness, and the progression cannot be used as evidence for Correspondence. Canon must state which of its 100 stages are ordered in time, which in logical dependency, and which only in exposition. That decision is not made anywhere in v5.1, v5.3 or v5.4 that this audit reached.

## Narrative stripped (if any)

Removed: "Dynamic middle of pre-oxygen metabolism" (Stage 16) — anaerobic respiration is measurably not confined to pre-oxygen conditions, so the qualifier is false, and "dynamic middle" names no measured quantity. Removed: "Yang-extreme intervention" for the Great Oxygenation Event (Stage 17) — an interpretation reality neither forces nor contradicts. Retained as accurate physics: Stage 21's "Polarity created", audited in SWEEP-023.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
