import type {PageLoad} from "./$types"

export const load: PageLoad = async ({params, fetch}) => {
  console.log(`/api/brands/${params.name}`)
  const getBrand = async () => {
    const response: Response = await fetch(`/api/brands/${params.name}`)
    return await response.json()
  }

  return {
    brand: await getBrand(),
  }
}