"""NotFoundCodeException — raised when a resource with specified Code is not found."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import INotFoundException


class NotFoundCodeException(INotFoundException):
    """
    Raised when a resource with specified Code is not found.
    Inherits HTTP status code 404 from :class:`INotFoundException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.NOT_FOUND_CODE
    key = ExceptionKey.NOT_FOUND_CODE

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.NotFoundCodeException"
