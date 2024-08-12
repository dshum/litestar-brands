from typing import Any

from advanced_alchemy.exceptions import NotFoundError
from litestar import Request
from litestar.exceptions import (
    NotFoundException,
    TooManyRequestsException,
)
from litestar.exceptions.responses import (
    create_exception_response,
)
from litestar.status_codes import HTTP_404_NOT_FOUND


def default_exception_handler(
        request: Request[Any, Any, Any],
        exception: TooManyRequestsException,
):
    return create_exception_response(request, exception)


def not_found_exception_handler(
        request: Request[Any, Any, Any],
        exception: NotFoundError | NotFoundException,
):
    exception = NotFoundException(status_code=HTTP_404_NOT_FOUND, detail=exception.detail)
    return create_exception_response(request, exception)


def too_many_requests_exception_handler(
        request: Request[Any, Any, Any],
        exception: TooManyRequestsException,
):
    exception.detail = "Too many requests. Try again in 1 minute"
    return create_exception_response(request, exception)
