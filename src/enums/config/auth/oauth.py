"""oauth enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import OAuthConfig


class OAuthConfigENUM(EnumLayer):
    CONFIG_PATH = OAuthConfig.CONFIG_PATH
    REDIRECT_URI = OAuthConfig.REDIRECT_URI
    EMAIL_SCOPE = OAuthConfig.EMAIL_SCOPE
    PROFILE_SCOPE = OAuthConfig.PROFILE_SCOPE
    OPENID_SCOPE = OAuthConfig.OPENID_SCOPE
    SCOPES = OAuthConfig.SCOPES

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "OAuthConfigENUM"

