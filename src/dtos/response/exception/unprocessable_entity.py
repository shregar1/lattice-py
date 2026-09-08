"""Unprocessable Entity response DTO."""


from typing import Optional, Self

from .abstraction import IResponseDTO


class UnprocessableEntityResponse(IResponseDTO):
    """Concrete 422 Unprocessable Entity response envelope."""

    @classmethod
    def build(
        cls,
        transaction_urn: str,
        message: str = 'Unprocessable entity payload',
        response_key: str = 'UNPROCESSABLE_ENTITY',
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
        return "UnprocessableEntityResponse"
