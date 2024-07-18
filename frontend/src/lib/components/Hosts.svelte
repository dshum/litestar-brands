<script lang="ts">
	export let hosts: string
	$: linkedHosts = hosts.split(",").map((item: string) => {
		return item.trim()
	})
</script>

<div class="flex flex-row flex-wrap gap-x-4">
	{#each linkedHosts as host}
		<a href="https://{host}" target="_blank" class="underline">{host}</a>
	{/each}
</div>