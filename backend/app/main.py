from litestar import Litestar, get
from litestar.openapi import OpenAPIConfig


@get("/")
async def index() -> dict[str, str]:
    return {"endpoint": "index"}


@get("/backend")
async def api_index() -> dict[str, str]:
    return {"endpoint": "backend/index"}


@get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"endpoint": "healthcheck"}


@get("/backend/healthcheck")
async def api_healthcheck() -> dict[str, str]:
    return {"endpoint": "/backend/healthcheck"}


openapi_config = OpenAPIConfig(title="Brands API", version="1.0.0", path="/backend/schema")


def create_app() -> Litestar:
    return Litestar(
        route_handlers=[index, api_index, healthcheck, api_healthcheck],
        openapi_config=openapi_config,
    )


app = create_app()
