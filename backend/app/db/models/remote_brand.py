from sqlalchemy import String, Text, cast
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, column_property

from app.config.remote_sqlalchemy import RemoteUUIDAuditBase
from app.db.models.status import Status


class RemoteBrand(RemoteUUIDAuditBase):
    __tablename__ = "brands"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    _settings: Mapped[dict] = mapped_column("settings", JSONB, deferred=True)
    hosts: Mapped[str] = mapped_column(Text)
    status: Mapped[Status]
    db_name: Mapped[str] = mapped_column(String(255))
    settings: Mapped[dict] = column_property(cast(_settings, JSONB)["settings"])
