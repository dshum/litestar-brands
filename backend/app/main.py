from litestar import Litestar, get


@get("/")
async def index() -> dict[str, str]:
    return {"endpoint": "index"}


@get("/api")
async def api_index() -> dict[str, str]:
    return {"endpoint": "api_index"}


@get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"endpoint": "healthcheck"}


@get("/api/healthcheck")
async def api_healthcheck() -> dict[str, str]:
    return {"endpoint": "/api/healthcheck"}


def create_app() -> Litestar:
    return Litestar(
        route_handlers=[index, api_index, healthcheck, api_healthcheck],
    )


app = create_app()
