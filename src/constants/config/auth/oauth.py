from typing import Final, List
from .abstraction import IConfigurationConstant


class OAuthConfig(IConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/auth/oauth/config.json"
    REDIRECT_URI: Final[str] = "http://localhost:8000/api/v1/auth/oauth/callback"
    EMAIL_SCOPE: Final[str] = "email"
    PROFILE_SCOPE: Final[str] = "profile"
    OPENID_SCOPE: Final[str] = "openid"
    SCOPES: Final[List[str]] = [OPENID_SCOPE, PROFILE_SCOPE, EMAIL_SCOPE]
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "OAuthConfig"
