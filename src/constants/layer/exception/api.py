"""API exception layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class ApiException(ILayerConstant):

    BAD_INPUT_DATE_TIME: Final[str] = "BadInputDateTimeException"
    BAD_INPUT_EMAIL: Final[str] = "BadInputEmailException"
    BAD_INPUT_ENUM: Final[str] = "BadInputEnumException"
    BAD_INPUT_FILE_NAME: Final[str] = "BadInputFileNameException"
    BAD_INPUT_NUMERIC: Final[str] = "BadInputNumericException"
    BAD_INPUT_STRING: Final[str] = "BadInputStringException"
    BAD_INPUT_DECIMAL: Final[str] = "BadInputDecimalException"
    BAD_INPUT_ALPHANUMERIC: Final[str] = "BadInputAlphanumericException"
    BAD_INPUT_PAGINATION: Final[str] = "BadInputPaginationException"
    BAD_INPUT_PASSWORD: Final[str] = "BadInputPasswordException"
    BAD_INPUT_PHONE: Final[str] = "BadInputPhoneException"
    BAD_INPUT_SLUG: Final[str] = "BadInputSlugException"
    BAD_INPUT_TIMEZONE: Final[str] = "BadInputTimezoneException"
    BAD_INPUT_URN: Final[str] = "BadInputURNException"
    BAD_INPUT_URL: Final[str] = "BadInputURLException"
    MALICIOUS_INPUT_DETECTED: Final[str] = "MaliciousInputDetectedException"
    NOT_FOUND_ITEM: Final[str] = "NotFoundItemException"
    NOT_FOUND_URN: Final[str] = "NotFoundURNException"
    NOT_FOUND_ID: Final[str] = "NotFoundIDException"
    NOT_FOUND_CODE: Final[str] = "NotFoundCodeException"
    NOT_FOUND_TENANT: Final[str] = "NotFoundTenantException"
    NOT_FOUND_USER: Final[str] = "NotFoundUserException"
    PROHIBITED_ID_PARAMETER: Final[str] = "ProhibitedIdParameterException"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ApiException"
