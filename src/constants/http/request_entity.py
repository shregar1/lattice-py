from typing import Final
from .abstraction import IHTTPConstant


class RequestEntity(IHTTPConstant):

    BODY: Final[str] = "body"
    HEADERS: Final[str] = "headers"
    METADATA: Final[str] = "metadata"
    QUERY_PARAMS: Final[str] = "query_params"
    PATH_PARAMS: Final[str] = "path_params"
    FORM_DATA: Final[str] = "form_data"
    FILE_DATA: Final[str] = "file_data"
    COOKIES: Final[str] = "cookies"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RequestEntity"
