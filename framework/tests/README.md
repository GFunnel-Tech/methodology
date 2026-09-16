# Test Runs

v5.4 §14 hands the next run six tests "in order of cost." This directory holds the ones that have been **executed**, each with a reproducible script, its numbers, and an honest verdict — including where the verdict is *less* favourable than the canon's wording.

These are **variable-evidence contributions**, not a new version. They narrow or fail to narrow what v5.4 left open; they add no architecture and change no base code. Per [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md), a version is the author's to declare.

| §14 | Test | Status | Result |
| --- | --- | --- | --- |
| 1 | Koide prediction — δ = 2/9, trefoil form | ✅ **run** | [koide-delta.md](koide-delta.md) — **passes** at 0.42σ; all three lepton masses to ≤0.0031% from one scale. Caveat: Koide's 2/3 is built into the form, so the whole test is one number. |
| 2 | Meson 1/3 test (two-fold partition) | ⛔ **not runnable as written** | [not-runnable.md](not-runnable.md) — no observable is specified. |
| 3 | Lamina falsifier vs nuclear-density data | ◐ **partially run** | [lamina-falsifier.md](lamina-falsifier.md) — one genuine plateau confirmed; the falsifier as stated is not currently decidable. |
| 4 | Test partition = phase (§4a reframing) | ⛔ **held open** | [not-runnable.md](not-runnable.md) — better posed than "strand ≠ generation", and integer harmonics are now **forced-no**; but *why three phases* still needs the tension law. |
| 5 | D1 energy budget with fold storage | ✅ **run** | [d1-energy-budget.md](d1-energy-budget.md) — "hundreds of tesla" **confirmed**, but only under the pressure criterion; plasma is *forced*, not preferred. |
| 6 | Open the CONTRIBUTING issue for rows 9–15 | ☐ **maintainer action** | Those are rows **8–14** in [`../registers.md`](../registers.md); §4a added canon row 16 (row 15 here) after that instruction was written. See the numbering note. |

## Reproducing

```bash
python3 framework/tests/koide_delta.py
python3 framework/tests/d1_budget.py
```

Standard library only; no dependencies. Physical constants and PDG masses are declared at the top of each script so a reader can see exactly what was assumed.
