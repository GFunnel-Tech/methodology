#!/usr/bin/env python3
"""
canon_pack.py — pull one algorithm's canon text into a SOURCE BLOCK for an
article generator (Video to Blog, or any AI writing from a transcript).

Status: derivation tooling (not canon). Standard library only (Python 3.8+).

Why it exists: an article that teaches an algorithm must carry the algorithm's
steps VERBATIM, in order, with the credit line the license requires. A
generator that paraphrases the steps from memory invents, merges or reorders
them. So the generator is handed the canon text as data, and the prompt in
operations/articles/videotoblog-prompt.md tells it to copy, never to recall.

Usage:
  python3 tools/canon_pack.py --list                 # every algorithm, with its "Use when" line
  python3 tools/canon_pack.py "Shepherd"             # the SOURCE BLOCK for the first heading matching "Shepherd"
  python3 tools/canon_pack.py "ACE System" --version 5.1
  python3 tools/canon_pack.py "Five Modes"           # any heading works, not only algorithms
  python3 tools/canon_pack.py --catalogue            # rewrite operations/articles/catalogue.md
  python3 tools/canon_pack.py --selftest

A match is a case-insensitive substring of a heading in the chosen version
file. Several matches: the first is used and the others are listed on stderr
so you can narrow the query. The block runs from the heading to the next
heading of the same or a higher level, so a `####` algorithm stops at the next
`####`, `###` or `##`.

Released versions are immutable (AGENTS.md), so the line numbers the block
cites stay valid.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSIONS = {
    "5.1": os.path.join(ROOT, "versions", "v5.1", "GFunnel-Methodology-v5.1.md"),
    "5.2": os.path.join(ROOT, "versions", "v5.2", "GFunnel-Methodology-v5.2.md"),
    "5.3": os.path.join(ROOT, "versions", "v5.3", "GFunnel-Methodology-v5.3.md"),
    "5.4": os.path.join(ROOT, "versions", "v5.4", "GFunnel-Methodology-v5.4.md"),
}
CATALOGUE = os.path.join(ROOT, "operations", "articles", "catalogue.md")
REPO_URL = "https://github.com/GFunnel-Tech/methodology"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
USE_WHEN_RE = re.compile(r"^\s*Use when:\s*(.*\S)\s*$", re.I)
STEP_RE = re.compile(r"^\s*(\d+)\.\s+\S")


def read_lines(version: str) -> list:
    path = VERSIONS[version]
    with open(path, encoding="utf-8") as fh:
        return fh.read().split("\n")


def headings(lines: list) -> list:
    """(line_no_1_based, level, text) for every markdown heading."""
    out = []
    for i, line in enumerate(lines, 1):
        m = HEADING_RE.match(line)
        if m:
            out.append((i, len(m.group(1)), m.group(2)))
    return out


def section(lines: list, start_idx: int, all_headings: list) -> tuple:
    """Return (start, end) 1-based inclusive line range for heading at start_idx in all_headings."""
    start, level, _ = all_headings[start_idx]
    end = len(lines)
    for j in range(start_idx + 1, len(all_headings)):
        ln, lv, _ = all_headings[j]
        if lv <= level:
            end = ln - 1
            break
    # trim trailing blank lines
    while end > start and not lines[end - 1].strip():
        end -= 1
    return start, end


def find(lines: list, query: str) -> list:
    """All heading indexes whose text contains query (case-insensitive)."""
    q = query.lower()
    hs = headings(lines)
    return [i for i, (_, _, text) in enumerate(hs) if q in text.lower()]


def is_algorithm_heading(text: str) -> bool:
    """A heading that names one algorithm (not an index, a section or the plural)."""
    return bool(re.search(r"\bAlgorithm\b", text)) and not re.search(r"\b(Index|Section|Algorithms)\b", text)


def credit(version: str) -> str:
    return ("Source: GFunnel Methodology (Omni Process) v%s, Cameron Garlick / GFunnel, "
            "%s, CC BY 4.0." % (version, REPO_URL))


def source_block(version: str, query: str) -> str:
    lines = read_lines(version)
    hs = headings(lines)
    hits = find(lines, query)
    if not hits:
        raise SystemExit("no heading in v%s matches %r (try --list)" % (version, query))
    if len(hits) > 1:
        # Prefer an ALGORITHM heading (the numbered steps) over the chapter that
        # teaches it: "Shepherd" matches both "## Layer VI — The Shepherd's Way"
        # and "#### Layer VI — The Shepherd's Way Algorithm", and an article
        # generator wants the steps. Pass a longer query to get the chapter.
        algos = [i for i in hits if is_algorithm_heading(hs[i][2])]
        idx = (algos or hits)[0]
        sys.stderr.write("note: %d headings match %r; using line %d. Others:\n" % (len(hits), query, hs[idx][0]))
        for i in hits:
            if i != idx:
                sys.stderr.write("  line %d: %s\n" % (hs[i][0], hs[i][2]))
    else:
        idx = hits[0]
    start, end = section(lines, idx, hs)
    title = hs[idx][2]
    body = "\n".join(lines[start - 1:end])
    steps = sum(1 for ln in lines[start - 1:end] if STEP_RE.match(ln))
    rel = os.path.relpath(VERSIONS[version], ROOT)
    out = []
    out.append("=== SOURCE BLOCK — canon text, copy verbatim, never paraphrase the numbered steps ===")
    out.append("Section: %s" % title)
    out.append("File: %s, lines %d–%d%s" % (rel, start, end, ("; %d numbered steps" % steps) if steps else ""))
    out.append("")
    out.append(body)
    out.append("")
    out.append("Credit line (print verbatim at the foot of the article):")
    out.append(credit(version))
    out.append("=== END SOURCE BLOCK ===")
    return "\n".join(out)


def algorithm_rows(version: str = "5.1") -> list:
    """(title, use_when, start, end, steps) for every heading whose text ends in 'Algorithm' or names one."""
    lines = read_lines(version)
    hs = headings(lines)
    # Only the operational section counts: the title page and "How To Run An
    # Algorithm" also carry the word, and neither is an algorithm to teach.
    first = next((ln for ln, _, text in hs if "Operational Algorithm Section" in text), 0)
    rows = []
    for i, (ln, lv, text) in enumerate(hs):
        if lv < 2 or ln < first:
            continue
        if not is_algorithm_heading(text):
            continue
        start, end = section(lines, i, hs)
        use_when = ""
        steps = 0
        for body_line in lines[start - 1:end]:
            m = USE_WHEN_RE.match(body_line)
            if m and not use_when:
                use_when = m.group(1)
            if STEP_RE.match(body_line):
                steps += 1
        rows.append((text, use_when, start, end, steps))
    return rows


def list_algorithms(version: str) -> str:
    rows = algorithm_rows(version)
    width = max(len(r[0]) for r in rows)
    out = ["%d algorithm headings in v%s" % (len(rows), version), ""]
    for title, use_when, start, end, steps in rows:
        out.append("%s  lines %d–%d  %s" % (title.ljust(width), start, end,
                                            ("steps %d  " % steps if steps else "") + (("use when: " + use_when) if use_when else "")))
    return "\n".join(out)


def catalogue_markdown(version: str = "5.1") -> str:
    rows = algorithm_rows(version)
    rel = os.path.relpath(VERSIONS[version], ROOT)
    out = []
    out.append("# Article catalogue — one article per algorithm")
    out.append("")
    out.append("> Generated by `tools/canon_pack.py --catalogue` from `%s` — do not edit by hand." % rel)
    out.append("> Each row is one article the library can carry. Pull its SOURCE BLOCK with")
    out.append("> `python3 tools/canon_pack.py \"<algorithm>\"` and paste it under the prompt in")
    out.append("> [`videotoblog-prompt.md`](videotoblog-prompt.md). Which rows are drafted or published is")
    out.append("> tracked where the drafts live (the platform's content store), not here.")
    out.append("")
    out.append("%d algorithms. The canon's own router is [`framework/algorithms.md`](../../framework/algorithms.md)." % len(rows))
    out.append("")
    out.append("| # | Algorithm | Use when (canon's words) | Steps | Canon lines |")
    out.append("| --- | --- | --- | --- | --- |")
    for n, (title, use_when, start, end, steps) in enumerate(rows, 1):
        anchor = title.replace("`", "")
        out.append("| %d | %s | %s | %s | %d–%d |" % (n, anchor, use_when or "*(no \"Use when\" line in canon)*",
                                                    steps or "", start, end))
    out.append("")
    out.append(credit(version))
    out.append("")
    return "\n".join(out)


def selftest() -> int:
    errors = []
    block = source_block("5.1", "Shepherd")
    if "Layer VI — The Shepherd" not in block:
        errors.append("Shepherd's Way heading not found")
    if "7 numbered steps" not in block:
        errors.append("Shepherd's Way should carry 7 numbered steps; got: %s" %
                      next((l for l in block.splitlines() if l.startswith("File:")), "?"))
    if "7. Repetition." not in block:
        errors.append("Shepherd's Way step 7 text missing from block")
    if "#### Layer VII" in block:
        errors.append("block ran into the next #### section")
    if credit("5.1") not in block:
        errors.append("credit line missing")
    mma = source_block("5.1", "The Master Meta-Algorithm")
    if "12. Restart at higher baseline." not in mma or "## Per-Layer Algorithms" in mma:
        errors.append("Master Meta-Algorithm block wrong (should include step 12 and stop before Per-Layer Algorithms)")
    rows = algorithm_rows("5.1")
    if len(rows) < 70:
        errors.append("expected 70+ algorithm headings in v5.1, found %d" % len(rows))
    titles = [r[0] for r in rows]
    if not any("Shepherd" in t for t in titles) or any("Fast-Reference" in t for t in titles) \
            or any("How To Run" in t for t in titles):
        errors.append("algorithm_rows() picked the wrong headings")
    if titles[0] != "The Master Meta-Algorithm":
        errors.append("the catalogue should open with the Master Meta-Algorithm, got %r" % titles[0])
    try:
        source_block("5.1", "no such heading anywhere zzz")
        errors.append("a missing heading should exit non-zero")
    except SystemExit:
        pass
    for e in errors:
        print("FAIL:", e)
    print("selftest:", "ok" if not errors else "%d error(s)" % len(errors))
    return 1 if errors else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("query", nargs="?", help="substring of the heading to extract")
    ap.add_argument("--version", default="5.1", choices=sorted(VERSIONS), help="canon version file (default 5.1)")
    ap.add_argument("--list", action="store_true", help="list every algorithm heading with its 'Use when' line")
    ap.add_argument("--catalogue", action="store_true", help="rewrite operations/articles/catalogue.md")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)

    if a.selftest:
        return selftest()
    if a.catalogue:
        os.makedirs(os.path.dirname(CATALOGUE), exist_ok=True)
        with open(CATALOGUE, "w", encoding="utf-8") as fh:
            fh.write(catalogue_markdown(a.version))
        print("wrote", os.path.relpath(CATALOGUE, ROOT))
        return 0
    if a.list:
        print(list_algorithms(a.version))
        return 0
    if not a.query:
        ap.print_help()
        return 2
    print(source_block(a.version, a.query))
    return 0


if __name__ == "__main__":
    sys.exit(main())
