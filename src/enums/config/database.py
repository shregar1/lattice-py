"""database enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import MongoConfig
from constants import PostgresConfig


class MongoConfigENUM(EnumLayer):
    URI = MongoConfig.URI
    DATABASE = MongoConfig.DATABASE
    MAX_POOL_SIZE = MongoConfig.MAX_POOL_SIZE
    MIN_POOL_SIZE = MongoConfig.MIN_POOL_SIZE
    SERVER_SELECTION_TIMEOUT_MS = MongoConfig.SERVER_SELECTION_TIMEOUT_MS
    CONNECT_TIMEOUT_MS = MongoConfig.CONNECT_TIMEOUT_MS
    DEFAULT_MAX_POOL_SIZE = MongoConfig.DEFAULT_MAX_POOL_SIZE
    DEFAULT_MIN_POOL_SIZE = MongoConfig.DEFAULT_MIN_POOL_SIZE
    DEFAULT_SERVER_SELECTION_TIMEOUT_MS = MongoConfig.DEFAULT_SERVER_SELECTION_TIMEOUT_MS
    DEFAULT_CONNECT_TIMEOUT_MS = MongoConfig.DEFAULT_CONNECT_TIMEOUT_MS

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "MongoConfigENUM"


class PostgresConfigENUM(EnumLayer):
    URL = PostgresConfig.URL
    POOL_SIZE = PostgresConfig.POOL_SIZE
    MAX_OVERFLOW = PostgresConfig.MAX_OVERFLOW
    POOL_TIMEOUT = PostgresConfig.POOL_TIMEOUT
    POOL_RECYCLE = PostgresConfig.POOL_RECYCLE
    ECHO = PostgresConfig.ECHO
    DEFAULT_POOL_SIZE = PostgresConfig.DEFAULT_POOL_SIZE
    DEFAULT_MAX_OVERFLOW = PostgresConfig.DEFAULT_MAX_OVERFLOW
    DEFAULT_POOL_TIMEOUT = PostgresConfig.DEFAULT_POOL_TIMEOUT
    DEFAULT_POOL_RECYCLE = PostgresConfig.DEFAULT_POOL_RECYCLE
    DEFAULT_ECHO = PostgresConfig.DEFAULT_ECHO

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "PostgresConfigENUM"

