from advanced_alchemy.base import create_registry, CommonTableAttributes, AuditColumns
from advanced_alchemy.config import AsyncSessionConfig
from advanced_alchemy.extensions.litestar import EngineConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

ssh_registry = create_registry()


class RemoteUUIDAuditBase(CommonTableAttributes, AuditColumns, DeclarativeBase):
    registry = ssh_registry


remote_sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.REMOTE_URL,
    metadata=ssh_registry.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.ECHO),
    session_dependency_key="remote_db_session",
    engine_dependency_key="remote_db_engine",
)

"""
class RemoteSQLAlchemyAsyncConfig(SQLAlchemyAsyncConfig):
    def provide_session(self, state: State, scope: Scope) -> AsyncSession:
        if not server.is_alive:
            server.start()
            logger.info("Remote server connected")
        return super().provide_session(state, scope)


def get_aa_scope_state(scope: Scope, key: str, default: Any = None, pop: bool = False) -> Any:
    namespace = scope.setdefault("_aa_connection_state", {})
    return namespace.pop(key, default) if pop else namespace.get(key, default)


def delete_aa_scope_state(scope: Scope, key: str) -> None:
    del scope.setdefault("_aa_connection_state", {})[key]


def remote_handler_maker(
        session_scope_key: str = SESSION_SCOPE_KEY,
) -> Callable[[Message, Scope], Coroutine[Any, Any, None]]:
    async def handler(message: Message, scope: Scope) -> None:
        session = cast("AsyncSession | None", get_aa_scope_state(scope, session_scope_key))
        if session and message["type"] in SESSION_TERMINUS_ASGI_EVENTS:
            await session.close()
            logger.info("Remote session closed")
            delete_aa_scope_state(scope, session_scope_key)

            if server.is_alive:
                server.stop()
                logger.info("Remote server disconnected")

    return handler


remote_before_send_handler = remote_handler_maker()
"""
