from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from app.db.models import Brand
from app.db.models.remote_brand import RemoteBrand
from app.db.models.test_brand import TestBrand
from app.features.brands.repositories import BrandRepository, RemoteBrandRepository, TestBrandRepository


class BrandService(SQLAlchemyAsyncRepositoryService[Brand]):
    repository_type = BrandRepository


class TestBrandService(SQLAlchemyAsyncRepositoryService[TestBrand]):
    repository_type = TestBrandRepository


class RemoteBrandService(SQLAlchemyAsyncRepositoryService[RemoteBrand]):
    repository_type = RemoteBrandRepository
