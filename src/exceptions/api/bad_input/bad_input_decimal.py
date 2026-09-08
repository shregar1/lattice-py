"""BadInputDecimalException — raised when a decimal field is invalid or out of precision."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputDecimalException(IBadInputException):
    """
    Raised when a decimal field is invalid or out of precision.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_DECIMAL
    key = ExceptionKey.BAD_INPUT_DECIMAL

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputDecimalException"
