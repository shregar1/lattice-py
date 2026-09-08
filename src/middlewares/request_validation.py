from collections.abc import Sequence
from typing import Any, Dict, List, Optional

from .validation import IValidationRule
from abstractions import MiddlewareLayer
from dtos import RequestValidationContext, ResponseValidationContext



class RequestValidationMiddleware(MiddlewareLayer):
    def __init__(
        self,
        rules: Sequence[IValidationRule] | None = None,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
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
        self._rules: List[IValidationRule] = list(rules or [])

    @classmethod
    def builder(cls) -> "RequestValidationMiddlewareBuilder":
        return RequestValidationMiddlewareBuilder()

    def register(
        self, rule_or_rules: IValidationRule | Sequence[IValidationRule]
    ) -> "RequestValidationMiddleware":
        if isinstance(rule_or_rules, Sequence) and (not isinstance(rule_or_rules, (str, bytes))):
            self._rules.extend(rule_or_rules)
        else:
            self._rules.append(rule_or_rules)
        return self

    def register_rule(self, rule: IValidationRule) -> "RequestValidationMiddleware":
        return self.register(rule)

    async def process(self, request_data: Dict[str, Any], call_next) -> Dict[str, Any]:
        path: str = request_data.get("path", "")
        method: str = request_data.get("method", "GET")
        req_ctx = RequestValidationContext(request_data)

        for rule in self._rules:
            if rule.is_excluded(path, method):
                continue
            result = await rule.validate_request(req_ctx)
            if result and result.should_abort:
                return result.to_http_response()

        response: Dict[str, Any] = await call_next(request_data)
        resp_ctx = ResponseValidationContext(response, path=path, method=method)

        for rule in self._rules:
            if rule.is_excluded(path, method):
                continue
            modified_body = await rule.sanitize_response(resp_ctx)
            if modified_body is not None:
                response["body"] = modified_body

        return response
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RequestValidationMiddleware"


class RequestValidationMiddlewareBuilder:
    def __init__(self) -> None:
        self._rules: List[IValidationRule] = []

    def with_rule(self, rule: IValidationRule) -> "RequestValidationMiddlewareBuilder":
        self._rules.append(rule)
        return self

    def with_rules(self, rules: Sequence[IValidationRule]) -> "RequestValidationMiddlewareBuilder":
        self._rules.extend(rules)
        return self

    def build(self) -> RequestValidationMiddleware:
        return RequestValidationMiddleware(rules=self._rules)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RequestValidationMiddlewareBuilder"
