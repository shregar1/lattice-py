from rivex import Dependency
from typing import Any, Dict, Optional, Sequence

from abstractions import MiddlewareLayer
from configurations.auth.jwt import JWTConfiguration
from constants import (
    Auth,
    Context,
    ExceptionMessage,
    HTTPHeader,
)
from dependencies import (
    JWTConfigurationDependency,
    TenantRepositoryDependency,
    UserRepositoryDependency,
    JWTUtilityDependency,
)
from exceptions.app import (
    ExpiredTokenException,
    IConfigurationException,
    IJWTException,
    InvalidTokenException,
    LoadConfigurationException,
)
from repositories import (
    TenantRepository,
    UserRepository,
)
from utilities import (
    JWTUtility, 
    MiddlewareUtility, 
    RequestHeaderUtility, 
    ResponseUtility,
)


class AuthenticationMiddleware(MiddlewareLayer):
    DEFAULT_SCHEME: str = Auth.DEFAULT_SCHEME
    SUBJECT_CLAIM: str = Auth.SUBJECT_CLAIM
    TENANT_CLAIM: str = Auth.TENANT_CLAIM
    USER_CLAIMS_KEY: str = Auth.USER_CLAIMS_KEY

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
        jwt_config: JWTConfiguration = Dependency(JWTConfigurationDependency),
        jwt_utility: JWTUtility = Dependency(JWTUtilityDependency),
        user_repository: UserRepository = Dependency(UserRepositoryDependency),
        tenant_repository: TenantRepository = Dependency(TenantRepositoryDependency),
        header_name: str = HTTPHeader.AUTHORIZATION,
        excluded_paths: Optional[Sequence[str]] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
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
        self.jwt_config = jwt_config
        self.jwt_utility = jwt_utility
        self.user_repository = user_repository
        self.tenant_repository = tenant_repository
        self.header_name = header_name.lower()
        self.scheme = self.DEFAULT_SCHEME.lower()
        self.excluded_paths = set(excluded_paths or [])

    async def process(self, request_data: Dict[str, Any], call_next) -> Dict[str, Any]:
        path = request_data.get("path", "")

        if path in self.excluded_paths:
            return await call_next(request_data)

        context_fields = self.extract_request_context(request_data)
        urn = context_fields[Context.URN]
        tenant_id = context_fields[Context.TENANT_ID]
        tenant_urn = context_fields[Context.TENANT_URN]
        user_id = context_fields[Context.USER_ID]
        user_urn = context_fields[Context.USER_URN]
        api_name = context_fields[Context.API_NAME]
        ip_address = context_fields[Context.IP_ADDRESS]
        user_agent = context_fields[Context.USER_AGENT]

        self.bind_request_context(
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
        )

        auth_header = RequestHeaderUtility.get_request_header(request_data, self.header_name)

        if not auth_header:
            return ResponseUtility.build_unauthorized_response(
                ExceptionMessage.UNAUTHORIZED, reference_urn=urn
            )

        parts = auth_header.split()

        if len(parts) != 2 or parts[0].lower() != self.scheme:
            return ResponseUtility.build_unauthorized_response(
                f"Invalid authorization scheme. Expected '{self.scheme}'", reference_urn=urn
            )

        token = parts[1]

        try:
            config_dto = self.jwt_config.get_instance()
            secret = config_dto.jwt_secret

            if not secret:
                raise LoadConfigurationException(message="JWT secret is not configured")

            try:
                payload = self.jwt_utility.decode_access_token(token)
            except Exception as exc:
                self.logger.error("JWT token decoding failed", exc=exc)
                if "expired" in str(exc).lower():
                    raise ExpiredTokenException() from exc
                raise InvalidTokenException() from exc

            user_urn = payload.get(self.SUBJECT_CLAIM) or payload.get(Context.USER_URN)

            if not user_urn:
                self.logger.error("JWT token missing user URN claim")
                raise InvalidTokenException(message="Invalid token: missing user URN")

            tenant_urn = payload.get(self.TENANT_CLAIM) or payload.get(Context.TENANT_URN)

            if not tenant_urn:
                self.logger.error("JWT token missing tenant URN claim")
                raise InvalidTokenException(message="Invalid token: missing tenant URN")

            user = self.user_repository.find_by_urn(user_urn)

            if not user:
                self.logger.error(
                    f"User validation failed: user_urn '{user_urn}' not found in database"
                )
                raise InvalidTokenException(message="Invalid token: user not found")

            tenant = self.tenant_repository.find_by_urn(tenant_urn)

            if not tenant:
                self.logger.error(
                    f"Tenant validation failed: tenant_urn '{tenant_urn}' not found in database"
                )
                raise InvalidTokenException(message="Invalid token: tenant not found")

            MiddlewareUtility.set_request_state(request_data, self.USER_CLAIMS_KEY, payload)
            MiddlewareUtility.set_request_state(request_data, Context.USER_URN, user_urn)
            MiddlewareUtility.set_request_state(request_data, Context.TENANT_URN, tenant_urn)
            MiddlewareUtility.set_request_state(request_data, Context.USER_ID, user.id)
            MiddlewareUtility.set_request_state(request_data, Context.TENANT_ID, tenant.id)

        except ExpiredTokenException as exc:
            self.logger.error(f"Authentication failed: {exc.message}", exc=exc)
            return ResponseUtility.build_unauthorized_response(exc.message, reference_urn=urn)

        except InvalidTokenException as exc:
            self.logger.error(f"Authentication failed: {exc.message}", exc=exc)
            return ResponseUtility.build_unauthorized_response(exc.message, reference_urn=urn)

        except (IJWTException, IConfigurationException, ValueError) as exc:
            msg = getattr(exc, "message", ExceptionMessage.UNAUTHORIZED)
            self.logger.error(f"Authentication failed: {msg}", exc=exc)
            return ResponseUtility.build_unauthorized_response(msg, reference_urn=urn)

        return await call_next(request_data)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "AuthenticationMiddleware"
