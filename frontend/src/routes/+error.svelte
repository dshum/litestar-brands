<script lang="ts">
  import {page} from "$app/stores"
</script>

<svelte:head>
  <title>Error {$page.error?.code || 500}</title>
</svelte:head>

<h1 class="my-6 text-3xl">{$page.error?.code || 500}</h1>
<div class="my-3 text-lg">{$page.error?.message}</div>