from pathlib import Path
from typing import Final

from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = [
    "BASE_DIR",
    "app",
    "db",
    "redis",
]

BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="app_")

    url: str = "http://localhost:8000"
    secret: str
    debug: bool = True


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="redis_")

    location: str = "redis://localhost:6379/1"
    namespace: str = "BRANDS"


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="database_")

    url: str = ""
    echo: bool = True


app = AppSettings.model_validate({})
db = DatabaseSettings.model_validate({})
redis = RedisSettings.model_validate({})
