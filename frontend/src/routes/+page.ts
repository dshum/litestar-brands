import type {PageLoad} from "./$types"

export const load: PageLoad = async ({fetch}) => {
  const getBrands = async () => {
    const response: Response = await fetch("/api/brands")
    return await response.json()
  }

  const getSettings = async () => {
    const response: Response = await fetch("/api/brands/settings")
    return await response.json()
  }

  return {
    brands: await getBrands(),
    settings: await getSettings(),
  }
}