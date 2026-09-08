from typing import Final
from .abstraction import IDatabaseConfigurationConstant
from ..default import Default


class MongoConfig(IDatabaseConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/database/mongo/config.json"
    DATABASE: Final[str] = ""
    MAX_POOL_SIZE: Final[int] = 10
    MIN_POOL_SIZE: Final[int] = 1
    SERVER_SELECTION_TIMEOUT_MS: Final[int] = 5000
    CONNECT_TIMEOUT_MS: Final[int] = 10000
    URI: Final[str] = ""

    DEFAULT_MAX_POOL_SIZE: Final[int] = Default.MONGO_MAX_POOL_SIZE
    DEFAULT_MIN_POOL_SIZE: Final[int] = Default.MONGO_MIN_POOL_SIZE
    DEFAULT_SERVER_SELECTION_TIMEOUT_MS: Final[int] = Default.MONGO_SERVER_SELECTION_TIMEOUT_MS
    DEFAULT_CONNECT_TIMEOUT_MS: Final[int] = Default.MONGO_CONNECT_TIMEOUT_MS


    @property
    def name(self) -> str:
        """Returns the class name."""
        return "MongoConfig"
