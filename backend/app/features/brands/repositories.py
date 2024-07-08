from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db.models import Brand
from app.db.models.remote_brand import RemoteBrand


class BrandRepository(SQLAlchemyAsyncRepository[Brand]):
    model_type = Brand
    id_attribute = "name"


class RemoteBrandRepository(SQLAlchemyAsyncRepository[RemoteBrand]):
    model_type = RemoteBrand
    id_attribute = "name"
