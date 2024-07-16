import {json, type RequestHandler} from "@sveltejs/kit"
import {API_URL} from "$env/static/private"

export const POST: RequestHandler = async () => {
  const URL = `${API_URL}/brands/refresh`

  const response = await fetch(URL, {method: "POST"})
  const data = await response.json()

  return json(data)
}