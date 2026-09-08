"""BadInputTimezoneException — raised when a timezone field is not a valid iana zone."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputTimezoneException(IBadInputException):
    """
    Raised when a timezone field is not a valid IANA zone.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_TIMEZONE
    key = ExceptionKey.BAD_INPUT_TIMEZONE

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputTimezoneException"
