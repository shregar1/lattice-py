import httpx
from typing import Dict, Optional, Any
from rivex import Dependency

from constants import Auth
from constants import Utility
from constants import Log
from configurations.sms import SMSConfiguration, SMSConfigurationDTO
from dependencies import CryptoUtilityDependency
from dependencies import LoggerUtilityDependency
from dependencies import SMSConfigurationDependency
from .abstraction import IUtility
from utilities import CryptoUtility
from utilities import Logger


class SMSUtility(IUtility):
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
        crypto_utility: CryptoUtility = Dependency(CryptoUtilityDependency),
        sms_configuration: SMSConfiguration = Dependency(SMSConfigurationDependency),
        logger: Logger = Dependency(LoggerUtilityDependency),
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
        self.crypto_utility: CryptoUtility = crypto_utility
        self.sms_configuration: SMSConfigurationDTO = sms_configuration.get_instance()

    def is_valid_phone(self, phone: str) -> bool:
        return bool(phone and len(phone) >= 10)

    def generate_otp(self, length: int = Auth.OTP_LENGTH) -> str:
        return self.crypto_utility.generate_otp(length)

    async def send(self, to: str, message: str) -> bool:
        if not self.is_valid_phone(to):
            raise ValueError(f"Invalid phone number: {to!r}")

        if not self.sms_configuration.is_configured:
            self.logger.warning(
                "SMS not configured; skipped send",
                code=Log.SMS_NOT_CONFIGURED,
                to=to,
                message_preview=message[:120],
            )
            return True

        try:
            await self._send_via_api(to, message)
            self.logger.info("SMS sent", code=Log.SMS_SENT, to=to)
            return True
        except Exception as exc:
            self.logger.error("SMS send failed", code=Log.SMS_SEND_FAILED, to=to, error=str(exc))
            raise

    async def send_otp(self, to: str, purpose: str) -> str:
        otp = self.generate_otp()
        message = f"Your mono-backend verification code for {purpose} is: {otp}"
        await self.send(to, message)
        return otp

    async def _send_via_api(self, to: str, message: str) -> None:
        url = self.sms_configuration.sms_api_url
        if url is None:
            raise RuntimeError("SMS API URL is not configured")
        headers: Dict[str, str] = {}
        if self.sms_configuration.sms_api_key:
            headers["Authorization"] = f"Bearer {self.sms_configuration.sms_api_key}"
        payload = {
            "to": to,
            "message": message,
            "from": getattr(self.sms_configuration, "from_number", None),
        }
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.SMS
