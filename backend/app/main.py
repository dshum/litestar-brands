from litestar import Litestar, get
from litestar.exceptions import TooManyRequestsException

from app.config import sentry, settings
from app.config.cache import cache_config
from app.config.openapi import openapi_config
from app.config.stores import redis_store
from app.features.brands.events import refresh_brands
from app.lib.exceptions import too_many_requests_exception_handler
from app.server.plugins import sqlalchemy_plugin, structlog_plugin, channels
from app.server.routes import router


@get("/")
async def index() -> dict[str, str]:
    return {"status": "OK"}


def create_app() -> Litestar:
    return Litestar(
        route_handlers=[index, router],
        plugins=[sqlalchemy_plugin, structlog_plugin, channels],
        on_startup=[sentry.on_startup],
        listeners=[refresh_brands],
        stores={"redis_store": redis_store},
        response_cache_config=cache_config,
        openapi_config=openapi_config,
        exception_handlers={
            TooManyRequestsException: too_many_requests_exception_handler,
        },
        debug=settings.app.DEBUG,
    )


app = create_app()
