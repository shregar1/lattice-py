"""Login request DTO."""

from pydantic import Field
from constants import DTO
from .abstraction import IAuthRequestDTO


class LoginRequestDTO(IAuthRequestDTO):
    """Request payload DTO for user login."""

    email: str = Field(..., description="User email address")
    password: str = Field(..., description="User password")

    @property
    def name(self) -> str:
        """Returns the class name."""
        return DTO.LOGIN_REQUEST
