<script lang="ts">
  import type {PageData} from "./$types"
  import type Brand from "$lib/types/brand"

  export let data: PageData

  const brand: Brand = data.brand
  const createdAt: Date = new Date(brand.created_at)
  const settings: { [i: string]: boolean | string | number | object | never; } = brand.settings
</script>

<svelte:head>
  <title>{brand.name} | Brands</title>
</svelte:head>

<h1 class="my-6 text-5xl text-slate-500 first-letter:uppercase">{brand.name}</h1>

<div class="my-6 text-2xl text-slate-400">
  <div>Status: {brand.status}</div>
  <div>DB name: {brand.db_name}</div>
  <div>Created at: {createdAt.toDateString()}</div>
</div>

<div class="flex flex-col gap-2">
  {#each Object.keys(settings).sort() as param}
    <div
        class="bg-slate-200 rounded-lg p-2 border-l-8 border-l-slate-300 flex flex-row justify-between items-center space-x-4">
      <div>
        {#if settings[param] === undefined}
          {param}: <span class="text-red-500">Empty</span>
        {:else if settings[param] === false}
          {param}: <span class="text-red-500">false</span>
        {:else if typeof settings[param] === "object"}
          {param}: <span class="">{JSON.stringify(settings[param])}</span>
        {:else if settings[param] instanceof Array}
          {param}: <span class="">{JSON.stringify(settings[param])}</span>
        {:else}
          {param}: <span class="">{settings[param]}</span>
        {/if}
      </div>
    </div>
  {/each}
</div>