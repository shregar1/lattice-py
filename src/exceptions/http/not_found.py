"""NotFoundException — raised when a requested resource does not exist."""

from typing import Any, Optional
from constants import ExceptionCode, ExceptionKey
from constants import HTTPStatus
from .abstraction import IException


class NotFoundException(IException):
    """
    Raised when a resource lookup by id or key returns no result.
    Attributes:
        code: Stable machine-readable code for this exception class.
        status_code: HTTP status code returned to the caller.
        key: Stable exception key used by the envelope factory.
        resource: Name of the resource type that was not found.
        entity_id: Optional identifier that was looked up.
    """

    code = ExceptionCode.NOT_FOUND
    status_code = HTTPStatus.NOT_FOUND
    key = ExceptionKey.NOT_FOUND

    def __init__(
        self,
        resource: str,
        entity_id: Optional[str] = None,
        **context: Any,
    ) -> None:
        """
        Initializes the exception with the resource name and optional identifier.
        Args:
            resource: Name of the resource type that was not found.
            entity_id: Optional identifier that was looked up.
            **context: Additional structured fields attached to the exception.
        """
        detail = (
            f"{resource} not found" if entity_id is None else f"{resource} '{entity_id}' not found"
        )
        super().__init__(detail, **context)
        self.resource = resource
        self.entity_id = entity_id

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "NotFoundException"
