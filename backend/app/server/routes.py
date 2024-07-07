from litestar import Router

from app.features.brands.controllers.brands import BrandController

router: Router = Router(
    path="/",
    route_handlers=[
        BrandController,
    ],
    # guards=[token_guard],
)

__all__ = ["router"]
