"""BadInputEmailException — raised when an email field is not rfc-compliant."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputEmailException(IBadInputException):
    """
    Raised when an email field is not RFC-compliant.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_EMAIL
    key = ExceptionKey.BAD_INPUT_EMAIL

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputEmailException"
