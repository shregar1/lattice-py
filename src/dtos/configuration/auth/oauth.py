from typing import Self, List

from .abstraction import IAuthConfigurationDTO
from constants import Configuration


class OAuthConfigurationDTO(IAuthConfigurationDTO):
    client_id: str
    client_secret: str
    redirect_uri: str
    scopes: List[str]

    @classmethod
    def build(
        cls, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str]
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scopes=scopes,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.O_AUTH
