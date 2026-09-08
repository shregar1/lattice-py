from typing import Final

from .abstraction import IConstant


class ExceptionKey(IConstant):

    DOMAIN: Final[str] = "domain"
    NOT_FOUND: Final[str] = "not_found"
    VALIDATION: Final[str] = "validation"
    CONFLICT: Final[str] = "conflict"
    FORBIDDEN: Final[str] = "forbidden"
    UNAUTHORIZED: Final[str] = "unauthorized"
    METHOD_NOT_ALLOWED: Final[str] = "method_not_allowed"
    PAYLOAD_TOO_LARGE: Final[str] = "payload_too_large"
    UNSUPPORTED_MEDIA_TYPE: Final[str] = "unsupported_media_type"
    UNPROCESSABLE_ENTITY: Final[str] = "unprocessable_entity"
    TOO_MANY_REQUESTS: Final[str] = "too_many_requests"
    INTERNAL_SERVER_ERROR: Final[str] = "internal_server_error"
    BAD_GATEWAY: Final[str] = "bad_gateway"
    SERVICE_UNAVAILABLE: Final[str] = "service_unavailable"
    GATEWAY_TIMEOUT: Final[str] = "gateway_timeout"
    PROHIBITED_ID_PARAMETER: Final[str] = "prohibited_id_parameter"
    MALICIOUS_INPUT_DETECTED: Final[str] = "malicious_input_detected"
    BAD_INPUT_EMAIL: Final[str] = "bad_input_email"
    BAD_INPUT_PASSWORD: Final[str] = "bad_input_password"
    BAD_INPUT_URN: Final[str] = "bad_input_urn"
    BAD_INPUT_URL: Final[str] = "bad_input_url"
    BAD_INPUT_ENUM: Final[str] = "bad_input_enum"
    BAD_INPUT_PAGINATION: Final[str] = "bad_input_pagination"
    BAD_INPUT_DATE_TIME: Final[str] = "bad_input_date_time"
    BAD_INPUT_NUMERIC: Final[str] = "bad_input_numeric"
    BAD_INPUT_STRING: Final[str] = "bad_input_string"
    BAD_INPUT_DECIMAL: Final[str] = "bad_input_decimal"
    BAD_INPUT_ALPHANUMERIC: Final[str] = "bad_input_alphanumeric"
    BAD_INPUT_SLUG: Final[str] = "bad_input_slug"
    BAD_INPUT_PHONE: Final[str] = "bad_input_phone"
    BAD_INPUT_TIMEZONE: Final[str] = "bad_input_timezone"
    BAD_INPUT_FILE_NAME: Final[str] = "bad_input_file_name"
    NOT_FOUND_USER: Final[str] = "not_found_user"
    NOT_FOUND_TENANT: Final[str] = "not_found_tenant"
    NOT_FOUND_ITEM: Final[str] = "not_found_item"
    NOT_FOUND_URN: Final[str] = "not_found_urn"
    NOT_FOUND_ID: Final[str] = "not_found_id"
    NOT_FOUND_CODE: Final[str] = "not_found_code"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionKey"
