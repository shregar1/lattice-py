from datetime import datetime
from typing import Optional, Self
from uuid import UUID


from pydantic import EmailStr

from constants import DBColumn, DBTable, Model
from ..abstraction import IUserModel
from ..fields import BooleanField, EmailField, Field, ForeignKey, TimestampTZField


class User(IUserModel):

    __tablename__ = DBTable.USER

    email: EmailStr = EmailField(unique=True, nullable=False)
    password: str = Field(max_length=255, nullable=False)
    is_mfa_enabled: bool = BooleanField(nullable=False)
    mfa_secret: Optional[str] = Field(max_length=255, nullable=True)
    last_login: Optional[datetime] = TimestampTZField(nullable=True)
    mfa_type_id: Optional[int] = ForeignKey(f"{DBTable.MFA_TYPE_LK}.{DBColumn.ID}", nullable=True)
    auth_type_id: int = ForeignKey(f"{DBTable.AUTH_TYPE_LK}.{DBColumn.ID}", nullable=False)

    @classmethod
    def build(
        cls,
        urn: UUID,
        email: str,
        password: str,
        auth_type_id: int,
        created_by: int,
        is_mfa_enabled: bool = False,
        mfa_secret: Optional[str] = None,
        last_login: Optional[datetime] = None,
        mfa_type_id: Optional[int] = None,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
    ) -> Self:
        """Construct an instance with named arguments."""
        return User(
            urn=urn,
            email=email,
            password=password,
            is_mfa_enabled=is_mfa_enabled,
            mfa_secret=mfa_secret,
            last_login=last_login,
            mfa_type_id=mfa_type_id,
            auth_type_id=auth_type_id,
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
        return Model.USER
