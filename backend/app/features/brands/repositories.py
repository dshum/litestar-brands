from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db.models import Brand
from app.db.models.remote_brand import RemoteBrand
from app.db.models.test_brand import TestBrand


class BrandRepository(SQLAlchemyAsyncRepository[Brand]):
    model_type = Brand
    id_attribute = "name"


class TestBrandRepository(SQLAlchemyAsyncRepository[TestBrand]):
    model_type = TestBrand
    id_attribute = "name"


class RemoteBrandRepository(SQLAlchemyAsyncRepository[RemoteBrand]):
    model_type = RemoteBrand
    id_attribute = "name"
