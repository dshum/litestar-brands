import { join } from "path"
import type { Config } from "tailwindcss"
import { skeleton } from "@skeletonlabs/tw-plugin"
import forms from "@tailwindcss/forms"
import typography from "@tailwindcss/typography"

export default {
	darkMode: "selector",
	content: ["./src/**/*.{html,js,svelte,ts}", join(require.resolve("@skeletonlabs/skeleton"), "../**/*.{html,js,svelte,ts}")],
	theme: {
		container: {
			center: true,
			padding: {
				DEFAULT: "1rem",
				sm: "1rem",
				lg: "2rem",
			},
		},
		extend: {},
	},
	plugins: [
		forms,
		typography,
		skeleton({
			themes: {
				preset: [
					{
						name: "skeleton",
						enhancements: true,
					},
				],
			},
		}),
	],
} satisfies Config
