from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig

from app.db.models import Brand


class BrandDTO(SQLAlchemyDTO[Brand]):
    config = DTOConfig(exclude={"settings"})
