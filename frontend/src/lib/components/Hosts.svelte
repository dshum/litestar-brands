<script lang="ts">
  export let hosts
  const linkedHosts = hosts.split(",").map((item) => {
    return item.trim()
  })
</script>

<div class="flex flex-row flex-wrap">
  {#each linkedHosts as host}
    <a href="https://{host}" target="_blank" class="mx-2 underline">{host}</a>
  {/each}
</div>