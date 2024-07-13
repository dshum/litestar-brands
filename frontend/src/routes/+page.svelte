<script lang="ts">
  import {fly} from "svelte/transition"
  import type {PageData} from "./$types"
  import Hosts from "$lib/components/Hosts.svelte"
  import Status from "$lib/components/Status.svelte"
  import ExtraParams from "$lib/components/ExtraParams.svelte"
  import type {Brand} from "$lib/interfaces/brand"
  import BrandStatus from "$lib/interfaces/status"

  export let data: PageData

  const statuses = Object.values(BrandStatus)

  let selectedStatus: string = ""
  let selectedParam: string = ""
  let selectedParams: Array<string> = []
  let removeParam: string = ""

  $: filteredBrands = data.brands.filter((brand: Brand) => {
    return selectedStatus ? brand.status === selectedStatus : true
  })

  $: {
    if (selectedParam && !selectedParams.includes(selectedParam)) {
      selectedParams = [...selectedParams, selectedParam]
    }
  }

  $: {
    if (removeParam) {
      let index = selectedParams.indexOf(removeParam)
      selectedParams = selectedParams.toSpliced(index, 1)
      removeParam = ""
    }
  }

  const removeParamHandler = (event: CustomEvent) => {
    removeParam = event.detail
  }
</script>

<svelte:head>
  <title>Brands</title>
</svelte:head>

<div class="my-6 flex flex-row justify-between items-center">
  <div>
    <select bind:value={selectedStatus}
            class="py-2 px-4 rounded-xl shadow-xl border-none outline-0 bg-white">
      <option value="">All statuses</option>
      {#each statuses as status}
        <option value="{status}">{status}</option>
      {/each}
    </select>
  </div>

  <div>
    <select bind:value={selectedParam}
            class="py-2 px-4 rounded-xl shadow-xl border-none outline-0 bg-white">
      <option value="">Add BM variable</option>
      {#each data.settings as param}
        <option value="{param}">{param}</option>
      {/each}
    </select>
  </div>
</div>

<div
    in:fly={{delay: 0, duration: 300}}
    class="my-6 rounded-3xl shadow-2xl p-6 bg-white break-all">
  <table class="w-full border-collapse">
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
        <tr class="bg-white even:bg-slate-100">
          <td class="p-2">{brand.name}</td>
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
                  on:remove-param={removeParamHandler}
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