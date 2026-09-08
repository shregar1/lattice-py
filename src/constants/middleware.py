from typing import Final, List, Tuple

from .abstraction import IConstant
from constants import HTTPHeader


class Middleware(IConstant):

    CONTENT_SECURITY_POLICY: Final[str] = "default-src 'self'"
    X_FRAME_OPTIONS: Final[str] = "DENY"
    X_CONTENT_TYPE_OPTIONS: Final[str] = "nosniff"
    REFERRER_POLICY: Final[str] = "strict-origin-when-cross-origin"
    PERMISSIONS_POLICY: Final[str] = "geolocation=(), microphone=(), camera=()"
    SECURITY_HEADERS: Final[List[Tuple[str, str]]] = [
        (HTTPHeader.CONTENT_SECURITY_POLICY, CONTENT_SECURITY_POLICY),
        (HTTPHeader.FRAME_OPTIONS, X_FRAME_OPTIONS),
        (HTTPHeader.CONTENT_TYPE_OPTIONS, X_CONTENT_TYPE_OPTIONS),
        (HTTPHeader.REFERRER_POLICY, REFERRER_POLICY),
        (HTTPHeader.PERMISSIONS_POLICY, PERMISSIONS_POLICY),
    ]

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Middleware"
