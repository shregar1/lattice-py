"""BadInputPasswordException — raised when a password does not meet the policy."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputPasswordException(IBadInputException):
    """
    Raised when a password does not meet the policy.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_PASSWORD
    key = ExceptionKey.BAD_INPUT_PASSWORD

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputPasswordException"
