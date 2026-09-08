"""BadInputDateTimeException — raised when a date-time field fails validation."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputDateTimeException(IBadInputException):
    """
    Raised when a date-time field fails validation.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_DATE_TIME
    key = ExceptionKey.BAD_INPUT_DATE_TIME

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputDateTimeException"
