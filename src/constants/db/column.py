from typing import Final
from .abstraction import IDBConstant


class DBColumn(IDBConstant):

    # Common Audit & Base Columns
    ID: Final[str] = "id"
    URN: Final[str] = "urn"
    CREATED_AT: Final[str] = "created_at"
    UPDATED_AT: Final[str] = "updated_at"
    CREATED_BY: Final[str] = "created_by"
    UPDATED_BY: Final[str] = "updated_by"
    IS_DELETED: Final[str] = "is_deleted"
    IS_ACTIVE: Final[str] = "is_active"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "DBColumn"
