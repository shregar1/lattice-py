import json
import re

from rivex import Dependency
from typing import Any, Dict, List, Optional

from constants import Encoding
from constants import ExceptionCode
from constants import HTTPMethod, HTTPStatus
from constants import Regex
from dependencies import LoggerUtilityDependency
from dependencies import RegexUtilityDependency
from dtos import RequestValidationContext
from dtos import ResponseValidationContext
from dtos import RuleValidationResult
from .abstraction import IValidationRule
from utilities import Logger
from utilities import RegexUtility


class ProhibitedIntegerIdRule(IValidationRule):
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

    @staticmethod
    def _is_integer_id(val: Any) -> bool:
        if isinstance(val, bool):
            return False
        if isinstance(val, int) and val > 0:
            return True
        if isinstance(val, str) and val.isdigit() and (int(val) > 0):
            return True
        return False

    async def validate_request(self, ctx: RequestValidationContext) -> RuleValidationResult | None:
        for seg in ctx.path_segments():
            if seg.isdigit() and ctx.path != "/health":
                return RuleValidationResult.abort(
                    message="Numeric integer IDs are prohibited in path parameters. Use URN instead.",
                    status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                    response_key=ExceptionCode.PROHIBITED_ID_PARAMETER,
                )

        if ctx.query_string:
            for param in ctx.query_string.split("&"):
                if "=" in param:
                    key, val = param.split("=", 1)
                    if re.match(Regex.ID_KEY, key) and self._is_integer_id(val):
                        return RuleValidationResult.abort(
                            message=f"Passing integer parameter '{key}' is prohibited. Use URN instead.",
                            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                            response_key=ExceptionCode.PROHIBITED_ID_PARAMETER,
                        )

        if ctx.method in {HTTPMethod.POST, HTTPMethod.PUT, HTTPMethod.PATCH}:
            body_json = ctx.json_body()
            if isinstance(body_json, dict):
                rejected_key = self._check_dict_for_request_ids(body_json)
                if rejected_key:
                    return RuleValidationResult.abort(
                        message=f"Prohibited integer ID field '{rejected_key}' in request payload. Use URN instead.",
                        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                        response_key=ExceptionCode.PROHIBITED_ID_PARAMETER,
                    )

        return None

    async def sanitize_response(self, ctx: ResponseValidationContext) -> bytes | None:
        body_json = ctx.json_body()
        if body_json is None or not isinstance(body_json, (dict, list)):
            return None
        stripped_keys: List[str] = []
        sanitized_json = self._sanitize_response_data(body_json, stripped_keys, path="")

        if stripped_keys:
            self.logger.warning(
                "DEVELOPER WARNING: Outgoing response payload contained integer entity IDs! Stripped automatically.",
                code="DEVELOPER_WARNING_ID_EXPOSED",
                path=ctx.path,
                method=ctx.method,
                stripped_fields=list(set(stripped_keys)),
                instruction="Please update DTO response schemas to exclude integer 'id' or '*_id' fields and expose UUID 'urn' handles only.",
            )
            return json.dumps(sanitized_json).encode(Encoding.UTF_8)

        return None

    def _check_dict_for_request_ids(self, data: Dict[str, Any]) -> Optional[str]:
        for key, val in data.items():
            if re.match(Regex.ID_KEY, key) and self._is_integer_id(val):
                return key
            if isinstance(val, dict):
                res = self._check_dict_for_request_ids(val)
                if res:
                    return res
            elif isinstance(val, list):
                for item in val:
                    if isinstance(item, dict):
                        res = self._check_dict_for_request_ids(item)
                        if res:
                            return res
        return None

    def _sanitize_response_data(self, data: Any, stripped_keys: List[str], path: str = "") -> Any:
        if isinstance(data, dict):
            cleaned: Dict[str, Any] = {}
            for key, val in data.items():
                field_path = f"{path}.{key}" if path else key
                if re.match(Regex.ID_KEY, key) and self._is_integer_id(val):
                    stripped_keys.append(field_path)
                    continue
                cleaned[key] = self._sanitize_response_data(val, stripped_keys, field_path)
            return cleaned
        elif isinstance(data, list):
            return [self._sanitize_response_data(item, stripped_keys, path) for item in data]
        return data
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ProhibitedIntegerIdRule"
