from litestar import Router

from app.features.brands.controllers.brands import BrandController
from app.server.guards import token_guard

router: Router = Router(
    path="/",
    route_handlers=[
        BrandController,
    ],
    guards=[token_guard],
)

__all__ = ["router"]
