"""Minimal front-matter reader shared by the audit and container validators.

Standard library only. Supports the subset of YAML the schemas use:
  key: value            scalar (quotes stripped; trailing `# comment` removed)
  key: [a, b, c]        inline list
  key: []               empty list
  key: null / ~ / ''    None
Anything else is reported as a parse error rather than guessed at.
"""

import re

FENCE = "---"
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _strip_comment(raw):
    """Remove a trailing ` # comment` that is outside quotes."""
    out, quote = [], None
    for i, ch in enumerate(raw):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or raw[i - 1].isspace()):
            break
        out.append(ch)
    return "".join(out).strip()


def _unquote(val):
    if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
        return val[1:-1]
    return val


def _scalar(val):
    val = _unquote(val.strip())
    if val in ("null", "~", ""):
        return None
    return val


def parse(text):
    """Return (fields, body, errors). fields is None if there is no front matter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != FENCE:
        return None, text, ["missing front matter (file must start with '---')"]
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == FENCE)
    except StopIteration:
        return None, text, ["front matter is not closed with '---'"]

    fields, errors = {}, []
    for n, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = KEY_RE.match(line)
        if not m:
            errors.append(f"line {n}: cannot parse front matter line: {line!r}")
            continue
        key, raw = m.group(1), _strip_comment(m.group(2))
        if key in fields:
            errors.append(f"line {n}: duplicate key '{key}'")
        if raw.startswith("["):
            if not raw.endswith("]"):
                errors.append(f"line {n}: unterminated list for '{key}'")
                continue
            inner = raw[1:-1].strip()
            fields[key] = [_unquote(x.strip()) for x in inner.split(",")] if inner else []
        else:
            fields[key] = _scalar(raw)
    body = "\n".join(lines[end + 1:])
    return fields, body, errors


def sections(body, level=2):
    """Map each heading at `level` to its text (up to the next heading of the same or higher level)."""
    marker = "#" * level + " "
    out, current, buf, in_fence = {}, None, [], False
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
        is_heading = stripped.startswith("#") and not in_fence
        depth = len(stripped) - len(stripped.lstrip("#")) if is_heading else 0
        if is_heading and depth <= level and stripped.startswith("#" * depth + " "):
            if current is not None:
                out[current] = "\n".join(buf)
            current = stripped[len(marker):].strip() if depth == level else None
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        out[current] = "\n".join(buf)
    return out


def find_section(secs, prefix):
    """Return the text of the first section whose heading starts with `prefix`, or None."""
    for heading, text in secs.items():
        if heading.lower().startswith(prefix.lower()):
            return text
    return None


def meaningful(text):
    """True if text has content other than blank lines, HTML comments, and bare table/list scaffolding."""
    if text is None:
        return False
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if re.fullmatch(r"[|\-:\s]+", s):          # table rule or empty row
            continue
        if re.fullmatch(r"(\d+\.|[-*])\s*", s):      # empty list item
            continue
        if s.startswith("|") and not re.sub(r"[|\s]", "", s):
            continue
        return True
    return False
