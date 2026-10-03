---
id: SWEEP-028
canon_ref: "v5.1 Appendix A, Stage 23 'ATP Hydrolysis / Cellular Work' ('Energy captured by molecular machines: motor proteins, ion pumps, ribosomes, polymerases. Universal currency.')"
canon_label: "ATP Hydrolysis / Cellular Work — ATP as the universal currency"
proposed_label: "Measured energy cost of solute import: ABC importers (ATP) and PTS sugar uptake (PEP)"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, Stage 23:

> "ATP Hydrolysis / Cellular Work | Energy captured by molecular machines: motor proteins, ion pumps, ribosomes, polymerases. Universal currency."

v5.1 Appendix A, Stage 24: "Ion Gradients / Membrane Potentials | Na+/K+ ATPase establishes electrochemical asymmetry. Polarity deliberately created and maintained."

**Split (RUNBOOK rule 4).** *Factual core graded here:* ATP is the universal currency of cellular work, and the machines that spend it are motor proteins, ion pumps, ribosomes and polymerases.

*Framework mapping (not graded; see Narrative stripped):* "Universal currency"; "Polarity deliberately created and maintained."

Canon names no transporter class, no cost per molecule imported, and no non-ATP phosphoryl donor. Stage 24's only named pump, the Na⁺/K⁺ ATPase, is an animal enzyme that *E. coli* does not have.

## Reality shows

Reference organism: *Escherichia coli* and *Salmonella typhimurium* (the binding-protein transport systems on which the in-vivo stoichiometry was measured); PTS data are for gram-negative and gram-positive bacteria generally.

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| ATP hydrolysed per substrate molecule transported, periplasmic binding-protein-dependent (ABC) transport systems, measured *in vivo* | "one to two molecules of ATP hydrolyzed per molecule of substrate transported" | apparent stoichiometry, as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/2682642/ | 2026-09-28 |
| Whether ATP hydrolysis is the direct energy source for these systems | ATP hydrolysis occurs in vivo concomitantly with transport and "directly energizes substrate accumulation" | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/2682642/ | 2026-09-28 |
| Phosphoryl donor for PTS carbohydrate uptake | phosphoenolpyruvate (PEP), **not ATP**: "This system transports and phosphorylates carbohydrates at the expense of PEP" | as published | derived | https://pubmed.ncbi.nlm.nih.gov/8246840/ | 2026-09-28 |
| Route of the phosphoryl group in the PTS | PEP → enzyme I (His) → HPr → enzyme II → carbohydrate; one phospho-transfer chain per sugar molecule transported | as published | derived | https://pubmed.ncbi.nlm.nih.gov/8246840/ | 2026-09-28 |
| Coupling of transport to phosphorylation in the PTS | transport and phosphorylation are the same event — the sugar arrives inside already phosphorylated | as published | derived | https://pubmed.ncbi.nlm.nih.gov/8246840/ | 2026-09-28 |
| Additional, regulatory function of the same transport proteins | unphosphorylated IIA^Glc binds and inhibits several non-PTS uptake systems; phosphorylated P-IIA^Glc activates adenylate cyclase — the transporter is also the sensor | as published | derived | https://pubmed.ncbi.nlm.nih.gov/8246840/ | 2026-09-28 |
| Scaling of periplasmic binding-protein abundance with its ABC transporter abundance across 22 growth conditions | linear regression slopes significantly different from zero (p < 0.0001) for all plots; binding proteins in large excess over transporters | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4888949/ | 2026-09-28 |
| Third import mode used by *E. coli*: proton-motive-force-driven symport (e.g. GalP, LacY), cost paid in Δp not ATP or PEP | present and functionally interchangeable with PTS uptake for glucose (GalP + glucokinase replaces PTS) | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC13101720/ | 2026-09-28 |
| A single audited figure for total transport cost as a fraction of the *E. coli* ATP budget | not retrieved | n/a | held-open | no primary source reached this run apportions the ATP budget across transport, biosynthesis and maintenance for *E. coli*; not filled from memory | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold the measured cost of importing a molecule into a bacterial cell, and does DETECT → PROCESS → RESPOND fit the measured transport mechanisms?
2. What an answer must look like: canon's wording; a measured ATP-per-substrate stoichiometry for one transporter class; the identity of the phosphoryl donor for another; and a DPR assignment tested for boundaries.
3. Falsifiability condition: canon's "universal currency" fails as an exclusive claim if a major, measured class of cellular work is energised by something other than ATP. PTS sugar uptake is exactly that: the donor is PEP, and PMF-driven symport is a third currency again.
4. Variables: measurable / bounded / held open: **Measurable** — ATP per substrate for ABC systems; the PTS phospho-transfer chain; binding-protein : transporter ratios. **Bounded** — ABC cost in 1–2 ATP per molecule. **Held open** — the fraction of the ATP budget spent on transport.
5. Test designed: for each of the two named transporter classes, find the measured energy input per molecule imported, and check it against canon's single-currency statement.
6. Data (unfiltered): the table above. Three distinct currencies are measured for solute import in one organism: ATP (ABC), PEP (PTS), and Δp (symport). The same sugar, glucose, can be taken up by two of them.
7. Variable Principle applied: "universal currency" fills a variable — *which* currency — that measurement leaves at three. The fraction of budget spent is genuinely unmeasured here and is left open rather than estimated.
8. Model update (Capsule: what the failed parts contribute): Stage 23 should read that ATP is *a* currency, and that bacterial cells also spend PEP and the proton gradient directly. Stage 24's Na⁺/K⁺ ATPase should be marked as an animal instance, since the stage is placed before Stage 25 (multicellularity) yet names an enzyme no bacterium has. The failed part contributes something canon can use: the three currencies are *interconvertible at measured exchange rates* (Δp ↔ ATP via SWEEP-024's H⁺/ATP; PEP ↔ ATP via pyruvate kinase), which is a stronger and testable version of "universal currency" than the one canon states.
9. Documented: this file. Attempted DPR assignment: for the PTS, **DETECT** → binding of the sugar by enzyme II at the outer face; **PROCESS** → the phospho-relay PEP → EI → HPr → EII; **RESPOND** → release of the phosphorylated sugar inside. Here the assignment is *partly* real and partly arbitrary. It is real in one respect the other files lack: the same protein, IIA^Glc, has a measured second role as a sensor whose phosphorylation state regulates other transporters and adenylate cyclase — a genuine detection function with a measured downstream response. It is arbitrary for the transport event itself: binding, translocation and phosphorylation are steps of one catalytic cycle with no branch, and reversing the labels changes nothing. **DPR mapping: applied after the fact for the transport cycle; fits for the IIA^Glc regulatory circuit that rides on it** — and canon's Stage 23 holds only the first of these.
10. Next baseline: an ATP-budget apportionment for *E. coli*. Re-review 2027-09-24.

## Forcing Test

- Test A (Ground): Grounded. The ABC stoichiometry is an in-vivo measurement; the PTS donor is established biochemistry with a primary review citation.
- Test B (Uniqueness): Not unique — that is the finding. Three currencies, and for glucose two interchangeable uptake routes in one organism.
- Test C (Direction): Measured: ABC importers accumulate against a gradient at 1–2 ATP per molecule; the PTS accumulates by trapping the substrate as a phosphate ester rather than by pumping.
- Test D (Falsifiability): Falsifiable and, read as an exclusive claim, failed.
- **Outcome:** `forced-no` for "ATP is *the* universal currency" as an exclusive statement. `accounted` would be correct for the weaker statement that ATP energises much cellular work, but canon's own word is "universal", and that word is what is tested.

## Anti-Operation (the gap this opens)

If three currencies exist with measured exchange rates, then the interesting quantity is the *exchange rate*, and canon has no item for it. Worse for Layer I.E: exchange between currencies is lossy (SWEEP-024 measured 0.85 for one conversion), so a cell that routes work through the wrong currency pays a measurable premium. Canon's Resolution One ("the energy did not diminish by one quantum") has no way to express a conversion premium, and Stage 23's "universal currency" actively hides the question.

## Narrative stripped (if any)

Removed: "Polarity deliberately created and maintained" (Stage 24). The word "deliberately" imports intent that no measurement reaches; the ion gradients measured here are maintained by enzyme kinetics and are indifferent to whether anything intends them. Retained as accurate: that gradients are established and maintained at a cost, which SWEEP-023 quantifies.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
