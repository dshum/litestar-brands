<script lang="ts">

  export let status
</script>

{#if status === "Active"}
  <span class="text-green-600">{status}</span>
{:else if status === "Dead"}
  <span class="text-red-600">{status}</span>
{:else}
  <span>{status}</span>
{/if}