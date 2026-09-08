from typing import Self

from constants import Configuration
from .abstraction import IDatabaseConfigurationDTO


class PostgresConfigurationDTO(IDatabaseConfigurationDTO):
    url: str
    host: str
    port: int
    database: str
    user: str
    password: str
    schema: str
    ssl_mode: str
    pool_size: int
    max_overflow: int
    pool_timeout: int
    pool_recycle: int
    echo: bool

    @classmethod
    def build(
        cls,
        password: str,
        host: str,
        port: int,
        database: str,
        user: str,
        schema: str,
        ssl_mode: str,
        pool_size: int,
        max_overflow: int,
        pool_timeout: int,
        pool_recycle: int,
        echo: bool,
    ) -> Self:
        url: str = (
            f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}?sslmode={ssl_mode}"
        )

        return cls(
            url=url,
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
            schema=schema,
            ssl_mode=ssl_mode,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_timeout=pool_timeout,
            pool_recycle=pool_recycle,
            echo=echo,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.POSTGRES
