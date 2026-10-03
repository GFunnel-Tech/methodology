---
id: SWEEP-002
canon_ref: v5.1 Layer I.C Domain 9 Biological Process Algorithm, step 3; v5.1 Layer 0 Cross-Domain Convergence Table, Biological row
canon_label: "Process the deviation through cellular signaling, gene expression, or hormonal cascade"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Domain 9 Biological Process Algorithm, step 3: "Process the deviation through cellular signaling, gene expression, or hormonal cascade."

v5.1 Layer 0, Biological row: "PROCESS: Cellular signaling cascade + gene expression."

v5.1 Layer I.C Domain 9, DNA as Base Code row: "Gene expression is the universal algorithm at molecular level: signal → transcription/translation → expressed protein."

Canon names no phosphorelay, no kinase, no phosphatase, and no response regulator. The three named PROCESS vehicles are gene expression, protein synthesis, and hormonal cascade.

**Split.** *Factual core:* a detected signal is processed by a cascade before a response is issued. *Framework mapping:* that the cascade's vehicle is gene expression or a hormone, and that the cascade is the PROCESS operation of a three-operation algorithm.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Decay rate constant of CheY~P bound to FliM after flash release of attractant, in vivo FRET | ≈2 s^-1 | as published, no σ stated | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12232047&rettype=abstract&retmode=text (Sourjik & Berg 2002, PNAS 99:12669) | 2026-09-28 |
| Rise rate constant of CheY~P bound to FliM after flash release of repellent, same assay | ≈20 s^-1 | as published, no σ stated | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12232047&rettype=abstract&retmode=text | 2026-09-28 |
| Cooperativity of CheY~P binding to FliM compared with cooperativity of motor switching | "much less cooperative than motor switching" | qualitative comparison as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12232047&rettype=abstract&retmode=text | 2026-09-28 |
| Amplification between fractional change in receptor occupancy and fractional change in CheA kinase activity (CheY/CheZ FRET) | 36 (addition), 27 (removal) | ± 1; ± 2 | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ (Sourjik & Berg 2002, PNAS 99:123) | 2026-09-28 |
| Steady-state intracellular CheY~P concentration assumed at the midpoint of the motor response curve in a fully adapted cell | ≈3.1 µM | stated as an assumption in the source, from ref. to Cluzel et al. 2000 | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ | 2026-09-28 |
| Fall in CheY~P and change in rotational bias for a small step of attractant, from the measured amplification | 3.1 µM to ≈2.9 µM; bias falls by ≈0.17 | as published | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ | 2026-09-28 |
| Weighting window over which wild-type cells compare receptor occupancy (impulse, step, ramp and sine stimuli) | 4 s: the past 1 s weighted positively, the previous 3 s weighted negatively, cells respond to the difference | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC387059/ (Segall, Block & Berg 1986, PNAS 83:8987) | 2026-09-28 |
| Weighting window in cheZ mutants (phosphatase absent) | extends at least 40 s into the past | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC387059/ | 2026-09-28 |
| Gain of the chemotactic system | "the change in occupancy of one receptor molecule produces a significant response" | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC387059/ | 2026-09-28 |
| Distribution of clockwise and counterclockwise rotation intervals, tethered cells | exponential; fitted by first-order rate constants controlled by an error signal | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=6339475&rettype=abstract&retmode=text (Block, Segall & Berg 1983, J Bacteriol 154:312) | 2026-09-28 |

## Scientific Inquiry run
1. Question (precise): Does canon's PROCESS operation hold the CheA/CheY/CheZ phosphorelay, and does the measured relay have distinguishable DETECT / PROCESS / RESPOND boundaries or is the three-way split imposed?
2. What an answer must look like: the canonical text that would cover a phosphotransfer relay; the molecule and covalent event assigned to each operation; and measured rate constants showing whether the boundaries are separable in time.
3. Falsifiability condition: the mapping fits if each operation is a distinct covalent state change with its own measured rate constant. It fails if the relay has a number of steps other than three with no principled grouping into three, or if canon's named PROCESS vehicles are absent from the mechanism.
4. Variables: measurable / bounded / held open: measurable — on/off rate constants (2 and 20 s^-1), amplification slope, temporal weighting window, interval distributions. Bounded — absolute CheY~P concentration (assumed, from a separate single-cell measurement). Held open — whether a relay of four covalent states should be read as three operations.
5. Test designed: fetch the in vivo FRET signal-processing-time measurement, the amplification measurement, and the impulse/ramp response analysis; then assign DPR step by step against the covalent chemistry.
6. Data (unfiltered): CheY~P occupancy of FliM falls with rate ≈2 s^-1 on attractant and rises with rate ≈20 s^-1 on repellent — a tenfold asymmetry. Binding of CheY~P to FliM is much less cooperative than motor switching, placing the ultrasensitive step downstream of binding. Amplification between receptor occupancy and kinase activity is 36 ± 1. Wild-type cells integrate occupancy over 4 s with a bilobed positive/negative weighting; deleting the phosphatase CheZ stretches that window past 40 s. Gain is high enough that a single receptor's occupancy change gives a significant response. Rotation intervals are exponential. Canon's named PROCESS vehicles — gene expression, protein synthesis, hormonal cascade — occur nowhere in this pathway.
7. Variable Principle applied: **Measured** — the rate constants, the asymmetry, the window, the amplification. **Structurally derived** — the CheY~P concentration and the predicted bias change. **Held open** — the operation count. Concretely: DETECT = ligand occupancy of the receptor (SWEEP-001); PROCESS = CheA autophosphorylation on its His residue and phosphotransfer to CheY, with CheZ setting the lifetime of CheY~P; RESPOND = CheY~P binding FliM and switching the motor (SWEEP-004). Here the boundaries *are* measurable: the covalent states (CheA~P, CheY~P, CheY~P·FliM) are chemically distinct, each has its own rate, and the CheZ deletion moves the memory window by an order of magnitude without touching detection or response. So the DPR split at this stage is not arbitrary — it is the best-supported instance of the base code found in this sweep. Two qualifications: (a) the relay has four distinguishable covalent states, not three, so the grouping into three operations is a choice about where to draw the line, not a count read off the mechanism; (b) canon's own description of PROCESS names none of the actual chemistry.
8. Model update (Capsule: what the failed parts contribute): the framework's PROCESS is the operation with the weakest canonical specification (three vehicles, all transcriptional or endocrine) and the strongest real-world instance (a phosphorelay with measured rates). The gap is in the canon text, not in the idea. Proposed: add "phosphotransfer relay (histidine kinase to response regulator), with a phosphatase setting the memory time constant" to step 3. The CheZ result is the load-bearing one: the *duration* of memory is set by a dedicated enzyme, which is a mechanism canon's Layer I.F (observation as capture-and-record) asserts but never localizes.
9. Documented: this file.
10. Next baseline: mapping fit — yes, with the operation count held open. Canon coverage — absent. Next question: whether a four-state relay grouped into three operations is a general pattern (see SWEEP-009, two-component systems, where the relay is His to Asp with no phosphatase in many cases).

## Forcing Test
- Test A (Ground): grounded in three independent in vivo measurements (flash-release FRET, FRET dose-response, tethered-cell impulse response), all fetched this run.
- Test B (Uniqueness): partly unique. Given the covalent chemistry, no other assignment puts PROCESS anywhere but the phosphorelay. But the number of operations is not forced: four covalent states admit a 2-2 or 1-3 grouping as readily as 1-2-1.
- Test C (Direction): here canon and measurement run the same way — signal in, covalent cascade, mechanical output. Direction agrees.
- Test D (Falsifiability): the fit condition at step 3 was met for boundary separability and failed for canon's named vehicles. Recorded as a split result rather than a pass.
- **Outcome:** `stipulation`. The DPR mapping fits the measured mechanism here better than anywhere else in this sweep, but the fit is a good description, not a forced result: the operation count is a stipulation, and the canonical item that should hold the mechanism names the wrong chemistry. `methodology-gap`, diagnosis `not-reached`.

## Anti-Operation (the gap this opens)

- If the phosphorelay is the framework's best case, then the framework's strongest evidence is a system with four states read as three. Every other domain's three-way reading inherits that slack. A test that counts operations independently of the reader is missing.
- The 2 s^-1 / 20 s^-1 asymmetry (response to bad news ten times faster than to good news) has no canonical slot. Layer I.D's dynamic middle is symmetric; the measured middle is not.
- CheZ sets memory duration. Canon asserts memory (Layer I.F, Layer I.G) but names no dedicated *forgetting* mechanism. A framework in which nothing is lost has no place for a phosphatase.

## Narrative stripped (if any)

- "Hormonal cascade" as a named PROCESS vehicle: an organism-scale mechanism generalized to a domain whose most-measured member has no hormones. Reality does not force it; it reflects the metazoan template noted in SWEEP-001.
- Reading CheZ as Layer I.G's Capsule ("nothing is lost, inefficient paths redistribute information"): CheZ measurably *destroys* the signal, and removing it degrades chemotaxis by stretching the comparison window tenfold. The Capsule reading is not forced and points the wrong way here.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
