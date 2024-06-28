from typing import Sequence

from litestar import Controller, get
from litestar.di import Provide

from app.db.models import Brand
from app.features.brands.dependencies import provide_brand_service
from app.features.brands.dtos import BrandDTO
from app.features.brands.services import BrandService


class BrandController(Controller):
    path = "/brands"
    dependencies = {
        "brand_service": Provide(provide_brand_service),
    }

    @get("/", return_dto=BrandDTO)
    async def index(self, brand_service: BrandService) -> Sequence[Brand]:
        return await brand_service.list()
