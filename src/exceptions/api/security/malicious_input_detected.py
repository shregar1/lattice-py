"""MaliciousInputDetectedException — raised when input is rejected as potentially malicious."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import ISecurityException


class MaliciousInputDetectedException(ISecurityException):
    """
    Raised when input is rejected as potentially malicious.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.MALICIOUS_INPUT_DETECTED
    key = ExceptionKey.MALICIOUS_INPUT_DETECTED

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.MaliciousInputDetectedException"
