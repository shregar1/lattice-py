"""Forbidden response DTO."""


from typing import Optional, Self

from .abstraction import IResponseDTO


class ForbiddenResponse(IResponseDTO):
    """Concrete 403 Forbidden response envelope."""

    @classmethod
    def build(
        cls,
        transaction_urn: str,
        message: str = 'Action forbidden',
        response_key: str = 'FORBIDDEN',
        status: str = "FAILED",
        data=None,
        errors=None,
        metadata=None,
        timestamp=None,
        reference_urn: Optional[str] = None,
    ) -> Self:
        """
        Method to ....
        """
        return super().build(
            transaction_urn=transaction_urn,
            response_message=message,
            response_key=response_key,
            status=status,
            data=data,
            errors=errors or [],
            metadata=metadata,
            timestamp=timestamp,
            reference_urn=reference_urn,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ForbiddenResponse"
