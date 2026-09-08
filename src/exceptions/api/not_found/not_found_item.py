"""NotFoundItemException — raised when an item cannot be located."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import INotFoundException


class NotFoundItemException(INotFoundException):
    """
    Raised when an item cannot be located.
    Inherits the HTTP status code and base message from :class:`NotFoundException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.NOT_FOUND_ITEM
    key = ExceptionKey.NOT_FOUND_ITEM

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.NotFoundItemException"
