"""Base abstraction for service DTOs."""

from ..abstraction import IDTO


class IServiceDTO(IDTO):
    """Marker base for service-layer DTOs."""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IServiceDTO"
