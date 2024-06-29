from typing import Sequence

from litestar import Controller, get
from litestar.config.response_cache import CACHE_FOREVER
from litestar.di import Provide
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Brand
from app.db.models.brand import Status
from app.features.brands.dependencies import provide_brand_service
from app.features.brands.dtos import BrandDTO
from app.features.brands.services import BrandService


class BrandController(Controller):
    path = "/brands"
    dependencies = {
        "brand_service": Provide(provide_brand_service),
    }

    @get("/", return_dto=BrandDTO, cache=CACHE_FOREVER)
    async def index(
            self,
            brand_service: BrandService,
            status: Status = Status.Active,
    ) -> Sequence[Brand]:
        statement = (select(Brand)
                     .where(Brand.status == status.value)
                     .order_by(Brand.name.asc()))
        return await brand_service.list(statement=statement)

    @get("/settings", cache=CACHE_FOREVER)
    async def settings(
            self,
            db_session: AsyncSession,
    ) -> list[str]:
        query = select(Brand.settings["settings"])
        res = await db_session.execute(query)
        brands = res.all()

        params = []
        for brand in brands:
            params = params | brand[0].keys()

        return list(sorted(params))
