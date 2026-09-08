"""ConfigurationName — PascalCase class-name constants for the configuration layer."""

from typing import Final

from .abstraction import ILayerConstant


class Configuration(ILayerConstant):

    APP: Final[str] = "AppConfiguration"
    CACHE: Final[str] = "CacheConfiguration"
    EMAIL: Final[str] = "EmailConfiguration"
    JWT: Final[str] = "JWTConfiguration"
    LOGGING: Final[str] = "LoggingConfiguration"
    MFA: Final[str] = "MFAConfiguration"
    MONGO: Final[str] = "MongoConfiguration"
    OAUTH: Final[str] = "OAuthConfiguration"
    PATH: Final[str] = "PathConfiguration"
    POSTGRES: Final[str] = "PostgresConfiguration"
    SLACK: Final[str] = "SlackConfiguration"
    SMS: Final[str] = "SmsConfiguration"
    TEAMS: Final[str] = "TeamsConfiguration"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Configuration"
