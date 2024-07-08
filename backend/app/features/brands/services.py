from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from app.db.models import Brand
from app.db.models.remote_brand import RemoteBrand
from app.features.brands.repositories import BrandRepository, RemoteBrandRepository


class BrandService(SQLAlchemyAsyncRepositoryService[Brand]):
    repository_type = BrandRepository


class RemoteBrandService(SQLAlchemyAsyncRepositoryService[RemoteBrand]):
    repository_type = RemoteBrandRepository
