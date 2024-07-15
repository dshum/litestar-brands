<script lang="ts">
  import {fly} from "svelte/transition"
  import type {PageData} from "./$types"
  import Hosts from "$lib/components/Hosts.svelte"
  import Status from "$lib/components/Status.svelte"
  import ExtraParams from "$lib/components/ExtraParams.svelte"
  import type {Brand} from "$lib/types/brand"
  import {Status as BrandStatus} from "$lib/types/status"
  import {Version} from "$lib/types/version"

  export let data: PageData

  const statuses = Object.entries(BrandStatus)
  const versions = Object.entries(Version)

  let selectedStatus: string = ""
  let selectedVersion: string = ""
  let selectedParam: string = ""
  let selectedParams: string[] = []
  let removeParam: string = ""
  let search: string = ""

  $: filteredBrands = data.brands.filter((brand: Brand) => {
    return selectedStatus ? brand.status === selectedStatus : true
  }).filter((brand: Brand) => {
    return selectedVersion ? brand.hosts.includes(selectedVersion + ".") : true
  }).filter((brand: Brand) => {
    return search.trim() === ""
      || brand.name.toLowerCase().includes(search.trim().toLowerCase())
      || brand.db_name.toLowerCase().includes(search.trim().toLowerCase())
  })

  $: {
    if (selectedParam && !selectedParams.includes(selectedParam)) {
      selectedParams = [...selectedParams, selectedParam]
      selectedParam = ""
    }
  }

  $: {
    if (removeParam) {
      let index = selectedParams.indexOf(removeParam)
      if (index > -1) {
        selectedParams = selectedParams.toSpliced(index, 1)
      }
      removeParam = ""
    }
  }

  const onRemoveParam = (event: CustomEvent) => {
    removeParam = event.detail
  }

  const onRefresh = async (event: MouseEvent & { currentTarget: EventTarget & HTMLButtonElement; }) => {
    const button = event.currentTarget
    button.disabled = true
    button.textContent = "Refreshing..."
    await fetch("/api/brands/refresh", {method: "POST"})
    button.textContent = "Complete"
    button.disabled = false
  }
</script>

<svelte:head>
  <title>Brands</title>
</svelte:head>

<div class="my-6 flex flex-row flex-wrap xl:flex-nowrap justify-between items-center gap-4">
  <div class="min-w-36 w-full md:w-auto">
    <select bind:value={selectedStatus}
            class="w-full py-2 px-4 rounded-xl shadow-lg border-none outline-0 bg-white">
      <option value="">All statuses</option>
      {#each statuses as status}
        <option class="max-w-sm" value="{status[0]}">{status[1]}</option>
      {/each}
    </select>
  </div>

  <div class="min-w-36 w-full md:w-auto">
    <select bind:value={selectedVersion}
            class="w-full py-2 px-4 rounded-xl shadow-lg border-none outline-0 bg-white">
      <option value="">All versions</option>
      {#each versions as version}
        <option class="max-w-sm" value="{version[0]}">{version[1]}</option>
      {/each}
    </select>
  </div>

  <div class="min-w-72 w-full md:w-auto">
    <input type="search" bind:value={search}
           class="w-full py-2 px-4 rounded-xl shadow-lg border-none outline-0 bg-white"
           placeholder="Start typing..."
    >
  </div>

  <div class="w-full md:max-w-72">
    <select bind:value={selectedParam}
            class="w-full py-2 px-4 rounded-xl shadow-lg border-none outline-0 bg-white">
      <option value="">Add BM variable</option>
      {#each data.settings as param}
        <option value="{param}">{param}</option>
      {/each}
    </select>
  </div>

  <div class="flex flex-row gap-4">
    <button on:click={onRefresh}
            class="py-2 px-4 rounded-xl shadow-lg bg-white text-blue-500 whitespace-nowrap">
      Refresh
    </button>

    <form action="/logout" method="POST">
      <button
          class="py-2 px-4 rounded-xl shadow-lg bg-white text-blue-500 whitespace-nowrap">Log
        out
      </button>
    </form>
  </div>
</div>

<div
    in:fly={{delay: 0, duration: 300}}
    class="my-6 rounded-3xl shadow-md p-6 bg-white break-all w-full overflow-x-auto">
  <table class="w-full min-w-[800px] border-collapse">
    <tr class="border-b-2 border-b-slate-300 text-slate-400 text-left">
      <th class="p-2 w-1/6">Name</th>
      <th class="p-2 w-4/12">Hosts</th>
      <th class="p-2 w-1/12">DB name</th>
      <th class="p-2 w-1/12">Status</th>
      {#if selectedParams.length}
        <th class="p-2 w-1/3">Settings</th>
      {/if}
    </tr>
    {#if filteredBrands.length}
      {#each filteredBrands as brand (brand.name)}
        <tr data-brand-name={brand.name} class="bg-white even:bg-slate-100">
          <td class="p-2"><a href="/{brand.name}" class="underline">{brand.name}</a></td>
          <td class="p-2 text-wrap">
            <Hosts bind:hosts={brand.hosts}/>
          </td>
          <td class="p-2">{brand.db_name}</td>
          <td class="p-2">
            <Status bind:status={brand.status}/>
          </td>
          {#if selectedParams.length}
            <td class="p-2 break-all">
              <ExtraParams
                  bind:params={selectedParams} bind:settings={brand.settings}
                  on:remove-param={onRemoveParam}
              />
            </td>
          {/if}
        </tr>
      {/each}
    {:else}
      <tr class="bg-white">
        <td class="p-6 text-center" colspan={selectedParams.length ? 5 : 4}>No brands found</td>
      </tr>
    {/if}
  </table>
</div>