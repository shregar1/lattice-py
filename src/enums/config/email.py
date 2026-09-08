"""email enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import EmailConfig


class EmailConfigENUM(EnumLayer):
    CONFIG_PATH = EmailConfig.CONFIG_PATH
    SMTP_HOST = EmailConfig.SMTP_HOST
    SMTP_PORT = EmailConfig.SMTP_PORT
    SMTP_USERNAME = EmailConfig.SMTP_USERNAME
    SMTP_PASSWORD = EmailConfig.SMTP_PASSWORD
    FROM = EmailConfig.FROM
    DEFAULT_TEMPLATE = EmailConfig.DEFAULT_TEMPLATE
    OTP_TEMPLATE = EmailConfig.OTP_TEMPLATE
    SMTP_USE_TLS = EmailConfig.SMTP_USE_TLS
    IS_CONFIGURED = EmailConfig.IS_CONFIGURED

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "EmailConfigENUM"

