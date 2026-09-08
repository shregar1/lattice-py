from typing import Final

from .abstraction import ILayerConstant


class Orchestrator(ILayerConstant):

    LOGIN_AUTH: Final[str] = "LoginAuthOrchestrator"
    REGISTER_AUTH: Final[str] = "RegisterAuthOrchestrator"
    LOGOUT_AUTH: Final[str] = "LogoutAuthOrchestrator"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Orchestrator"
