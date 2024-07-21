from advanced_alchemy.base import create_registry, CommonTableAttributes, AuditColumns
from advanced_alchemy.config import AsyncSessionConfig
from advanced_alchemy.extensions.litestar import EngineConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

default_registry = create_registry()


class DefaultUUIDAuditBase(CommonTableAttributes, AuditColumns, DeclarativeBase):
    registry = default_registry


sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.url,
    metadata=default_registry.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.echo),
    before_send_handler="autocommit",
    create_all=True,
)
