import type {PageLoad} from "./$types"

export const load: PageLoad = async ({cookies, fetch}) => {
  const getBrands = async () => {
    const response: Response = await fetch("/api/brands")
    return await response.json()
  }

  const getSettings = async () => {
    const response: Response = await fetch("/api/brands/settings")
    return await response.json()
  }

  // console.log(cookies.get)

  return {
    brands: await getBrands(),
    settings: await getSettings(),
  }
}