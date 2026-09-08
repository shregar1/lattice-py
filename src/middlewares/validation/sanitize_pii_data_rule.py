import json
import re

from rivex import Dependency
from typing import Any, Dict, List, Optional

from constants import Encoding
from constants import Regex
from dependencies import LoggerUtilityDependency
from dependencies import RegexUtilityDependency
from dtos import ResponseValidationContext
from .abstraction import IValidationRule
from utilities import Logger
from utilities import RegexUtility


class SanitizePiiDataRule(IValidationRule):
    def __init__(
        self,
        exclude_paths: Optional[List[str]] = None,
        exclude_methods: Optional[List[str]] = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        regex_utility: RegexUtility = Dependency(RegexUtilityDependency),
    ) -> None:
        super().__init__(exclude_paths, exclude_methods)
        self.logger: Logger = logger
        self.regex_utility: RegexUtility = regex_utility

    async def sanitize_response(self, ctx: ResponseValidationContext) -> bytes | None:
        if self.is_excluded(ctx.path, ctx.method):
            return None
        body_json = ctx.json_body()

        if body_json is None or not isinstance(body_json, (dict, list)):
            return None
        pii_keys: List[str] = []
        sanitized_json = self._sanitize_payload(body_json, pii_keys, path="")

        if pii_keys:
            self.logger.warning(
                "DEVELOPER WARNING: Outgoing response payload contained raw PII data! Redacted automatically.",
                code="DEVELOPER_WARNING_PII_LEAK",
                path=ctx.path,
                method=ctx.method,
                stripped_fields=list(set(pii_keys)),
                instruction="If this endpoint is intentionally supposed to return masked PII, please format values appropriately before returning DTOs.",
            )
            return json.dumps(sanitized_json).encode(Encoding.UTF_8)

        return None

    def _sanitize_payload(self, data: Any, pii_keys: List[str], path: str = "") -> Any:
        if isinstance(data, dict):
            cleaned: Dict[str, Any] = {}
            for key, val in data.items():
                field_path = f"{path}.{key}" if path else key
                if self._is_pii_value(val):
                    pii_keys.append(field_path)
                    cleaned[key] = "[REDACTED_PII]"
                else:
                    cleaned[key] = self._sanitize_payload(val, pii_keys, field_path)
            return cleaned
        elif isinstance(data, list):
            return [self._sanitize_payload(item, pii_keys, path) for item in data]
        return data

    def _is_pii_value(self, val: Any) -> bool:
        if not isinstance(val, str) or not val:
            return False

        if re.match(Regex.SSN, val):
            return True
        clean_num = val.replace("-", "").replace(" ", "")

        if re.match(Regex.CARD, clean_num):
            return True

        return False
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "SanitizePiiDataRule"
