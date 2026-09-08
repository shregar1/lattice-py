"""method enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import HTTPMethod


class HTTPMethodENUM(EnumLayer):
    GET = HTTPMethod.GET
    POST = HTTPMethod.POST
    PUT = HTTPMethod.PUT
    PATCH = HTTPMethod.PATCH
    DELETE = HTTPMethod.DELETE
    HEAD = HTTPMethod.HEAD
    OPTIONS = HTTPMethod.OPTIONS
    QUERY = HTTPMethod.QUERY

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "HTTPMethodENUM"

