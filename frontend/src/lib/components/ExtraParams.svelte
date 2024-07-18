<script lang="ts">
	import { createEventDispatcher } from "svelte"

	export let params: string[]
	export let settings: { [key: string]: boolean | string | number | object | never; }

	const dispatch = createEventDispatcher()
</script>

<div class="flex flex-col gap-2">
	{#each params as param}
		<div class="bg-surface-400/30 rounded-lg p-2 border-l-8 border-l-surface-400/50
								flex flex-row justify-between items-center space-x-4">
			<div>
				<span>{param}:</span>

				{#if settings[param] === undefined || settings[param] === ""}
					<span class="text-red-500">Empty</span>
				{:else if settings[param] === true}
					<span class="text-primary-600 dark:text-success-500">true</span>
				{:else if settings[param] === false}
					<span class="text-red-500">false</span>
				{:else if typeof settings[param] === "object"}
					<span class="">{JSON.stringify(settings[param])}</span>
				{:else if settings[param] instanceof Array}
					<span class="">{JSON.stringify(settings[param])}</span>
				{:else}
					<span class="">{settings[param]}</span>
				{/if}
			</div>

			<button on:click={() => dispatch("remove-param", param)} class="">
				<svg class="w-6 h-6 text-surface-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
						 width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
					<path fill-rule="evenodd"
								d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm7.707-3.707a1 1 0 0 0-1.414 1.414L10.586 12l-2.293 2.293a1 1 0 1 0 1.414 1.414L12 13.414l2.293 2.293a1 1 0 0 0 1.414-1.414L13.414 12l2.293-2.293a1 1 0 0 0-1.414-1.414L12 10.586 9.707 8.293Z"
								clip-rule="evenodd" />
				</svg>
			</button>
		</div>
	{/each}
</div>