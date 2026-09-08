"""UtilityName — PascalCase class-name constants for the utility layer."""

from typing import Final

from .abstraction import ILayerConstant


class Utility(ILayerConstant):

    CRYPTO: Final[str] = "CryptoUtility"
    HMAC: Final[str] = "HMACUtility"
    DISPLAY_NAME: Final[str] = "DisplayNameUtility"
    EMAIL: Final[str] = "EmailUtility"
    RESPONSE: Final[str] = "ResponseUtility"
    EXCEPTION: Final[str] = "ExceptionUtility"
    HASHING: Final[str] = "HashingUtility"
    JWT: Final[str] = "JWTUtility"
    MONGO_DATABASE: Final[str] = "MongoDatabaseUtility"
    POSTGRES_DATABASE: Final[str] = "PostgresDatabaseUtility"
    REGEX: Final[str] = "RegexUtility"
    REQUEST_HEADER: Final[str] = "RequestHeaderUtility"
    REQUEST_TIMING: Final[str] = "RequestTimingUtility"
    SMS: Final[str] = "SMSUtility"
    TIMING: Final[str] = "TimingUtility"
    URN: Final[str] = "URNUtility"
    VALIDATION: Final[str] = "ValidationUtility"
    MIDDLEWARE: Final[str] = "MiddlewareUtility"
    OUTBOX: Final[str] = "OutboxUtility"
    LOGGER: Final[str] = "LoggerUtility"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Utility"
