from typing import Any

from sqlalchemy import Text, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column, Mapped

from app.config.sqlalchemy import DefaultUUIDAuditBase
from app.db.models.status import Status


class Brand(DefaultUUIDAuditBase):
    __tablename__ = "brands"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    settings: Mapped[dict[str, Any]] = mapped_column(JSONB)
    hosts: Mapped[str] = mapped_column(Text)
    status: Mapped[Status]
    db_name: Mapped[str] = mapped_column(String(255))
