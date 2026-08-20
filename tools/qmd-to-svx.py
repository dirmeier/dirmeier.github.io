"""Convert a Quarto source document to an .svx page.

Works from the authored `.qmd` rather than the rendered HTML, so the prose,
code and math stay as markdown. Because a `.qmd`'s outputs only exist after
execution, the figures already rendered under
`static/blog/<slug>/<stem>_files/figure-html/` are re-attached to the code
cells they came from — Quarto numbers those `cell-N-output-M.png`, counting
every executable chunk from one.

    python3 tools/qmd-to-svx.py <qmd> <slug> [--date YYYY-MM]
"""

import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import bib as bibtex

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHUNK = re.compile(r"^```\{(\w+)\}\s*$", re.M)


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


def figures_for(slug, stem):
    """cell number -> list of rendered output images, in order."""
    d = ROOT / "static" / "blog" / slug / f"{stem}_files" / "figure-html"
    out = {}
    if not d.is_dir():
        return out
    for path in sorted(d.iterdir()):
        m = re.match(r"cell-(\d+)-output-(\d+)\.", path.name)
        if m:
            out.setdefault(int(m.group(1)), []).append(
                f"/blog/{slug}/{stem}_files/figure-html/{path.name}"
            )
    return out


def convert_body(body, figures):
    """Rewrite executable chunks as plain fences and append their figures."""
    lines = body.split("\n")
    out, cell, i = [], 0, 0
    in_markdown = False
    while i < len(lines):
        chunk = CHUNK.match(lines[i])
        if not chunk:
            # A run of prose is one notebook cell, and Quarto counts it when
            # numbering cell-N-output-M.
            if lines[i].strip() and not in_markdown:
                in_markdown = True
                cell += 1
            out.append(lines[i])
            i += 1
            continue

        in_markdown = False
        cell += 1
        out.append(f"```{chunk.group(1)}")
        i += 1
        while i < len(lines) and not lines[i].startswith("```"):
            if not lines[i].startswith("#| "):  # Quarto cell options
                out.append(lines[i])
            i += 1
        out.append("```")
        i += 1

        for src in figures.get(cell, []):
            out.append("")
            out.append(f"![]({src})")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("qmd")
    parser.add_argument("slug")
    parser.add_argument("--date", default="")
    parser.add_argument("--bib", default="")
    args = parser.parse_args()

    text = pathlib.Path(args.qmd).read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)
    stem = pathlib.Path(args.qmd).stem

    body = convert_body(body, figures_for(args.slug, stem))
    if args.bib:
        body = bibtex.apply(body, bibtex.parse(pathlib.Path(args.bib).read_text()))

    title = meta.get("title", args.slug).replace("'", "’")
    dest = ROOT / "src" / "routes" / "blog" / args.slug / "+page.svx"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        f"---\ntitle: '{title}'\ndate: '{args.date}'\n---\n\n{body.strip()}\n",
        encoding="utf-8",
    )
    print(f"{dest.relative_to(ROOT)}  {len(body)} bytes")


if __name__ == "__main__":
    main()
