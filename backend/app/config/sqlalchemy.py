from advanced_alchemy.config import EngineConfig, AsyncSessionConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


class DefaultBase(DeclarativeBase):
    ...


class TestRemoteBase(DeclarativeBase):
    ...


sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.url,
    metadata=DefaultBase.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.echo),
    before_send_handler="autocommit",
    create_all=True,
)

test_sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.test_remote_url,
    metadata=TestRemoteBase.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.echo),
    # before_send_handler=autocommit_before_send_handler,
    # create_all=True,
    session_dependency_key="test_db_session",
    engine_dependency_key="test_db_engine",
    # session_scope_key="_sqlalchemy_test_db_session",
)
