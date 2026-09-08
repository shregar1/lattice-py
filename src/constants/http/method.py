from typing import Final
from rivex import HTTPMethod as RivexHTTPMethod
from .abstraction import IHTTPConstant


class HTTPMethod(IHTTPConstant):

    GET: Final[str] = str(RivexHTTPMethod.GET)
    POST: Final[str] = str(RivexHTTPMethod.POST)
    PUT: Final[str] = str(RivexHTTPMethod.PUT)
    PATCH: Final[str] = str(RivexHTTPMethod.PATCH)
    DELETE: Final[str] = str(RivexHTTPMethod.DELETE)
    HEAD: Final[str] = str(RivexHTTPMethod.HEAD)
    OPTIONS: Final[str] = str(RivexHTTPMethod.OPTIONS)
    QUERY: Final[str] = str(RivexHTTPMethod.QUERY)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "HTTPMethod"
