import enum

from advanced_alchemy.base import AuditColumns, CommonTableAttributes
from sqlalchemy import Text, String, cast
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column, Mapped, column_property

from app.config.sqlalchemy import Base


class Status(enum.Enum):
    Active = "Active"
    Closed = "Closed"
    Dead = "Dead"


class Brand(CommonTableAttributes, AuditColumns, Base):
    __tablename__ = 'brands'

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    settings: Mapped[dict] = mapped_column(JSONB, deferred=True)
    hosts: Mapped[str] = mapped_column(Text)
    status: Mapped[Status] = mapped_column(String(255))
    db_name: Mapped[str] = mapped_column(String(255))
    params: Mapped[dict] = column_property(cast(settings, JSONB)["settings"].label("params"))
