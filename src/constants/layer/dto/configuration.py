"""Configuration DTO layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class ConfigurationDTO(ILayerConstant):

    APP_CONFIGURATION_DTO: Final[str] = "AppConfigurationDTO"
    CACHE_CONFIGURATION_DTO: Final[str] = "CacheConfigurationDTO"
    EMAIL_CONFIGURATION_DTO: Final[str] = "EmailConfigurationDTO"
    JWT_CONFIGURATION_DTO: Final[str] = "JWTConfigurationDTO"
    LOGGING_CONFIGURATION_DTO: Final[str] = "LoggingConfigurationDTO"
    MFA_CONFIGURATION_DTO: Final[str] = "MFAConfigurationDTO"
    MONGO_CONFIGURATION_DTO: Final[str] = "MongoConfigurationDTO"
    OAUTH_CONFIGURATION_DTO: Final[str] = "OAuthConfigurationDTO"
    PATH_CONFIGURATION_DTO: Final[str] = "PathConfigurationDTO"
    POSTGRES_CONFIGURATION_DTO: Final[str] = "PostgresConfigurationDTO"
    SLACK_CONFIGURATION_DTO: Final[str] = "SlackConfigurationDTO"
    TEAMS_CONFIGURATION_DTO: Final[str] = "TeamsConfigurationDTO"
    WEBHOOK_CONFIGURATION_DTO: Final[str] = "WebhookConfigurationDTO"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ConfigurationDTO"
