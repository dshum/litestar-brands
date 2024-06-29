from typing import Sequence

from litestar import Controller, get
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
        # "remote_brand_service": Provide(provide_remote_brand_service),
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
        query = select(Brand.settings["settings"])
        res = await db_session.execute(query)
        brands = res.all()

        params = []
        for brand in brands:
            params = params | brand[0].keys()

        return list(sorted(params))

    # @get("/refresh", return_dto=BrandDTO)
    # async def refresh(
    #         self,
    #         brand_service: BrandService,
    # ) -> Sequence[Brand]:
    #     with sshtunnel.open_tunnel(
    #             ssh_address_or_host=(settings.ssh.url, 22),
    #             ssh_username=settings.ssh.user,
    #             ssh_pkey=settings.ssh.key,
    #             ssh_private_key_password=settings.ssh.secret,
    #             remote_bind_address=(settings.ssh.private_server, 5432),
    #             local_bind_address=("localhost", 6432)
    #     ) as tunnel:
    #         statement = (select(Brand)
    #                      .order_by(Brand.name.asc()))
    #         brands = await brand_service.list(statement=statement)
    #     return brands

    # @post("/refresh2")
    # async def refresh2(
    #         self,
    #         remote_db_session: AsyncSession,
    # ) -> None:
    #     server = sshtunnel.SSHTunnelForwarder(
    #         ssh_address_or_host=settings.ssh.url,
    #         ssh_username=settings.ssh.user,
    #         ssh_pkey=settings.ssh.key,
    #         ssh_private_key_password=settings.ssh.secret,
    #         remote_bind_address=(settings.ssh.private_server, 5432),
    #         local_bind_address=("localhost", 6432),
    #     )
    #     server.start()
    #     query = select(Brand.name).order_by(Brand.name.asc())
    #     res = await remote_db_session.execute(query)
    #     brands = res.all()
    #     server.stop()
    #     return None
