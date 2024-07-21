from typing import Any

from advanced_alchemy.exceptions import RepositoryError, NotFoundError, ConflictError, IntegrityError
from litestar import Request, Response
from litestar.exceptions import HTTPException, NotFoundException, PermissionDeniedException, InternalServerException
from litestar.exceptions.responses import ExceptionResponseContent, create_debug_response, create_exception_response
from litestar.status_codes import HTTP_409_CONFLICT
from redis.exceptions import AuthorizationError


class ApplicationError(Exception):
    """Base exception type for the lib's custom exception types."""

    detail: str

    def __init__(self, *args: Any, detail: str = "") -> None:
        str_args = [str(arg) for arg in args if arg]
        if not detail:
            if str_args:
                detail, *str_args = str_args
            elif hasattr(self, "detail"):
                detail = self.detail
        self.detail = detail
        super().__init__(*str_args)

    def __repr__(self) -> str:
        if self.detail:
            return f"{self.__class__.__name__} - {self.detail}"
        return self.__class__.__name__

    def __str__(self) -> str:
        return " ".join((*self.args, self.detail)).strip()


class HTTPConflictException(HTTPException):
    status_code = HTTP_409_CONFLICT


def exception_to_http_response(
        request: Request[Any, Any, Any],
        exc: ApplicationError | RepositoryError,
) -> Response[ExceptionResponseContent]:
    http_exc: type[HTTPException]

    if isinstance(exc, NotFoundError):
        http_exc = NotFoundException
    elif isinstance(exc, ConflictError | RepositoryError | IntegrityError):
        http_exc = HTTPConflictException
    elif isinstance(exc, AuthorizationError):
        http_exc = PermissionDeniedException
    else:
        http_exc = InternalServerException

    if request.app.debug and http_exc not in (PermissionDeniedException, NotFoundException, PermissionDeniedException):
        return create_debug_response(request, exc)
    return create_exception_response(request, http_exc(detail=str(exc)))
