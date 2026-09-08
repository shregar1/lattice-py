from datetime import datetime
from typing import Optional, Self
from uuid import UUID


from pydantic import HTTPUrl

from constants import DBColumn, DBTable, Model
from ..abstraction import ITenantModel
from ..fields import Field, ForeignKey, HTTPURLField, TextField, URLField


class TenantProfile(ITenantModel):

    __tablename__ = DBTable.TENANT_PROFILE

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)
    name: str = Field(max_length=255, nullable=False)
    logo_url: Optional[HTTPUrl] = URLField(max_length=2048, nullable=True)
    website: HTTPUrl = HTTPURLField(max_length=2048, nullable=False)
    industry: Optional[str] = Field(max_length=100, nullable=True)
    description: Optional[str] = TextField(nullable=True)

    @classmethod
    def build(
        cls,
        urn: UUID,
        tenant_id: int,
        name: str,
        website: str,
        created_by: int,
        logo_url: Optional[str] = None,
        industry: Optional[str] = None,
        description: Optional[str] = None,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
    ) -> Self:
        """Construct an instance with named arguments."""
        return TenantProfile(
            urn=urn,
            name=name,
            website=website,
            logo_url=logo_url,
            industry=industry,
            description=description,
            tenant_id=tenant_id,
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
        return Model.TENANT_PROFILE
