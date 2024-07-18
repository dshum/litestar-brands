import type { Actions } from "./$types"
import { fail, redirect } from "@sveltejs/kit"
import { USER_EMAIL, USER_PASSWORD, USER_SESSION } from "$env/static/private"
import { SESSION_NAME } from "$lib/constants"

export const actions = {
	default: async ({ cookies, request }) => {
		const data = await request.formData()
		const email = data.get("email")
		const password = data.get("password")

		if (!email) {
			return fail(400, { email, missing: true })
		}

		if (email !== USER_EMAIL || password !== USER_PASSWORD) {
			return fail(400, { email, incorrect: true })
		}

		cookies.set(SESSION_NAME, USER_SESSION, {
			path: "/",
			httpOnly: true,
		})

		return redirect(302, "/")
	},
} satisfies Actions