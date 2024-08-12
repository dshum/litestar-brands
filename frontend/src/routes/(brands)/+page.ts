import type {PageLoad} from "../../../.svelte-kit/types/src/routes/(brands)/$types"

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