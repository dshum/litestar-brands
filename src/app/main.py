from litestar import Litestar, get


@get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"status": "OK"}


def create_app() -> Litestar:
    return Litestar(
        route_handlers=[healthcheck],
    )


app = create_app()
