"""company composite repositories."""

from .company import CompanyRepository
from .company_profile import CompanyProfileRepository

__all__ = [
    "CompanyProfileRepository",
    "CompanyRepository",
]
