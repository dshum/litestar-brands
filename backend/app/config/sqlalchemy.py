from advanced_alchemy import AsyncSessionConfig
from advanced_alchemy.config import EngineConfig
from advanced_alchemy.extensions.litestar.plugins.init.config.asyncio import autocommit_before_send_handler
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from sqlalchemy.orm import declarative_base

from app.config import settings

Base = declarative_base()

sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.url,
    metadata=Base.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.echo),
    before_send_handler=autocommit_before_send_handler,
    create_all=True,
)
