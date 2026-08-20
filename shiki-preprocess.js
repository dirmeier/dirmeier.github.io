import { createHighlighter } from 'shiki';

const LANGS = ['python', 'cpp', 'clojure'];
const THEMES = { light: 'github-light', dark: 'github-dark' };
// Tolerant of Prettier's split-tag output, which breaks after `<pre` and after
// the class attribute rather than keeping the tags on one line.
const CODE_RE =
  /<pre\s*><code\s+class="language-(\w+)"\s*>([\s\S]*?)<\/code\s*><\/pre\s*>/g;

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

// Shiki's output is spliced straight into a Svelte component, so braces have to
// go back to entities or Svelte reads them as expressions.
function forSvelte(html) {
  return html
    .replace(/ tabindex="0"/g, '')
    .replace(/{/g, '&lbrace;')
    .replace(/}/g, '&rbrace;');
}

function escapeHtml(source) {
  return source
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/{/g, '&lbrace;')
    .replace(/}/g, '&rbrace;');
}

// mdsvex highlighter for fenced code blocks. Unlike the preprocessor below it
// gets raw source and a language straight from the fence, so there is no HTML
// to parse and nothing to decode.
export async function highlightFence(code, lang) {
  if (!lang) return `<pre><code>${escapeHtml(code)}</code></pre>`;

  const highlighter = await getHighlighter();
  if (!highlighter.getLoadedLanguages().includes(lang)) {
    try {
      await highlighter.loadLanguage(lang);
    } catch {
      return `<pre><code>${escapeHtml(code)}</code></pre>`;
    }
  }
  return forSvelte(highlighter.codeToHtml(code, { lang, themes: THEMES }));
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
        const html = forSvelte(
          highlighter.codeToHtml(decode(raw), { lang, themes: THEMES })
        );
        out += content.slice(last, match.index) + html;
        last = match.index + full.length;
      }
      out += content.slice(last);
      return { code: out };
    }
  };
}
