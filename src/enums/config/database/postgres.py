"""postgres enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import PostgresConfig


class PostgresConfigENUM(EnumLayer):
    CONFIG_PATH = PostgresConfig.CONFIG_PATH
    PG_HOST = PostgresConfig.PG_HOST
    PG_PORT = PostgresConfig.PG_PORT
    PG_DATABASE = PostgresConfig.PG_DATABASE
    PG_USER = PostgresConfig.PG_USER
    PG_SCHEMA = PostgresConfig.PG_SCHEMA
    PG_POOL_SIZE = PostgresConfig.PG_POOL_SIZE
    PG_MAX_OVERFLOW = PostgresConfig.PG_MAX_OVERFLOW
    PG_POOL_TIMEOUT = PostgresConfig.PG_POOL_TIMEOUT
    PG_POOL_RECYCLE = PostgresConfig.PG_POOL_RECYCLE
    PG_ECHO = PostgresConfig.PG_ECHO
    PG_SSL_MODE = PostgresConfig.PG_SSL_MODE

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "PostgresConfigENUM"

