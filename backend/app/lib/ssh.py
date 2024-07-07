from sshtunnel import SSHTunnelForwarder

from app.config import settings

server = SSHTunnelForwarder(
    ssh_address_or_host=settings.ssh.url,
    ssh_username=settings.ssh.user,
    ssh_pkey=settings.ssh.key,
    ssh_private_key_password=settings.ssh.secret,
    remote_bind_address=(settings.ssh.private_server, 5432),
    local_bind_address=("localhost", 6432),
)
