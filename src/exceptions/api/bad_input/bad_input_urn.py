"""BadInputURNException — raised when a urn field does not match the urn pattern."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputURNException(IBadInputException):
    """
    Raised when a URN field does not match the URN pattern.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_URN
    key = ExceptionKey.BAD_INPUT_URN

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputURNException"
