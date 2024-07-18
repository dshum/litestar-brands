import type { Actions, PageServerLoad } from "./$types"
import { redirect } from "@sveltejs/kit"
import { SESSION_NAME } from "$lib/constants"

export const load: PageServerLoad = async () => {
	return redirect(302, "/")
}

export const actions = {
	default: async ({ cookies }) => {
		cookies.set(SESSION_NAME, "", {
			path: "/",
			expires: new Date(0)
		})

		return redirect(302, "/login")
	}
} satisfies Actions