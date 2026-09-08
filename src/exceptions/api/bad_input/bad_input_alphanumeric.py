"""BadInputAlphanumericException — raised when an alphanumeric string field is invalid."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputAlphanumericException(IBadInputException):
    """
    Raised when an alphanumeric string field is invalid or contains non-alphanumeric characters.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_ALPHANUMERIC
    key = ExceptionKey.BAD_INPUT_ALPHANUMERIC

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputAlphanumericException"
