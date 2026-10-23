# Articles — turning the methodology into content a business can run

> **Status: operations tooling, not canon.** Nothing in this directory adds to the
> framework. It is the pipeline that turns the canon's algorithms into articles, one
> algorithm per article, through an AI video-to-article tool, with the canon's own rules
> carried into that tool and a human approval before anything publishes.

**Mode: Contribute** (this is tooling), built on the canon's Layer IV. The Five Modes of
Propagation (v5.1, "How Processes Outlast the Vessel") name **Documentation** as the third
mode: "encode the process into text, video, or structured media." An article that says
*here is the algorithm, here is how to run it in your business* is that mode applied to the
methodology itself, so this pipeline is one of the framework's own prescribed outputs, not
a marketing layer beside it.

## The pipeline

```
   a video that teaches one algorithm
            │
            ▼
   canon_pack.py "<algorithm>"  ──►  SOURCE BLOCK   (the steps, verbatim, with the credit line)
            │                              │
            ▼                              ▼
   Video to Blog  ◄── prompt (videotoblog-prompt.md §A) + SOURCE BLOCK + footer (§C)
            │
            ▼
   a DRAFT in the shape of article-template.md
            │
            ▼
   a person checks it against the checklist below      ◄── nothing skips this
            │
            ▼
   published to the platform's library (/resources), its search feed, and wherever else
   the platform's articles pipeline carries it
```

Three files do the work:

| File | What it is |
| --- | --- |
| [`videotoblog-prompt.md`](videotoblog-prompt.md) | The prompt (full and short), the footer, and the per-video addendum. Paste once; add the SOURCE BLOCK per video. |
| [`article-template.md`](article-template.md) | The shape every draft must come out in, and why each part is there. The editor's reference. |
| [`catalogue.md`](catalogue.md) | Every algorithm the canon carries (77 in v5.1), with its "Use when" line and canon lines. One row is one article. Generated. |

And one tool, [`../../tools/canon_pack.py`](../../tools/canon_pack.py):

```bash
python3 tools/canon_pack.py --list                 # the 77 algorithms, with "Use when" and step counts
python3 tools/canon_pack.py "Shepherd"             # the SOURCE BLOCK to paste under the prompt
python3 tools/canon_pack.py "Five Modes"           # any canon section, not only algorithms
python3 tools/canon_pack.py --catalogue            # regenerate catalogue.md
python3 tools/canon_pack.py --selftest
```

## Two kinds of video, one SOURCE BLOCK

The block is never optional, and it means a different thing depending on who is speaking:

| The speaker is… | The SOURCE BLOCK is… | The article… |
| --- | --- | --- |
| Cameron, teaching an algorithm | the algorithm taught | reproduces it and shows how to run it |
| anyone else (GaryVee, a podcast guest, a conference talk) | the **lens**: the algorithm their advice corresponds to | teaches the algorithm, with the speaker's material as the worked example, each match labelled "Correspondence (this article's reading)" |

The second kind is how the methodology "pulls" tactics out of content it did not produce:
the canon supplies the structure and the steps, the speaker supplies the examples, the
stories and the numbers, and the article says plainly which is which. Without a block the
prompt refuses to write the article and instead names the two or three algorithms the video
most corresponds to, so the operator can paste the right one and run again.

### Picking the lens

One judgement per video. Start from what the speaker is really advising, not the title.

| The speaker is advising… | Paste |
| --- | --- |
| what business, product or niche to build; "follow your passion", "your niche is you" | `canon_pack.py "Co-Creator Identity"` |
| documenting, posting, showing the work, building an audience | `canon_pack.py "Five Modes"` (a section, not an algorithm) or `"ACE System"` for the acquisition half |
| how to build, fix or systemise a process, an onboarding, an SOP | `canon_pack.py "Shepherd"` |
| sales conversations, closing, objections, referrals | `canon_pack.py "ACE System"` or `"Sales Algorithm"` |
| hiring, firing, delegating | `canon_pack.py "Hiring"` |
| burnout, overwork, or stalling and not shipping | `canon_pack.py "Dynamic Middle"` |
| a failure, a pivot, a loss | `canon_pack.py "Slime Mold"` |
| planning, goals, strategy | `canon_pack.py "Strategic Planning"` |
| money, pricing, investing | `canon_pack.py "Financial Decisions"` |
| brand, positioning, reputation | `canon_pack.py "Brand and Identity"` |
| "is this business healthy" | `canon_pack.py "Garlick Equilibrium"` |
| anything else | `canon_pack.py --list`, or run the video with no block and read the prompt's candidate paragraph |

A video that genuinely spans two algorithms gets two articles, not one with two blocks.

## Why the generator is handed the text and not trusted to know it

An article that teaches an algorithm must carry the steps **verbatim, in order**. That is the
canon's own run rule (AGENTS.md rule 3: "the sequence is load-bearing") and it is what makes
the credit line true. A language model writing from a transcript, or from what it remembers
of the framework, will paraphrase a step, merge two, drop one or add a plausible eighth. So
the SOURCE BLOCK is pasted as data and the prompt's first rule is *copy, never recall*.
The same reasoning puts the applications behind the words "Applied, not canon" and puts
every number behind "the speaker said": the generator cannot be prevented from inventing,
so it is told exactly where invention is allowed (the applications) and where it is not
(the steps, the figures, the promises).

## The editor's checklist (the approval gate)

A draft publishes only when every line is true. One failure sends it back to the tool or to
a person, never through.

- [ ] **Steps match the SOURCE BLOCK character for character**, same count, same order.
      Open the block beside the draft; do not trust the draft's own "verbatim".
- [ ] **Every number is in the transcript and attributed.** Search the draft for digits
      and the `%` and `$` signs; each one has a "Cameron says" or equivalent, or it goes.
- [ ] **No banned word**: guaranteed, proven, unlock, supercharge, game-changer, skyrocket,
      10x, secret, hack.
- [ ] **Each applied section opens with "Applied, not canon:"** and the "What the
      methodology says" section contains nothing but the canon.
- [ ] **"Not covered in this video" appears where the video did not cover it**, instead
      of a filled-in answer. If the three scenarios are all fluent and the video covered
      one, two were invented.
- [ ] **The falsifier is present** and is an observation, not a feeling.
- [ ] **The credit line is present and unaltered**, with the right version number, and the
      "not endorsed by the author" sentence follows it.
- [ ] **Title ≤ 70 characters, meta ≤ 155, 1,500 to 2,500 words**, H2 sections in the
      template's order.
- [ ] **The video link is right** and the article names the algorithm the video actually
      teaches (the generator will happily write the Sales Algorithm over a Shepherd's Way
      transcript if the wrong block was pasted).

## What the first run showed (2026-10-23)

The prompt was run once, before the lens mode existed, on an outside speaker's video
(GaryVee, "How I'd Grow a Business With $0 in 2026") with **no SOURCE BLOCK**. Measured on
the draft: 2,210 words (inside the 1,500–2,500 range), zero banned words, all five dollar
figures attributed to the speaker and marked hypothetical or anecdotal, "Not covered in this
video" used for operations, the falsifier marked as the article's own, the credit line
honestly reported absent. **The five rules held.** What failed was the design: with no
block the writer took the fallback "steps as given in the video" and presented three of
the speaker's sentences as a numbered algorithm, so the article taught GaryVee and the
methodology appeared only as the three-beat vocabulary. That fallback is removed; the
no-block output is now a candidate paragraph, and the lens mode above is what that video
needed (Co-Creator Identity, with the Five Modes close behind). H-2 is still open: no
block has yet been run through, so the verbatim-steps behaviour is unmeasured.

## What this pipeline does not do, on purpose

- **It publishes nothing by itself.** The draft is the tool's output; the gate is a person.
- **It invents no article.** Every article maps to a row in `catalogue.md`, which is
  generated from the canon; there is no article about a thing the methodology does not say.
- **It records no outcome.** Whether a reader ran the tactic and what happened is not
  measured here or anywhere on the platform yet. Articles therefore promise nothing.
- **It does not decide where drafts live** (Supabase, the platform's `bx_posts`, or a
  file). That is the platform's articles spec's open question and is held open there.

## Held open

| # | Variable | Best value now | What closes it |
| --- | --- | --- | --- |
| H-1 | How many characters Video to Blog's custom-instructions field accepts | `estimate`: 2,000–10,000 characters. Prior: the vendor documents the feature and a 3,000-word post cap and states no instruction limit; analogue: comparable AI writing tools cap free-text instructions in that band. Section A is 10,626 characters and section B is 2,427 (`measured`), so A sits at the top of the range and B inside it. The first run accepted the 7,058-character version uncut (`measured`), which raises the floor to 7,058. Falsifier: paste the new A once; if it is cut, the limit is between 7,058 and 10,626 and B is the prompt. | One paste |
| H-2 | Whether a first draft keeps the steps verbatim without editing | `assumption`: it will on most runs and fail on some, because the prompt makes copying the only allowed path and a model still paraphrases under length pressure. Falsifier: three drafts checked line by line against their SOURCE BLOCKs; one mismatch means the editor's first checklist item stays load-bearing, zero in three means it can be sampled. | The first three drafts |
| H-3 | Where a draft is stored and approved on the platform | Not a quantity. The platform's `docs/supabase-articles-filter-spec.md` holds it open (I-1, I-7). | The owner's decision there |
| H-4 | Whether readers act on an article, and what happens when they do | Not a quantity yet; nothing measures it, so every article promises nothing. | A follow-up mechanism the platform does not have |

Attribution for anything this directory produces: `../../AGENTS.md` → Attribution, and
[`../../ATTRIBUTION.md`](../../ATTRIBUTION.md).
