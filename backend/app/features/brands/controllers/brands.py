from typing import Sequence

from litestar import Controller, get, post
from litestar.di import Provide
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Brand
from app.db.models.brand import Status
from app.db.models.remote_brand import RemoteBrand
from app.features.brands.dependencies import (
    provide_brand_service,
    provide_remote_db_session,
    provide_remote_brand_service,
)
from app.features.brands.dtos import BrandDTO
from app.features.brands.services import BrandService, RemoteBrandService


class BrandController(Controller):
    path = "/brands"
    dependencies = {
        "remote_db_session": Provide(provide_remote_db_session),
        "brand_service": Provide(provide_brand_service),
        "remote_brand_service": Provide(provide_remote_brand_service),
    }

    @get("/", cache=600, return_dto=BrandDTO)
    async def index(
            self,
            brand_service: BrandService,
            status: Status | None = None,
    ) -> Sequence[Brand]:
        filters = []
        if status is not None:
            filters.append(Brand.status == status.value)
        statement = (select(Brand)
                     .where(*filters)
                     .order_by(Brand.name.asc()))
        return await brand_service.list(statement=statement)

    @get("/settings", cache=600)
    async def settings(
            self,
            db_session: AsyncSession,
    ) -> list[str]:
        query = select(Brand.settings)
        res = await db_session.execute(query)
        brands = res.all()

        params = []
        for brand in brands:
            params = params | brand[0].keys()

        return list(sorted(params))

    @post("/refresh", return_dto=BrandDTO)
    async def refresh(
            self,
            remote_brand_service: RemoteBrandService,
            brand_service: BrandService,
    ) -> list[Brand]:
        statement = (select(RemoteBrand)
                     .order_by(RemoteBrand.name.asc()))
        remote_brands = await remote_brand_service.list(statement=statement)
        data = [brand.to_dict() for brand in remote_brands]
        return await brand_service.upsert_many(data=data, match_fields=["name"])
