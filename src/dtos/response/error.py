from typing import Optional, Self

from .abstraction import IDTO


class ErrorDTO(IDTO):
    """Concrete error item DTO used inside ``IResponseDTO.errors``."""

    message: str
    code: str
    field: Optional[str] = None
    reference_urn: Optional[str] = None

    @classmethod
    def build(
        cls,
        message: str,
        code: str,
        field: Optional[str] = None,
        reference_urn: Optional[str] = None,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            message=message,
            code=code,
            field=field,
            reference_urn=reference_urn,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ErrorDTO"
