from typing import Self

from constants import Configuration
from .abstraction import IConfigurationDTO


class SMSConfigurationDTO(IConfigurationDTO):
    account_sid: str
    auth_token: str
    from_number: str
    messaging_service_sid: str

    @classmethod
    def build(
        cls,
        from_number: str,
        account_sid: str,
        auth_token: str,
        messaging_service_sid: str,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            account_sid=account_sid,
            auth_token=auth_token,
            from_number=from_number,
            messaging_service_sid=messaging_service_sid,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.SMS
