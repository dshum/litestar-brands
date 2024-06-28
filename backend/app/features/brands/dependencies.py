from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import load_only

from app.db.models import Brand
from app.features.brands.services import BrandService


async def provide_brand_service(db_session: AsyncSession) -> BrandService:
    statement = (select(Brand)
                 .options(load_only(Brand.name, Brand.hosts, Brand.status, Brand.db_name))
                 .order_by(Brand.name))
    return BrandService(session=db_session, statement=statement)
