# Cell Information — Gap Register

> **Status: derivation / work-in-progress. Not canon.** IDs use **IG** so they do not collide with canon's Gap 1–5 or the membrane register's MG / MF. Status vocabulary is the same as [`../membrane/gaps.md`](../membrane/gaps.md).

## Summary

| ID | Gap | Status |
| --- | --- | --- |
| IG-01 | Canon says information is never discarded (Layer I.G) and calls the biological case "Confirmed"; measured biology shows active erasure at every level | **candidate conflict** → route to the Reality Audit |
| IG-02 | Canon says filter nothing at intake (*Gather*); the cell filters at intake but lets variation in unfiltered | **held open** (scale rule missing) |
| IG-03 | Container rule says re-form, never overwrite; the cell overwrites its record | **held open** (counter-instance) |
| IG-04 | Canon names an "optimal mutation rate" as evolution's dynamic middle; whether the measured rate is an optimum is not shown | **held open** |
| IG-05 | What in the cell does the "adapting"? (Third Kingdom placement) | **held open**, same as MF-04 |
| IG-06 | Inheritance outside the DNA sequence across generations | **held open** |
| IG-07 | The atlas is organized by structure, but information is a function that crosses all structures | **solved by derivation** (awaiting author) |
| IG-08 | Many L2 items have no measured source yet | **open** (listed in [`README.md`](README.md)) |

---

### IG-01 — Is information conserved? Canon vs. measured erasure — **candidate conflict**

**Canon says** (v5.1 Layer I.G):
- *"information is conserved across all paths; nothing is discarded."*
- The Slime Mold Stack, biological row: *"Mutation as genome's exploration of fitness space, with most variants retracting and the surviving ones carrying forward the structural information of failed ones in regulatory regions, methylation patterns, transposable elements."* Graded **"Confirmed."**

**Measured** ([`README.md`](README.md) anchors):
- **Errors are erased, not kept.** Proofreading and mismatch repair remove ~160–1000-fold and ~65–250-fold of copying errors (N1, N2). The mismatch is corrected and nothing records that it happened.
- **Most sequence is not maintained.** About 8.2% of the human genome is under purifying selection, and only 2.2% stayed constrained along both human and mouse lineages (N5). The rest turns over.
- **Erasure is built in.** Protein degradation, RNA decay and apoptosis (C1–C6) each remove items deliberately.
- **Some things do persist.** About half the human genome derives from transposable elements (N6). Immune memory persists (D5).

**Two readings, kept apart:**

| Reading | Status |
| --- | --- |
| **Strong:** failed variants' information is carried in regulatory regions, methylation and transposable elements | Testable. The measurements above do not support it as a general rule. Transposable-element sequence is mostly not the record of failed variants; it persists for other reasons (whether those reasons are known is not settled here). |
| **Weak:** survivors are shaped by what failed, because selection removed the failures | True by the definition of selection. But it is not "nothing is discarded": the failed sequence itself is gone. |

**Material vs. information:** autophagy and degradation recycle **material** (C2). So material conservation holds at the cell level. Information conservation, at the level of sequence and molecular state, does not.

**What to do:** do **not** edit canon. This is the kind of item the Reality Audit's domain phase (DOMAIN-09, DOMAIN-10) and the Slime Mold Stack row are for. Its classification belongs to the Forcing Test, and its diff state is a `conflict` candidate. The author decides when to route it.

**Data that would settle it:** a measured case where a lost variant's information is shown to be carried forward in the surviving lineage, beyond the weak reading.

### IG-02 — Filter at intake, or capture everything? — **held open**

Canon's *Gather* step (Shepherd's Way 03; Master Meta-Algorithm step 3) says capture without filtering. Its failure mode is filtering during gathering.

The cell does **both**, at different scales:
- **Sensing filters at intake.** Receptors are selective and switches have thresholds (A1).
- **Variation enters unfiltered.** Mutation is not screened in advance (F1); selection filters afterwards (F3). That matches *Gather* then filter.

**Gap:** canon has no rule for *which* intake should be unfiltered. A candidate reading, unchecked: intake that updates the long-term record (variation) is gathered unfiltered and selected later; intake that triggers action now (sensing) is filtered first.

### IG-03 — Overwrite vs. re-form — **held open (counter-instance)**

The container rule says *re-form, never overwrite; append, never delete*. The cell's record works the other way: repair restores the template and degradation removes the old state (B1, C1–C3). The only long-term traces are what persists in the genome (N6).

**Question for the author:** is "never overwrite" a rule for a *log of knowledge* that the cell simply does not need, or a correspondence that fails at cell scale? Not filled.

### IG-04 — Is the mutation rate an optimum? — **held open**

Canon (v5.1 Yin/Yang table) gives evolution's dynamic middle as *"Optimal mutation rate,"* between excess variation (chaos) and excess selection (stasis).

**Measured:** the human rate is 1.20 × 10⁻⁸ per nucleotide per generation (N3). That rate is the residue left after the fidelity pipeline (N1, N2). So the cell's *cleaning* machinery is what sets its *variation* rate (pattern P-06).

**Not shown:** that this rate is an optimum, as opposed to as low as the pipeline can reach. Settling it would need measurements across species that this run does not have, and **no outside theory is imported to fill it**.

### IG-05 — What adapts? — **held open**

Canon Domain 9 places "homeostatic regulatory intelligence" in the Third Kingdom. This area's adaptation mechanisms (E1–E5) are all molecular. Same open question as membrane MF-04. **Not filled.**

### IG-06 — Inheritance outside the DNA sequence — **held open**

Whether marks outside the DNA sequence pass across generations (F5), and how far, is not settled by any source collected here. **Not filled.**

**Data needed:** measured transmission of a defined mark across at least two generations, with the sequence controlled.

### IG-07 — Structure areas vs. function areas — **solved by derivation, awaiting author**

The atlas began organized by structure (membrane, then nucleus, ER and so on). Information processing crosses every structure, and so would energy, building and division.

**Proposed:** two axes.
- **Structure areas** list *where* things happen.
- **Function areas** (information, energy, building, division) list *what* the cell does.
- Each L2 item links to both.

This area is the first function area.

### IG-08 — Sources pending — **open**

Items marked *source pending* in [`README.md`](README.md) need a measured source before their runs. They are not filled from memory.
