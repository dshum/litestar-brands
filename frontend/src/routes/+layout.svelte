<script lang="ts">
  import "../app.postcss"
  import {initializeStores, LightSwitch, storePopup, Toast} from "@skeletonlabs/skeleton"
  import {arrow, autoUpdate, computePosition, flip, offset, shift} from "@floating-ui/dom"
  import RefreshButton from "$lib/components/RefreshButton.svelte"

  initializeStores()
  storePopup.set({computePosition, autoUpdate, flip, shift, offset, arrow})
  
  export let data

  const user = data.user
</script>

<Toast/>

<div class="flex flex-col h-screen">
  <div class="backdrop-blur-xl bg-white/20 dark:bg-slate-500/20">
    <div class="container flex flex-row justify-between items-center py-2 gap-6 min-h-12">
      <div class="flex flex-row items-center gap-2">
        <svg class="w-6 h-6 text-secondary-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
             width="24" height="24" fill="none" viewBox="0 0 24 24">
          <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M5 7h14M5 12h14M5 17h10"/>
        </svg>

        <a href="/">Brands</a>
      </div>

      <div class="flex flex-row gap-12 items-center">
        <LightSwitch/>

        {#if user}
          <RefreshButton/>

          <form action="/logout" method="POST">
            <button class="btn btn-sm variant-filled-surface">
								<span><svg class="w-[16px] h-[16px]" aria-hidden="true"
                           xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
													<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M20 12H8m12 0-4 4m4-4-4-4M9 4H7a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h2"/>
												</svg></span>
              <span>Log out</span>
            </button>
          </form>
        {/if}
      </div>
    </div>
  </div>

  <div class="container">
    <slot/>
  </div>
</div>