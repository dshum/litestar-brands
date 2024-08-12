<script lang="ts">
  import {fly} from "svelte/transition"
  import type {PageData} from "./$types"
  import type {Brand} from "$lib/types/brand"
  import Status from "$lib/components/Status.svelte"
  import Hosts from "$lib/components/Hosts.svelte"
  import {error} from "@sveltejs/kit"

  export let data: PageData

  if (data.brand.status_code === 404) {
    error(404, {
      code: 404,
      message: "Brand not found",
    })
  } else if (data.brand.message) {
    error(500, {
      code: 500,
      message: "Cannot load brand",
    })
  }

  const brand: Brand = data.brand
  const createdAt: Date = new Date(brand.created_at)
  const settings: { [i: string]: boolean | string | number | object | never; } = brand.settings

  let params = Object.keys(settings).sort()
  let search: string = ""

  $: filteredParams = params.filter((param: string) => {
    return search.trim() === ""
      || param.toLowerCase().includes(search.trim().toLowerCase())
      || (typeof settings[param] === "string"
        && settings[param].toString().toLowerCase().includes(search.trim().toLowerCase()))
  })
</script>

<svelte:head>
  <title>{brand.name} | Brands</title>
</svelte:head>

<h1 class="my-6 h1 first-letter:uppercase">{brand.name}</h1>

<div class="my-6 flex flex-row justify-start items-start gap-16">
  <div>
    <div class="text-sm text-surface-400">Status</div>
    <div class="text-lg">
      <Status bind:status={brand.status}/>
    </div>
  </div>
  <div>
    <div class="text-sm text-surface-400">DB name</div>
    <div class="text-lg">{brand.db_name}</div>
  </div>
  <div>
    <div class="text-sm text-surface-400">Created at</div>
    <div class="text-lg whitespace-nowrap">{createdAt.toDateString()}</div>
  </div>
  <div>
    <div class="text-sm text-surface-400">Hosts</div>
    <div class="text-lg">
      <Hosts bind:hosts={brand.hosts}/>
    </div>
  </div>
</div>

<div class="my-6">
  <div class="w-72">
    <input type="search" bind:value={search} class="input" placeholder="Start typing...">
  </div>
</div>

<div class="my-6 flex flex-col gap-2" in:fly={{delay: 0, duration: 300}}>
  {#each filteredParams as param}
    <div class="bg-surface-400/30 rounded-lg p-2 border-l-8 border-l-surface-400/50">
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
  {/each}
</div>