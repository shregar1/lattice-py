from typing import Final
from .abstraction import ConfigKey


class SMSConfig(ConfigKey):
    CONFIG_PATH: Final[str] = "configs/sms/config.json"
    ACCOUNT_SID: Final[str] = ""
    AUTH_TOKEN: Final[str] = ""
    FROM_NUMBER: Final[str] = "+1234567890"
    MESSAGING_SERVICE_SID: Final[str] = ""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "SMSConfig"
