from datetime import datetime
from typing import Optional, Self
from uuid import UUID


from pydantic import EmailStr, HTTPUrl

from constants import DBTable, Model
from ..abstraction import ICompanyProfileModel
from ..fields import EmailField, Field, HTTPURLField, SmallIntegerField, TextField, TimestampTZField, URLField


class CompanyProfile(ICompanyProfileModel):
    """Tenant company profile captured during onboarding and settings."""

    __tablename__ = DBTable.COMPANY_PROFILE

    legal_name: str = Field(max_length=255, nullable=False)
    display_name: str = Field(max_length=255, nullable=False)
    industry: Optional[str] = Field(max_length=100, nullable=True)
    company_size: Optional[str] = Field(max_length=32, nullable=True)
    business_type: Optional[str] = Field(max_length=64, nullable=True)
    description: Optional[str] = TextField(nullable=True)
    tax_id: Optional[str] = Field(max_length=64, nullable=True)
    website: Optional[HTTPUrl] = HTTPURLField(max_length=2048, nullable=True)
    phone: Optional[str] = Field(max_length=32, nullable=True)
    support_email: Optional[EmailStr] = EmailField(nullable=True)
    billing_email: Optional[EmailStr] = EmailField(nullable=True)
    address_line_1: Optional[str] = Field(max_length=255, nullable=True)
    address_line_2: Optional[str] = Field(max_length=255, nullable=True)
    city: Optional[str] = Field(max_length=100, nullable=True)
    state: Optional[str] = Field(max_length=100, nullable=True)
    zip_code: Optional[str] = Field(max_length=20, nullable=True)
    country_code: Optional[str] = Field(max_length=2, min_length=2, nullable=True)
    logo_url: Optional[HTTPUrl] = URLField(max_length=2048, nullable=True)
    logo_text: Optional[str] = Field(max_length=12, nullable=True)
    accent_color: Optional[str] = Field(max_length=7, pattern=r"^#[0-9a-fA-F]{6}$", nullable=True)
    email_footer: Optional[str] = Field(max_length=500, nullable=True)
    timezone: Optional[str] = Field(max_length=100, nullable=True)
    onboarding_step: int = SmallIntegerField(default=0, nullable=False)
    onboarding_completed_at: Optional[datetime] = TimestampTZField(nullable=True)

    @classmethod
    def build(
        cls,
        urn: UUID,
        tenant_id: int,
        legal_name: str,
        display_name: str,
        created_by: int,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
        industry: Optional[str] = None,
        company_size: Optional[str] = None,
        business_type: Optional[str] = None,
        description: Optional[str] = None,
        tax_id: Optional[str] = None,
        website: Optional[str] = None,
        phone: Optional[str] = None,
        support_email: Optional[str] = None,
        billing_email: Optional[str] = None,
        address_line_1: Optional[str] = None,
        address_line_2: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        zip_code: Optional[str] = None,
        country_code: Optional[str] = None,
        logo_url: Optional[str] = None,
        logo_text: Optional[str] = None,
        accent_color: Optional[str] = None,
        email_footer: Optional[str] = None,
        timezone: Optional[str] = None,
        onboarding_step: int = 0,
        onboarding_completed_at: Optional[datetime] = None,
    ) -> Self:
        """Construct a company profile instance."""
        return CompanyProfile(
            urn=urn,
            tenant_id=tenant_id,
            legal_name=legal_name,
            display_name=display_name,
            industry=industry,
            company_size=company_size,
            business_type=business_type,
            description=description,
            tax_id=tax_id,
            website=website,
            phone=phone,
            support_email=support_email,
            billing_email=billing_email,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state=state,
            zip_code=zip_code,
            country_code=country_code,
            logo_url=logo_url,
            logo_text=logo_text,
            accent_color=accent_color,
            email_footer=email_footer,
            timezone=timezone,
            onboarding_step=onboarding_step,
            onboarding_completed_at=onboarding_completed_at,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            is_deleted=is_deleted,
            is_active=is_active,
        )

    @property
    def name(self) -> str:
        """Returns the model name constant."""
        return Model.COMPANY_PROFILE
