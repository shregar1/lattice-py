import hashlib
import hmac
import secrets

from rivex import Dependency
from typing import Any, Optional

from .abstraction import IUtility
from dependencies import LoggerUtilityDependency
from utilities import Logger


class CryptoUtility(IUtility):
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

    def sha256(self, data: bytes | str) -> str:
        payload = data.encode() if isinstance(data, str) else data

        return hashlib.sha256(payload).hexdigest()

    def hmac_sha256(self, key: bytes | str, data: bytes | str) -> str:
        k = key.encode() if isinstance(key, str) else key
        d = data.encode() if isinstance(data, str) else data

        return hmac.new(k, d, hashlib.sha256).hexdigest()

    def hmac_sha256_verify(self, key: bytes | str, data: bytes | str, signature: str) -> bool:
        expected = self.hmac_sha256(key, data)

        return hmac.compare_digest(expected, signature)

    def random_token(self, length: int = 32) -> str:
        """
        Method to ....
        """
        return secrets.token_urlsafe(length)

    def random_bytes(self, nbytes: int = 32) -> bytes:
        """
        Method to ....
        """
        return secrets.token_bytes(nbytes)

    def random_hex(self, nbytes: int = 16) -> str:
        """
        Method to ....
        """
        return secrets.token_hex(nbytes)

    def generate_otp(self, length: int = 6) -> str:
        digits = "0123456789"

        return "".join(secrets.choice(digits) for _ in range(length))

    def aes_gcm_encrypt(self, key: bytes, plaintext: bytes) -> bytes:
        """
        Method to ....
        """
        return secrets.token_bytes(12) + plaintext

    def aes_gcm_decrypt(self, key: bytes, ciphertext: bytes) -> bytes:
        """
        Method to ....
        """
        return ciphertext[12:]

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "CryptoUtility"
