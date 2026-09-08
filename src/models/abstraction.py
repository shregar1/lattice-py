"""Base ORM models for SignFlow entities."""

from datetime import datetime
from typing import Any, Optional, Self
from uuid import UUID, uuid4

from abstractions import ModelLayer
from constants import DBColumn, DBTable

from .fields import (
    BigIntegerField,
    BooleanField,
    Field,
    ForeignKey,
    TextField,
    TimestampTZField,
    UUIDField,
)


class IModel(ModelLayer):
    """Base ORM model for all entities in the models package."""

    id: int = BigIntegerField(primary_key=True, nullable=False)
    urn: UUID = UUIDField(unique=True, default_factory=uuid4, nullable=False)
    created_at: datetime = TimestampTZField(server_default="now()", nullable=False)
    updated_at: datetime = TimestampTZField(nullable=True)
    created_by: int = ForeignKey(f"{DBTable.USER}.{DBColumn.ID}", nullable=False)
    updated_by: int = ForeignKey(f"{DBTable.USER}.{DBColumn.ID}", nullable=False)
    is_deleted: bool = BooleanField(default=False, nullable=False)
    is_active: bool = BooleanField(default=True, nullable=False)

    @classmethod
    def build(cls, **kwargs: Any) -> Self:
        """Constructs a fully-populated model instance from named arguments."""
        return cls(**kwargs)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IModel"


class ISignFlowModel(IModel):
    """SignFlow domain models carrying an app-facing external identifier."""

    external_id: str = Field(max_length=64, unique=True, nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ISignFlowModel"


class ICoreLookupModel(ModelLayer):
    """Base ORM model for identity/core lookup tables (code + description only)."""

    id: int = BigIntegerField(primary_key=True, nullable=False)
    urn: UUID = UUIDField(unique=True, default_factory=uuid4, nullable=False)
    code: str = Field(max_length=50, unique=True, nullable=False)
    description: str = Field(max_length=255, nullable=False)
    created_at: datetime = TimestampTZField(server_default="now()", nullable=False)
    updated_at: datetime = TimestampTZField(server_default="now()", nullable=False)
    is_deleted: bool = BooleanField(default=False, nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICoreLookupModel"


class ILookupModel(ModelLayer):
    """Base ORM model for reference/lookup tables."""

    id: int = BigIntegerField(primary_key=True, nullable=False)
    urn: UUID = UUIDField(unique=True, default_factory=uuid4, nullable=False)
    code: str = Field(max_length=50, unique=True, nullable=False)
    label: str = Field(max_length=255, nullable=False)
    description: str = TextField(nullable=False)
    created_at: datetime = TimestampTZField(server_default="now()", nullable=False)
    updated_at: datetime = TimestampTZField(nullable=True)
    is_deleted: bool = BooleanField(default=False, nullable=False)
    is_active: bool = BooleanField(default=True, nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ILookupModel"


class IUserModel(IModel):
    """Base model class for user domain entities."""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IUserModel"


class ITenantModel(IModel):
    """Base model class for tenant domain entities."""

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ITenantModel"


class ICompanyProfileModel(IModel):
    """Base model class for tenant-scoped company profile entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False, unique=True)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICompanyProfileModel"


class IEnvelopeModel(ISignFlowModel):
    """Base model class for envelope domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IEnvelopeModel"


class IContactModel(ISignFlowModel):
    """Base model class for contact domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IContactModel"


class IInviteModel(ISignFlowModel):
    """Base model class for invite domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IInviteModel"


class IContractModel(ISignFlowModel):
    """Base model class for contract domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IContractModel"


class IExportModel(ISignFlowModel):
    """Base model class for export domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IExportModel"


class IWebhookModel(ISignFlowModel):
    """Base model class for webhook domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IWebhookModel"


class ITeamModel(ISignFlowModel):
    """Base model class for team domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ITeamModel"


class ITemplateModel(ISignFlowModel):
    """Base model class for template domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ITemplateModel"


class IProjectModel(ISignFlowModel):
    """Base model class for project domain entities."""

    tenant_id: int = ForeignKey(f"{DBTable.TENANT}.{DBColumn.ID}", nullable=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IProjectModel"
