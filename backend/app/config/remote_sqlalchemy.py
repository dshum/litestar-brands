from advanced_alchemy.config import EngineConfig, AsyncSessionConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from litestar.datastructures import State
from litestar.types import Scope
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base

from app.config import settings

RemoteBase = declarative_base()


class SSHTunnelSQLAlchemyAsyncConfig(SQLAlchemyAsyncConfig):
    def provide_session(self, state: State, scope: Scope) -> AsyncSession:
        # server.start()
        return super().provide_session(state, scope)


remote_sqlalchemy_config = SSHTunnelSQLAlchemyAsyncConfig(
    connection_string=settings.db.remote_url,
    metadata=RemoteBase.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.echo),
    session_dependency_key="remote_db_session",
    engine_dependency_key="remote_db_engine",
)
