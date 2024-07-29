from typing import Sequence

from litestar.events import listener
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import settings
from app.config.logging import logger
from app.config.stores import redis_store
from app.db.models import RemoteBrand
from app.features.brands.services import RemoteBrandService, BrandService
from app.lib.ssh import server
from app.server.plugins import channels


@listener("refresh_brands")
async def refresh_brands() -> None:
    logger.info("Start refreshing brands")
    try:
        remote_brands = await get_remote_brands()
        await update_local_brands(remote_brands)
        channels.publish({"message": "Brands have been updated"}, "brands")
    except Exception as err:
        logger.error("Error while refreshing brands", error=err)


async def get_remote_brands() -> Sequence[RemoteBrand]:
    remote_engine = create_async_engine(url=settings.db.REMOTE_URL, pool_pre_ping=True)
    remote_async_session = async_sessionmaker(remote_engine, expire_on_commit=False)

    if not server.is_alive:
        server.start()
        logger.info("Remote server connected")

    async with remote_async_session() as session:
        logger.info("Remote session opened")

        remote_brand_service = RemoteBrandService(session=session)
        statement = (select(RemoteBrand)
                     .order_by(RemoteBrand.name.asc()))
        remote_brands = await remote_brand_service.list(statement=statement)
        logger.info("Remote brands received")

        await session.close()
        logger.info("Remote session closed")

    if server.is_alive:
        server.stop()
        logger.info("Remote server disconnected")

    return remote_brands


async def update_local_brands(remote_brands: Sequence[RemoteBrand]):
    data = [brand.to_dict() for brand in remote_brands]

    local_engine = create_async_engine(url=settings.db.URL, pool_pre_ping=True)
    local_async_session = async_sessionmaker(local_engine, expire_on_commit=False)

    async with local_async_session() as session:
        logger.info("Local session opened")

        brand_service = BrandService(session=session)
        await brand_service.upsert_many(data=data, match_fields=["name"], auto_commit=True)
        logger.info("Local brands refreshed")
        await session.close()
        logger.info("Local session closed")

        await redis_store.delete_all()
        logger.info("Redis cache cleaned")
