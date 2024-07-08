from advanced_alchemy.base import create_registry, CommonTableAttributes, AuditColumns
from advanced_alchemy.config import EngineConfig, AsyncSessionConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from litestar.datastructures import State
from litestar.types import Scope
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.config import settings
from app.lib.ssh import server

ssh_registry = create_registry()


class RemoteUUIDAuditBase(CommonTableAttributes, AuditColumns, DeclarativeBase):
    registry = ssh_registry


class RemoteSQLAlchemyAsyncConfig(SQLAlchemyAsyncConfig):
    def provide_session(self, state: State, scope: Scope) -> AsyncSession:
        if not server.is_alive:
            server.start()
            print("Remote server connected")
        return super().provide_session(state, scope)


remote_sqlalchemy_config = RemoteSQLAlchemyAsyncConfig(
    connection_string=settings.db.remote_url,
    metadata=ssh_registry.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.echo),
    session_dependency_key="remote_db_session",
    engine_dependency_key="remote_db_engine",
    session_maker_app_state_key="remote_session_maker_class",
    engine_app_state_key="remote_db_engine",
)
