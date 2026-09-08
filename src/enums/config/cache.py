"""cache enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import CacheConfig


class CacheConfigENUM(EnumLayer):
    CONFIG_PATH = CacheConfig.CONFIG_PATH
    MAX_CONNECTIONS = CacheConfig.MAX_CONNECTIONS
    SOCKET_TIMEOUT = CacheConfig.SOCKET_TIMEOUT
    SOCKET_CONNECT_TIMEOUT = CacheConfig.SOCKET_CONNECT_TIMEOUT
    TTL_SECONDS = CacheConfig.TTL_SECONDS
    KEY_PREFIX = CacheConfig.KEY_PREFIX

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "CacheConfigENUM"

