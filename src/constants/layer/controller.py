from typing import Final

from .abstraction import ILayerConstant


class Controller(ILayerConstant):

    LOGIN_AUTH: Final[str] = "LoginAuthController"
    REGISTER_AUTH: Final[str] = "RegisterAuthController"
    LOGOUT_AUTH: Final[str] = "LogoutAuthController"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Controller"
