"""Configuration dependency layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class ConfigurationDependency(ILayerConstant):

    APP: Final[str] = "AppConfigurationDependency"
    CACHE: Final[str] = "CacheConfigurationDependency"
    EMAIL: Final[str] = "EmailConfigurationDependency"
    JWT: Final[str] = "JWTConfigurationDependency"
    LOGGING: Final[str] = "LoggingConfigurationDependency"
    MFA: Final[str] = "MFAConfigurationDependency"
    MONGO: Final[str] = "MongoConfigurationDependency"
    OAUTH: Final[str] = "OAuthConfigurationDependency"
    PATH: Final[str] = "PathConfigurationDependency"
    POSTGRES: Final[str] = "PostgresConfigurationDependency"
    SLACK: Final[str] = "SlackConfigurationDependency"
    SMS: Final[str] = "SmsConfigurationDependency"
    TEAMS: Final[str] = "TeamsConfigurationDependency"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ConfigurationDependency"
