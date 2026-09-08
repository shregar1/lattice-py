"""mongo enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import MongoConfig


class MongoConfigENUM(EnumLayer):
    CONFIG_PATH = MongoConfig.CONFIG_PATH
    DATABASE = MongoConfig.DATABASE
    MONGO_MAX_POOL_SIZE = MongoConfig.MONGO_MAX_POOL_SIZE
    MONGO_MIN_POOL_SIZE = MongoConfig.MONGO_MIN_POOL_SIZE
    MONGO_SERVER_SELECTION_TIMEOUT_MS = MongoConfig.MONGO_SERVER_SELECTION_TIMEOUT_MS
    MONGO_CONNECT_TIMEOUT_MS = MongoConfig.MONGO_CONNECT_TIMEOUT_MS

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "MongoConfigENUM"

