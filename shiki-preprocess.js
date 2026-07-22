import { createHighlighter } from 'shiki';

const LANGS = ['python', 'cpp', 'clojure'];
const THEMES = { light: 'github-light', dark: 'github-dark' };
const CODE_RE = /<pre><code class="language-(\w+)">([\s\S]*?)<\/code><\/pre>/g;

// Entities are decoded to raw source before highlighting; &amp; must be last so
// an escaped entity like &amp;lt; does not get decoded twice.
const DECODE = [
  [/&lt;/g, '<'],
  [/&gt;/g, '>'],
  [/&quot;/g, '"'],
  [/&#39;/g, "'"],
  [/&lbrace;/g, '{'],
  [/&rbrace;/g, '}'],
  [/&amp;/g, '&']
];

let highlighterPromise;
function getHighlighter() {
  if (!highlighterPromise) {
    highlighterPromise = createHighlighter({
      themes: Object.values(THEMES),
      langs: LANGS
    });
  }
  return highlighterPromise;
}

function decode(source) {
  return DECODE.reduce((acc, [re, ch]) => acc.replace(re, ch), source);
}

// Highlights hand-written <pre><code class="language-*"> blocks at build time.
// Only tagged blocks are touched; untagged code is left as plain markup. Braces
// in Shiki's output are re-escaped so Svelte does not read them as expressions.
export function shikiHighlight() {
  return {
    name: 'shiki-highlight',
    async markup({ content }) {
      if (!content.includes('language-')) return;
      const matches = [...content.matchAll(CODE_RE)];
      if (matches.length === 0) return;

      const highlighter = await getHighlighter();
      let out = '';
      let last = 0;
      for (const match of matches) {
        const [full, lang, raw] = match;
        if (!highlighter.getLoadedLanguages().includes(lang)) {
          await highlighter.loadLanguage(lang);
        }
        const html = highlighter
          .codeToHtml(decode(raw), { lang, themes: THEMES })
          .replace(/ tabindex="0"/g, '')
          .replace(/{/g, '&lbrace;')
          .replace(/}/g, '&rbrace;');
        out += content.slice(last, match.index) + html;
        last = match.index + full.length;
      }
      out += content.slice(last);
      return { code: out };
    }
  };
}
