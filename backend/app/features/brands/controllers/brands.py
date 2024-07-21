from typing import Sequence

from litestar import Controller, get, post
from litestar.di import Provide
from litestar.params import Parameter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.stores import redis_store
from app.db.models import Brand
from app.db.models.remote_brand import RemoteBrand
from app.db.models.status import Status
from app.features.brands.dependencies import (
    provide_brand_service,
    provide_remote_brand_service,
)
from app.features.brands.dtos import BrandDTO, RemoteBrandDTO
from app.features.brands.services import BrandService, RemoteBrandService


class BrandController(Controller):
    path = "/brands"
    dependencies = {
        "brand_service": Provide(provide_brand_service),
        "remote_brand_service": Provide(provide_remote_brand_service),
    }

    @get("/", return_dto=BrandDTO, cache=3600)
    async def get_brands(
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

    @get("/{name:str}", return_dto=BrandDTO, cache=3600)
    async def get_brand(
            self,
            brand_service: BrandService,
            name: str = Parameter(title="Brand name")
    ) -> Brand:
        return await brand_service.get(name)

    @get("/settings", cache=3600)
    async def get_settings(
            self,
            db_session: AsyncSession,
    ) -> list[str]:
        query = select(Brand.settings)
        res = await db_session.execute(query)
        brands = res.all()

        params: list[str] = []
        for brand in brands:
            params = params | brand[0].keys()

        return list(sorted(params))

    @post("/refresh", return_dto=BrandDTO)
    async def refresh(
            self,
            remote_brand_service: RemoteBrandService,
            brand_service: BrandService,
    ) -> dict[str, str]:
        statement = (select(RemoteBrand)
                     .order_by(RemoteBrand.name.asc()))
        remote_brands = await remote_brand_service.list(statement=statement)
        data = [brand.to_dict() for brand in remote_brands]
        await brand_service.upsert_many(data=data, match_fields=["name"])
        await redis_store.delete_all()
        return {"result": "refreshed"}

    @get("/remote", return_dto=RemoteBrandDTO)
    async def remote(
            self,
            remote_brand_service: RemoteBrandService,
            brand_service: BrandService,
    ) -> Sequence[RemoteBrand]:
        statement = (select(RemoteBrand)
                     .order_by(RemoteBrand.name.asc()))
        return await remote_brand_service.list(statement=statement)
