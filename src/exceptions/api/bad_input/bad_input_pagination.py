"""BadInputPaginationException — raised when pagination parameters are invalid."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputPaginationException(IBadInputException):
    """
    Raised when pagination parameters are invalid.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_PAGINATION
    key = ExceptionKey.BAD_INPUT_PAGINATION

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputPaginationException"
