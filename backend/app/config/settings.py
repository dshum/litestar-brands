from pathlib import Path
from typing import Final

from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = [
    "BASE_DIR",
    "app",
    "log",
    "db",
    "redis",
    "ssh",
    "sentry",
]

BASE_DIR: Final[Path] = Path(__file__).parent.parent.resolve()


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_")

    URL: str = "http://localhost:8000"
    SECRET: str
    ENVIRONMENT: str = "development"
    BUILD_NUMBER: str = "0"
    DEBUG: bool = False


class LogSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="LOG_")

    LEVEL: str = "INFO"
    SAQ_LEVEL: Final[str] = "INFO"
    SQLALCHEMY_LEVEL: Final[str] = "INFO"


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="REDIS_")

    LOCATION: str = "redis://localhost:6379/1"
    NAMESPACE: str = "BRANDS"


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DATABASE_")

    URL: str
    REMOTE_URL: str
    BACKGROUND_REMOTE_URL: str
    TEST_REMOTE_URL: str
    ECHO: bool = False


class SSHSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SSH_")

    URL: str
    PRIVATE_SERVER: str
    USER: str
    KEY: str
    SECRET: str


class SentrySettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SENTRY_")

    DSN: str
    TRACES_SAMPLE_RATE: float = 0.0
    ENABLE: bool = False


app = AppSettings.model_validate({})
log = LogSettings.model_validate({})
db = DatabaseSettings.model_validate({})
redis = RedisSettings.model_validate({})
ssh = SSHSettings.model_validate({})
sentry = SentrySettings.model_validate({})
