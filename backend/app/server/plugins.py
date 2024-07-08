from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin

from app.config.remote_sqlalchemy import remote_sqlalchemy_config
from app.config.sqlalchemy import sqlalchemy_config

sqlalchemy_plugin = SQLAlchemyPlugin(config=[sqlalchemy_config, remote_sqlalchemy_config])
