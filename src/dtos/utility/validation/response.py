"""Response-validation context DTO."""

from typing import Any, Dict, List, Optional, Self

from .abstraction import IValidationUtilityDTO


class ResponseValidationContext(IValidationUtilityDTO):
    """Context describing the response slice under validation."""

    status_code: int
    body: Optional[Dict[str, Any] | List[Any]] = None
    headers: Optional[Dict[str, str]] = None

    @classmethod
    def build(
        cls,
        status_code: int,
        body: Optional[Dict[str, Any] | List[Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            status_code=status_code,
            body=body,
            headers=headers,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ResponseValidationContext"
