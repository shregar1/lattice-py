"""Register request DTO."""

from pydantic import Field
from constants import DTO
from .abstraction import IAuthRequestDTO


class RegisterRequestDTO(IAuthRequestDTO):
    """Request payload DTO for user registration."""

    email: str = Field(..., description="User email address")
    password: str = Field(..., description="User password")
    auth_type_id: int = Field(..., description="Authentication type ID")

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RegisterRequestDTO"
