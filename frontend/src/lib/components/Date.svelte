<script lang="ts">
  export let data: string

  const date: Date = new Date(data)
  const year: string = date.getFullYear().toString().padStart(4, "0")
  const month: string = date.getMonth().toString().padStart(2, "0")
  const day: string = date.getDay().toString().padStart(2, "0")
</script>

<span>{year}-{month}-{day}</span>

