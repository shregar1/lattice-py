"""Base abstraction for health controllers."""

from abstractions import ControllerLayer


class IHealthController(ControllerLayer):
    """Marker base for all controllers served under the health."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IHealthController"
