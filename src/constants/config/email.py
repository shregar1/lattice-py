from typing import Final
from .abstraction import IConfigurationConstant


class EmailConfig(IConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/email/config.json"
    SMTP_HOST: Final[str] = "smtp.mailgun.org"
    SMTP_PORT: Final[int] = 587
    SMTP_USERNAME: Final[str] = ""
    SMTP_PASSWORD: Final[str] = ""
    FROM: Final[str] = ""
    DEFAULT_TEMPLATE: Final[str] = "email_templates/default.html"
    OTP_TEMPLATE: Final[str] = "email_templates/otp.html"
    SMTP_USE_TLS: Final[bool] = True
    IS_CONFIGURED: Final[bool] = False

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "EmailConfig"
