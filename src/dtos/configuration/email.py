from typing import Self

from constants import Configuration
from .abstraction import IConfigurationDTO


class EmailConfigurationDTO(IConfigurationDTO):
    email_from: str
    smtp_host: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    smtp_use_tls: bool
    is_configured: bool

    @classmethod
    def build(
        cls,
        email_from: str,
        smtp_host: str,
        smtp_port: int,
        smtp_username: str,
        smtp_password: str,
        smtp_use_tls: bool,
        is_configured: bool,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            email_from=email_from,
            smtp_host=smtp_host,
            smtp_port=smtp_port,
            smtp_username=smtp_username,
            smtp_password=smtp_password,
            smtp_use_tls=smtp_use_tls,
            is_configured=is_configured,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.EMAIL
