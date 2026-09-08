"""Domain exception base carrying a message, key, code and HTTP status."""

from abc import ABC, abstractmethod


class ExceptionLayer(Exception, ABC):
    """
    Base class for application-level domain exceptions.

    Carries a developer-facing message, a stable machine-readable key, an
    internal code, and the HTTP status code that should be returned to the
    caller. Extra context fields can be supplied as ``**context`` kwargs.
    """

    def __init__(
        self,
        message: str,
        key: str,
        code: str,
        status_code: int,
    ) -> None:
        """Initializes the exception with its message, key, code and HTTP status."""

        self.message = message
        self.key = key
        self.code = code
        self.status_code = status_code

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
