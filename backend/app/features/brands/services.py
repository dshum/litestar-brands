from advanced_alchemy import SQLAlchemyAsyncRepositoryService

from app.db.models import Brand
from app.features.brands.repositories import BrandRepository


class BrandService(SQLAlchemyAsyncRepositoryService[Brand]):
    repository_type = BrandRepository
