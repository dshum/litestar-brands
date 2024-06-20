import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		port: 5000,
		host: '0.0.0.0',
		strictPort: false
	},
	preview: {
		port: 4173,
		host: '0.0.0.0',
		strictPort: false
	},
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});
