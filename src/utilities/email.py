import asyncio
import smtplib

from email.message import EmailMessage
from rivex import Dependency
from typing import Any, Optional

from configurations.email import EmailConfiguration, EmailConfigurationDTO
from constants import Utility
from constants import Log
from dependencies import EmailConfigurationDependency
from dependencies import LoggerUtilityDependency
from utilities import Logger
from .abstraction import IUtility


class EmailUtility(IUtility):
    def __init__(
        self,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        email_configuration: EmailConfiguration = Dependency(EmailConfigurationDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        IUtility.__init__(
            self,
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            logger=logger,
            *args,
            **kwargs,
        )

        self.urn=urn
        self.tenant_id=tenant_id
        self.tenant_urn=tenant_urn
        self.user_id=user_id
        self.user_urn=user_urn
        self.api_name=api_name
        self.ip_address=ip_address
        self.user_agent=user_agent
        self.logger=logger
        self.email_configuration: EmailConfigurationDTO = email_configuration.get_instance()

    def is_valid_address(self, address: str) -> bool:
        return "@" in address and "." in address

    async def send(self, to: str, subject: str, body: str, *, html: Optional[str] = None) -> bool:
        if not self.is_valid_address(to):
            raise ValueError(f"Invalid email address: {to!r}")

        if not self.email_configuration.is_configured:
            self.logger.warning(
                "Email not configured; skipped send",
                code=Log.EMAIL_NOT_CONFIGURED,
                to=to,
                subject=subject,
                body_preview=body[:120],
            )
            return True

        message = EmailMessage()
        message["From"] = self.email_configuration.email_from
        message["To"] = to
        message["Subject"] = subject
        message.set_content(body)

        if html is not None:
            message.add_alternative(html, subtype="html")

        try:
            await self._send_smtp(message)
            self.logger.info("Email sent", code=Log.EMAIL_SENT, to=to, subject=subject)
            return True
        except Exception as exc:
            self.logger.error(
                "Email send failed",
                code=Log.EMAIL_SEND_FAILED,
                to=to,
                subject=subject,
                error=str(exc),
            )
            raise

    async def _send_smtp(self, message: EmailMessage) -> None:
        email = self.email_configuration
        host = email.smtp_host

        if host is None:
            raise RuntimeError("SMTP host is not configured")
        port = email.smtp_port
        user = email.smtp_user
        password = email.smtp_password

        def _deliver() -> None:
            if email.smtp_use_tls:
                with smtplib.SMTP(host, port, timeout=30) as client:
                    client.starttls()
                    if user and password:
                        client.login(user, password)
                    client.send_message(message)
            else:
                with smtplib.SMTP(host, port, timeout=30) as client:
                    if user and password:
                        client.login(user, password)
                    client.send_message(message)

        await asyncio.to_thread(_deliver)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.EMAIL
