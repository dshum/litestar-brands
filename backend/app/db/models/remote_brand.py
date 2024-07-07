from advanced_alchemy.base import CommonTableAttributes, AuditColumns
from sqlalchemy import String, Text, cast
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, column_property

from app.config.remote_sqlalchemy import RemoteBase


class RemoteBrand(CommonTableAttributes, AuditColumns, RemoteBase):
    __tablename__ = "brands"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    _settings: Mapped[dict] = mapped_column("settings", JSONB, deferred=True)
    hosts: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(255))
    db_name: Mapped[str] = mapped_column(String(255))
    settings: Mapped[dict] = column_property(cast(_settings, JSONB)["settings"])
