import adapter from '@sveltejs/adapter-auto';
import { shikiHighlight } from './shiki-preprocess.js';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: [shikiHighlight()],
  kit: {
    adapter: adapter()
  }
};

export default config;
