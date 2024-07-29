from typing import Any

from litestar import Request
from litestar.exceptions import (
    TooManyRequestsException,
)
from litestar.exceptions.responses import (
    create_exception_response,
)


def too_many_requests_exception_handler(
        request: Request[Any, Any, Any],
        exception: TooManyRequestsException,
):
    exception.detail = "Too many requests. Try again in 1 minute"
    return create_exception_response(request, exception)
