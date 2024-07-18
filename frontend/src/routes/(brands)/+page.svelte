<script lang="ts">
	import {fly} from "svelte/transition"
	import type {PageData} from "./$types"
	import Hosts from "$lib/components/Hosts.svelte"
	import Status from "$lib/components/Status.svelte"
	import type {Brand} from "$lib/types/brand"
	import {Status as BrandStatus} from "$lib/types/status"
	import {Version} from "$lib/types/version"
	import ExtraParams from "$lib/components/ExtraParams.svelte"


	export let data: PageData

  const statuses = Object.entries(BrandStatus)
  const versions = Object.entries(Version)

  let selectedStatus: string = "Active"
  let selectedVersion: string = "crm2"
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
</script>

<svelte:head>
  <title>Brands</title>
</svelte:head>

<div class="my-6 flex flex-row flex-wrap xl:flex-nowrap justify-between items-center gap-4">
  <div class="min-w-36 w-full md:w-auto">
    <select bind:value={selectedStatus} class="select">
      <option value="">All statuses</option>
      {#each statuses as status}
        <option class="max-w-sm" value="{status[0]}">{status[1]}</option>
      {/each}
    </select>
  </div>

  <div class="min-w-36 w-full md:w-auto">
    <select bind:value={selectedVersion} class="select">
      <option value="">All versions</option>
      {#each versions as version}
        <option class="max-w-sm" value="{version[0]}">{version[1]}</option>
      {/each}
    </select>
  </div>

  <div class="min-w-72 w-full md:w-auto">
    <input type="search" bind:value={search} class="input" placeholder="Start typing...">
  </div>

  <div class="w-full md:max-w-72">
    <select bind:value={selectedParam} class="select">
      <option value="">Add BM variable</option>
      {#each data.settings as param}
        <option value="{param}">{param}</option>
      {/each}
    </select>
  </div>
</div>

<div class="my-6 table-container" in:fly={{delay: 0, duration: 300}}>
  <table class="table table-hover">
    <thead>
    <tr>
      <th class="w-1/6">Name</th>
      <th class="w-1/3">Hosts</th>
      <th class="w-1/12">DB name</th>
      <th class="w-1/12 text-right">Status</th>
      {#if selectedParams.length}
        <th class="w-1/3">Settings</th>
      {/if}
    </tr>
    </thead>

    <tbody>
    {#if filteredBrands.length}
      {#each filteredBrands as brand}
        <tr>
          <td>
            <a href="/{brand.name}" class="underline">{brand.name}</a>
          </td>
          <td>
            <Hosts bind:hosts={brand.hosts}/>
          </td>
          <td>{brand.db_name}</td>
          <td class="text-right">
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
      <tr>
        <td class="text-center" colspan={selectedParams.length ? 5 : 4}>No brands found</td>
      </tr>
    {/if}
    </tbody>

    <tfoot>
    <tr>
      <th colspan={selectedParams.length ? 4 : 3}>Brands totally</th>
      <td class="text-right">{filteredBrands.length}</td>
    </tr>
    </tfoot>
  </table>
</div>
