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


def initials_of(token):
    """`Brian` -> `B.`, but `DO` -> `D. O.` — Scholar drops the dots."""
    if len(token) > 1 and token.isupper():
        return " ".join(f"{c}." for c in token)
    return f"{token[0]}."


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
    initials = " ".join(initials_of(p) for p in given.split() if p)
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


def cited_authors(entry):
    """`Vincent`, `Song and Ermon`, `Ho et al.`"""
    names = re.split(r"\s+and\s+", entry.get("author", ""))
    who = surname(entry.get("author", ""))
    if len(names) == 2:
        who = f"{who} and {surname(names[1])}"
    elif len(names) > 2:
        who = f"{who} et al."
    return who


def label(entry):
    """Parenthetical form, `Ho et al., 2020`."""
    who, year = cited_authors(entry), entry.get("year", "")
    return f"{who}, {year}" if year else who


def render_entry(entry):
    parts = [format_authors(entry.get("author", ""))]
    if entry.get("year"):
        parts.append(f"({entry['year']}).")
    # Titles that end in a period would otherwise render as `*Title.*.`
    title = entry.get("title", "").rstrip(".")
    if title:
        parts.append(f"*{title}*.")
    venue = entry.get("journal") or entry.get("booktitle") or ""
    if venue:
        if entry.get("volume"):
            venue += f", {entry['volume']}"
            if entry.get("number"):
                venue += f"({entry['number']})"
        if entry.get("pages"):
            venue += f", {entry['pages'].replace('--', '–')}"
        parts.append(f"{venue}.")
        # A journal's publisher is noise; a proceedings' is how it is found.
        imprint = entry.get("organization") or (
            entry.get("publisher") if entry.get("booktitle") else ""
        )
        if imprint:
            parts.append(f"{imprint}.")
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
        year = entry.get("year", "")
        who = cited_authors(entry)
        # Narrative form: the year is already set off by its parentheses, so
        # it takes no comma the way the parenthetical `label` does.
        cited = f"{who} ({year})" if year else who
        return f"[{cited}](#ref-{key})"

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
