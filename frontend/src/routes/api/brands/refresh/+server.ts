import {json, type RequestHandler} from "@sveltejs/kit"
import {API_SECRET, API_URL} from "$env/static/private"

export const POST: RequestHandler = async ({fetch}) => {
  const url = `${API_URL}/brands/refresh`
  const response = await fetch(url, {
    method: "POST",
    headers: {"Authorization": `Bearer ${API_SECRET}`},
  })
  const data = await response.json()

  return json(data)
}