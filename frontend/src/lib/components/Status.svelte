<script lang="ts">
	import { Status } from "$lib/types/status"

	export let status: string
</script>

{#if status === Status.Active}
	<span class="text-primary-600 dark:text-success-500">{status}</span>
{:else if status === Status.Dead}
	<span class="text-error-500">{status}</span>
{:else}
	<span>{status}</span>
{/if}
