import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	css: {
		preprocessorOptions: {
			scss: {
				includePaths: ['node_modules'],
				additionalData: '@use "variables.scss" as *;'
			}
		}
	}
});
