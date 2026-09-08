from configurations.notification.abstraction import INotificationConfiguration
from rivex import Dependency

from constants import AppConfig
from constants import ConfigurationDependency
from configurations.notification.slack import SlackConfiguration

from configurations.notification.teams import TeamsConfiguration

__all__ = ["INotificationConfiguration", "SlackConfiguration", "TeamsConfiguration"]
