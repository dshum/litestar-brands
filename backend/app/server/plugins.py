from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar.channels import ChannelsPlugin
from litestar.channels.backends.memory import MemoryChannelsBackend
from litestar.plugins.structlog import StructlogPlugin

from app.config.logging import structlog_config
from app.config.remote_sqlalchemy import remote_sqlalchemy_config
from app.config.sqlalchemy import sqlalchemy_config

sqlalchemy_plugin = SQLAlchemyPlugin(config=[sqlalchemy_config, remote_sqlalchemy_config])

structlog_plugin = StructlogPlugin(config=structlog_config)

channels = ChannelsPlugin(
    backend=MemoryChannelsBackend(),
    channels=["brands"],
    create_ws_route_handlers=True,
)
