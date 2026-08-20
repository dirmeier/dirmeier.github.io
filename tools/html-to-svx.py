"""Wrap a rendered pandoc/Quarto post as an .svx page.

The body markup is kept verbatim rather than converted to markdown, so plots,
code outputs and tables survive exactly as rendered. Only the parts Svelte
cannot swallow are touched: <script> is removed, braces are escaped, and
relative asset paths are made absolute so they still resolve from a route URL
without a trailing slash.

    python3 tools/html-to-svx.py <slug> [--date YYYY-MM]
"""

import argparse
import pathlib
import re
from html import unescape

ROOT = pathlib.Path(__file__).resolve().parent.parent


def body_of(html):
    match = re.search(r"<body[^>]*>(.*)</body>", html, re.S)
    return match.group(1) if match else html


def strip(html):
    # Svelte reads a top-level <script> as the component's instance script, and
    # <style> here would fight app.scss.
    html = re.sub(r"<script\b.*?</script>", "", html, flags=re.S)
    html = re.sub(r"<style\b.*?</style>", "", html, flags=re.S)
    html = re.sub(r"<noscript\b.*?</noscript>", "", html, flags=re.S)
    return html


def drop_title_block(html):
    """The layout supplies title, metadata and contents itself."""
    html = re.sub(
        r'<header[^>]*id="title-block-header".*?</header>', "", html, flags=re.S
    )
    # Quarto's own sidebar would render inline as a second table of contents.
    return re.sub(
        r'<div[^>]*id="quarto-margin-sidebar".*?</nav>\s*</div>', "", html, flags=re.S
    )


def absolutise(html, slug):
    """Rewrite `foo_files/...` so it resolves from /blog/<slug> as well as /blog/<slug>/."""
    return re.sub(
        r'((?:src|href)=")(?!https?://|/|#)([^"]*_files/)',
        rf'\1/blog/{slug}/\2',
        html,
    )


MATH = re.compile(r"\\\[(.+?)\\\]|\\\((.+?)\\\)", re.S)


def escape_braces(html):
    """Escape braces for Svelte, but hand math through untouched.

    Quarto emits MathJax delimiters and relies on a runtime script we strip.
    The TeX is rewritten to `$`/`$$` so katex-preprocess.js renders it at build
    time, and is held out of the brace escaping that would otherwise turn every
    \\frac{a}{b} into entities.
    """
    parts, last = [], 0
    for match in MATH.finditer(html):
        display, inline = match.group(1), match.group(2)
        # The TeX is HTML-encoded in the source: alignment `&` arrives as
        # `&amp;`, which KaTeX would render literally as "amp;".
        tex = unescape((display or inline)).strip()
        delim = "$$" if display else "$"
        parts.append(html[last : match.start()].replace("{", "&lbrace;").replace("}", "&rbrace;"))
        parts.append(f"{delim}{tex}{delim}")
        last = match.end()
    parts.append(html[last:].replace("{", "&lbrace;").replace("}", "&rbrace;"))
    return "".join(parts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("--date", default="")
    parser.add_argument("--title", default="")
    args = parser.parse_args()

    src = ROOT / "static" / "blog" / args.slug / "index.html"
    html = src.read_text(encoding="utf-8", errors="replace")

    title = args.title or re.search(r"<title>(.*?)</title>", html, re.S).group(1)
    title = re.sub(r"\s+", " ", title).strip()

    out = escape_braces(
        absolutise(drop_title_block(strip(body_of(html))), args.slug)
    ).strip()

    dest = ROOT / "src" / "routes" / "blog" / args.slug / "+page.svx"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        f"---\ntitle: {title!r}\ndate: '{args.date}'\n---\n\n<div class=\"imported\">\n\n{out}\n\n</div>\n",
        encoding="utf-8",
    )
    print(f"{dest.relative_to(ROOT)}  {len(out)} bytes of body")


if __name__ == "__main__":
    main()
