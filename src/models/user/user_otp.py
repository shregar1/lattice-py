from datetime import datetime
from typing import Optional, Self
from uuid import UUID



from constants import DBColumn, DBTable, Model
from ..abstraction import IUserModel
from ..fields import Field, ForeignKey, SmallIntegerField, TimestampTZField


class UserOtp(IUserModel):

    __tablename__ = DBTable.USER_OTP

    otp_hash: str = Field(max_length=255, nullable=False)
    expires_at: datetime = TimestampTZField(nullable=False)
    attempts: int = SmallIntegerField(nullable=False)
    verified_at: Optional[datetime] = TimestampTZField(nullable=True)
    otp_type_id: int = ForeignKey(f"{DBTable.OTP_TYPE_LK}.{DBColumn.ID}", nullable=False)
    user_id: int = ForeignKey(f"{DBTable.USER}.{DBColumn.ID}", nullable=False)

    @classmethod
    def build(
        cls,
        urn: UUID,
        otp_hash: str,
        expires_at: datetime,
        attempts: int,
        otp_type_id: int,
        user_id: int,
        created_by: int,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
        verified_at: Optional[datetime] = None,
    ) -> Self:
        """Construct an instance with named arguments."""
        return UserOtp(
            urn=urn,
            otp_hash=otp_hash,
            expires_at=expires_at,
            attempts=attempts,
            verified_at=verified_at,
            otp_type_id=otp_type_id,
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
        return Model.USER_OTP
