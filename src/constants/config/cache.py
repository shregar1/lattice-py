from typing import Final
from .abstraction import IConfigurationConstant


class CacheConfig(IConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/cache/config.json"
    MAX_CONNECTIONS: Final[int] = 20
    SOCKET_TIMEOUT: Final[int] = 5
    SOCKET_CONNECT_TIMEOUT: Final[int] = 5
    TTL_SECONDS: Final[int] = 3600
    KEY_PREFIX: Final[str] = ""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "CacheConfig"
