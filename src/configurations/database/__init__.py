from configurations.database.abstraction import IDatabaseConfiguration
from rivex import Dependency

from constants import AppConfig
from constants import ConfigurationDependency
from configurations.database.mongo import MongoConfiguration

from configurations.database.postgres import PostgresConfiguration

__all__ = ["IDatabaseConfiguration", "MongoConfiguration", "PostgresConfiguration"]
