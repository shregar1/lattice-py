"""BadInputPhoneException — raised when a phone number is not in a recognised format."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputPhoneException(IBadInputException):
    """
    Raised when a phone number is not in a recognised format.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_PHONE
    key = ExceptionKey.BAD_INPUT_PHONE

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputPhoneException"
