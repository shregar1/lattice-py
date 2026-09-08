"""Base abstraction for v1 API controllers."""

from abstractions import ControllerLayer


class IAPIController(ControllerLayer):
    """Marker base for all controllers served under the API."""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAPIController"
