<script lang="ts">
  import type {ActionData} from "./$types"

  export let form: ActionData
</script>

<div class="flex flex-row justify-center">
  <div class="flex flex-col min-w-72 min-h-screen justify-center gap-4">
    {#if form?.missing}
      <p class="error">The email field is required</p>
    {/if}

    {#if form?.incorrect}
      <p class="error">Invalid credentials!</p>
    {/if}

    <div class="rounded-xl shadow-xl bg-white p-4">
      <form method="POST">
        <div class="flex flex-col gap-4">
          <label>
            <div>Email</div>
            <div><input name="email" type="email" value={form?.email ?? ""}></div>
          </label>

          <label>
            <div>Password</div>
            <div><input name="password" type="password"></div>
          </label>

          <div>
            <button>Log in</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</div>

<style lang="postcss">
    input {
        @apply w-full py-2 px-4 rounded-lg border border-slate-400 outline-0 bg-slate-50;
    }

    button {
        @apply w-full rounded-lg shadow-lg bg-blue-600 text-white py-2 px-8;
    }

    p.error {
        @apply w-full rounded-lg bg-red-500 text-white py-2 px-4;
    }
</style>