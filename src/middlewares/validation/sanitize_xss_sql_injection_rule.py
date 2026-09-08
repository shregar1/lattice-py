from typing import Any, Optional
from rivex import sanitize_html, strip_html_tags
from constants import ExceptionCode
from constants import HTTPMethod, HTTPStatus
from constants import InjectionRegex
from dtos import RequestValidationContext, RuleValidationResult
from .abstraction import IValidationRule

_XSS_PATTERN, _SQLI_PATTERN = InjectionRegex.compile_patterns(
    [InjectionRegex.XSS_PATTERN, InjectionRegex.SQLI_PATTERN]
)


class SanitizeXssSqlInjectionRule(IValidationRule):
    @property
    def rule_id(self) -> str:
        return "sanitize_xss_sql_injection_rule"

    async def validate_request(self, ctx: RequestValidationContext) -> RuleValidationResult | None:
        if self.is_excluded(ctx.path, ctx.method):
            return None

        if ctx.query_string:
            for param in ctx.query_string.split("&"):
                if "=" in param:
                    key, val = param.split("=", 1)
                    if self._contains_malicious_content(val):
                        return RuleValidationResult.abort(
                            message=f"Malicious script/SQL injection detected in query parameter '{key}'.",
                            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                            response_key=ExceptionCode.MALICIOUS_INPUT_DETECTED,
                        )

        if ctx.method in {HTTPMethod.POST, HTTPMethod.PUT, HTTPMethod.PATCH}:
            body_json = ctx.json_body()
            if isinstance(body_json, (dict, list)):
                detected_field = self._inspect_payload(body_json)
                if detected_field:
                    return RuleValidationResult.abort(
                        message=f"Malicious script/SQL injection detected in request payload field '{detected_field}'.",
                        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                        response_key=ExceptionCode.MALICIOUS_INPUT_DETECTED,
                    )

        return None

    def _inspect_payload(self, data: Any, path: str = "") -> Optional[str]:
        if isinstance(data, dict):
            for key, val in data.items():
                field_path = f"{path}.{key}" if path else key
                res = self._inspect_payload(val, field_path)
                if res:
                    return res
        elif isinstance(data, list):
            for idx, item in enumerate(data):
                field_path = f"{path}[{idx}]"
                res = self._inspect_payload(item, field_path)
                if res:
                    return res
        elif isinstance(data, str):
            if self._contains_malicious_content(data):
                return path

        return None

    def _contains_malicious_content(self, text: str) -> bool:
        if not text:
            return False

        if _XSS_PATTERN.match(text) or _SQLI_PATTERN.match(text):
            return True

        sanitized = sanitize_html(text)
        strip_html_tags(text)

        if ("<script" in text.lower() or "javascript:" in text.lower()) and sanitized != text:
            return True

        return False
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "SanitizeXssSqlInjectionRule"
