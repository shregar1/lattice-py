import hashlib
import hmac

from rivex import Dependency
from typing import Any, Optional

from .abstraction import IUtility
from dependencies import LoggerUtilityDependency
from utilities import Logger


class HMACUtility(IUtility):
    """Utility provider for HMAC signature generation and timing-attack safe verification."""

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

        self.urn = urn
        self.tenant_id = tenant_id
        self.tenant_urn = tenant_urn
        self.user_id = user_id
        self.user_urn = user_urn
        self.api_name = api_name
        self.ip_address = ip_address
        self.user_agent = user_agent
        self.logger = logger

    def generate(self, key: bytes | str, data: bytes | str, algorithm: str = "sha256") -> str:
        """Generate HMAC hex digest for given data and key using specified digest algorithm."""
        k = key.encode() if isinstance(key, str) else key
        d = data.encode() if isinstance(data, str) else data
        digestmod = getattr(hashlib, algorithm.lower(), hashlib.sha256)
        return hmac.new(k, d, digestmod).hexdigest()

    def verify(
        self,
        key: bytes | str,
        data: bytes | str,
        signature: str,
        algorithm: str = "sha256",
    ) -> bool:
        """Verify HMAC signature using timing-attack safe comparison."""
        expected = self.generate(key, data, algorithm=algorithm)
        return hmac.compare_digest(expected, signature)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "HMACUtility"
