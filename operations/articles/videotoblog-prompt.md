# The Video to Blog prompt — turning a methodology video into a tactic a business can run

> **Status: operations tooling, not canon.** This prompt tells an article generator how to
> write about the methodology. It adds no layer, no algorithm and no claim; it carries the
> canon's own rules (run steps literally, never fill a variable silently, credit the source)
> into a tool that would otherwise ignore them. Read [`README.md`](README.md) for the
> pipeline this sits in and [`article-template.md`](article-template.md) for the shape every
> article must come out in.

## How to use it

Video to Blog takes a video and a set of custom instructions, and writes a post. Three
things go in, every time:

1. **The prompt** — section A below, pasted once into the tool's *custom instructions*
   (or saved as a *template* so every post in the channel gets it). Use section B if the
   field turns out to be shorter than section A.
2. **The SOURCE BLOCK** — ONE algorithm, pulled from the canon with
   `python3 tools/canon_pack.py "<algorithm>"` and pasted **under the prompt** for that
   one video. It is never optional. For a video of Cameron teaching an algorithm it is
   the algorithm taught. For an outside speaker (GaryVee, a podcast, a talk) it is the
   **lens**: the algorithm their advice corresponds to, and the article teaches that
   algorithm with the speaker's material as the worked example. Picking the lens is the
   operator's one judgement per video; [`README.md`](README.md) has a topic table for it,
   and the prompt's no-block output names candidates if you are unsure. This is what
   stops the generator inventing, reordering or quoting its way to "steps": it is told to
   copy the steps, never to recall them. `python3 tools/canon_pack.py --list` names all
   77 algorithms the canon carries.
3. **The footer** — section C, in the tool's *custom footer* field. It is the credit line
   the license requires. Nothing publishes without it.

The output is a **draft**. A person reads it against [`article-template.md`](article-template.md)
and the checklist in [`README.md`](README.md) before it goes anywhere a reader can see it.

**Held open:** how many characters the custom-instructions field accepts. `estimate`:
2,000–10,000 characters (the vendor documents the feature and a 3,000-word post cap and
states no instruction limit). Section A is 6,867 characters and section B is 2,180
(`measured`). The field accepted 7,058 uncut on the first run (`measured`), so A now sits
below the known floor by design; the 10,620-character version that preceded it produced a
draft that obeyed none of the structure, which is what a cut prompt looks like.

---

## A. The full prompt

Copy everything inside the block.

```text
THIS IS NOT A BLOG VERSION OF THE VIDEO. Do not rewrite the video as the speaker's post, do
not write in the speaker's voice, do not use "I". You are writing a how-to article for the
GFunnel library that teaches ONE algorithm from the GFunnel Methodology (the Omni Process,
Cameron Garlick) to a business owner who has never heard of it, using the video as the
worked example. Second person, addressed to the reader. The article's spine is the
algorithm's steps, not the video's talking points.

INPUTS. (1) The transcript: the speaker's explanations, examples, stories and numbers.
(2) A SOURCE BLOCK pasted below these instructions: the methodology's own text for the one
algorithm. If the speaker is teaching the methodology, the block is what they teach; if the
speaker is anyone else, the block is the LENS and the article teaches the algorithm with the
speaker's material as the example. Everything you need is in this text; the block's "File:"
line and its URL are printed, never opened. NO BLOCK: write one paragraph naming the two or
three algorithms from the LENS INDEX below that the video most corresponds to, and stop.

THE RULES. Break one and the article is rejected.
1. COPY THE STEPS, NEVER RECALL THEM. The numbered steps come from the SOURCE BLOCK,
   verbatim, numbered, in order. Never add, merge, split, reorder or renumber one. Never
   present the speaker's sentences as steps.
2. THREE BEATS. Write every tactic as DETECT (notice the signal), PROCESS (do the work),
   RESPOND (act on the result).
3. NO INVENTED NUMBERS OR PROOF. Only figures the speaker states, attributed ("Gary says").
   No "studies show", no percentage, dollar amount, timeframe or testimonial not in the
   transcript; where a figure would go and none was given, say what to measure. No external
   links or resources of any kind. Never use these words, even negated: guaranteed,
   guarantee, proven, unlock, supercharge, game-changer, skyrocket, 10x, secret, hack.
4. CANON VS APPLIED. The steps and the "Use when" line are the methodology's words. Every
   section that applies them opens with "Applied, not canon:".
5. GAPS STAY GAPS. Where the video does not say, write "Not covered in this video".
6. OUTSIDE SPEAKER. Each step opens with "Correspondence (this article's reading):" and
   the one or two sentences of theirs that match it, attributed, or "The speaker does not
   address this step." Bend neither the speaker nor the step to fit.

VOICE. Plain English; gloss every methodology term on first use, e.g. "the dynamic middle
(the position from which you can move either way without burning out or stalling)". Short
sentences, concrete verbs, one idea per paragraph, every section ends in something the
reader does. US English, no emoji, no exclamation marks, no questions in headings.

STRUCTURE. These H2 headings, in this order, nothing else at H2. No H1.
Title (under 70 chars): "How to <result the reader wants> (The <Algorithm Name>)".
Meta description (under 155 chars): the result and the method.
## The problem this solves
  The symptom in the reader's words, then the algorithm named with its "Use when" line
  from the block. For an outside speaker, one sentence placing them: "Read through the
  methodology, Gary's advice here is the Co-Creator Identity Algorithm run on one person's
  business."
## What the methodology says
  Name, "Use when" line, then the numbered steps VERBATIM. Nothing else. Failure modes or a
  falsifier in the block go verbatim under an H3 "What breaks it".
## How to run it in your business
  "Applied, not canon:" then one H3 per step, "Step N - <step name>", 120 to 200 words
  each: the Correspondence line (rule 6) if an outside speaker; what you do; what it
  produces (a document, a list, a decision, a number); who does it; one line each for
  DETECT, PROCESS, RESPOND. The speaker's examples go here, attributed. A tool, time or
  template only if the video gave it.
## Three places to use it this week
  "Applied, not canon:" then H3s "In operations", "In marketing", "In growth and sales":
  four to six sentences each, the same algorithm run on that part of the business, ending
  with the first artifact produced. An area the video does not cover gets "Not covered in
  this video" plus the one decision the reader would have to make to apply it there.
## How you will know it is working, and how you will know it is not
  Two short lists. Working: the observable change the speaker describes, figures only if
  given. Not working: the observation that would show it failed (the falsifier). If the
  video names none: "The video does not name one. A reasonable one to set yourself:" and
  ONE, marked as the article's.
## Common mistakes
  Only the speaker's. Else "The video names none."
## Start here
  The smallest action within 24 hours, from step 1. One paragraph.
## Key terms
  Three to six methodology terms, one plain sentence each.
## Questions this video answers
  Three to five search-shaped questions, two or three sentences each, from the transcript.
## Source
  The credit line from the block, verbatim. Then: "The steps above are reproduced from the
  methodology; the applications are this article's and are not endorsed by the author."
  Then "Watch the original" linking the video if it is on YouTube.

LENGTH 1,500 to 2,500 words. Markdown; H2 and H3 only; tables allowed for the steps and the
three scenarios; no images unless the tool inserts a video frame, then caption it.

BEFORE YOU FINISH: every step matches the block character for character and keeps its
number; every figure is in the transcript and attributed; every applied section opens
"Applied, not canon:"; every step has its Correspondence line or "does not address"; no
banned word; the credit line is unaltered; the article is in second person and not the
speaker's voice. Fix any failure before producing the article.

LENS INDEX (for the no-block paragraph only): Master Meta-Algorithm, a domain nothing else
names · Three Kingdoms, vision/system/execution misaligned · Dynamic Middle, burnout or
stall · Energy Continuation, running out of energy · Slime Mold Integration, a failure
treated as waste · Co-Creator Identity, choosing the work that is structurally yours ·
Garlick Equilibrium (BEAS), unhealthy and nobody can say where · Shepherd's Way, building or
fixing any process · ACE System, attention to customers to referrals · Falsifiability, an
untested claim · Negotiation, Sales, Hiring, Client Onboarding, Customer Service, Vendor
Management, the named activity · Decision-Making, Strategic Planning, Financial Decisions,
Risk Management, Forecasting · Brand and Identity, Influence, Movement Building · Project,
Time, Energy Management, Habit Formation · Creative Work, Writing, Communication and
Speaking, Teaching and Mentoring · Innovation and R&D, System Architecture, Software
Development.
```

---

## B. The short prompt (if the field is capped)

Same rules, compressed. Pair it with the same SOURCE BLOCK and footer.

```text
This is NOT a blog version of the video: no first person, not the speaker's voice. Write a
second-person how-to article teaching ONE algorithm from the GFunnel Methodology (Omni
Process, Cameron Garlick) to a business owner who has never heard of it, with the video as
the worked example. A SOURCE BLOCK with the algorithm is pasted below; if the speaker
teaches the methodology it is what they teach, otherwise it is the LENS. Everything you
need is in this text; the block's file line and URL are printed, never opened. With NO
block, write one paragraph naming the two or three methodology algorithms the video most
corresponds to and stop. Rules: (1) steps VERBATIM, numbered, in order from the block; never
add, merge, reorder or renumber, never present the speaker's sentences as steps; (2) every
tactic as DETECT (notice), PROCESS (do), RESPOND (act); (3) only figures the speaker states,
attributed; no external links or resources; never, even negated: guaranteed, guarantee,
proven, unlock, supercharge, game-changer, skyrocket, 10x, secret, hack; (4) every applied
section opens "Applied, not canon:"; (5) where the video does not say, "Not covered in this
video"; (6) for an outside speaker each step opens "Correspondence (this article's
reading):" plus what they said that matches, or "The speaker does not address this step".
Gloss every methodology term on first use. H2 sections, this order only: The problem this
solves / What the methodology says (steps verbatim) / How to run it in your business (one H3
per step, 120-200 words: what you do, what it produces, who does it, DETECT-PROCESS-RESPOND)
/ Three places to use it this week (In operations, In marketing, In growth and sales) / How
you will know it is working, and how you will know it is not / Common mistakes (only the
speaker's) / Start here / Key terms / Questions this video answers / Source (credit line
verbatim, then "the applications are this article's and are not endorsed by the author").
Title under 70 chars: "How to <result> (The <Algorithm>)". Meta under 155 chars. 1,500 to
2,500 words. Before finishing, check every step against the block and that no sentence is in
the speaker's voice.
```

---

## C. The footer

Paste into Video to Blog's custom footer so it rides every post. Change the version number
only if the SOURCE BLOCK came from a different version file; the tool prints the right one.

```text
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. The numbered steps are reproduced
from the methodology. The business applications are this article's and are not endorsed by
the author.
```

---

## D. The per-video addendum

Under the prompt, **in the same field**, for each video, paste the output of:

```bash
python3 tools/canon_pack.py "Shepherd" --compact   # or any algorithm / section name
```

`--compact` is the same canon text with the blank lines and the editor header removed, so
the prompt and the block together stay small (6,867 + about 1,500 characters). Run 3 showed
the block must be in the field the writer reads: pasted anywhere else, the writer sees no
block and correctly stops at the candidate paragraph. The full form below is for an editor
checking a draft; it says the same things with more air in them.

It looks like this (shortened):

```text
=== SOURCE BLOCK — canon text, copy verbatim, never paraphrase the numbered steps ===
Section: Layer VI — The Shepherd's Way Algorithm
File: versions/v5.1/GFunnel-Methodology-v5.1.md, lines 2498–2515; 7 numbered steps

#### Layer VI — The Shepherd's Way Algorithm
Use when: building, fixing, or extending any system, deliverable, project, or process ...
1. Direct. ...
...
7. Repetition. ...

Credit line (print verbatim at the foot of the article):
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
=== END SOURCE BLOCK ===
```

If a video teaches two algorithms, paste two blocks and add one line above them: "This
video covers two algorithms; write the article on the first and mention the second in
Key terms." One article, one algorithm. A reader can run one thing this week.
