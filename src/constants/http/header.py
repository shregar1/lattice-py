from typing import Final
from .abstraction import IHTTPConstant


class HTTPHeader(IHTTPConstant):

    REQUEST_ID: Final[str] = "x-request-id"
    USER_URN: Final[str] = "x-user-urn"
    USER_ID: Final[str] = "x-subject-id"
    CONTENT_TYPE: Final[str] = "content-type"
    CONTENT_LENGTH: Final[str] = "content-length"
    ACCEPT: Final[str] = "accept"
    AUTHORIZATION: Final[str] = "authorization"
    CONTENT_SECURITY_POLICY: Final[str] = "content-security-policy"
    FRAME_OPTIONS: Final[str] = "x-frame-options"
    CONTENT_TYPE_OPTIONS: Final[str] = "x-content-type-options"
    REFERRER_POLICY: Final[str] = "referrer-policy"
    PERMISSIONS_POLICY: Final[str] = "permissions-policy"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "HTTPHeader"
