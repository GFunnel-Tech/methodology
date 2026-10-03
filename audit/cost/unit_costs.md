# Unit costs of ordinary research: grants, papers, studies

> **Status: sourced inputs plus one labelled derivation. Not canon.** This record prices "one primary study", the ordinary lab paper or field study that sits under parts of the methodology. Every figure below came from a page fetched on **2026-09-27** (curl or WebFetch). None comes from memory. Where no figure could be fetched, the item is **held open** (Variable Principle).

Machine-readable version: [`unit_costs.json`](unit_costs.json) (83 entries). Each entry has `source_url`, `source_type`, `retrieved`, a verbatim `quote` of 25 words or fewer (`…` marks an elision), `price_year` and a `note`. CPI for inflating to 2025 dollars is [`cpi_us.json`](cpi_us.json); EUR→USD rates are in [`fx.json`](fx.json).

**Price years.** A `price_year` is recorded only where the source states the year or the series is annual nominal (the fiscal or calendar year of the figure). Where the source gives no year it is `null`, and any 2025-dollar value shown is a **range across the possible years**, not a point value.

---

## 1. Source figures

### Grant sizes and durations

| id | What | Amount | Price year | Per | Source (type) |
|---|---|---|---|---|---|
| nih_r01eq_avg_fy2024 | NIH R01-equivalent average award size (total cost) | $606,393 | FY2024 | award-year | [NIH Data Book, rpt 158](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=158) (primary) |
| nih_r01eq_avg_fy2021 | same, FY2021 | $571,561 | FY2021 | award-year | NIH Data Book (primary) |
| nih_r01eq_avg_fy2025 | same, FY2025 (**inflated by forward funding**; NIH says so) | $664,005 | FY2025 | award-year | [NIH Extramural Nexus, Mar 2026](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/03/fiscal-year-2025-by-the-numbers-extramural-grant-investments-in-research) (primary) |
| nih_rpg_avg_fy2024 | NIH research project grants (all RPGs), average size | $620,233 | FY2024 | award-year | NIH Data Book, rpt 155 (primary) |
| nih_r01eq_mean_total_fy2021_lauer | R01-equivalent mean **total** cost (confirms Data Book is direct + indirect) | $560,000 | 2021 | award-year | [Lauer et al., eLife 2023](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9984192/fullTextXML) (primary) |
| nih_r01eq_mean_direct_fy2021_lauer | R01-equivalent mean **direct** cost | $390,000 | 2021 | award-year | Lauer et al. 2023 (primary) |
| nih_r01_budget_periods | R01 duration | 1–5 twelve-month budget periods | — | award | [NIH R01 activity code page](https://grants.nih.gov/funding/activity-codes/R01) (primary) |
| nsf_mean_annualized_fy2023 | NSF mean annualized award per research project | $211,000 | FY2023 | award-year | [NSF FY2023 Merit Review Digest](https://nsf-gov-resources.nsf.gov/files/FY-2023-MeritReviewDigest.pdf), Table 19 (primary) |
| nsf_median_annualized_fy2023 | NSF median annualized award | $154,000 | FY2023 | award-year | same (primary) |
| nsf_mean_duration_fy2023 | NSF mean research award duration | 3.1 years | — | award | same, Table 21 (primary) |

**NSF by directorate, FY2023** (Table 20; annualized award per research project; nominal dollars):

| Directorate | Field | Mean | Median |
|---|---|---|---|
| BIO | biology | $288,000 | $234,000 |
| CISE | computer and information science | $238,000 | $200,000 |
| EDU | STEM education | $274,000 | $180,000 |
| ENG | engineering | $174,000 | $136,000 |
| GEO | geosciences | $236,000 | $186,000 |
| MPS | mathematical and physical sciences (incl. astronomy, physics, chemistry) | $170,000 | $136,000 |
| SBE | social, behavioral and economic sciences (incl. psychology) | $174,000 | $145,000 |

### Papers per grant and cost per paper

| id | What | Amount | Price year | Per | Source (type) |
|---|---|---|---|---|---|
| berg_nigms_median_direct_fy2006 | NIGMS R01/P01 investigators, median annual **direct** cost | $220,000 | FY2006 | investigator-year | [Berg, NIGMS Feedback Loop 2010](https://nigms.nih.gov/loop/2010/09/measuring-the-scientific-output-and-impact-of-nigms-grants) (primary) |
| berg_nigms_median_pubs | same investigators, median grant-linked papers, 2007 to mid-2010 | 6 | — | investigator (about 3.5 years) | same (primary) |
| riley_mean_pubs_per_r01 | NIH R01 and U01 grants (2008–2014), mean papers within 60 months | 17 | — | grant | [Riley et al., PLoS ONE 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7665634/fullTextXML) (primary) |
| riley_typical_r01_investment | "typical $3 to $4 million investment" per R01 or U01 (an authors' remark in the published peer-review response) | $3–4 M | not stated | grant | same (primary, informal) |
| sfi_cost_per_publication | Science Foundation Ireland Investigator Awards: average cost of an original research paper (**upper bound**) | €65,000 | not stated (awards 2012–16) | paper | [Ó Colgáin, arXiv:2602.05836](https://arxiv.org/pdf/2602.05836) (secondary: preprint) |
| sfi_avg_award | SFI average award budget | €1.42 M | not stated | award | same (secondary) |

### Field-specific cost per study or per paper

| id | What | Amount | Price year | Per | Source (type) |
|---|---|---|---|---|---|
| moore_pivotal_trial_median | Pivotal efficacy trials for 59 FDA-approved drugs (2015–16), median (IQR $12.2–33.1 M) | $19.0 M | not stated (≈2015–17) | trial | [Moore et al., JAMA Intern Med 2018 (PubMed)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30264133,33031559,32114790&rettype=abstract&retmode=text) (primary) |
| hsiue_oncology_pivotal_median | Oncology pivotal trials (2015–17), median | $31.7 M | not stated | trial | Hsiue, Moore, Alexander, Clin Trials 2020 (primary) |
| moore_biosimilar_trial_median | Biosimilar comparative-efficacy trials (2010–19), median | $20.8 M | not stated | trial | Moore et al., JAMA Intern Med 2021 (primary) |
| rpcb_cost_per_replication | Reproducibility Project: Cancer Biology, actual mean cost per replication study (median $53,089); **excludes admin and personnel** | $52,574 | not stated (≈2013–20) | study | [Errington et al., eLife 2021](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8651289/fullTextXML) (primary) |
| hubble_lifetime_cost | Hubble mission cost since 1977, excluding shuttle | $16 B | 2021 | facility | [NASA Hubble FAQ](https://science.nasa.gov/mission/hubble/overview/faqs/) (primary) |
| hubble_papers | Peer-reviewed papers using Hubble data | 23,000 | — | facility | [NASA Hubble by the numbers](https://science.nasa.gov/mission/hubble/overview/hubble-by-the-numbers/) (primary) |
| cms_papers_2020 | CMS (LHC) peer-reviewed papers, cumulative to Nov 2020 | 1,000 | — | experiment | [CMS news](https://cms.cern/news/cms-collaboration-publishes-its-1000th-paper) (primary) |

### National macro inputs: US academic R&D and US papers, by field

The R&D figures are academic R&D spending from all funding sources, nominal. They come from the NSB *Indicators 2025* Discovery report, Figure DISC-13 (HERD survey), [fetched page](https://ncses.nsf.gov/pubs/nsb20257/table/DISC-6). The paper counts are US S&E articles in Scopus, fractional count, **all US sectors**. They come from NSB-2023-33, supplemental tables SPBS-3 to SPBS-16 ([zip](https://ncses.nsf.gov/pubs/nsb202333/assets/nsb202333-supplemental-materials.zip)). All are primary sources.

| HERD field | Matched Scopus fields | R&D FY2018 | R&D FY2023 | Papers 2018 | Papers 2022 |
|---|---|---|---|---|---|
| Life sciences | agricultural + biological/biomedical + health + natural resources | $45.6 B | $62.2 B | 223,356 | 247,772 |
| Engineering | engineering + materials science | $12.4 B | $17.5 B | 64,158 | 54,745 |
| Physical sciences | astronomy + chemistry + physics | $5.2 B | $6.9 B | 48,489 | 40,966 |
| Geo/atmos/ocean sciences | geosciences | $3.2 B | $4.0 B | 16,601 | 12,555 |
| Computer and information sciences | same | $2.4 B | $3.6 B | 34,718 | 33,405 |
| Social sciences | same | $2.7 B | $3.6 B | 33,583 | 38,861 |
| Psychology | same | $1.3 B | $1.6 B | 17,195 | 19,152 |
| Mathematics and statistics | same | $0.8 B | $1.1 B | 9,065 | 9,879 |

The field mapping (which Scopus fields go under which HERD field) is **my choice, not the sources'**. It is part of the derivation below.

---

## 2. Proposed method: cost per primary study, by field — **DERIVATION**

> This section is a **derivation**, not a sourced figure and not a primary algorithm. It combines the sourced inputs above with arithmetic stated in full. Values in 2025 dollars use `cpi_us.json` (CPI-U, 2025 = 321.943).

**Step 0: the quantity actually measured is cost per paper, not cost per study.**
No fetched source gives the number of papers per "primary study". So:

> **cost per study = cost per paper × k**, where **k (papers per study) is held open**.

Every number below is a cost per paper, except Route C, which measures cost per study directly. Treating one paper as one study (k = 1) is a choice the user would have to make; this record does not make it.

### Route A: top-down, by field (US academic R&D ÷ US papers)

The arithmetic is: cost per paper(field) = academic R&D(field, FY) ÷ US articles(field, year).

- The **matched-year** version divides FY2018 R&D by 2018 papers.
- The **recent** version divides FY2023 R&D by 2022 papers. The years are mismatched by one because DISC-13 has no FY2022 column.

| Field | FY2018 ÷ 2018 (nominal) | 2025 $ | FY2023 ÷ 2022 (nominal) | 2025 $ |
|---|---|---|---|---|
| Life sciences (biomedical, health, agriculture) | $204,000 | **$262,000** | $251,000 | **$265,000** |
| Engineering | $193,000 | $248,000 | $320,000 | $338,000 |
| Physical sciences (physics, chemistry, astronomy) | $107,000 | $137,000 | $168,000 | $178,000 |
| Geosciences | $193,000 | $247,000 | $319,000 | $337,000 |
| Computer and information sciences | $69,000 | $89,000 | $108,000 | $114,000 |
| Social sciences | $80,000 | $103,000 | $93,000 | $98,000 |
| Psychology | $76,000 | $97,000 | $84,000 | $88,000 |
| Mathematics and statistics | $88,000 | $113,000 | $111,000 | $118,000 |
| **All mapped S&E fields** | $165,000 | **$211,000** | $220,000 | **$232,000** |

Known biases, all of which are open:

- **The numerator is academic R&D only; the denominator counts papers from all US sectors.** This pushes the result low. The academic share of US papers was not fetched.
- **R&D also produces outputs other than papers** (training, patents, data). This pushes the result high.
- **There is a publication lag.** No lag is applied.
- **Paper counts moved between vintages.** Engineering, physics and geosciences counts fell 2018→2022; NSB-2023-33 notes filtering of low-quality Scopus sources. This is why those fields' ratios jump between the two columns.
- **It excludes non-academic performers** (industry, federal labs), and so excludes most of the cost of big-facility physics.

### Route B: bottom-up, from grants (biomedical, all fields)

| Derivation | Arithmetic | Nominal | 2025 $ |
|---|---|---|---|
| B1: NIH, stated project cost ÷ papers | $3–4 M (Riley authors' remark) ÷ 17 papers per grant | $176,000–$235,000 | $240,000–$352,000 (price year unknown, 2008–2014 bounds) |
| B2: NIH, Data Book × assumed 5 years ÷ papers | $571,561 (FY2021) × 5 ÷ 17 | $168,000 | $200,000 |
| B3: NIGMS, direct-cost basis | $220,000 × 3.5 years ÷ 6 papers = $128,000 direct; × (0.56/0.39) total/direct ratio from Lauer FY2021 | $184,000 | $294,000 (FY2006 base) |
| B4: Ireland, all fields (upper bound) | €65,000 × EURUSD (2012 to 2016) | $72,000–$86,000 | $97,000–$118,000 |

Caveats for Route B:

- **B2's "5 years" is the maximum** of the stated 1–5 budget periods. The mean realised R01 length is held open, so B2 is an upper-end choice.
- **B3 divides medians,** which does not give a median cost per paper. It also treats the 3.5-year publication window as 3.5 years of funding.
- **Riley counts a paper once for each grant it cites,** which pushes per-grant paper counts high and cost per paper low.

**Convergence.** The two independent NIH routes (B1–B3: $200,000–$352,000) and the macro life-sciences figure (Route A: $262,000–$265,000) overlap. For **biomedical lab research, cost per paper ≈ $0.2–0.35 M (2025 $)**.

**NSF fields have no bottom-up figure.** An NSF award costs about $654,000 nominal ($211,000 × 3.1 years; $691,000 in 2025 $). By directorate it runs from $527,000 (MPS) to $893,000 (BIO) nominal. Papers per NSF award were **not found**, so NSF cost per paper stays open. Route A is the only field-resolved number for NSF-type fields.

### Route C: direct cost per study (where studies are priced as studies)

| Field | Figure | 2025 $ (range over the unstated price year) |
|---|---|---|
| Clinical: pivotal drug-efficacy trial (industry) | median $19.0 M | ≈ $25.0–25.5 M (2016–2017 base) |
| Clinical: oncology pivotal trial | median $31.7 M | ≈ $40.6–41.6 M (2017–2018 base) |
| Preclinical cancer biology: one lab experiment, replicated from a known protocol | mean $52,574 | ≈ $65,000–71,000 (2016–2020 base). This is a **floor**: it has no personnel, admin or discovery costs. |
| Astronomy: facility cost per Hubble paper | $16 B (2021 $) ÷ 23,000 | ≈ $827,000. **Facility only, not the scientists' grants.** The cost window ends in 2021; the paper count runs later. |

### Proposed per-field reading (derivation summary, 2025 $, per paper; × k for a study)

| Field | Proposed central range | Built from |
|---|---|---|
| Biomedical / life-science lab study | $0.20–0.35 M per paper | A + B1–B3 (converge) |
| Clinical efficacy trial (industry pivotal) | $19–32 M **per trial** (nominal); ≈ $25–42 M (2025 $) | C (a per-study figure; k does not apply) |
| Physical sciences, small-lab (university) | $0.14–0.18 M per paper | A only |
| Astronomy using a flagship facility | ≳ $0.83 M per paper (facility share alone) | C (Hubble) |
| Engineering | $0.25–0.34 M per paper | A only (unstable across vintages) |
| Geosciences / field science | $0.25–0.34 M per paper | A only (unstable across vintages) |
| Computer science, mathematics | $0.09–0.12 M per paper | A only |
| Social sciences, psychology | $0.09–0.10 M per paper | A only |
| All fields, generic | $0.21–0.23 M per paper (A); $0.10–0.12 M (Ireland B4 upper bound) | A, B4 |

---

## 3. Held open

- **k, papers per primary study.** Not sourced. It governs every conversion from paper to study.
- **Mean realised NIH R01 duration.** Only the 1–5 budget-period rule was fetched.
- **Papers per NSF award,** by directorate or overall. Not found, so NSF bottom-up cost per paper is open.
- **Academic share of US papers.** Not fetched; it would correct Route A's sector mismatch.
- **Particle physics cost per paper.** The CMS paper count (1,000 by 2020) was fetched, but CMS detector cost alone is open (see `facilities.md`), and allocating LHC cost across ATLAS, CMS, LHCb and ALICE is unsourced. No figure is given.
- **Psychology per-study cost** (for example, cost per experiment or per participant) from a primary source. Only the Route A macro figure exists. Commercial blog figures surfaced by search were not used.
- **Price years** of Moore/Hsiue ($ "unadjusted current dollars" from contracts "from the previous 2 years"), Errington (RPCB), Riley's $3–4 M remark, and SFI's €65k. These are shown as ranges.
- **Clinical trials outside industry pivotal trials** (for example, NIH-funded academic trials). Not sourced.
- **Cost-per-paper studies from other bibliometric sources.** The NIH intramural-vs-extramural comparison (eLife, [PMC13349378](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13349378/fullTextXML)) reports cost-efficiency only in figures. Its fetched text gave no dollars-per-paper number, so it is not recorded. Mongeon et al. (arXiv:1602.07396) was fetched and gives no dollar-per-paper figure.
- **Direct fetch failures.** `pmc.ncbi.nlm.nih.gov` returned a reCAPTCHA page, so articles were read through Europe PMC instead. `loop.nigms.nih.gov` returned a proxy 502, so the nigms.nih.gov mirror was used. The eLife site returned 406, so Europe PMC was used.

---

Source framework context: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. This file is an audit input, not part of the canonical text.
