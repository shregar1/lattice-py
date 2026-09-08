"""BadInputSlugException — raised when a slug field does not match the slug pattern."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputSlugException(IBadInputException):
    """
    Raised when a slug field does not match the slug pattern.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_SLUG
    key = ExceptionKey.BAD_INPUT_SLUG

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputSlugException"
