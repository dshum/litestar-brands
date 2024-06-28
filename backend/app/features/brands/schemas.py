from datetime import datetime

from app.lib.schema import CameCaseBaseStruct


class Brand(CameCaseBaseStruct):
    name: str
    settings: str
    hosts: str
    db_name: str
    created_at: datetime
