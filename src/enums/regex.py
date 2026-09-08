"""regex enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Regex


class RegexENUM(EnumLayer):
    XSS = Regex.XSS
    SQLI = Regex.SQLI
    SSN = Regex.SSN
    EIN = Regex.EIN
    ITIN = Regex.ITIN
    PAN_CARD = Regex.PAN_CARD
    GSTIN = Regex.GSTIN
    AADHAAR = Regex.AADHAAR
    TAN = Regex.TAN
    NINO = Regex.NINO
    UTR = Regex.UTR
    UK_VAT = Regex.UK_VAT
    SIN = Regex.SIN
    CANADA_BN = Regex.CANADA_BN
    TFN = Regex.TFN
    ABN = Regex.ABN
    EU_VAT = Regex.EU_VAT
    GERMANY_STEUER_ID = Regex.GERMANY_STEUER_ID
    UUID = Regex.UUID
    ULID = Regex.ULID
    URN = Regex.URN
    CARD = Regex.CARD
    VISA = Regex.VISA
    MASTERCARD = Regex.MASTERCARD
    AMEX = Regex.AMEX
    DISCOVER = Regex.DISCOVER
    CVV = Regex.CVV
    IBAN = Regex.IBAN
    SWIFT_BIC = Regex.SWIFT_BIC
    ROUTING_NUMBER = Regex.ROUTING_NUMBER
    DEFAULT_KEY_NAME = Regex.DEFAULT_KEY_NAME
    SK_LIVE = Regex.SK_LIVE
    SK_TEST = Regex.SK_TEST
    VX_SECRET = Regex.VX_SECRET
    GHP = Regex.GHP
    JWT = Regex.JWT
    ID_KEY = Regex.ID_KEY
    DEFAULT_VALUES = Regex.DEFAULT_VALUES

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "RegexENUM"

