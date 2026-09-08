from datetime import datetime
from typing import Self, Optional
from uuid import UUID



from constants import DBTable, Model
from ..abstraction import ITenantModel
from ..fields import Field


class Tenant(ITenantModel):

    __tablename__ = DBTable.TENANT

    subdomain: str = Field(max_length=100, unique=True, nullable=False)

    @classmethod
    def build(
        cls,
        urn: UUID,
        subdomain: str,
        created_by: int,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
    ) -> Self:
        """Construct an instance with named arguments."""
        return Tenant(
            urn=urn,
            subdomain=subdomain,
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
        return Model.TENANT
