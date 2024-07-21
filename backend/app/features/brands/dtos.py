from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.db.models import Brand, RemoteBrand


class BrandDTO(SQLAlchemyDTO[Brand]):
    config = SQLAlchemyDTOConfig()


class RemoteBrandDTO(SQLAlchemyDTO[RemoteBrand]):
    config = SQLAlchemyDTOConfig()
