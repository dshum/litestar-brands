from enum import Enum

from advanced_alchemy.base import AuditColumns, CommonTableAttributes
from sqlalchemy import Text, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column, Mapped

from app.config.sqlalchemy import DefaultBase


class Status(Enum):
    Active = "Active"
    Closed = "Closed"
    Dead = "Dead"


class Brand(CommonTableAttributes, AuditColumns, DefaultBase):
    __tablename__ = "brands"

    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    settings: Mapped[dict] = mapped_column(JSONB)
    hosts: Mapped[str] = mapped_column(Text)
    status: Mapped[Status]
    db_name: Mapped[str] = mapped_column(String(255))
