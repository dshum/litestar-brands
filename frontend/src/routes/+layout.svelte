<script lang="ts">
	import {LightSwitch, storePopup} from "@skeletonlabs/skeleton"
	import "../app.postcss"

	// Floating UI for Popups
	import {arrow, autoUpdate, computePosition, flip, offset, shift} from "@floating-ui/dom"
	import {invalidate} from "$app/navigation"

	storePopup.set({computePosition, autoUpdate, flip, shift, offset, arrow})

  export let data

  const user = data.user
  let refreshButtonText: string = "Refresh"

  const onRefresh = async (event: MouseEvent & { currentTarget: EventTarget & HTMLButtonElement; }) => {
    const button = event.currentTarget
    refreshButtonText = "Refreshing..."
    button.disabled = true

    try {
      let response = await fetch("/api/brands/refresh", {method: "POST"})
      refreshButtonText = response.ok ? "Complete" : "Failed"
      await invalidate("/api/brands")
    } catch {
      refreshButtonText = "Failed"
    } finally {
      button.disabled = false
    }
  }
</script>

<div class="flex flex-col h-screen">
  <div class="backdrop-blur-xl bg-white/20 dark:bg-slate-500/20">
    <div class="container flex flex-row justify-between items-center py-2 gap-6">
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
          <button on:click={onRefresh} class="btn btn-sm variant-filled-primary">
						<span><svg class="w-[16px] h-[16px]" aria-hidden="true"
                       xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
													<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M17.651 7.65a7.131 7.131 0 0 0-12.68 3.15M18.001 4v4h-4m-7.652 8.35a7.13 7.13 0 0 0 12.68-3.15M6 20v-4h4"/>
												</svg></span>
            <span>{refreshButtonText}</span>
          </button>

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