from sqlalchemy.ext.asyncio import AsyncSession
from sshtunnel import open_tunnel

from app.config import settings
from app.config.sqlalchemy import remote_async_session
from app.features.brands.services import BrandService


async def provide_brand_service(db_session: AsyncSession) -> BrandService:
    return BrandService(session=db_session)


async def provide_remote_brand_service(remote_db_session: AsyncSession) -> BrandService:
    return BrandService(session=remote_db_session)


async def provide_remote_db_session() -> AsyncSession:
    with open_tunnel(
            ssh_address_or_host=(settings.ssh.url, 22),
            ssh_username=settings.ssh.user,
            ssh_pkey=settings.ssh.key,
            ssh_private_key_password=settings.ssh.secret,
            remote_bind_address=(settings.ssh.private_server, 5432),
            local_bind_address=("localhost", 6432)
    ) as tunnel:
        async with remote_async_session() as session:
            yield session
            session.close()
