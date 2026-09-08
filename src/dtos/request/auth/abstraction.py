"""Base abstraction for auth request DTOs."""

from .abstraction import IRequestDTO


class IAuthRequestDTO(IRequestDTO):
    """Marker base for authentication request DTOs."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAuthRequestDTO"
