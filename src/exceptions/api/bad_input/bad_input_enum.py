"""BadInputEnumException — raised when an enum field receives an unknown value."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputEnumException(IBadInputException):
    """
    Raised when an enum field receives an unknown value.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_ENUM
    key = ExceptionKey.BAD_INPUT_ENUM

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputEnumException"
