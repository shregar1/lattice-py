"""IException — base class for every exception in the application."""

from abstractions import ExceptionLayer


class IException(ExceptionLayer):
    """
    Domain exception base carrying the message, code, key and HTTP status.
    Subclasses typically fix ``code``, ``status_code`` and ``key`` at the
    class level and only vary the ``message`` per instance.
    Attributes:
        message: Human-readable error message.
        code: Stable machine-readable code.
        key: Stable exception key used by the envelope factory.
        status_code: HTTP status code returned to the caller.
    """

    def __init__(
        self,
        message: str,
        code: str,
        key: str,
        status_code: int,
    ) -> None:
        """
        Initializes the exception with its identifying fields.
        Args:
            message: Human-readable error message.
            code: Stable machine-readable code.
            key: Stable exception key used by the envelope factory.
            status_code: HTTP status code returned to the caller.
        """
        self.message = message
        self.code = code
        self.key = key
        self.status_code = status_code
        super().__init__(message)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IException"
