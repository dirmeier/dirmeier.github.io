"""Convert a Quarto source document to an .svx page.

Works from the authored `.qmd` rather than the rendered HTML, so the prose,
code and math stay as markdown. Because a `.qmd`'s outputs only exist after
execution, the figures under `static/blog/<slug>/` are re-attached to the code
cells they came from, matched up through the rendered `index.html`.

    python3 tools/qmd-to-svx.py <qmd> <slug> [--date YYYY-MM] [--bib file.bib]
"""

import argparse
import pathlib
import re
import sys
from html import unescape

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import bib as bibtex

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHUNK = re.compile(r"^```\{(\w+)\}\s*$", re.M)
HEADING = re.compile(r"^(#{1,5}) ", re.M)
# The rendered site carries its own footer, and every case study closes with
# the same two boilerplate sections.
BOILERPLATE = re.compile(r"^# (Session info|License)\b.*?(?=^#)", re.M | re.S)


def split_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        return {}, text
    meta = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t", "-")):
            meta[key.strip()] = value.strip().strip("'\"")
    return meta, match.group(2)


def source_key(code):
    """Whitespace-insensitive identity of a code cell."""
    return re.sub(r"\s+", "", code)


def figures_for(slug):
    """source code -> one list of output images per cell that ran it.

    Quarto's `cell-N-output-M.png` numbering counts prose blocks as well as
    code, and the count drifts from anything recoverable out of the `.qmd`.
    The rendered page already pairs each cell with its outputs, so the code
    itself is used as the key instead. A post may run the same few lines more
    than once, so the occurrences are kept apart and handed out in order.
    """
    page = ROOT / "static" / "blog" / slug / "index.html"
    out = {}
    if not page.is_file():
        return out
    html = page.read_text(encoding="utf-8", errors="replace")
    for cell in re.split(r'<div class="cell"[^>]*>', html)[1:]:
        images = [
            f"/blog/{slug}/{src}"
            for src in re.findall(r'src="([^"]*_files/figure-html/[^"]+)"', cell)
        ]
        if not images:
            continue
        code = "".join(
            unescape(re.sub(r"<[^>]+>", "", block))
            for block in re.findall(r"<code class=\"sourceCode[^\"]*\">(.*?)</code>", cell, re.S)
        )
        out.setdefault(source_key(code), []).append(images)
    return out


def convert_body(body, figures):
    """Rewrite executable chunks as plain fences and append their figures."""
    lines = BOILERPLATE.sub("", body).split("\n")
    out, i = [], 0
    while i < len(lines):
        chunk = CHUNK.match(lines[i])
        if not chunk:
            # Demoted here rather than over the whole document, so that a `#`
            # comment on the first column of a code chunk is left alone.
            out.append(HEADING.sub(r"#\1 ", lines[i]))
            i += 1
            continue

        out.append(f"```{chunk.group(1)}")
        i += 1
        code = []
        while i < len(lines) and not lines[i].startswith("```"):
            if not lines[i].startswith("#| "):  # Quarto cell options
                code.append(lines[i])
            i += 1
        # Cell options left a blank first line behind once they were dropped.
        if code and not code[0].strip():
            del code[0]
        out.extend(code)
        out.append("```")
        i += 1

        pending = figures.get(source_key("\n".join(code)))
        for src in pending.pop(0) if pending else []:
            out.append("")
            out.append(f"![]({src})")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("qmd")
    parser.add_argument("slug")
    parser.add_argument("--date", default="")
    parser.add_argument("--title", default="")
    # Repeatable, so a local .bib can top up what the upstream one is missing.
    parser.add_argument("--bib", action="append", default=[])
    args = parser.parse_args()

    text = pathlib.Path(args.qmd).read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)

    body = convert_body(body, figures_for(args.slug))
    if args.bib:
        entries = {}
        for path in args.bib:
            entries.update(bibtex.parse(pathlib.Path(path).read_text()))
        body = bibtex.apply(body, entries)

    title = (args.title or meta.get("title", args.slug)).replace("'", "’")
    dest = ROOT / "src" / "routes" / "blog" / args.slug / "+page.svx"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        f"---\ntitle: '{title}'\ndate: '{args.date}'\n---\n\n{body.strip()}\n",
        encoding="utf-8",
    )
    print(f"{dest.relative_to(ROOT)}  {len(body)} bytes")


if __name__ == "__main__":
    main()
