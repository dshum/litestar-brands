<script lang="ts">
	import {invalidate} from "$app/navigation"
	import {getToastStore, type ToastSettings} from "@skeletonlabs/skeleton"

	const toastStore = getToastStore()

  let refreshButtonText: string = "Refresh"

  const onRefresh = async (event: MouseEvent & { currentTarget: EventTarget & HTMLButtonElement; }) => {
    const button = event.currentTarget
    refreshButtonText = "Refreshing..."
    button.disabled = true

    await fetch("/api/brands/refresh", {method: "POST"})
      .then(response => response.json())
      .then(async ({status_code}) => {
        if (status_code > 299) {
          refreshButtonText = "Failed"
          alert(status_code)
        } else {
          refreshButtonText = "Complete"
          await invalidate("/api/brands")
        }
      }).catch(() => {
        refreshButtonText = "Failed"
        alert(500)
      }).finally(() => {
        button.disabled = false
      })
  }

  const alert = (status_code: number) => {
    let message: string
    switch (status_code) {
      case 429:
        message = "Too many requests. Try again in 1 minute."
        break
      default:
        message = "Something went wrong"
        break
    }

    const t: ToastSettings = {
      message: message,
      background: "variant-filled-warning",
      timeout: 5000,
    }
    toastStore.trigger(t)
  }
</script>

<button on:click={onRefresh} class="btn btn-sm variant-filled-primary">
						<span><svg class="w-[16px] h-[16px]" aria-hidden="true"
                       xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
													<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M17.651 7.65a7.131 7.131 0 0 0-12.68 3.15M18.001 4v4h-4m-7.652 8.35a7.13 7.13 0 0 0 12.68-3.15M6 20v-4h4"/>
												</svg></span>
  <span>{refreshButtonText}</span>
</button>