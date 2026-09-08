"""Base abstraction for authentication API controllers."""

from ..abstraction import IV1Controller


class IAuthController(IV1Controller):
    """Marker base for all controllers in the auth domain under v1 API."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAuthController"

