# Usage Tracking — Who Is Using This, and What

You asked whether there's a way to track **who is using the methodology and what they're using.** Here is the honest answer: **partly, and it depends on how the repo is hosted.** GitHub gives you real but *aggregate* signals automatically; anything tied to a person or naming *which parts* they use has to be **opt-in**. There is no hidden per-reader log — and that's a feature, not a limitation you can engineer around within GitHub.

This page lays out every option, what it can and can't tell you, and what's already wired up in this repo.

---

## Tier 1 — Automatic & free (GitHub native, aggregate only)

Available on any GitHub repo with no setup. **These are counts, not identities.**

| Signal | Where | What it tells you | Limits |
| --- | --- | --- | --- |
| **Traffic: Views & Unique visitors** | Insights → Traffic | How many views / distinct visitors in the **last 14 days** | Rolling 14-day window only; no identities; needs push/admin access to view |
| **Traffic: Clones & Unique cloners** | Insights → Traffic | How often the repo was cloned (incl. by CI/AI tools) | Aggregate counts; 14-day window; no identities |
| **Traffic: Popular content / Referring sites** | Insights → Traffic | Which files are viewed most; where visitors come from | Top 10 only; 14-day window |
| **Stars / Forks / Watchers** | Repo header, Insights | *Named* accounts that starred, forked, or subscribed | Only counts people who chose to click; a proxy for interest, not use |
| **Dependency graph / "Used by"** | Insights → Dependency graph | Public repos that depend on yours | Mostly for code packages; limited value for docs |

**Retention tip:** the 14-day traffic window is the big gap. If you care about long-term trends, snapshot traffic periodically. Options: the GitHub **Traffic API** (`GET /repos/{owner}/{repo}/traffic/views`, `.../clones`, `.../popular/paths`) run on a schedule (e.g. a GitHub Action writing to a data branch), or a third-party "repo analytics" service. This still only ever gives you **aggregate** numbers.

> **Private repos:** traffic insights are limited/unavailable and there are no stars/forks from the public. If the repo is private, Tier 1 mostly goes away and you rely on Tier 2.

---

## Tier 2 — Opt-in identity + "what they use" (wired up in this repo)

This is the only reliable way to learn **who** is using it and **which layers/algorithms**. It works because people *tell you* — so it's accurate and consent-based, but only captures those who opt in.

1. **The Adoption Registry** — [`adoption/registry.md`](../adoption/registry.md). People and orgs add a row (name, how they use it, which parts) via pull request. Every entry is a real, attributable signal.
2. **The "Application / Usage report" issue template** — [`.github/ISSUE_TEMPLATE/application-report.yml`](../.github/ISSUE_TEMPLATE). Lower-friction than a PR; asks which layers/algorithms were used and in what context. Each submission is a tracked, searchable record.
3. **Iteration & variable-evidence issues** — contributions themselves are usage signals: they tell you which parts are being actively worked with.
4. **GitHub Discussions** (enable in repo Settings → Features) — a Q&A / "show your use" space; participation is attributable and searchable.

**To measure "what they use" quantitatively** without waiting for opt-in, combine:
- **Traffic → Popular content** (which files/layers get the most views), plus
- **Search/referrer data** and **issue labels** (label issues by layer, then filter).

---

## Tier 3 — Deeper telemetry (requires hosting the docs yourself)

GitHub will never tell you *which reader* opened *which file*. If you need that granularity, serve the content somewhere you control and add analytics:

| Host | How you'd track use | Gives you |
| --- | --- | --- |
| **GitHub Pages + privacy analytics** (Plausible, Fathom, GoatCounter, or Google Analytics) | Publish `versions/` + `framework/` as a site; analytics script per page | Per-page views, sessions, geography, referrers, trends over time (still not personal identity unless you add auth) |
| **A gated docs portal** (e.g. auth-protected site, or a docs platform with accounts) | Require sign-in to read | *Named* readers + exactly which pages/sections they open |
| **A "framework API" / hosted endpoint** | Serve the methodology (or an AI wrapper) behind API keys | Per-key usage: who called, which layer/algorithm, how often |
| **Versioned/embedded distribution** | Ship the framework inside a product with your own telemetry | Whatever your product measures |

Trade-off: more telemetry = more setup, and (for anything tied to a person) a **privacy/consent obligation**. If you go past aggregate counts, tell users what you collect and why, and keep it lawful (GDPR/CCPA etc. where applicable).

---

## What is **not** possible on GitHub (don't let anyone tell you otherwise)

- You **cannot** see the identity of someone who cloned the repo or viewed a file. Traffic is aggregate by design.
- You **cannot** get a per-user reading history.
- You **cannot** retroactively recover traffic older than the 14-day window if you never snapshotted it.

---

## Recommended setup for this repo

1. **Turn on and check Insights → Traffic** monthly (or snapshot it via the Traffic API on a schedule).
2. **Keep the opt-in paths visible** — the [adoption registry](../adoption/registry.md) and the application-report issue template are already in place; the README links them prominently.
3. **Label issues by layer** so "what's being used" is filterable.
4. **If you want long-term or per-page trends,** publish the docs via GitHub Pages with a privacy-friendly analytics tool (Plausible/Fathom/GoatCounter).
5. **If you ever need named, per-section usage,** move to a gated portal or an API-key'd endpoint (Tier 3) and add a short privacy notice.

> Bottom line: **aggregate interest** is free and automatic; **who + what** is opt-in and already scaffolded here; **per-reader detail** requires hosting you control. Pick the tier that matches how much you need to know versus how much you want to build.
