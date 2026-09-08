"""BadInputURLException — raised when a url field is malformed or unsafe."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputURLException(IBadInputException):
    """
    Raised when a URL field is malformed or unsafe.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_URL
    key = ExceptionKey.BAD_INPUT_URL

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputURLException"
