# Macro cost series: sources, units, coverage, gaps

Retrieved: **2026-09-27**. Every figure in `cpi_us.json`, `fx.json` and `rd_series.json` was fetched during this run from the URL recorded next to it. None was written from memory. Where this run computed a value from fetched series (a product or a ratio), the JSON labels it **DERIVATION**. Money is in full units (dollars, not millions). Shares are fractions (0-1).

Following the Variable Principle, each value is one of three kinds. **Measured** means a published figure. **Derived** means arithmetic on published figures, and it is labelled. **Held open** means it was not obtainable, and the reason is given.

## Files

| File | Content | Coverage | Source |
|---|---|---|---|
| `cpi_us.json` | CPI-U annual averages (CUUR0000SA0, U.S. city average, all items, NSA, 1982-84=100) | 1913-2025, no gaps | BLS Public Data API v2, `annualaverage=true` (the M13 values BLS publishes, not averaged here) |
| `fx.json` | EURUSD, CHFUSD, JPYUSD annual averages, **USD per 1 unit of foreign currency** | EUR 1999-2025; CHF and JPY 1985-2025 | Federal Reserve H.10 annual series via FRED (AEXUSEU, AEXSZUS, AEXJPUS). CHF and JPY are inverted from FRED's foreign-per-USD. Raw values are kept. Checked against daily DEX* means (they match to 4 decimals). |
| `rd_series.json` → `global_gerd` | World GERD, current international $ (PPP) | 1996-2023 | DERIVATION: UNESCO UIS `EXPGDP.TOT` (SDG: World) × World Bank `NY.GDP.MKTP.PP.CD` |
| `rd_series.json` → `basic_share` | US basic research / total US R&D | 1953-2024 | DERIVATION (ratio): NSF NCSES National Patterns (NSF 26-313), Tables 7 / 6 |
| `rd_series.json` → `us_federal_rd` | Federal outlays for the conduct of R&D, current $ | FY1949-FY2025 actuals | OMB Historical Tables, Table 9.7 (FY2027 budget) |
| `rd_series.json` → `nih_appropriations` | NIH program level, current $ | FY1996-FY2026 | CRS R43341 (updated 2026-05-18), Table 3, via everycrsreport.com mirror. This is a **secondary** source. |

### Alternates in `rd_series.json`

- **global_gerd**
  - UIS share × GDP PPP in constant 2021 int'l $.
  - UIS share × GDP at market exchange rates (current US$).
  - World Bank share (`GB.XPD.RSDV.GD.ZS`) × market GDP.
  - OECD MSTI GERD, OECD total, current and constant-2020 PPP, 1991-2024.
  - OECD MSTI US GERD, 1981-2024.
- **basic_share**
  - US share from OECD MSTI (G_BR / G), 1981-2024.
  - A PPP-weighted aggregate over the OECD-MSTI countries that report basic research. The country list is included for each year.
- **us_federal_rd**
  - OMB figures in constant FY2017 dollars.
  - OMB estimates for FY2026-27, plus the 1976 transition quarter.
  - NCSES federally funded R&D, current and constant-2017 dollars, 1953-2024.
  - NCSES federally funded basic research.
  - NCSES total US R&D and total US basic research, current dollars.
- **nih_appropriations**
  - CRS constant-FY2024 dollars (deflated by the Biomedical R&D Price Index, BRDPI).

## Held open

1. **World R&D spending before 1996.** UIS and the World Bank both start in 1996. OECD MSTI starts in 1991 (OECD members only) and 1981 (US). No world series for 1913-1995 was fetched.
2. **World basic-research share.** The UIS public API has no basic-research indicator. OECD MSTI publishes no OECD-total or world aggregate for basic research. The nearest proxies fetched are the US share and the reporting-country aggregate. Neither is a world figure.
3. **Which world R&D/GDP ratio is correct.** The UIS SDG world figure (2023: 1.92%) and the World Bank world figure (2023: 2.60%) differ by 0.5-0.7 percentage points in every year. The World Bank aggregate covers reporting economies only, and its weighting was not verified. The primary series uses UIS, the official SDG 9.5.1 custodian. Treat the World Bank-based alternate as an upper bracket.
4. **NIH appropriations FY1938-FY1995.** Four sources were tried and all failed:
   - NIH Office of Budget: HTTP 403 (Cloudflare).
   - nih.gov almanac: HTTP 403.
   - congress.gov and crsreports.congress.gov: HTTP 403.
   - Wayback Machine: connection reset.

   The primary NIH table was therefore not fetched either. FY1996+ comes from CRS, which cites it.
5. **EURUSD before 1999.** The euro did not exist. Pre-1999 EUR amounts need legacy-currency conversion (DEM, FRF, ECU), which was not collected.
6. **AAAS historical R&D tables.** HTTP 403. OMB and NCSES were used instead.
7. **BLS flat file** (`download.bls.gov`). HTTP 403. The API was used, so nothing is lost.

## Caveats for anyone summing these

- **PPP vs market exchange rates.** The 2023 world GERD figure is about $3.63T in PPP int'l $ but about $2.07T at market rates. PPP inflates low-price economies, especially China. Choose one basis and do not mix it with USD project costs converted at market FX (`fx.json` is market-rate).
- **Current vs constant.** The primary values in every series are nominal. Deflating with CPI-U (`cpi_us.json`) is a consumer-price deflator. NCSES uses the GDP deflator (2017 = 100), OMB uses its own FY2017 deflator, and NIH/CRS uses BRDPI. These do not agree with each other.
- **Fiscal year vs calendar year.** OMB and NIH use US federal fiscal years (Oct-Sep). NCSES uses calendar-year approximations. UIS, the World Bank and OECD use calendar or national reporting years.
- **Series breaks.**
  - OMB defense R&D was redefined in 2017 ($24.5B of outlays reclassified), so defense R&D before and after 2017 is not comparable.
  - NCSES marks 2023 as partly preliminary and 2024 as estimates.
  - OECD flags OECD-total GERD as E (estimated) and US GERD as D (definition differs).
  - The 2025 CPI-U annual average is BLS-published, although BLS marks October 2025 as unavailable (the 2025 lapse in appropriations). How BLS formed the average was not verified.
- **Scope.**
  - GERD is all R&D: business, government, universities and non-profits, including experimental development. Only a fraction is basic research: 8.9% (1953) to 15.7% (2000) of US R&D, and 14.6% in 2024.
  - The reporting-country aggregate is lower once China is included.
  - OMB "conduct of R&D" excludes R&D facilities and equipment.
  - NIH program level excludes emergency supplementals (ARRA 2009, COVID-19).
- **Overlap.** NIH is part of US federal R&D. US federal R&D is part of US GERD. US GERD is part of world GERD. Do not add these series together.
