"""ProhibitedIdParameterException — raised when a client supplies a forbidden id parameter."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import ISecurityException


class ProhibitedIdParameterException(ISecurityException):
    """
    Raised when a client supplies a forbidden id parameter.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.PROHIBITED_ID_PARAMETER
    key = ExceptionKey.PROHIBITED_ID_PARAMETER

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.ProhibitedIdParameterException"
