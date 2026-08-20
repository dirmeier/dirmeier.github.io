import katex from 'katex';

// mdsvex replaces remark's parser with its own, so micromark-based plugins like
// remark-math never run. Math is therefore rendered here, before mdsvex sees the
// file, and handed on as plain HTML.
const PROTECTED = /```[\s\S]*?```|`[^`\n]*`/g;
const DISPLAY = /\$\$([\s\S]+?)\$\$/g;
const INLINE = /(?<![\\$])\$(?!\s)([^$\n]+?)(?<!\s)\$(?!\$)/g;

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
    .replace(DISPLAY, (_, tex) => `\n\n${render(tex, true)}\n\n`)
    .replace(INLINE, (_, tex) => render(tex, false));
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
