from typing import Self

from .abstraction import IAuthConfigurationDTO
from constants import Configuration


class JWTConfigurationDTO(IAuthConfigurationDTO):
    secret: str
    refresh_secret: str
    expires_minutes: int
    refresh_expires_days: int
    algorithm: str

    @classmethod
    def build(
        cls,
        secret: str,
        refresh_secret: str,
        expires_minutes: int,
        refresh_expires_days: int,
        algorithm: str,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            secret=secret,
            refresh_secret=refresh_secret,
            expires_minutes=expires_minutes,
            refresh_expires_days=refresh_expires_days,
            algorithm=algorithm,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.JWT
