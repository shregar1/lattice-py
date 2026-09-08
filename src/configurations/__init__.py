"""Configuration singletons — one per config domain."""

from configurations.app import AppConfiguration
from configurations.auth import AuthConfiguration
from configurations.database import DatabaseConfiguration
from configurations.email import EmailConfiguration
from configurations.logging import LoggingConfiguration
from configurations.paths import PathsConfiguration
from configurations.sms import SmsConfiguration
from configs import AppSettings, Settings, get_settings

__all__ = [
    "AppConfiguration",
    "AuthConfiguration",
    "DatabaseConfiguration",
    "EmailConfiguration",
    "LoggingConfiguration",
    "PathsConfiguration",
    "SmsConfiguration",
    "AppSettings",
    "Settings",
    "get_settings",
]
