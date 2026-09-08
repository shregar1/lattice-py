"""header enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import HTTPHeader


class HTTPHeaderENUM(EnumLayer):
    REQUEST_ID = HTTPHeader.REQUEST_ID
    USER_URN = HTTPHeader.USER_URN
    USER_ID = HTTPHeader.USER_ID
    CONTENT_TYPE = HTTPHeader.CONTENT_TYPE
    CONTENT_LENGTH = HTTPHeader.CONTENT_LENGTH
    ACCEPT = HTTPHeader.ACCEPT
    AUTHORIZATION = HTTPHeader.AUTHORIZATION
    CONTENT_SECURITY_POLICY = HTTPHeader.CONTENT_SECURITY_POLICY
    FRAME_OPTIONS = HTTPHeader.FRAME_OPTIONS
    CONTENT_TYPE_OPTIONS = HTTPHeader.CONTENT_TYPE_OPTIONS
    REFERRER_POLICY = HTTPHeader.REFERRER_POLICY
    PERMISSIONS_POLICY = HTTPHeader.PERMISSIONS_POLICY

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "HTTPHeaderENUM"

