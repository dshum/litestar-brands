from litestar.types import ASGIApp, Scope, Receive, Send
from sshtunnel import open_tunnel

from app.config import settings


def ssh_tunnel_middleware_factory(app: ASGIApp) -> ASGIApp:
    async def ssh_tunnel_middleware(scope: Scope, receive: Receive, send: Send) -> None:
        with open_tunnel(
                ssh_address_or_host=(settings.ssh.url, 22),
                ssh_username=settings.ssh.user,
                ssh_pkey=settings.ssh.key,
                ssh_private_key_password=settings.ssh.secret,
                remote_bind_address=(settings.ssh.private_server, 5432),
                local_bind_address=("localhost", 6432)
        ) as tunnel:
            await app(scope, receive, send)

    return ssh_tunnel_middleware
