---
id: CONST-holevo-theorem
canon_ref: "v5.1 Appendix D, Information & Computation Laws, row 'Holevo’s Theorem' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2066)"
canon_label: "Holevo’s Theorem"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Information & Computation Laws*, line 2066:

> **Law:** Holevo’s Theorem  
> **Statement:** Maximum classical information extractable from n qubits is n bits  
> **Framework Role:** Hard limit on quantum-to-classical information transfer. The bridge between First Kingdom (classical) and the substrate beneath (quantum).

**Split (RUNBOOK rule 4).** *Factual core graded here:* at most n bits of classical information can be extracted from n qubits.

*Framework mapping (not graded; see Narrative stripped):* 'The bridge between First Kingdom (classical) and the substrate beneath (quantum).'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Holevo bound (accessible information of one qubit) | no more than one bit (Holevo 1973) | n/a (proved) | derived | https://plato.stanford.edu/entries/qt-quantcomp/ | 2026-09-24 |
| Superdense coding (bibliographic record) | Bennett & Wiesner, PRL 1992: communication via operators on EPR states | n/a | derived | https://api.crossref.org/works/10.1103/PhysRevLett.69.2881 | 2026-09-24 |

A proved theorem is not a measurement. Rows graded `derived` record the published statement the canon wording was checked against; no experiment can raise or lower their grade. With pre-shared entanglement, superdense coding sends 2 classical bits per transmitted qubit; this does not violate Holevo because the entangled partner qubit is also used.

## Scientific Inquiry run

1. Question (precise): Does canon state Holevo's theorem correctly?
2. What an answer must look like: Wording compared with the source.
3. Falsifiability condition: Canon's bound differs from Holevo's.
4. Variables: measurable / bounded / held open: Measurable: none. Bounded: n/a. Held open: none.
5. Test designed: Compare with SEP.
6. Data (unfiltered): Match: one bit per qubit, n bits from n qubits, absent prior entanglement.
7. Variable Principle applied: The entanglement caveat is recorded, not assumed.
8. Model update (Capsule: what the failed parts contribute): Add 'without prior shared entanglement'.
9. Documented: This file.
10. Next baseline: Integrated.

## Forcing Test

- Test A (Ground): Proved theorem.
- Test B (Uniqueness): Unique.
- Test C (Direction): n/a.
- Test D (Falsifiability): Passes.
- **Outcome:** `forced-fill`.

## Anti-Operation (the gap this opens)

Canon does not distinguish accessible information (≤ n bits) from the information needed to specify an n-qubit state (continuous parameters). Which one the framework means by 'information' is held open.

## Narrative stripped

Removed: 'bridge between First Kingdom (classical) and the substrate beneath (quantum)'. The Kingdom vocabulary is framework interpretation. Reality does not force it.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
