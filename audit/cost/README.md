# What the Reality Log Cost to Build

> **Status: derivation / work-in-progress. Not canon.** A sourced estimate of what it cost to produce the measurements the Reality Audit reads. Every input figure is in this directory with its source URL, source type, a verbatim quote, and retrieval date (2026-09-27). The totals are computed by [`compute_cost.py`](compute_cost.py); every choice the script makes is declared in it.

**Why this is here.** Substrate item 6 says every solved item becomes a container, so no one has to re-study it from zero. This record puts a number on "from zero": the audit read 240 canonical items against measurements that took decades and very large sums to produce. Reading them costs almost nothing; reproducing them would cost what is below.

All totals are in **constant 2025 US dollars** (US CPI-U, BLS). Foreign-currency figures are converted at the Federal Reserve annual-average rate for their price year, then inflated.

---

## Level 1 — the facilities whose results the audit read directly

| Facility | Audit used it for | Cost (2025 $) | Source |
| --- | --- | --- | --- |
| International Space Station (US share, to 2014) | Stage 63 (continuous off-planet occupation) | $106.1 B | NASA OIG IG-15-021 |
| Hubble Space Telescope (lifetime) | SH0ES H₀ (Hubble constant, tension) | $19.0 – 22.3 B | NASA; NASA OIG; GAO-05-34 |
| LHC + ATLAS + CMS | Higgs mass (Stage 3) | $6.0 – 18.6 B | CERN (materials, low); Forbes via IBTimes (to Higgs discovery, high; secondary) |
| Human Genome Project | genome / phylogeny dating (Stages 14–31) | $6.4 B | genome.gov |
| Cassini–Huygens | PPN-γ test of general relativity | $4.3 – 5.1 B | NASA; Wikipedia (secondary) |
| Planck (ESA) | H₀, Ω_m, Λ, CMB (constants; Stages 3–6) | $1.5 B | ESA factsheet |
| OSIRIS-REx | Bennu amino acids, nucleobases (Stage 10) | $1.1 – 1.3 B | NASA; Planetary Society |
| RHIC | quark–gluon plasma (Stage 4) | $1.2 – 1.3 B | DOE IG-0543 |
| LIGO | GW170817 neutron-star merger, heavy elements (Stage 8) | $0.77 – 0.96 B | LIGO-G980034; NSF |
| WMAP | CMB (Stages 3–6) | $0.32 B | BBC Sky at Night (secondary; proposed budget, not final cost) |
| Super-Kamiokande | neutrino oscillation, proton-decay limits | $0.15 – 0.24 B | OSTI / CERN Courier 1991; Wikipedia (secondary) |
| DESI | dark-energy evidence (Stages 81–84) | $0.07 – 0.09 B | Berkeley Lab |
| KamLAND | neutrino / lepton-number limits | $0.05 B | Berkeley Lab |
| **Total** | | **$147 – 164 B** | |
| **Total excluding the ISS** | | **$41 – 58 B** | |

The ISS supplied **one fact** to one stage, so the ex-ISS total is the fairer "cost of the audit's evidence". NIST's metrology budget (FY2024: $1.46 B, of which $1.08 B for the measurement labs) sits under every CODATA value and is annual, so it is not summed here.

**Held open:** COBE (only a $30 M approval cap was found, not an actual cost); WMAP's final cost; Borexino and KamLAND-Zen; Virgo construction; CMS alone; Hubble's shuttle-servicing total; the ISS after 2014. The ranges are **lower bounds** in one respect: multi-year nominal totals are inflated from their end year, which understates earlier spending.

## Level 2 — the research enterprise underneath

No facility above stands alone. These are sums of annual spending, inflated year by year to 2025 dollars.

| Series | Years | Total (2025 $) | Source |
| --- | --- | --- | --- |
| World R&D, all kinds (PPP $) | 1996–2023 | **$62.8 T** | UNESCO UIS R&D/GDP × World Bank GDP (PPP) |
| World **basic** research (proxy: US basic-research share) | 1996–2023 | **$10.4 T** | as above × NSF NCSES National Patterns |
| US federal R&D outlays | 1949–2025 | $10.3 T | OMB Historical Tables, Table 9.7 |
| US NIH appropriations | 1996–2025 | $1.3 T | CRS R43341 (secondary, citing NIH Office of Budget) |

These series are **nested** (NIH ⊂ US federal ⊂ world); do not add them.

**Held open:**
- **World R&D before 1996.** No global series was sourced, so the true cumulative total is larger than $62.8 T.
- **A true world basic-research share.** The US share (9–16%) is used as a proxy. The OECD-reporting aggregate is lower, about 12% including China.
- **NIH before 1996.** The NIH, congress.gov and CRS sites blocked retrieval.
- **Which world R&D/GDP ratio is right.** UIS gives 1.92% for 2023 and the World Bank 2.60%; UIS is used.

---

## Level 3 — the knowledge the methodology holds: what it cost to gain, and what it produced

This answers a narrower question than Level 2: **for the 248 items the audit examined** (100 stages, 87 constants and laws, 10 domains, 20 register claims, 17 layer names, 14 further canon items), what research established the knowledge each one rests on, and what did that research cost? Computed by [`knowledge_value.py`](knowledge_value.py) from [`knowledge_map.json`](knowledge_map.json) (item → programs/studies), [`facilities.json`](facilities.json) + [`programs_extra.json`](programs_extra.json) (program costs) and [`unit_costs.json`](unit_costs.json) (cost per paper by field).

### Where each item's knowledge comes from

| Basis | Items | Meaning |
| --- | --- | --- |
| facility | 29 | a large named program (Planck, Hubble, LHC, LIGO …) |
| studies | 83 | ordinary research papers (219 cited in all) |
| reference | 24 | a compilation of many experiments (CODATA, PDG, KEGG) |
| proof | 31 | a mathematical theorem or definition |
| none | 81 | nothing measured: projected stages, framework constructs, stipulations |

### A. Knowledge the methodology **contains**

| Part | Cost (2025 $) |
| --- | --- |
| 24 programs and facilities, each counted once | $158 – 177 B |
| 219 cited studies × field cost per paper | $0.04 – 0.07 B |
| **Total** | **$158 – 177 B** |
| **Total excluding the ISS** (it supplies one fact to one stage) | **$52 – 71 B** |

Largest contributors: ISS $106 B · Hubble $19–22 B · LHC $6–19 B · JWST $11.5 B · Cassini $4–5 B · ALMA $1.8–1.9 B · NIST (one year) $1.1–1.5 B · Planck $1.5 B (relied on by 11 items).

**Read this as a floor, for four reasons:**
1. Compilations (NIST/CODATA, PDG) are counted at one year of budget; the experiments they compile span decades.
2. The item-to-evidence mapping uses the evidence the audit *cited*, which is a sample of each field, not the whole field.
3. A paper's cost excludes the prior work it builds on.
4. Nine programs are held open with no usable cost: Borexino, COBE, KEGG, MEG, MICROSCOPE, NCBI, NICER, UN WUP and Census BFS.

The whole-enterprise context is Level 2 (world R&D ≈ $63 T since 1996).

### B. Knowledge the methodology **produced**

A result counts as produced by the methodology when the methodology stated it **before** it was measured, and a later measurement confirmed it. On that test the confirmed value is **$0 to date**:

- The measured content the methodology holds matches the scientific record because it was recorded from it. The Appendix D constants carry CODATA's own digits.
- v5.4 §7/§11 states **zero novel predictions** beyond the Standard Model and general relativity.
- The one quantitative match, Koide δ = 2/9 at 0.42σ ([`framework/tests/koide-delta.md`](../../framework/tests/koide-delta.md)), is a fit to known lepton masses, not a prior prediction. The test file itself notes Koide's 2/3 is built into the form.
- Where the methodology's principles filled gaps beyond the record, the audit found most of its conflicts (see [`../FINDINGS.md`](../FINDINGS.md) §A–D).

**Where that can change.** These are the methodology's own open tests. A pass on any of them, stated in advance, would be the first produced result:

| Open test | Status | Where |
| --- | --- | --- |
| Lepton masses → neutrino masses from the trefoil form (v5.4 §14.1, second half) | not run | v5.4 §14 |
| Meson 1/3 test | not runnable as written (no observable named) | [`not-runnable.md`](../../framework/tests/not-runnable.md) |
| Lamina falsifier vs nuclear-density data | not decidable as written | [`lamina-falsifier.md`](../../framework/tests/lamina-falsifier.md) |
| Partition = phase ("why three generations") | held open; needs the tension law | v5.4 §14.4 |
| Any operational falsifier for DETECT → PROCESS → RESPOND | none stated | FINDINGS F-042 |

### C. Cost of organizing the knowledge

**Held open — by author decision (2026-09-28).** The author's judgment is that the hours and thought that went into gaining and organizing this knowledge are not meaningfully countable in dollars, and that word counts do not measure them either. The record therefore does not assign this a dollar value. It is not zero and not unknown-but-estimable: it is outside what this cost record measures.

For reference only (size, not cost): canon v5.1–v5.4 is about 58,000 words; maps and guides about 10,000; this audit about 166,000 words across 249 files.

## Caveats (read before quoting)

- **PPP vs market rates.** World R&D is in PPP dollars, about $3.6 T in 2023, against about $2.1 T at market rates. It is deflated with US CPI as an approximation.
- **Scope differs by source.** Construction-only, lifecycle, and "to discovery" figures are not comparable. Each row's scope is in [`facilities.json`](facilities.json).
- **Shared costs.** The ISS, Hubble and the LHC served thousands of results, not just the ones this audit used. Level 1 is the cost of the instruments, not a cost allocated to this audit.
- **Secondary sources** are marked. The LHC's high figure, WMAP, part of Super-Kamiokande and part of Cassini rest on them.

## Files

| File | Contents |
| --- | --- |
| [`facilities.json`](facilities.json) / [`facilities.md`](facilities.md) | 17 facilities: every figure, scope, quote, URL, source type |
| [`rd_series.json`](rd_series.json) / [`rd_series.md`](rd_series.md) | World R&D, basic share, US federal R&D, NIH — with alternates |
| [`cpi_us.json`](cpi_us.json) | US CPI-U annual averages 1913–2025 (BLS API) |
| [`fx.json`](fx.json) | EUR, CHF, JPY → USD annual averages (Federal Reserve H.10 via FRED) |
| [`compute_cost.py`](compute_cost.py) | Levels 1–2; `--json` writes [`results.json`](results.json) |
| [`knowledge_map.json`](knowledge_map.json) / [`.md`](knowledge_map.md) | 248 items → the programs and studies behind them |
| [`programs_extra.json`](programs_extra.json) / [`.md`](programs_extra.md) | 17 further programs, sourced |
| [`unit_costs.json`](unit_costs.json) / [`.md`](unit_costs.md) | Cost per paper / per study by field, sourced |
| [`knowledge_value.py`](knowledge_value.py) | Level 3; `--json` writes [`knowledge_value.json`](knowledge_value.json) |

```bash
python3 audit/cost/compute_cost.py
```
