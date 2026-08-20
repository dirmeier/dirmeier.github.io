"""Minimal BibTeX support for the qmd converter.

Only what these posts use: `[@key]` and `@key` citations resolved against a
.bib file, rendered author-year style with links down to a reference list.
"""

import re

ENTRY = re.compile(r"@\w+\s*\{\s*([^,]+),(.*?)\n\}", re.S)
FIELD = re.compile(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*\n", re.S)


ACCENTS = {
    '\\"a': "ä", '\\"o': "ö", '\\"u': "ü", '\\"A': "Ä", '\\"O': "Ö", '\\"U': "Ü",
    "\\'e": "é", "\\'a": "á", "\\'o": "ó", "\\'i": "í", "\\`e": "è",
    "\\^e": "ê", "\\^o": "ô", "\\~n": "ñ", "\\c c": "ç", "\\ss": "ß"
}


def strip_braces(value):
    value = re.sub(r"[{}]", "", value)
    for tex, char in ACCENTS.items():
        value = value.replace(tex, char)
    return value.strip()


def parse(text):
    """key -> {field: value}"""
    out = {}
    for match in ENTRY.finditer(text):
        key = match.group(1).strip()
        body = match.group(2) + "\n"
        fields = {f.lower(): strip_braces(v) for f, v in FIELD.findall(body)}
        out[key] = fields
    return out


def split_name(name):
    """(surname, initials) from `Surname, Given` or `Given Middle Surname`."""
    name = name.strip()
    if not name:
        return "", ""
    if "," in name:
        last, _, given = name.partition(",")
    else:
        parts = name.split()
        last, given = parts[-1], " ".join(parts[:-1])
    initials = " ".join(f"{p[0]}." for p in given.split() if p)
    return last.strip(), initials


def surname(authors):
    """First author's surname."""
    return split_name(re.split(r"\s+and\s+", authors)[0])[0]


def format_authors(authors):
    """`Surname, G., Surname, G., and Surname, G.`"""
    people = [split_name(n) for n in re.split(r"\s+and\s+", authors) if n.strip()]
    formatted = [f"{last}, {initials}" if initials else last for last, initials in people]
    if len(formatted) > 2:
        return ", ".join(formatted[:-1]) + ", and " + formatted[-1]
    return " and ".join(formatted)


def label(entry):
    names = re.split(r"\s+and\s+", entry.get("author", ""))
    who = surname(entry.get("author", ""))
    if len(names) == 2:
        who = f"{who} and {surname(names[1])}"
    elif len(names) > 2:
        who = f"{who} et al."
    return f"{who} {entry.get('year', '')}".strip()


def render_entry(entry):
    parts = [format_authors(entry.get("author", ""))]
    if entry.get("year"):
        parts.append(f"({entry['year']}).")
    if entry.get("title"):
        parts.append(f"*{entry['title']}*.")
    venue = entry.get("journal") or entry.get("booktitle") or ""
    if venue:
        parts.append(f"{venue}.")
    text = " ".join(p for p in parts if p)
    url = entry.get("url")
    return f"{text} [{url}]({url})" if url else text


def apply(body, bib):
    """Replace citations and append a reference list for the keys used."""
    used = []

    def note(key):
        if key in bib and key not in used:
            used.append(key)
        return key in bib

    def bracketed(match):
        keys = [k.strip().lstrip("@") for k in match.group(1).split(";")]
        rendered = []
        for key in keys:
            if note(key):
                rendered.append(f"[{label(bib[key])}](#ref-{key})")
        return f"({'; '.join(rendered)})" if rendered else match.group(0)

    def inline(match):
        key = match.group(1)
        if not note(key):
            return match.group(0)
        entry = bib[key]
        who = label(entry).rsplit(" ", 1)[0]
        return f"[{who}](#ref-{key}) ([{entry.get('year', '')}](#ref-{key}))"

    body = re.sub(r"\[(@[^\]]+)\]", bracketed, body)
    body = re.sub(r"(?<![\w`])@([A-Za-z][\w:-]*)", inline, body)

    if not used:
        return body

    # Quarto documents already end with the heading its bibliography fills in.
    body = re.sub(r"\n#+\s*References\s*$", "", body.rstrip())
    # Each entry is left as its own markdown paragraph: wrapping them in a div
    # would make mdsvex treat the block as raw HTML and skip the markdown
    # inside, running every entry together.
    # The anchor goes on its own line: a paragraph that *starts* with a tag is
    # treated by mdsvex as a raw HTML block, so its markdown would be skipped.
    lines = ["", "## References", ""]
    for key in sorted(used, key=lambda k: label(bib[k])):
        lines.append(f'<span id="ref-{key}"></span>')
        lines.append("")
        lines.append(render_entry(bib[key]))
        lines.append("")
    return body.rstrip() + "\n" + "\n".join(lines)
