from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin

from app.config.sqlalchemy import sqlalchemy_config

sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)
