from typing import Coroutine, Callable, Any, cast

from advanced_alchemy.base import create_registry, CommonTableAttributes, AuditColumns
from advanced_alchemy.config import AsyncSessionConfig
from advanced_alchemy.extensions.litestar import EngineConfig
from advanced_alchemy.extensions.litestar._utils import get_aa_scope_state, delete_aa_scope_state
from advanced_alchemy.extensions.litestar.plugins.init.config.common import SESSION_SCOPE_KEY, \
    SESSION_TERMINUS_ASGI_EVENTS
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from litestar.datastructures import State
from litestar.types import Scope, Message
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
            print("Remote server not alive")
            server.start()
            print("Remote server connected")
        return super().provide_session(state, scope)


def remote_handler_maker(
        session_scope_key: str = SESSION_SCOPE_KEY,
) -> Callable[[Message, Scope], Coroutine[Any, Any, None]]:
    async def handler(message: Message, scope: Scope) -> None:
        session = cast("AsyncSession | None", get_aa_scope_state(scope, session_scope_key))
        if session and message["type"] in SESSION_TERMINUS_ASGI_EVENTS:
            await session.close()
            delete_aa_scope_state(scope, session_scope_key)
        if server.is_alive:
            print("Remote server is alive")
            server.stop()
            print("Remote server disconnected")

    return handler


remote_before_send_handler = remote_handler_maker()

remote_sqlalchemy_config = RemoteSQLAlchemyAsyncConfig(
    connection_string=settings.db.remote_url,
    metadata=ssh_registry.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.echo),
    session_dependency_key="remote_db_session",
    engine_dependency_key="remote_db_engine",
    before_send_handler=remote_before_send_handler,
)
