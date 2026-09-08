"""NotFoundIDException — raised when a resource with specified ID is not found."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import INotFoundException


class NotFoundIDException(INotFoundException):
    """
    Raised when a resource with specified ID is not found.
    Inherits HTTP status code 404 from :class:`INotFoundException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.NOT_FOUND_ID
    key = ExceptionKey.NOT_FOUND_ID

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.NotFoundIDException"
