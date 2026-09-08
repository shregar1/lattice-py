from typing import Final, Sequence
from .abstraction import IConstant


class Regex(IConstant):

    XSS: Final[str] = r"^.*(<script|javascript:|onload=|onerror=|<iframe|<img).*"
    SQLI: Final[str] = r"^.*(UNION\s+SELECT|DROP\s+TABLE|ALTER\s+TABLE|DELETE\s+FROM|--|/\*).*"

    # Tax & Government Identifiers
    # USA
    SSN: Final[str] = r"^\d{3}-\d{2}-\d{4}$"
    EIN: Final[str] = r"^\d{2}-\d{7}$"
    ITIN: Final[str] = r"^9\d{2}-(7[0-9]|8[0-8]|9[0-2]|9[4-9])-\d{4}$"

    # India
    PAN_CARD: Final[str] = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
    GSTIN: Final[str] = r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$"
    AADHAAR: Final[str] = r"^[2-9]{1}[0-9]{3}\s?[0-9]{4}\s?[0-9]{4}$"
    TAN: Final[str] = r"^[A-Z]{4}[0-9]{5}[A-Z]{1}$"

    # UK
    NINO: Final[str] = (
        r"^(?!BG|GB|NK|KN|TN|NT|ZZ)[A-CEGHJ-PR-TW-Z]{1}[A-CEGHJ-NPR-TW-Z]{1}[0-9]{6}[A-D]{1}$"
    )
    UTR: Final[str] = r"^[0-9]{10}$"
    UK_VAT: Final[str] = r"^(GB)?([0-9]{9}|[0-9]{12}|(GD|HA)[0-9]{3})$"

    # Canada
    SIN: Final[str] = r"^\d{3}-\d{3}-\d{3}$"
    CANADA_BN: Final[str] = r"^[0-9]{9}RC[0-9]{4}$"

    # Australia
    TFN: Final[str] = r"^[0-9]{8,9}$"
    ABN: Final[str] = r"^[0-9]{11}$"

    # EU
    EU_VAT: Final[str] = r"^[A-Z]{2}[0-9A-ZA-z]{2,12}$"
    GERMANY_STEUER_ID: Final[str] = r"^[0-9]{11}$"

    # Identifiers
    UUID: Final[str] = (
        r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$"
    )
    ULID: Final[str] = r"^[0-7][0-9A-HJKMNP-TV-Z]{25}$"
    URN: Final[str] = r"^urn:[a-z0-9][a-z0-9-]{0,31}:[a-z0-9()+\,-.:=@;$_!*'%?#]+$"

    # Payment & Financial
    CARD: Final[str] = r"^\d{13,19}$"
    VISA: Final[str] = r"^4[0-9]{12}(?:[0-9]{3})?$"
    MASTERCARD: Final[str] = (
        r"^(?:5[1-5][0-9]{14}|2(?:2[2-9][0-9]{12}|[3-6][0-9]{13}|7[0-1][0-9]{12}|720[0-9]{12}))$"
    )
    AMEX: Final[str] = r"^3[47][0-9]{13}$"
    DISCOVER: Final[str] = r"^6(?:011|5[0-9]{2})[0-9]{12}$"
    CVV: Final[str] = r"^[0-9]{3,4}$"
    IBAN: Final[str] = r"^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$"
    SWIFT_BIC: Final[str] = r"^[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?$"
    ROUTING_NUMBER: Final[str] = r"^(0[1-9]|1[0-2]|2[1-9]|3[0-2]|6[1-9]|7[0-2]|80)[0-9]{7}$"

    # Security & Tokens
    DEFAULT_KEY_NAME: Final[str] = (
        r"^.*(api_key|apikey|secret|secret_key|access_token|auth_token|private_key|password|bearer_token).*$"
    )

    SK_LIVE: Final[str] = r"^sk_live_[a-zA-Z0-9]{16,}$"
    SK_TEST: Final[str] = r"^sk_test_[a-zA-Z0-9]{16,}$"
    VX_SECRET: Final[str] = r"^vx_secret_[a-zA-Z0-9]{16,}$"
    GHP: Final[str] = r"^ghp_[a-zA-Z0-9]{20,}$"
    JWT: Final[str] = r"^eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}$"

    # Generic Patterns
    ID_KEY: Final[str] = r"^.*_id$|^id$"

    DEFAULT_VALUES: Final[Sequence[str]] = (
        SK_LIVE,
        SK_TEST,
        VX_SECRET,
        GHP,
        JWT,
    )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Regex"
