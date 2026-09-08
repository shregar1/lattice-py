from datetime import datetime
from typing import Optional, Self
from uuid import UUID



from constants import DBColumn, DBTable, Model
from ..abstraction import IUserModel
from ..fields import BooleanField, Field, ForeignKey


class UserRecoveryCode(IUserModel):

    __tablename__ = DBTable.USER_RECOVERY_CODE

    code_hash: str = Field(max_length=255, nullable=False)
    is_used: bool = BooleanField(nullable=False)
    user_id: int = ForeignKey(f"{DBTable.USER}.{DBColumn.ID}", nullable=False)

    @classmethod
    def build(
        cls,
        urn: UUID,
        code_hash: str,
        user_id: int,
        created_by: int,
        is_used: bool = False,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
    ) -> Self:
        """Construct an instance with named arguments."""
        return UserRecoveryCode(
            urn=urn,
            code_hash=code_hash,
            is_used=is_used,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            is_deleted=is_deleted,
            is_active=is_active,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Model.USER_RECOVERY_CODE
