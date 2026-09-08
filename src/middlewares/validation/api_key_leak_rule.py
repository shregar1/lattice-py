from constants import Encoding
import json
import re

from rivex import Dependency
from typing import List, Dict, Any, Sequence

from constants import Regex
from dependencies import LoggerUtilityDependency
from dtos import RequestValidationContext
from .abstraction import IValidationRule
from utilities import Logger


class ApiKeyLeakRule(IValidationRule):
    def __init__(
        self,
        exclude_paths: List[str] | None = None,
        exclude_methods: List[str] | None = None,
        custom_key_patterns: Sequence[str | re.Pattern[str]] | None = None,
        custom_value_patterns: Sequence[str | re.Pattern[str]] | None = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
    ) -> None:
        super().__init__(exclude_paths=exclude_paths, exclude_methods=exclude_methods)
        key_patterns: List[str | re.Pattern[str]] = list(Regex.DEFAULT_KEY_NAMES) + list(
            custom_key_patterns or []
        )
        value_patterns: List[str | re.Pattern[str]] = list(Regex.DEFAULT_VALUE_PATTERNS) + list(
            custom_value_patterns or []
        )
        self.key_regexes: List[re.Pattern[str]] = Regex.compile_patterns(key_patterns)
        self.value_regexes: List[re.Pattern[str]] = Regex.compile_patterns(value_patterns)
        self.logger: Logger = logger

    async def sanitize_response(self, ctx: RequestValidationContext) -> bytes | None:
        if self.is_excluded(ctx.path, ctx.method):
            return None
        body_json = ctx.json_body()

        if body_json is None or not isinstance(body_json, (dict, list)):
            return None
        leaked_keys: List[str] = []
        sanitized_json = self._sanitize_payload(body_json, leaked_keys, path="")

        if leaked_keys:
            self.logger.warning(
                "DEVELOPER WARNING: Outgoing response payload contained exposed API keys/secrets! Stripped automatically.",
                code="DEVELOPER_WARNING_API_KEY_LEAK",
                path=ctx.path,
                method=ctx.method,
                stripped_fields=list(set(leaked_keys)),
                instruction="If this endpoint is intentionally supposed to return API keys (e.g. key creation API), please add its route path to ApiKeyLeakRule(exclude_paths=[...]).",
            )
            return json.dumps(sanitized_json).encode(Encoding.UTF_8)

        return None

    def _sanitize_payload(self, data: Any, leaked_keys: List[str], path: str = "") -> Any:
        if isinstance(data, dict):
            cleaned: Dict[str, Any] = {}
            for key, val in data.items():
                field_path = f"{path}.{key}" if path else key
                if self._is_sensitive_pair(key, val):
                    leaked_keys.append(field_path)
                    continue
                cleaned[key] = self._sanitize_payload(val, leaked_keys, field_path)
            return cleaned
        elif isinstance(data, list):
            return [self._sanitize_payload(item, leaked_keys, path) for item in data]
        return data

    def _is_sensitive_pair(self, key: str, val: Any) -> bool:
        if not isinstance(val, (str, bytes)):
            return False
        val_str = val.decode(Encoding.UTF_8) if isinstance(val, bytes) else val

        if not val_str:
            return False
        for pattern in self.key_regexes:
            if pattern.match(key):
                return True
        for pattern in self.value_regexes:
            if pattern.match(val_str):
                return True

        return False
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ApiKeyLeakRule"
