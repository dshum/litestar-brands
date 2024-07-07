from sqlalchemy.ext.asyncio import AsyncSession

from app.features.brands.services import BrandService, RemoteBrandService, TestBrandService


async def provide_brand_service(db_session: AsyncSession) -> BrandService:
    return BrandService(session=db_session)


async def provide_test_brand_service(test_db_session: AsyncSession) -> TestBrandService:
    return TestBrandService(session=test_db_session)


async def provide_remote_brand_service(remote_db_session: AsyncSession) -> RemoteBrandService:
    return RemoteBrandService(session=remote_db_session)
