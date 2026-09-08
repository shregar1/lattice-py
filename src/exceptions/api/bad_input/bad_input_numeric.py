"""BadInputNumericException — raised when a numeric field is out of range or non-numeric."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputNumericException(IBadInputException):
    """
    Raised when a numeric field is out of range or non-numeric.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_NUMERIC
    key = ExceptionKey.BAD_INPUT_NUMERIC

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputNumericException"
