"""sms enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import SMSConfig


class SMSConfigENUM(EnumLayer):
    CONFIG_PATH = SMSConfig.CONFIG_PATH
    ACCOUNT_SID = SMSConfig.ACCOUNT_SID
    AUTH_TOKEN = SMSConfig.AUTH_TOKEN
    FROM_NUMBER = SMSConfig.FROM_NUMBER
    MESSAGING_SERVICE_SID = SMSConfig.MESSAGING_SERVICE_SID

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "SMSConfigENUM"

