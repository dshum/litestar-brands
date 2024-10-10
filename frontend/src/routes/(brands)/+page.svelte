<script lang="ts">
  import {fly} from "svelte/transition"
  import type {PageData} from "./$types"
  import Hosts from "$lib/components/Hosts.svelte"
  import Status from "$lib/components/Status.svelte"
  import type {Brand} from "$lib/types/brand"
  import {Status as BrandStatus} from "$lib/types/status"
  import {Version} from "$lib/types/version"
  import ExtraParams from "$lib/components/ExtraParams.svelte"
  import {error} from "@sveltejs/kit"
  import Date from "$lib/components/Date.svelte"


  export let data: PageData

  if (data.brands.message) {
    error(500, {
      code: 500,
      message: "Cannot load brands",
    })
  }

  const statuses = Object.values(BrandStatus)
  const versions = Object.values(Version)

  let selectedStatus: string = BrandStatus.Active
  let selectedVersion: string = Version.crm2
  let selectedParam: string = ""
  let selectedParams: string[] = []
  let removeParam: string = ""
  let search: string = ""

  $: filteredBrands = data.brands.filter((brand: Brand) => {
    return selectedStatus ? brand.status === selectedStatus : true
  }).filter((brand: Brand) => {
    return selectedVersion
      ? brand.hosts.toLowerCase().includes(selectedVersion.toLowerCase() + ".")
      : true
  }).filter((brand: Brand) => {
    return search.trim() === ""
      || brand.name.toLowerCase().includes(search.trim().toLowerCase())
      || brand.hosts.toLowerCase().includes(search.trim().toLowerCase())
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
        <option selected={status === selectedStatus}>{status}</option>
      {/each}
    </select>
  </div>

  <div class="min-w-36 w-full md:w-auto">
    <select bind:value={selectedVersion} class="select">
      <option value="">All versions</option>
      {#each versions as version}
        <option selected={version === selectedVersion}>{version}</option>
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
        <option value={param}>{param}</option>
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
      <th class="w-1/12">Created at</th>
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
          <td>
            <Date bind:data={brand.created_at}/>
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
