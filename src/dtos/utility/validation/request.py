"""Request-validation context DTO."""

from typing import Any, Dict, List, Optional, Self

from .abstraction import IValidationUtilityDTO


class RequestValidationContext(IValidationUtilityDTO):
    """Context describing the request slice under validation."""

    body: Optional[Dict[str, Any] | List[Any]] = None
    query_params: Optional[Dict[str, Any]] = None
    path_params: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None

    @classmethod
    def build(
        cls,
        body: Optional[Dict[str, Any] | List[Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        path_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Self:
        """Constructs a RequestValidationContext instance."""
        return cls(
            body=body,
            query_params=query_params,
            path_params=path_params,
            headers=headers,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RequestValidationContext"
