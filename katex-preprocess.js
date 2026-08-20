import katex from 'katex';

// mdsvex replaces remark's parser with its own, so micromark-based plugins like
// remark-math never run. Math is therefore rendered here, before mdsvex sees the
// file, and handed on as plain HTML.
const PROTECTED = /```[\s\S]*?```|`[^`\n]*`/g;
// Pandoc treats a bare LaTeX environment as display math, with no $$ around it.
const ENVIRONMENT =
  /\\begin\{(align\*?|aligned|alignat\*?|gather\*?|equation\*?|split|cases|array|matrix|[bpvBV]matrix)\}[\s\S]*?\\end\{\1\}/g;
const DISPLAY = /\$\$([\s\S]+?)\$\$/g;
// Newlines are allowed inside inline math because authored prose wraps mid
// expression; the length cap stops a stray `$` from swallowing a paragraph.
const INLINE = /(?<![\\$])\$(?!\s)([^$]{1,600}?)(?<!\s)\$(?!\$)/g;

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
  return text
    .replace(ENVIRONMENT, (env) => `\n\n${render(env, true)}\n\n`)
    .replace(DISPLAY, (_, tex) => `\n\n${render(tex, true)}\n\n`)
    .replace(INLINE, (_, tex) => render(tex, false));
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
