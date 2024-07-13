<script lang="ts">
  import {createEventDispatcher} from "svelte"

  export let params: string[]
  export let settings: { [key: string]: boolean | string | number | object | never; }

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
          class="cursor-pointer">
        <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 24 24"
             style="fill:#BCBCBC;">
          <path
              d="M12,2C6.47,2,2,6.47,2,12c0,5.53,4.47,10,10,10s10-4.47,10-10C22,6.47,17.53,2,12,2z M16.707,15.293 c0.391,0.391,0.391,1.023,0,1.414C16.512,16.902,16.256,17,16,17s-0.512-0.098-0.707-0.293L12,13.414l-3.293,3.293 C8.512,16.902,8.256,17,8,17s-0.512-0.098-0.707-0.293c-0.391-0.391-0.391-1.023,0-1.414L10.586,12L7.293,8.707 c-0.391-0.391-0.391-1.023,0-1.414s1.023-0.391,1.414,0L12,10.586l3.293-3.293c0.391-0.391,1.023-0.391,1.414,0 s0.391,1.023,0,1.414L13.414,12L16.707,15.293z"></path>
        </svg>
      </button>
    </div>
  {/each}
</div>