"""tenant composite repositories."""

from .tenant import TenantRepository
from .tenant_profile import TenantProfileRepository

__all__ = [
    "TenantProfileRepository",
    "TenantRepository",
]
