from sshtunnel import SSHTunnelForwarder

from app.config import settings

params = {
    "ssh_address_or_host": settings.ssh.URL,
    "ssh_username": settings.ssh.USER,
    "ssh_pkey": settings.ssh.KEY,
    "ssh_private_key_password": settings.ssh.SECRET,
    "remote_bind_address": (settings.ssh.PRIVATE_SERVER, 5432),
    # "local_bind_address": ("localhost", 6432),
}

server = SSHTunnelForwarder(local_bind_address=("localhost", 6432), **params)
background_server = SSHTunnelForwarder(local_bind_address=("localhost", 6433), **params)
