from litestar.connection import ASGIConnection
from litestar.exceptions import NotAuthorizedException
from litestar.handlers import BaseRouteHandler

from app.config import settings


def token_guard(connection: ASGIConnection, route_handler: BaseRouteHandler) -> None:
    if connection.headers.get("Authorization", "") != f"Bearer {settings.app.SECRET}":
        raise NotAuthorizedException("Invalid token")
