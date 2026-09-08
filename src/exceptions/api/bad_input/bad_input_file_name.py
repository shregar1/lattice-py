"""BadInputFileNameException — raised when an uploaded file name is invalid or unsafe."""

from constants import ExceptionCode, ExceptionKey
from .abstraction import IBadInputException


class BadInputFileNameException(IBadInputException):
    """
    Raised when an uploaded file name is invalid or unsafe.
    Inherits the HTTP status code and base message from :class:`BadInputException`;
    only ``code`` and ``key`` are specialised for this domain.
    Attributes:
        code: Stable machine-readable code for this exception class.
        key: Stable exception key used by the envelope factory.
    """

    code = ExceptionCode.BAD_INPUT_FILE_NAME
    key = ExceptionKey.BAD_INPUT_FILE_NAME

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionName.BadInputFileNameException"
