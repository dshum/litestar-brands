import {json, type RequestHandler} from "@sveltejs/kit"
import {API_URL} from "$env/static/private"

export const GET: RequestHandler = async ({setHeaders}) => {
  const URL = `${API_URL}/brands`

  const response = await fetch(URL)
  const data = await response.json()

  setHeaders({"cache-control": "max-age=300"})

  return json(data)
}