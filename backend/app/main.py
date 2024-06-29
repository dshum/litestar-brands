from litestar import Litestar, get

from app.config.cache import cache_config
from app.config.openapi import openapi_config
from app.config.stores import redis_store
from app.server.plugins import sqlalchemy_plugin
from app.server.routes import router


@get("/")
async def index() -> dict[str, str]:
    return {"status": "OK"}


def create_app() -> Litestar:
    return Litestar(
        route_handlers=[index, router],
        plugins=[sqlalchemy_plugin],
        stores={"redis_store": redis_store},
        response_cache_config=cache_config,
        openapi_config=openapi_config,
        debug=True,
    )


app = create_app()
