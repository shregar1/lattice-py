from typing import Self

from constants import Configuration
from .abstraction import IConfigurationDTO


class CacheConfigurationDTO(IConfigurationDTO):
    url: str
    max_connections: int
    socket_timeout: int
    socket_connect_timeout: int
    ttl_seconds: int
    key_prefix: str
    is_configured: bool

    @classmethod
    def build(
        cls,
        url: str,
        max_connections: int,
        socket_timeout: int,
        socket_connect_timeout: int,
        ttl_seconds: int,
        key_prefix: str,
        is_configured: bool,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            url=url,
            max_connections=max_connections,
            socket_timeout=socket_timeout,
            socket_connect_timeout=socket_connect_timeout,
            ttl_seconds=ttl_seconds,
            key_prefix=key_prefix,
            is_configured=is_configured,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.CACHE
