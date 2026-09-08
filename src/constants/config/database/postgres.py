from typing import Final
from .abstraction import IDatabaseConfigurationConstant
from ..default import Default



class PostgresConfig(IDatabaseConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/database/postgres/config.json"
    HOST: Final[str] = "localhost"
    PORT: Final[int] = 5432
    DATABASE: Final[str] = ""
    USER: Final[str] = ""
    SCHEMA: Final[str] = "public"
    POOL_SIZE: Final[int] = 10
    MAX_OVERFLOW: Final[int] = 5
    POOL_TIMEOUT: Final[int] = 30
    POOL_RECYCLE: Final[int] = 1800
    ECHO: Final[bool] = False
    URL: Final[str] = "url"
    

    DEFAULT_POOL_SIZE: Final[int] = Default.PG_POOL_SIZE
    DEFAULT_MAX_OVERFLOW: Final[int] = Default.PG_MAX_OVERFLOW
    DEFAULT_POOL_TIMEOUT: Final[int] = Default.PG_POOL_TIMEOUT
    DEFAULT_POOL_RECYCLE: Final[int] = Default.PG_POOL_RECYCLE
    DEFAULT_ECHO: Final[bool] = Default.PG_ECHO

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "PostgresConfig"
