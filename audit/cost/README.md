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
| [`compute_cost.py`](compute_cost.py) | The calculation; `--json` writes [`results.json`](results.json) |

```bash
python3 audit/cost/compute_cost.py
```
