# The article template — what every methodology article must come out as

> **Status: operations tooling, not canon.** This is the shape the prompt in
> [`videotoblog-prompt.md`](videotoblog-prompt.md) enforces, written out so an editor can
> hold a draft against it without re-reading the prompt. One article teaches one algorithm.

The shape is the methodology's own run form applied to writing about it: **what the canon
says** (reproduced, credited), **how to run it** (applied, labelled), **how you would know it
failed** (the falsifier), **the smallest first step** (so it is run, not read).

## The skeleton

```markdown
Title:  How to <result the reader wants> (The <Algorithm Name>)        ≤ 70 characters
Meta:   <one sentence: the result and the method>                       ≤ 155 characters

## The problem this solves
<the symptom, in the reader's words> ... <the algorithm's name and its canon "Use when" line>

## What the methodology says
<Algorithm name>. Use when: <canon line>.
1. <step, verbatim>
2. <step, verbatim>
...
### What breaks it                       (only if the canon names failure modes or a falsifier)
<verbatim>

## How to run it in your business
Applied, not canon:
### Step 1 - <step name>                                            (120–200 words each)
Correspondence (this article's reading): <what the speaker said that matches this step>
                                           (outside speakers only; else "The speaker does not address this step.")
What you do · What it produces · Who does it
DETECT: ... PROCESS: ... RESPOND: ...
### Step 2 - ...

## Three places to use it this week
Applied, not canon:
### In operations          <4–6 sentences, ends with the first artifact>
### In marketing           <or "Not covered in this video" + the decision the reader must make>
### In growth and sales

## How you will know it is working, and how you will know it is not
Working:     - <observable change the speaker describes>
Not working: - <the observation that would show it failed>   (if the video names none: ONE, marked as the article's)

## Common mistakes
<only the speaker's; else "The video names none">

## Start here
<one action within 24 hours, from step 1>

## Key terms
<3–6 terms, one plain sentence each>

## Questions this video answers
<3–5 search-shaped questions, 2–3 sentences each, from the transcript>

## Source
Source: GFunnel Methodology (Omni Process) v<N>, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
The steps above are reproduced from the methodology; the applications are this article's
and are not endorsed by the author.
Watch the original: <video link>
```

## Why each part is there

| Section | What it is for | The rule behind it |
| --- | --- | --- |
| The problem this solves | The reader finds themselves before they find the method. | `framework/algorithms.md` routes by symptom ("If you are…"), not by layer name. |
| What the methodology says | The canon, reproduced, so the reader can run the real thing and so the credit is earned. | AGENTS.md rules 1 and 3: authoritative text, steps run literally and in order. |
| How to run it in your business | Each step becomes an action with an artifact. For an outside speaker, each step first says what they said that corresponds to it, as a reading. | Layer VI step 6 (Database): if it is not written, it does not exist as a process. AGENTS.md rule 6: a Correspondence is stated explicitly, never implied. |
| Three places to use it this week | The same algorithm at three scales of the business. | Hermetic Correspondence (AGENTS.md rule 6); each is labelled an application, never canon (rule 7). |
| How you will know it is working / not | The falsifier. | Layer ◇ step 2: a claim nothing could falsify is a belief, not a claim. |
| Common mistakes | Only what the speaker said. | Rule 5: never fill a variable silently. |
| Start here | The run begins. | Layer VI step 5 (Create) follows Direct, Guide, Gather, Organize; one small first step is the honest size. |
| Key terms | The methodology's vocabulary, glossed. | A reader who never heard of it should still finish. |
| Questions this video answers | What people type into a search box. | The platform's `/resources` library and search feed carry the article; the questions are how it is found. |
| Source | The credit line, verbatim. | The license (CC BY 4.0): copying requires attribution and a note that changes were made. |

## What an article may never contain

- A number, percentage, dollar figure, timeframe or testimonial the speaker did not state.
- A step the SOURCE BLOCK does not carry, the canon's steps in a different order, or the
  speaker's own sentences presented as steps.
- An outside speaker's advice presented as the methodology's position, or a step bent to
  fit what the speaker said.
- The words guaranteed, proven, unlock, supercharge, game-changer, skyrocket, 10x, secret, hack.
- An application presented as the methodology's own position.
- A missing or altered credit line.
- The speaker's voice: any sentence in the first person, or the video retold as a post.
- A link or resource the transcript did not name (run 2 added two).
- A banned word in any form, negated included ("not guaranteed" is still the word).

Anything a reader is asked to do about **their** business is tagged for them by the section
it sits in: canon reproduces, "Applied, not canon" applies, "Not covered in this video" holds
open. That is the Variable Principle written for a reader who has never heard the phrase.
