<script lang="ts">
  import {createEventDispatcher} from "svelte"

  export let params: string[]
  export let settings: object

  const dispatch = createEventDispatcher()
</script>

<div class="flex flex-col gap-2">
  {#each params as param}
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
      <button
          on:click={() => dispatch("remove-param", param)}
          class="text-xl text-red-500 cursor-pointer">&#215;
      </button>
    </div>
  {/each}
</div>