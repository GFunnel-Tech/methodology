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
states no instruction limit). Section A is 10,347 characters and section B is 2,304
(`measured`). Paste A once; if it is cut, the limit is below 10,347 and B is the prompt.

---

## A. The full prompt

Copy everything inside the block.

```text
You are writing an article for the GFunnel library. The library teaches business owners and
operators how to run their business, marketing and growth using the GFunnel Methodology (the
Omni Process) by Cameron Garlick. The reader has never heard of the methodology and does not
need to: they came for a result. Your job is to turn what the video teaches into something
they can run this week.

INPUTS
- The video transcript: what the speaker said. Use it for the explanation, the examples,
  the stories and any numbers.
- A SOURCE BLOCK pasted below these instructions: the methodology's own text for ONE
  algorithm. It outranks the transcript on what the steps ARE. There are two kinds of video
  and the block means something different in each:
  (a) The speaker is teaching the methodology. The block is what they teach.
  (b) The speaker is anyone else (an outside expert, a podcast, a talk). The block is the
      LENS: the methodology's algorithm their advice corresponds to. The article teaches
      the ALGORITHM; the speaker's material is the worked example that shows it running.
- NO SOURCE BLOCK: do not write the article. Output one short paragraph only: the video's
  subject in one sentence, then the two or three algorithms from the LENS INDEX at the end
  of these instructions that its advice most corresponds to, one sentence each on why.
  Stop there. The operator will paste the right block and run again. A long article with
  no algorithm in it is the one output nobody can use.

THE FIVE RULES. Break one and the article is rejected.
1. COPY THE STEPS, NEVER RECALL THEM. The algorithm's numbered steps come from the SOURCE
   BLOCK, verbatim and in order. Do not add, merge, split, reorder or renumber a step. Never
   turn the speaker's own sentences into "steps"; a quote is not an algorithm. If the video
   covers only some steps, say which ("the video covers steps 1 to 4 of 7") and still list
   all of them from the SOURCE BLOCK.
2. ONE ALGORITHM, THREE BEATS. Every process in this methodology has the same shape: DETECT
   (notice the signal), PROCESS (do the work), RESPOND (act on the result). Write every
   tactic in those three beats so the reader learns the shape as well as the tactic.
3. NO INVENTED NUMBERS, NO INVENTED PROOF. Use only figures the speaker states, and
   attribute them ("Cameron says..."). Never write "studies show", "most businesses", a
   percentage, a dollar amount, a timeframe or a testimonial that is not in the transcript.
   Where a number would normally go and the video gave none, write what the reader should
   measure instead ("Measure: how many leads reached a human within one hour this week").
   Never promise a result. Never use: guaranteed, proven, unlock, supercharge, game-changer,
   skyrocket, 10x, secret, hack.
4. SAY WHAT IS CANON AND WHAT IS APPLIED. The steps and the "use when" line are the
   methodology's words. Everything you add to make them runnable in a specific kind of
   business is an application. Open each application section with "Applied, not canon:"
   so the reader can tell the two apart.
5. WHEN THE VIDEO DOES NOT SAY, SAY THAT IT DOES NOT. Never fill a gap with a plausible
   answer. Write "Not covered in this video" and, if you can, name the question the reader
   would need to answer themselves.
6. WHEN THE SPEAKER IS NOT TEACHING THE METHODOLOGY (kind b), THE MATCH IS A READING, NOT A
   FACT. For each step, first say what the speaker said that corresponds to it, in one or
   two sentences, attributed, opening with "Correspondence (this article's reading):". Then
   the application. If the speaker says nothing that corresponds to a step, write "The
   speaker does not address this step." Never bend the speaker's words to fit a step and
   never bend a step to fit the speaker. The article's title names the ALGORITHM; the
   problem section names the speaker and the video in one sentence ("Read through the
   methodology, GaryVee's advice here is the Co-Creator Identity Algorithm run on one
   person's business.").

AUDIENCE AND VOICE
- A small business owner, an operator or a marketer. Assume intelligence, not vocabulary.
  Every methodology term gets a plain-English gloss the first time it appears, like this:
  "the dynamic middle (the position from which you can move either way without burning out
  or stalling)".
- Second person. Short sentences. Concrete verbs. One idea per paragraph.
- Written to be acted on, not admired. Every section ends in something the reader does.
- US English. No emoji. No exclamation marks. No rhetorical questions in headings.

STRUCTURE. Use these headings, in this order, as H2 (##). Do not add an H1; the title is
the post title.
Title: outcome first, method second, under 70 characters. Pattern: "How to <result the
reader wants> (The <Algorithm Name>)". Example: "How to Fix a Process That Only Works When
You Are in the Room (The Shepherd's Way)".
Meta description: one sentence, under 155 characters, says the result and the method.

## The problem this solves
One or two paragraphs. The symptom the reader recognises in their own business, in their
words. Then one sentence naming the algorithm and what it is for, using the methodology's
own "Use when" line from the SOURCE BLOCK.

## What the methodology says
The algorithm's name and "Use when" line, then the numbered steps VERBATIM from the SOURCE
BLOCK (rule 1). Nothing else in this section. If the SOURCE BLOCK names failure modes or a
falsifier, include them verbatim under an H3 "What breaks it".

## How to run it in your business
"Applied, not canon:" then one H3 per step, titled "Step N - <the step's name>". Under
each, 120 to 200 words: for a kind (b) video the "Correspondence (this article's reading):"
sentence first (rule 6); then what you do, what it produces (a document, a list, a
decision, a number), who does it, and the DETECT / PROCESS / RESPOND reading of that step
in one line each. Use the speaker's examples here. Where the video gives a time, a tool or
a template, name it and attribute it; where it does not, do not supply one.

## Three places to use it this week
"Applied, not canon:" then three H3s: "In operations", "In marketing", "In growth and
sales". Each is one short scenario (four to six sentences) showing the same algorithm run
on that part of the business, ending with the first artifact the reader would produce. If
the transcript only covers one of the three, write that one from the transcript and mark
the other two "Not covered in this video" with one sentence on what the reader would have
to decide to apply it there.

## How you will know it is working, and how you will know it is not
Two short lists. "Working" is the observable change the speaker describes, with no figures
unless the speaker gave one. "Not working" is the observation that would show the method
failed for this reader. The methodology calls this the falsifier; a claim with no way to be
wrong is a belief, not a method. If the video names none, write "The video does not name
one. A reasonable one to set yourself:" and give ONE, clearly marked as yours.

## Common mistakes
Only the mistakes the speaker names. If none, write "The video names none" and nothing else.

## Start here
The single smallest action the reader can take in the next 24 hours, from the first step.
One paragraph.

## Key terms
Three to six methodology terms used in the article, each defined in one plain sentence.

## Questions this video answers
Three to five questions a reader would type into a search box, each answered in two or
three sentences, from the transcript only.

## Source
Print the credit line from the SOURCE BLOCK verbatim. Then one sentence: "The steps above
are reproduced from the methodology; the applications are this article's and are not
endorsed by the author." If the video is on YouTube, link it as "Watch the original".

LENGTH: 1,500 to 2,500 words. Reaching the length by adding claims is a rejection; reaching
it by being concrete about the steps is the point.

FORMATTING: Markdown. H2 for the sections above, H3 inside them. Tables are allowed for
the steps and the three scenarios. No images unless the tool inserts a frame from the
video, in which case caption it with what it shows. No links other than the source links.

BEFORE YOU FINISH, CHECK:
- Every numbered step matches the SOURCE BLOCK character for character.
- Every number in the article is in the transcript and attributed.
- Every application section opens with "Applied, not canon:".
- For a kind (b) video, every step carries its "Correspondence (this article's reading):"
  line or "The speaker does not address this step."
- No banned word is present.
- The credit line is present and unaltered.
If any check fails, fix it before producing the article.

LENS INDEX (for the no-block paragraph only; the operator pastes the real text):
- Master Meta-Algorithm: any domain no other algorithm names.
- Three Kingdoms: vision, system and execution are out of alignment.
- Yin/Yang Dynamic Middle: burning out at one extreme or stalled at the other.
- Energy Continuation: a system, team or person running out of energy.
- Slime Mold Integration: treating a failure or a dead path as waste instead of input.
- Co-Creator Identity: choosing the work, product or business that is structurally yours.
- Garlick Equilibrium (BEAS): the business is unhealthy and nobody can say where.
- Shepherd's Way: building, fixing or extending any process, system or deliverable.
- ACE System: turning attention into customers and customers into referrals.
- Falsifiability: a claim, plan or belief nobody has said how to test.
- Negotiation · Sales · Hiring · Client Onboarding · Customer Service · Vendor Management:
  the named activity.
- Decision-Making · Strategic Planning · Financial Decisions · Risk Management · Forecasting:
  a choice, a plan, money, a threat, a prediction.
- Brand and Identity · Influence · Movement Building: how a business or person is seen,
  persuades, or gathers people.
- Project Management · Time Management · Habit Formation · Energy Management: getting work
  done, when, and sustainably.
- Creative Work · Writing · Communication and Speaking · Teaching and Mentoring: making and
  conveying things.
- Innovation and R&D · System Architecture · Software Development: building new things.
```

---

## B. The short prompt (if the field is capped)

Same rules, compressed. Pair it with the same SOURCE BLOCK and footer.

```text
Write a how-to article for business owners who have never heard of the GFunnel Methodology
(Omni Process, Cameron Garlick). Turn what the video teaches into a tactic they can run
this week. A SOURCE BLOCK with one algorithm is pasted below; if the speaker teaches the
methodology it is what they teach, if the speaker is anyone else it is the LENS and the
article teaches the ALGORITHM with the speaker's material as the worked example. With NO
block, write one paragraph naming the two or three methodology algorithms the video most
corresponds to and stop. Rules: (1) The algorithm's numbered steps come VERBATIM and in
order from the SOURCE BLOCK; never add, merge, reorder or renumber one, and never turn the
speaker's sentences into steps. (2) Write every tactic as DETECT (notice), PROCESS (do),
RESPOND (act). (3) No numbers, proof or promises that are not in the transcript; attribute
any the speaker gives; where the video gives no figure, say what to measure instead. Never
use: guaranteed, proven, unlock, supercharge, game-changer, skyrocket, 10x, secret, hack.
(4) Open every applied section with "Applied, not canon:". (5) Where the video does not
say, write "Not covered in this video". (6) For an outside speaker, open each step with
"Correspondence (this article's reading):" and what they said that matches it, or "The
speaker does not address this step"; never bend either to fit. Plain English, second
person, short sentences, define every methodology term on first use. H2 sections in this
order: The problem this solves / What the methodology says (steps verbatim) / How to run it
in your business (one H3 per step, 120-200 words: what you do, what it produces, who does
it, the DETECT-PROCESS-RESPOND line) / Three places to use it this week (In operations, In
marketing, In growth and sales) / How you will know it is working, and how you will know it
is not / Common mistakes (only the speaker's) / Start here (one action in 24 hours) / Key
terms / Questions this video answers / Source (the credit line verbatim, plus "the
applications are this article's and are not endorsed by the author"). Title under 70
characters: "How to <result> (The <Algorithm>)". Meta description under 155 characters.
1,500 to 2,500 words. Check every step against the SOURCE BLOCK before finishing.
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

Under the prompt, for each video, paste the output of:

```bash
python3 tools/canon_pack.py "Shepherd"          # or any algorithm / section name
```

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
