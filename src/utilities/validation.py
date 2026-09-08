import html
import ipaddress
import re
import ulid
import uuid
from datetime import datetime
from decimal import Decimal
from typing import Any, Optional
from rivex import Dependency

from constants import Utility
from exceptions import BadInputException
from .abstraction import IUtility
from dependencies import LoggerUtilityDependency
from utilities import Logger


class ValidationUtility(IUtility):
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

    def validate_none(self, value: Any, field_name: str = "field", required: bool = True) -> bool:
        if value is None:
            if required:
                raise BadInputException(f"{field_name} cannot be null")
            return True
        return False

    def validate_instance(
        self,
        value: Any,
        expected_type: Any,
        field_name: str = "field",
        required: bool = True,
        disallow_bool: bool = False,
    ) -> Any:
        if disallow_bool and isinstance(value, bool):
            msg_suffix = " when provided" if not required else ""
            type_desc = expected_type.__name__ if hasattr(expected_type, "__name__") else str(expected_type)
            raise BadInputException(f"{field_name} must be a valid {type_desc}{msg_suffix}, got bool")
        if not isinstance(value, expected_type):
            msg_suffix = " when provided" if not required else ""
            type_desc = expected_type.__name__ if hasattr(expected_type, "__name__") else str(expected_type)
            raise BadInputException(f"{field_name} must be a valid {type_desc}{msg_suffix}, got {type(value).__name__}")
        return value

    def validate_empty(self, value: Any, field_name: str = "field") -> Any:
        if isinstance(value, str):
            if not value.strip():
                raise BadInputException(f"{field_name} cannot be empty")
        elif hasattr(value, "__len__") and len(value) == 0:
            raise BadInputException(f"{field_name} cannot be empty")
        return value

    def validate_regex(self, value: str, pattern: str, field_name: str = "field", message: Optional[str] = None) -> str:
        if not re.match(pattern, value):
            err_msg = message or f"{field_name} '{value}' does not match valid pattern"
            raise BadInputException(err_msg)
        return value

    def validate_among(
        self,
        value: Any,
        candidates: Any,
        field_name: str = "field",
        class_name: Optional[str] = None,
    ) -> Any:
        candidate_set = set(candidates)
        if value not in candidate_set:
            sorted_candidates = sorted(list(candidate_set))
            cls_str = f" for {class_name}" if class_name else ""
            raise BadInputException(f"Invalid {field_name} '{value}'{cls_str}. Must be one of: {sorted_candidates}")
        return value

    def validate_urn(self, value: Any, field_name: str = "urn", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        cleaned = self.validate_empty(v.strip(), field_name=field_name)
        if cleaned.lower().startswith("urn:"):
            raise BadInputException(f"{field_name} must be a plain UUID or ULID without 'urn:' prefix, got {value!r}")
        try:
            uuid.UUID(cleaned)
            return cleaned
        except ValueError:
            pass
        try:
            ulid.ULID.from_str(cleaned)
            return cleaned
        except ValueError:
            pass
        raise BadInputException(f"{field_name} '{value}' does not match a valid URN, UUID, or ULID pattern")

    def validate_id(self, value: Any, field_name: str = "id", required: bool = True) -> Optional[int]:
        v = self.validate_int(value, field_name=field_name, required=required)
        if v is not None and v <= 0:
            raise BadInputException(f"{field_name} must be a positive integer greater than zero")
        return v

    def validate_string(self, value: Any, field_name: str = "string", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        return self.validate_empty(v, field_name=field_name)

    def validate_bool(self, value: Any, field_name: str = "bool", required: bool = False) -> Optional[bool]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        return self.validate_instance(value, bool, field_name=field_name, required=required)

    def validate_int(self, value: Any, field_name: str = "int", required: bool = True) -> Optional[int]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        return self.validate_instance(value, int, field_name=field_name, required=required, disallow_bool=True)

    def validate_float(self, value: Any, field_name: str = "float", required: bool = True) -> Optional[float]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, (float, int), field_name=field_name, required=required, disallow_bool=True)
        return float(v)

    def validate_decimal(self, value: Any, field_name: str = "decimal", required: bool = True) -> Optional[Decimal]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, (Decimal, float, int, str), field_name=field_name, required=required, disallow_bool=True)
        try:
            return Decimal(str(v))
        except Exception:
            raise BadInputException(f"{field_name} '{value}' is not a valid decimal")

    def validate_list(self, value: Any, field_name: str = "list", required: bool = True) -> Optional[list]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        return self.validate_instance(value, list, field_name=field_name, required=required)

    def validate_dict(self, value: Any, field_name: str = "dict", required: bool = True) -> Optional[dict]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        return self.validate_instance(value, dict, field_name=field_name, required=required)

    def validate_tuple(self, value: Any, field_name: str = "tuple", required: bool = True) -> Optional[tuple]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        return self.validate_instance(value, tuple, field_name=field_name, required=required)

    def validate_set(self, value: Any, field_name: str = "set", required: bool = True) -> Optional[set]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        return self.validate_instance(value, set, field_name=field_name, required=required)

    def validate_code(
        self,
        value: Any,
        valid_codes: Optional[list] = None,
        field_name: str = "code",
        required: bool = True,
        class_name: Optional[str] = None,
    ) -> Optional[str]:
        v = self.validate_string(value, field_name=field_name, required=required)
        if v is not None and valid_codes:
            self.validate_among(v, valid_codes, field_name=field_name, class_name=class_name)
        return v

    def validate_datetime(self, value: Any, field_name: str = "datetime", required: bool = True) -> Optional[datetime]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            cleaned = self.validate_empty(value, field_name=field_name)
            try:
                return datetime.fromisoformat(cleaned.replace("Z", "+00:00"))
            except ValueError:
                raise BadInputException(f"{field_name} '{value}' is not a valid ISO datetime format")
        msg_suffix = " when provided" if not required else ""
        raise BadInputException(f"{field_name} must be a datetime or ISO datetime string{msg_suffix}, got {type(value).__name__}")

    def validate_email(self, value: Any, field_name: str = "email", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        cleaned = self.validate_empty(v, field_name=field_name)
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return self.validate_regex(cleaned, pattern, field_name=field_name, message=f"{field_name} '{value}' is not a valid email address")

    def validate_uuid(self, value: Any, field_name: str = "uuid", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        cleaned = self.validate_empty(v, field_name=field_name)
        try:
            uuid.UUID(cleaned)
            return cleaned
        except ValueError:
            raise BadInputException(f"{field_name} '{value}' is not a valid UUID")

    def validate_url(self, value: Any, field_name: str = "url", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        cleaned = self.validate_empty(v, field_name=field_name)
        pattern = r"^(?:http|ftp)s?://(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d+)?(?:/?|[/?]\S+)$"
        return self.validate_regex(cleaned, pattern, field_name=field_name, message=f"{field_name} '{value}' is not a valid URL")

    def validate_ip(self, value: Any, field_name: str = "ip_address", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        cleaned = self.validate_empty(v, field_name=field_name)
        try:
            ipaddress.ip_address(cleaned)
            return cleaned
        except ValueError:
            raise BadInputException(f"{field_name} '{value}' is not a valid IP address")

    def validate_phone(self, value: Any, field_name: str = "phone", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        cleaned = self.validate_empty(v, field_name=field_name)
        pattern = r"^\+?[1-9]\d{1,14}$"
        raw_digits = re.sub(r"[\s\-\(\)]", "", cleaned)
        self.validate_regex(raw_digits, pattern, field_name=field_name, message=f"{field_name} '{value}' is not a valid phone number")
        return cleaned

    def validate_iban(self, value: Any, field_name: str = "iban", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        cleaned = self.validate_empty(v, field_name=field_name).replace(" ", "").upper()
        if not re.match(r"^[A-Z]{2}\d{2}[A-Z0-9]{11,30}$", cleaned):
            raise BadInputException(f"{field_name} '{value}' is not a valid IBAN format")
        rearranged = cleaned[4:] + cleaned[:4]
        converted = "".join(str(ord(c) - 55) if c.isalpha() else c for c in rearranged)
        if int(converted) % 97 != 1:
            raise BadInputException(f"{field_name} '{value}' failed IBAN checksum verification")
        return cleaned

    def format_iban(self, value: Any, field_name: str = "iban") -> str:
        v = self.validate_iban(value, field_name=field_name)
        return " ".join(v[i:i+4] for i in range(0, len(v), 4))

    def validate_ascii(self, value: Any, field_name: str = "string", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        if not v.isascii():
            raise BadInputException(f"{field_name} must contain only ASCII characters")
        return v

    def validate_luhn(self, value: Any, field_name: str = "number", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        digits = [int(c) for c in v if c.isdigit()]
        if not digits:
            raise BadInputException(f"{field_name} must contain digits for Luhn verification")
        checksum = 0
        reverse_digits = digits[::-1]
        for idx, digit in enumerate(reverse_digits):
            if idx % 2 == 1:
                doubled = digit * 2
                checksum += doubled - 9 if doubled > 9 else doubled
            else:
                checksum += digit
        if checksum % 10 != 0:
            raise BadInputException(f"{field_name} '{value}' failed Luhn checksum verification")
        return v

    def sanitize_html(self, value: Any, field_name: str = "html", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        return html.escape(v)

    def strip_html_tags(self, value: Any, field_name: str = "html", required: bool = True) -> Optional[str]:
        if self.validate_none(value, field_name=field_name, required=required):
            return None
        v = self.validate_instance(value, str, field_name=field_name, required=required)
        return re.sub(r"<[^>]*>", "", v)

    def validate_json_schema(self, instance: Any, schema: Any, field_name: str = "json") -> Any:
        if not isinstance(schema, dict):
            raise BadInputException("JSON schema specification must be a dictionary")
        if "type" in schema:
            expected = schema["type"]
            if expected == "object":
                self.validate_dict(instance, field_name=field_name)
            elif expected == "array":
                self.validate_list(instance, field_name=field_name)
            elif expected == "string":
                self.validate_string(instance, field_name=field_name)
            elif expected == "integer":
                self.validate_int(instance, field_name=field_name)
            elif expected == "boolean":
                self.validate_bool(instance, field_name=field_name)
        return instance
    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.VALIDATION
