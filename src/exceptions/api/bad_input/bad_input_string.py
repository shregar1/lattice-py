"""BadInputStringException — raised when a string field is invalid or format is incorrect."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputStringException(IBadInputException):
    """
    Raised when a string field is invalid or format is incorrect.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_STRING
    key = ExceptionKey.BAD_INPUT_STRING

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputStringException"
