from advanced_alchemy import SQLAlchemyAsyncRepository

from app.db.models import Brand


class BrandRepository(SQLAlchemyAsyncRepository[Brand]):
    model_type = Brand
