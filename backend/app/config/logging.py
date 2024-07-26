import logging

from litestar.logging import LoggingConfig, StructLoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogConfig

from app.config import settings

structlog_config = StructlogConfig(
    structlog_logging_config=StructLoggingConfig(
        log_exceptions="never",
        standard_lib_logging_config=LoggingConfig(
            root={
                "level": logging.getLevelName(settings.log.LEVEL),
                "handlers": ["queue_listener"],
            },
            loggers={
                "saq": {
                    "propagate": False,
                    "level": settings.log.SAQ_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "sqlalchemy.engine": {
                    "propagate": False,
                    "level": settings.log.SQLALCHEMY_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "sqlalchemy.pool": {
                    "propagate": False,
                    "level": settings.log.SQLALCHEMY_LEVEL,
                    "handlers": ["queue_listener"],
                },
            },
        ),
    ),
    middleware_logging_config=LoggingMiddlewareConfig(
        request_log_fields=["method", "path", "path_params", "query", "headers"],
        response_log_fields=["status_code", "headers"],
    ),
)

logger = structlog_config.structlog_logging_config.configure()()
