"""request_entity enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import RequestEntity


class RequestEntityENUM(EnumLayer):
    BODY = RequestEntity.BODY
    HEADERS = RequestEntity.HEADERS
    METADATA = RequestEntity.METADATA
    QUERY_PARAMS = RequestEntity.QUERY_PARAMS
    PATH_PARAMS = RequestEntity.PATH_PARAMS
    FORM_DATA = RequestEntity.FORM_DATA
    FILE_DATA = RequestEntity.FILE_DATA
    COOKIES = RequestEntity.COOKIES

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "RequestEntityENUM"

