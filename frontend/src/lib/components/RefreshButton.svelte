<script lang="ts">
	import {onMount} from "svelte"
	import {getToastStore, type ToastSettings} from "@skeletonlabs/skeleton"
	import {invalidate} from "$app/navigation"
	import {PUBLIC_WS_URL} from "$env/static/public"

	const toastStore = getToastStore()

  const onRefresh = async (event: MouseEvent & { currentTarget: EventTarget & HTMLButtonElement; }) => {
    const button = event.currentTarget
    button.disabled = true

    try {
      const response = await fetch("/api/brands/refresh", {method: "POST"})
      const data = await response.json()
      if (response.status > 299) {
        onRefreshError(response.status, data.message)
      } else if (data.status_code > 299) {
        onRefreshError(data.status_code, data.detail)
      } else {
        await onRefreshSuccess()
      }
    } catch {
      onRefreshError(500, "Something went wrong")
    } finally {
      button.disabled = false
    }
  }

  const onRefreshSuccess = async () => {
    toast("Brand updates added to the queue", "tertiary")
  }

  const onRefreshError = (status_code: number, detail: string) => {
    if (status_code < 500) {
      toast(detail, "warning")
    } else {
      toast(detail, "error")
    }
  }

  const toast = (message: string, type: string, timeout: number = 5000) => {
    const t: ToastSettings = {
      message: message,
      background: `variant-filled-${type}`,
      timeout: timeout,
    }
    toastStore.trigger(t)
  }

  onMount(() => {
    const ws = new WebSocket(`${PUBLIC_WS_URL}/brands`)

    ws.onmessage = async (event) => {
      const data = JSON.parse(event.data)

      if (data.message) {
        if (data.status === "error") {
          toast(data.message, "error")
        } else {
          await invalidate("/api/brands")
          toast(data.message, "success")
        }
      }
    }
  })
</script>

<button on:click={onRefresh} class="btn btn-sm variant-filled-primary">
	<span><svg class="w-[16px] h-[16px]" aria-hidden="true"
             xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
			<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M17.651 7.65a7.131 7.131 0 0 0-12.68 3.15M18.001 4v4h-4m-7.652 8.35a7.13 7.13 0 0 0 12.68-3.15M6 20v-4h4"/>
		</svg></span>
  <span>Refresh</span>
</button>