"""middleware enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Middleware


class MiddlewareENUM(EnumLayer):
    CONTENT_SECURITY_POLICY = Middleware.CONTENT_SECURITY_POLICY
    X_FRAME_OPTIONS = Middleware.X_FRAME_OPTIONS
    X_CONTENT_TYPE_OPTIONS = Middleware.X_CONTENT_TYPE_OPTIONS
    REFERRER_POLICY = Middleware.REFERRER_POLICY
    PERMISSIONS_POLICY = Middleware.PERMISSIONS_POLICY
    SECURITY_HEADERS = Middleware.SECURITY_HEADERS

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "MiddlewareENUM"

