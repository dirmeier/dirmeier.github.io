import { resolve } from 'node:path';
import adapter from '@sveltejs/adapter-auto';
import { mdsvex } from 'mdsvex';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import rehypeSlug from 'rehype-slug';
import { escapeTextBraces, katexMath } from './katex-preprocess.js';
import { highlightFence } from './shiki-preprocess.js';

// katexMath runs first: mdsvex uses its own markdown parser, so micromark-based
// remark plugins (remark-math, remark-gfm) never fire. Rehype plugins do, and
// mdsvex handles GFM tables natively.
/** @type {import('@sveltejs/kit').Config} */
const config = {
  extensions: ['.svelte', '.svx'],
  preprocess: [
    katexMath(),
    mdsvex({
      extensions: ['.svx'],
      // mdsvex reads this path off disk and re-emits it as the import
      // specifier, so it has to be absolute — neither $lib nor a relative
      // path works for both jobs.
      layout: { _: resolve('src/lib/PostLayout.svelte') },
      rehypePlugins: [
        rehypeSlug,
        [rehypeAutolinkHeadings, { behavior: 'wrap' }]
      ],
      highlight: { highlighter: highlightFence }
    }),
    escapeTextBraces()
  ],
  kit: {
    adapter: adapter()
  }
};

export default config;
