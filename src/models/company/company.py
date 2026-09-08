from datetime import datetime
from typing import Optional, Self
from uuid import UUID



from constants import DBColumn, DBTable, Model
from ..abstraction import IModel
from ..fields import Field, ForeignKey


class Company(IModel):
    """User membership within a tenant workspace."""

    __tablename__ = DBTable.COMPANY

    name: str = Field(max_length=255, nullable=False)
    title: str = Field(max_length=255, nullable=False)
    user_type_id: int = ForeignKey(f"{DBTable.USER_TYPE_LK}.{DBColumn.ID}", nullable=False)
    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)
    user_id: int = ForeignKey(f"{DBTable.USER}.{DBColumn.ID}", nullable=False)

    @classmethod
    def build(
        cls,
        urn: UUID,
        user_type_id: int,
        tenant_id: int,
        user_id: int,
        created_by: int,
        name: str,
        title: str = None,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
    ) -> Self:
        """Construct an instance with named arguments."""
        return Company(
            name=name,
            title=title,
            user_type_id=user_type_id,
            tenant_id=tenant_id,
            user_id=user_id,
            urn=urn,
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
        return Model.COMPANY
