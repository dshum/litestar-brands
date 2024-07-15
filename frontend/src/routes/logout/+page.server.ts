import type {Actions} from "./$types"
import {redirect} from "@sveltejs/kit"

export const load: PageServerLoad = async () => {
  return redirect(302, "/")
}

export const actions = {
  default: async ({cookies}) => {
    cookies.set("brands_session", "", {
      path: "/",
      expires: new Date(0),
    })

    return redirect(302, "/login")
  },
} satisfies Actions