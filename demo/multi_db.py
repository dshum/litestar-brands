from typing import Sequence
from uuid import UUID

from advanced_alchemy.base import create_registry, CommonTableAttributes, UUIDPrimaryKey, AuditColumns, UUIDAuditBase
from advanced_alchemy.config import EngineConfig, AsyncSessionConfig
from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from litestar import Litestar, get
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from litestar.di import Provide
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, DeclarativeBase

########## Database ##########

DEFAULT_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:8116/brands"
STATISTICS_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:8116/remote_brands"

stat_registry = create_registry()


class StatUUIDAuditBase(CommonTableAttributes, UUIDPrimaryKey, AuditColumns, DeclarativeBase):
    registry = stat_registry


sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=DEFAULT_DATABASE_URL,
    metadata=UUIDAuditBase.registry.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=True),
    before_send_handler="autocommit",
    create_all=True,
)

stat_sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=STATISTICS_DATABASE_URL,
    metadata=stat_registry.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=True),
    before_send_handler="autocommit",
    session_dependency_key="stat_db_session",
    engine_dependency_key="stat_db_engine",
    session_maker_app_state_key="stat_session_maker_class",
    engine_app_state_key="stat_db_engine",
    create_all=True,
)

sqlalchemy_plugin = SQLAlchemyPlugin(config=[sqlalchemy_config, stat_sqlalchemy_config])


########## Models ##########

class Person(UUIDAuditBase):
    __tablename__ = "person"

    name: Mapped[str]


class PersonRepository(SQLAlchemyAsyncRepository[Person]):
    model_type = Person


class PersonService(SQLAlchemyAsyncRepositoryService[Person]):
    repository_type = PersonRepository


class Statistics(StatUUIDAuditBase):
    __tablename__ = "statistics"

    person_id: Mapped[UUID]
    login_count: Mapped[int]


class StatisticsRepository(SQLAlchemyAsyncRepository[Statistics]):
    model_type = Statistics


class StatisticsService(SQLAlchemyAsyncRepositoryService[Statistics]):
    repository_type = StatisticsRepository


########## Server ##########

async def provide_person_service(db_session: AsyncSession) -> PersonService:
    return PersonService(session=db_session)


async def provide_statistics_service(stat_db_session: AsyncSession) -> StatisticsService:
    return StatisticsService(session=stat_db_session)


@get("/persons", dependencies={"person_service": Provide(provide_person_service)})
async def get_persons(person_service: PersonService) -> Sequence[Person]:
    return await person_service.list()


@get("/statistics", dependencies={"statistics_service": Provide(provide_statistics_service)})
async def get_statistics(statistics_service: StatisticsService) -> Sequence[Statistics]:
    return await statistics_service.list()


########## Application ##########

def create_app() -> Litestar:
    return Litestar(
        route_handlers=[get_persons, get_statistics],
        plugins=[sqlalchemy_plugin],
        debug=True,
    )


app = create_app()
