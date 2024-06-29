from sqlalchemy.ext.asyncio import AsyncSession

from app.features.brands.services import BrandService


async def provide_brand_service(db_session: AsyncSession) -> BrandService:
    return BrandService(session=db_session)
