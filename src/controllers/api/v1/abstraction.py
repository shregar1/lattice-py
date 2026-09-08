"""Base abstraction for v1 API controllers."""

from ..abstraction import IAPIController


class IV1Controller(IAPIController):
    """Marker base for all controllers served under the v1 API version."""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IV1Controller"
