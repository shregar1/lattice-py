"""Utility dependency layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class UtilityDependency(ILayerConstant):

    CRYPTO: Final[str] = "CryptoUtilityDependency"
    HMAC: Final[str] = "HMACUtilityDependency"
    DISPLAY_NAME: Final[str] = "DisplayNameUtilityDependency"
    EMAIL: Final[str] = "EmailUtilityDependency"
    RESPONSE: Final[str] = "ResponseUtilityDependency"
    EXCEPTION: Final[str] = "ExceptionUtilityDependency"
    HASHING: Final[str] = "HashingUtilityDependency"
    JWT: Final[str] = "JWTUtilityDependency"
    LOGGER: Final[str] = "LoggerUtilityDependency"
    MIDDLEWARE: Final[str] = "MiddlewareUtilityDependency"
    MONGO_DATABASE: Final[str] = "MongoDatabaseUtilityDependency"
    OUTBOX: Final[str] = "OutboxUtilityDependency"
    POSTGRES_DATABASE: Final[str] = "PostgresDatabaseUtilityDependency"
    REDIS: Final[str] = "RedisUtilityDependency"
    REGEX: Final[str] = "RegexUtilityDependency"
    REQUEST_HEADER: Final[str] = "RequestHeaderUtilityDependency"
    REQUEST_TIMING: Final[str] = "RequestTimingUtilityDependency"
    SMS: Final[str] = "SMSUtilityDependency"
    TIMING: Final[str] = "TimingUtilityDependency"
    URN: Final[str] = "URNUtilityDependency"
    VALIDATION: Final[str] = "ValidationUtilityDependency"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "UtilityDependency"
