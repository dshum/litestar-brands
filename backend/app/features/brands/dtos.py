from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig

from app.db.models import Brand, RemoteBrand


class BrandDTO(SQLAlchemyDTO[Brand]):
    config = DTOConfig()


class RemoteBrandDTO(SQLAlchemyDTO[RemoteBrand]):
    config = DTOConfig()
