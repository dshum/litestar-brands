<script lang="ts">
	import type { ActionData } from "./$types"

	export let form: ActionData
</script>

<div class="my-6 flex flex-row justify-center m-auto">
	<div class="flex flex-col min-w-72 justify-center gap-4">
		<h1 class="h1">Log in</h1>

		{#if form?.missing}
			<p class="error">The email field is required</p>
		{/if}

		{#if form?.incorrect}
			<p class="error">Invalid credentials!</p>
		{/if}

		<form method="POST">
			<div class="flex flex-col gap-4">
				<label class="label">
					<span>Email</span>
					<input name="email" type="email" value={form?.email ?? ""} class="input"
								 autocomplete="on"
					>
				</label>

				<label class="label">
					<span>Password</span>
					<input name="password" type="password" class="input"
								 autocomplete="current-password"
					>
				</label>

				<label>
					<button>Log in</button>
				</label>
			</div>
		</form>
	</div>
</div>

<style lang="postcss">
    input {
        @apply w-full py-2 px-4 rounded-lg border border-slate-400 outline-0 bg-slate-50;
    }

    button {
        @apply w-full rounded-lg shadow-lg bg-primary-500 text-white py-2 px-8;
    }

    p.error {
        @apply w-full rounded-lg bg-error-500 text-white py-2 px-4;
    }
</style>