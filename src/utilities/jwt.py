import time

from rivex import jwt_decode, jwt_encode, Dependency
from typing import Any, Dict, Optional

from constants import JWT
from configurations.auth.jwt import JWTConfiguration
from dependencies import JWTConfigurationDependency
from dependencies import JWTUtilityDependency
from dependencies import LoggerUtilityDependency
from dtos import JWTConfigurationDTO
from .abstraction import IUtility
from utilities import Logger
from utilities import URNUtility


class JWTUtility(IUtility):
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
        urn_utility: URNUtility = Dependency(JWTUtilityDependency),
        jwt_configuration: JWTConfiguration = Dependency(JWTConfigurationDependency),
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
        self.jwt_configuration: JWTConfigurationDTO = jwt_configuration.get_instance().settings
        self.urn_utility = urn_utility

    def _create_payload(
        self,
        user_urn: str,
        tenant_urn: str,
        company_urn: str,
        user_type_urn: str,
        role_type_urn: str,
        expires_at: int,
        type: str,
        jti: str,
        **claims: Any,
    ):
        """
        Method to ....
        """
        return {
            "sub": user_urn,
            "user_urn": user_urn,
            "tenant_urn": tenant_urn,
            "type": type,
            "exp": expires_at,
            "company_urn": company_urn,
            "user_type_urn": user_type_urn,
            "role_type_urn": role_type_urn,
            "jti": jti,
            **claims,
        }

    def create_access_token(
        self,
        user_urn: str,
        tenant_urn: str,
        company_urn: str,
        user_type_urn: str,
        role_type_urn: str,
        **claims: Any,
    ) -> str:
        expires_at = int(time.time()) + self._auth.access_ttl_seconds
        payload: Dict[str, Any] = self._create_payload(
            user_urn=user_urn,
            tenant_urn=tenant_urn,
            company_urn=company_urn,
            user_type_urn=user_type_urn,
            role_type_urn=role_type_urn,
            expires_at=expires_at,
            type=JWT.ACCESS,
            **claims,
        )

        return jwt_encode(payload, self._auth.jwt_secret)

    def create_refresh_token(
        self,
        user_urn: str,
        tenant_urn: str,
        company_urn: str,
        user_type_urn: str,
        role_type_urn: str,
        **claims: Any,
    ) -> str:
        expires_at = int(time.time()) + self._auth.refresh_ttl_seconds
        payload: Dict[str, Any] = self._create_payload(
            user_urn=user_urn,
            tenant_urn=tenant_urn,
            company_urn=company_urn,
            user_type_urn=user_type_urn,
            role_type_urn=role_type_urn,
            expires_at=expires_at,
            type=JWT.REFRESH,
            jti=str(self.urn_utility.generate_uuid(JWT.JTI)),
            **claims,
        )

        return jwt_encode(payload, self._auth.jwt_refresh_secret)

    def decode_access_token(self, token: str) -> Dict[str, Any]:
        """
        Method to ....
        """
        return jwt_decode(token, self._auth.jwt_secret)

    def decode_refresh_token(self, token: str) -> Dict[str, Any]:
        """
        Method to ....
        """
        return jwt_decode(token, self._auth.jwt_refresh_secret)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "JWTUtility"
