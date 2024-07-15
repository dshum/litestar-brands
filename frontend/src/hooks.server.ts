import {type Handle, redirect} from "@sveltejs/kit"
import {USER_EMAIL, USER_SESSION} from "$env/static/private"

export const handle: Handle = async ({event, resolve}) => {
  const session = event.cookies.get("brands_session")

  if (session && session === USER_SESSION) {
    event.locals.user = {
      email: USER_EMAIL
    }
  } else {
    event.locals.user = null
  }

  switch (true) {
    case event.locals.user && event.url.pathname.startsWith("/login"):
      return redirect(302, "/")
    case event.locals.user && event.url.pathname.startsWith("/logout"):
      break
    case !event.locals.user && !event.url.pathname.startsWith("/login"):
      return redirect(302, "/login")
  }

  return resolve(event)
}