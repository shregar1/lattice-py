from typing import Self

from constants import Configuration
from .abstraction import IDatabaseConfigurationDTO


class MongoConfigurationDTO(IDatabaseConfigurationDTO):
    url: str
    database: str
    max_pool_size: int
    min_pool_size: int
    server_selection_timeout_ms: int
    connect_timeout_ms: int

    @classmethod
    def build(
        cls,
        url: str,
        database: str,
        max_pool_size: int,
        min_pool_size: int,
        server_selection_timeout_ms: int,
        connect_timeout_ms: int,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            url=url,
            database=database,
            max_pool_size=max_pool_size,
            min_pool_size=min_pool_size,
            server_selection_timeout_ms=server_selection_timeout_ms,
            connect_timeout_ms=connect_timeout_ms,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.MONGO
