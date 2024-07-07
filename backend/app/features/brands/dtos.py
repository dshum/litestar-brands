from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig

from app.db.models import Brand, RemoteBrand
from app.db.models.test_brand import TestBrand


class BrandDTO(SQLAlchemyDTO[Brand]):
    config = DTOConfig()


class TestBrandDTO(SQLAlchemyDTO[TestBrand]):
    config = DTOConfig(exclude={"settings"})


class RemoteBrandDTO(SQLAlchemyDTO[RemoteBrand]):
    config = DTOConfig()
