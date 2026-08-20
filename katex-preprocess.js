import katex from 'katex';

// mdsvex replaces remark's parser with its own, so micromark-based plugins like
// remark-math never run. Math is therefore rendered here, before mdsvex sees the
// file, and handed on as plain HTML.
const PROTECTED = /```[\s\S]*?```|`[^`\n]*`/g;
// Pandoc treats a bare LaTeX environment as display math, with no $$ around it.
const ENVIRONMENTS =
  'align\\*?|aligned|alignat\\*?|gather\\*?|equation\\*?|split|cases|array|matrix|[bpvBV]matrix';
// Display, bare environment and inline are matched in a single pass, so
// whichever opens first claims the span. Run separately, the environment
// sweep would carve up a `$$\begin{pmatrix}…$$` block from the inside and
// leave the delimiters wrapped around markup for the display sweep to typeset.
// Newlines are allowed inside inline math because authored prose wraps mid
// expression; the length cap stops a stray `$` from swallowing a paragraph.
const MATH = new RegExp(
  [
    '\\$\\$([\\s\\S]+?)\\$\\$',
    `\\\\begin\\{(${ENVIRONMENTS})\\}[\\s\\S]*?\\\\end\\{\\2\\}`,
    '(?<![\\\\$])\\$(?!\\s)([^$]{1,600}?)(?<!\\s)\\$(?!\\$)'
  ].join('|'),
  'g'
);

// output: 'html' drops the MathML branch, whose <annotation> would otherwise
// carry the raw TeX — braces included — into the component.
function render(tex, displayMode) {
  return katex
    .renderToString(tex.trim(), {
      displayMode,
      throwOnError: false,
      output: 'html'
    })
    .replace(/{/g, '&lbrace;')
    .replace(/}/g, '&rbrace;');
}

function renderSegment(text) {
  return text.replace(MATH, (match, display, environment, inline) => {
    if (display !== undefined) return `\n\n${render(display, true)}\n\n`;
    if (environment !== undefined) return `\n\n${render(match, true)}\n\n`;
    return render(inline, false);
  });
}

// mdsvex parses the rendered math into hast and serialises it again, which
// decodes `&lbrace;` back to a literal `{` that Svelte then reads as an
// expression. Re-escape braces in text nodes once mdsvex is done with them.
export function escapeTextBraces() {
  return {
    name: 'escape-text-braces',
    markup({ content, filename }) {
      if (!filename?.endsWith('.svx')) return;

      // mdsvex emits the frontmatter as a module script; its object braces are
      // real JavaScript and must survive untouched.
      const SKIP = /<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/g;
      const escape = (text) =>
        text.replace(
          />([^<>]*)</g,
          (_, inner) =>
            `>${inner.replace(/{/g, '&lbrace;').replace(/}/g, '&rbrace;')}<`
        );

      let code = '';
      let last = 0;
      for (const match of content.matchAll(SKIP)) {
        code += escape(content.slice(last, match.index)) + match[0];
        last = match.index + match[0].length;
      }
      code += escape(content.slice(last));
      return code === content ? undefined : { code };
    }
  };
}

export function katexMath() {
  return {
    name: 'katex-math',
    markup({ content, filename }) {
      if (!filename?.endsWith('.svx') || !content.includes('$')) return;

      let out = '';
      let last = 0;
      for (const match of content.matchAll(PROTECTED)) {
        out += renderSegment(content.slice(last, match.index)) + match[0];
        last = match.index + match[0].length;
      }
      out += renderSegment(content.slice(last));
      return { code: out };
    }
  };
}
