"""Logout request DTO."""

from pydantic import Field
from typing import Optional
from constants import DTO
from .abstraction import IAuthRequestDTO


class LogoutRequestDTO(IAuthRequestDTO):
    """Request payload DTO for user logout."""

    user_urn: Optional[str] = Field(None, description="Optional user URN to logout")

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "LogoutRequestDTO"
