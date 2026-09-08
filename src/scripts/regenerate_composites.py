#!/usr/bin/env python3
"""Regenerate all composites inheriting from their atomic repositories."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPOSITE = ROOT / "repositories" / "composite"

SPECS: dict[str, tuple] = {
    "auth_type_lk": (
        "AuthTypeLK",
        "AuthTypeLKRepository",
        "CompositeAuthTypeLKRepository",
        "AuthTypeLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "envelope_status_lk": (
        "EnvelopeStatusLK",
        "EnvelopeStatusLKRepository",
        "CompositeEnvelopeStatusLKRepository",
        "EnvelopeStatusLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "event_type_lk": (
        "EventTypeLK",
        "EventTypeLKRepository",
        "CompositeEventTypeLKRepository",
        "EventTypeLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "mfa_type_lk": (
        "MFATypeLK",
        "MFATypeLKRepository",
        "CompositeMFATypeLKRepository",
        "MFATypeLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "mime_type_lk": (
        "MimeTypeLK",
        "MimeTypeLKRepository",
        "CompositeMimeTypeLKRepository",
        "MimeTypeLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "otp_type_lk": (
        "OtpTypeLK",
        "OtpTypeLKRepository",
        "CompositeOtpTypeLKRepository",
        "OtpTypeLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "recipient_status_lk": (
        "RecipientStatusLK",
        "RecipientStatusLKRepository",
        "CompositeRecipientStatusLKRepository",
        "RecipientStatusLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "team_member_status_lk": (
        "TeamMemberStatusLK",
        "TeamMemberStatusLKRepository",
        "CompositeTeamMemberStatusLKRepository",
        "TeamMemberStatusLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "user_type_lk": (
        "UserTypeLK",
        "UserTypeLKRepository",
        "CompositeUserTypeLKRepository",
        "UserTypeLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "webhook_delivery_status_lk": (
        "WebhookDeliveryStatusLK",
        "WebhookDeliveryStatusLKRepository",
        "CompositeWebhookDeliveryStatusLKRepository",
        "WebhookDeliveryStatusLKDependency",
        "lookup_model",
        "lookup",
        [("code", "str", "code")],
    ),
    "audit_event": (
        "AuditEvent",
        "AuditEventRepository",
        "CompositeAuditEventRepository",
        "AuditEventDependency",
        "audit_event_model",
        "tenant",
        [("tenant", "int", "tenant_id"), ("envelope_id", "int", "envelope_id")],
    ),
    "company_profile": (
        "CompanyProfile",
        "CompanyProfileRepository",
        "CompositeCompanyProfileRepository",
        "CompanyProfileDependency",
        "company_profile_model",
        "tenant",
        [("tenant", "int", "tenant_id")],
    ),
    "contact": (
        "Contact",
        "ContactRepository",
        "CompositeContactRepository",
        "ContactDependency",
        "contact_model",
        "tenant",
        [("tenant", "int", "tenant_id"), ("email", "str", "email")],
    ),
    "envelope": (
        "Envelope",
        "EnvelopeRepository",
        "CompositeEnvelopeRepository",
        "EnvelopeDependency",
        "envelope_model",
        "tenant",
        [
            ("tenant", "int", "tenant_id"),
            ("status_id", "int", "status_id"),
            ("template_id", "int", "template_id"),
            ("external_id", "str", "external_id"),
        ],
    ),
    "export_record": (
        "ExportRecord",
        "ExportRepository",
        "CompositeExportRepository",
        "ExportDependency",
        "export_model",
        "tenant",
        [
            ("tenant", "int", "tenant_id"),
            ("envelope_id", "int", "envelope_id"),
            ("kind", "str", "kind"),
        ],
    ),
    "team_member": (
        "TeamMember",
        "TeamMemberRepository",
        "CompositeTeamMemberRepository",
        "TeamMemberDependency",
        "team_member_model",
        "tenant",
        [
            ("tenant", "int", "tenant_id"),
            ("email", "str", "email"),
            ("status_id", "int", "status_id"),
            ("role", "str", "role"),
        ],
    ),
    "template": (
        "Template",
        "TemplateRepository",
        "CompositeTemplateRepository",
        "TemplateDependency",
        "template_model",
        "tenant",
        [
            ("tenant", "int", "tenant_id"),
            ("template_name", "str", "template_name"),
            ("shared", "bool", "shared"),
        ],
    ),
    "webhook_delivery": (
        "WebhookDelivery",
        "WebhookDeliveryRepository",
        "CompositeWebhookDeliveryRepository",
        "WebhookDeliveryDependency",
        "webhook_delivery_model",
        "tenant",
        [
            ("tenant", "int", "tenant_id"),
            ("endpoint_id", "int", "endpoint_id"),
            ("envelope_id", "int", "envelope_id"),
            ("event_type_id", "int", "event_type_id"),
        ],
    ),
    "webhook_endpoint": (
        "WebhookEndpoint",
        "WebhookEndpointRepository",
        "CompositeWebhookEndpointRepository",
        "WebhookEndpointDependency",
        "webhook_endpoint_model",
        "tenant",
        [("tenant", "int", "tenant_id"), ("active", "bool", "active")],
    ),
    "tenant_profile": (
        "TenantProfile",
        "TenantProfileRepository",
        "CompositeTenantProfileRepository",
        "TenantProfileDependency",
        "tenant_profile_model",
        "tenant",
        [("tenant_id", "int", "tenant_id"), ("name", "str", "name")],
    ),
    "recipient": (
        "Recipient",
        "RecipientRepository",
        "CompositeRecipientRepository",
        "RecipientDependency",
        "recipient_model",
        "nested_envelope",
        [("envelope_id", "int", "envelope_id")],
    ),
    "template_role": (
        "TemplateRole",
        "TemplateRoleRepository",
        "CompositeTemplateRoleRepository",
        "TemplateRoleDependency",
        "template_role_model",
        "nested_template",
        [("template_id", "int", "template_id")],
    ),
    "field": (
        "Field",
        "FieldRepository",
        "CompositeFieldRepository",
        "FieldDependency",
        "field_model",
        "nested_field",
        [("envelope_id", "int", "envelope_id")],
    ),
    "company": (
        "Company",
        "CompanyRepository",
        "CompositeCompanyRepository",
        "CompanyDependency",
        "company_model",
        "company",
        [
            ("user_id", "int", "user_id"),
            ("tenant_id", "int", "tenant_id"),
            ("user_type_id", "int", "user_type_id"),
        ],
    ),
    "user": (
        "User",
        "UserRepository",
        "CompositeUserRepository",
        "UserDependency",
        "user_model",
        "user",
        [
            ("email", "str", "email"),
            ("auth_type_id", "int", "auth_type_id"),
            ("is_mfa_enabled", "bool", "is_mfa_enabled"),
        ],
    ),
    "tenant": (
        "Tenant",
        "TenantRepository",
        "CompositeTenantRepository",
        "TenantDependency",
        "tenant_model",
        "tenant_root",
        [("subdomain", "str", "subdomain")],
    ),
    "user_otp": (
        "UserOtp",
        "UserOtpRepository",
        "CompositeUserOtpRepository",
        "UserOtpDependency",
        "user_otp_model",
        "user_owned",
        [("user_id", "int", "user_id"), ("otp_type_id", "int", "otp_type_id")],
    ),
    "user_recovery_code": (
        "UserRecoveryCode",
        "UserRecoveryCodeRepository",
        "CompositeUserRecoveryCodeRepository",
        "UserRecoveryCodeDependency",
        "user_recovery_code_model",
        "user_owned",
        [("user_id", "int", "user_id"), ("is_used", "bool", "is_used")],
    ),
}


def logged_exists(doc: str, body: str) -> str:
    return f'''    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """{doc}"""
        start_time = time.time()

        try:
{body}
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for exists_by_id_user_and_tenant",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={{"entity_id": entity_id, "user_id": user_id, "tenant_id": tenant_id}},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for exists_by_id_user_and_tenant",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={{"entity_id": entity_id, "user_id": user_id, "tenant_id": tenant_id}},
                error=str(exc),
                exc=exc,
            )
            return False
'''


def logged_filter(fname: str, pname: str, ptype: str, model: str, attr: str, col: str) -> str:
    return f'''    def {fname}(self, {pname}: {ptype}) -> List[{model}]:
        """Filter {model} records by {col}."""
        start_time = time.time()

        try:
            result = list(self.{attr}.find_many({col}={pname}))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for {fname}",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={{"{pname}": {pname}}},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for {fname}",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={{"{pname}": {pname}}},
                error=str(exc),
                exc=exc,
            )
            raise exc
'''


def exists_body(kind: str, attr: str) -> tuple[str, str]:
    if kind == "lookup":
        return (
            "Verifies lookup record existence.",
            f"            result = self.{attr}.exists(id=entity_id)",
        )
    if kind == "company":
        return (
            "Prevents IDOR by verifying company user and tenant ownership.",
            f"            result = self.{attr}.exists(id=entity_id, user_id=user_id, tenant_id=tenant_id)",
        )
    if kind == "tenant":
        return (
            "Prevents IDOR: record in tenant and caller is a company member.",
            f"""            result = (
                self.{attr}.exists(id=entity_id, tenant_id=tenant_id)
                and self.company_model.exists(user_id=user_id, tenant_id=tenant_id)
            )""",
        )
    if kind == "user_owned":
        return (
            "Prevents IDOR: record owned by user and caller is a company member.",
            f"""            result = (
                self.{attr}.exists(id=entity_id, user_id=user_id)
                and self.company_model.exists(user_id=user_id, tenant_id=tenant_id)
            )""",
        )
    if kind == "user":
        return (
            "Prevents IDOR: target user and caller both belong to the tenant.",
            """            result = (
                self.user_model.exists(id=entity_id)
                and self.company_model.exists(user_id=entity_id, tenant_id=tenant_id)
                and self.company_model.exists(user_id=user_id, tenant_id=tenant_id)
            )""",
        )
    if kind == "tenant_root":
        return (
            "Prevents IDOR: tenant id matches and caller is a company member.",
            """            result = (
                entity_id == tenant_id
                and self.tenant_model.exists(id=entity_id)
                and self.company_model.exists(user_id=user_id, tenant_id=tenant_id)
            )""",
        )
    if kind == "nested_envelope":
        return (
            "Prevents IDOR: parent tenant match and caller is a company member.",
            """            record: Optional[Recipient] = self.recipient_model.find_one(id=entity_id)
            if record is None:
                result = False
            else:
                parent: Optional[Envelope] = self.envelope_model.find_one(
                    id=getattr(record, "envelope_id")
                )
                if parent is None or getattr(parent, "tenant_id") != tenant_id:
                    result = False
                else:
                    result = self.company_model.exists(user_id=user_id, tenant_id=tenant_id)""",
        )
    if kind == "nested_template":
        return (
            "Prevents IDOR: parent tenant match and caller is a company member.",
            """            record: Optional[TemplateRole] = self.template_role_model.find_one(id=entity_id)
            if record is None:
                result = False
            else:
                parent: Optional[Template] = self.template_model.find_one(
                    id=getattr(record, "template_id")
                )
                if parent is None or getattr(parent, "tenant_id") != tenant_id:
                    result = False
                else:
                    result = self.company_model.exists(user_id=user_id, tenant_id=tenant_id)""",
        )
    if kind == "nested_field":
        return (
            "Prevents IDOR: parent tenant match and caller is a company member.",
            """            record: Optional[Field] = self.field_model.find_one(id=entity_id)
            if record is None:
                result = False
            else:
                parent_tenant_id: Optional[int] = None
                envelope_id = getattr(record, "envelope_id", None)
                template_id = getattr(record, "template_id", None)
                if envelope_id is not None:
                    parent: Optional[Envelope] = self.envelope_model.find_one(id=envelope_id)
                    parent_tenant_id = (
                        getattr(parent, "tenant_id", None) if parent is not None else None
                    )
                elif template_id is not None:
                    template_parent: Optional[Template] = self.template_model.find_one(
                        id=template_id
                    )
                    parent_tenant_id = (
                        getattr(template_parent, "tenant_id", None)
                        if template_parent is not None
                        else None
                    )
                if parent_tenant_id != tenant_id:
                    result = False
                else:
                    result = self.company_model.exists(user_id=user_id, tenant_id=tenant_id)""",
        )
    raise ValueError(kind)


def render(module: str, spec: tuple) -> str:
    model, atomic, composite, dep, attr, kind, filters = spec

    models_import: set[str] = {model}
    deps_import: set[str] = {dep}
    related_params: list[str] = []
    related_assigns: list[str] = []

    needs_company = kind not in {"lookup", "company"}
    if needs_company:
        models_import.add("Company")
        deps_import.add("CompanyDependency")
        related_params.append(
            "company_model: type[Company] = Dependency(CompanyDependency)"
        )
        related_assigns.append("self.company_model = company_model")

    if kind in {
        "tenant",
        "nested_envelope",
        "nested_template",
        "nested_field",
        "user",
        "user_owned",
        "company",
        "lookup",
    }:
        models_import.update(["Tenant", "User"])
        deps_import.update(["TenantDependency", "UserDependency"])
        related_params.append(
            "tenant_model: type[Tenant] = Dependency(TenantDependency)"
        )
        related_params.append("user_model: type[User] = Dependency(UserDependency)")
        related_assigns.append("self.tenant_model = tenant_model")
        related_assigns.append("self.user_model = user_model")
    elif kind == "tenant_root":
        models_import.add("User")
        deps_import.add("UserDependency")
        related_params.append("user_model: type[User] = Dependency(UserDependency)")
        related_assigns.append("self.user_model = user_model")

    if kind == "nested_envelope":
        models_import.add("Envelope")
        deps_import.add("EnvelopeDependency")
        related_params.insert(
            1, "envelope_model: type[Envelope] = Dependency(EnvelopeDependency)"
        )
        related_assigns.insert(1, "self.envelope_model = envelope_model")
    if kind == "nested_template":
        models_import.add("Template")
        deps_import.add("TemplateDependency")
        related_params.insert(
            1, "template_model: type[Template] = Dependency(TemplateDependency)"
        )
        related_assigns.insert(1, "self.template_model = template_model")
    if kind == "nested_field":
        models_import.update(["Envelope", "Template"])
        deps_import.update(["EnvelopeDependency", "TemplateDependency"])
        related_params.insert(
            1, "envelope_model: type[Envelope] = Dependency(EnvelopeDependency)"
        )
        related_params.insert(
            2, "template_model: type[Template] = Dependency(TemplateDependency)"
        )
        related_assigns.insert(1, "self.envelope_model = envelope_model")
        related_assigns.insert(2, "self.template_model = template_model")
    if kind == "company":
        models_import.add("UserTypeLK")
        deps_import.add("UserTypeLKDependency")
        related_params.append(
            "user_type_lk_model: type[UserTypeLK] = Dependency(UserTypeLKDependency)"
        )
        related_assigns.append("self.user_type_lk_model = user_type_lk_model")
    if kind == "user":
        models_import.update(["AuthTypeLK", "MFATypeLK"])
        deps_import.update(["AuthTypeLKDependency", "MFATypeLKDependency"])
        related_params.append(
            "auth_type_lk_model: type[AuthTypeLK] = Dependency(AuthTypeLKDependency)"
        )
        related_params.append(
            "mfa_type_lk_model: type[MFATypeLK] = Dependency(MFATypeLKDependency)"
        )
        related_assigns.append("self.auth_type_lk_model = auth_type_lk_model")
        related_assigns.append("self.mfa_type_lk_model = mfa_type_lk_model")

    models_list = sorted(models_import)
    deps_list = sorted(deps_import)

    ctor_params = [
        "logger: Logger = Dependency(LoggerUtilityDependency)",
        f"model: type[{model}] = Dependency({dep})",
    ] + related_params

    assigns = [f"self.{attr} = model"] + related_assigns

    doc, body = exists_body(kind, attr)
    exists_method = logged_exists(doc, body)

    filter_methods: list[str] = []
    for suffix, ptype, col in filters:
        if suffix == "tenant":
            fname, pname = "filter_by_tenant", "tenant_id"
        else:
            fname, pname = f"filter_by_{suffix}", suffix
        filter_methods.append(logged_filter(fname, pname, ptype, model, attr, col))

    deps_block = ",\n    ".join(deps_list)
    models_block = ", ".join(models_list)
    ctor_block = ",\n        ".join(ctor_params)
    assign_block = "\n        ".join(assigns)
    filters_block = "\n".join(filter_methods)

    return f'''""" repository implementation for {model}."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    {deps_block},
)
from dependencies.utility import LoggerUtilityDependency
from models import {models_block}
from repositories.atomic import {atomic}
from utilities import Logger

from .abstraction import ICompositeRepository


class {composite}({atomic}, ICompositeRepository):
    """ repository for {model}; extends atomic {atomic}."""

    def __init__(
        self,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        {ctor_block},
        *args: Any,
        **kwargs: Any,
    ) -> None:
        {atomic}.__init__(
            self,
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            logger=logger,
            model=model,
            *args,
            **kwargs,
        )
        {assign_block}

{exists_method}
{filters_block}
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "{composite}"
'''


def main() -> None:
    composites: list[str] = []
    for module, spec in sorted(SPECS.items()):
        (COMPOSITE / f"{module}.py").write_text(render(module, spec))
        composites.append(spec[2])
        print("wrote", module)

    init = '"""SignFlow composite repositories."""\n\n'
    for module, spec in sorted(SPECS.items()):
        init += f"from .{module} import {spec[2]}\n"
    init += "\n__all__ = [\n"
    for name in sorted(composites):
        init += f'    "{name}",\n'
    init += "]\n"
    (COMPOSITE / "__init__.py").write_text(init)

    atomic_names = sorted({s[1] for s in SPECS.values()})
    composite_names = sorted(composites)
    repo_init = '"""Repositories package top-level exports."""\n\n'
    repo_init += "from repositories.atomic import (\n"
    for n in atomic_names:
        repo_init += f"    {n},\n"
    repo_init += ")\n\nfrom repositories.composite import (\n"
    for n in composite_names:
        repo_init += f"    {n},\n"
    repo_init += ")\n\n__all__ = [\n"
    for n in composite_names + atomic_names:
        repo_init += f'    "{n}",\n'
    repo_init += "]\n"
    (ROOT / "repositories" / "__init__.py").write_text(repo_init)

    mapping = [
        ("AUDIT_EVENT", "AuditEvent"),
        ("AUTH_TYPE_LK", "AuthTypeLK"),
        ("COMPANY", "Company"),
        ("COMPANY_PROFILE", "CompanyProfile"),
        ("CONTACT", "Contact"),
        ("ENVELOPE", "Envelope"),
        ("ENVELOPE_STATUS_LK", "EnvelopeStatusLK"),
        ("EVENT_TYPE_LK", "EventTypeLK"),
        ("EXPORT", "Export"),
        ("FIELD", "Field"),
        ("MFA_TYPE_LK", "MFATypeLK"),
        ("MIME_TYPE_LK", "MimeTypeLK"),
        ("OTP_TYPE_LK", "OtpTypeLK"),
        ("RECIPIENT", "Recipient"),
        ("RECIPIENT_STATUS_LK", "RecipientStatusLK"),
        ("TEAM_MEMBER", "TeamMember"),
        ("TEAM_MEMBER_STATUS_LK", "TeamMemberStatusLK"),
        ("TEMPLATE", "Template"),
        ("TEMPLATE_ROLE", "TemplateRole"),
        ("TENANT", "Tenant"),
        ("TENANT_PROFILE", "TenantProfile"),
        ("USER", "User"),
        ("USER_OTP", "UserOtp"),
        ("USER_RECOVERY_CODE", "UserRecoveryCode"),
        ("USER_TYPE_LK", "UserTypeLK"),
        ("WEBHOOK_DELIVERY", "WebhookDelivery"),
        ("WEBHOOK_DELIVERY_STATUS_LK", "WebhookDeliveryStatusLK"),
        ("WEBHOOK_ENDPOINT", "WebhookEndpoint"),
    ]

    dep_const = '''"""Repository dependency layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class RepositoryDependency(ILayerConstant):
'''
    for key, base in mapping:
        dep_const += f'\n    {key}: Final[str] = "{base}RepositoryDependency"'
        dep_const += f'\n    COMPOSITE_{key}: Final[str] = "{base}RepositoryDependency"'
    dep_const += '''

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RepositoryDependency"
'''
    (ROOT / "constants" / "layer" / "dependency" / "repository.py").write_text(dep_const)

    repo_const = '''"""RepositoryName — PascalCase class-name constants for the repository layer."""

from typing import Final

from .abstraction import ILayerConstant


class Repository(ILayerConstant):
'''
    for key, base in mapping:
        repo_const += f'\n    {key}: Final[str] = "{base}Repository"'
        repo_const += f'\n    COMPOSITE_{key}: Final[str] = "{base}Repository"'
    repo_const += '''

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Repository"
'''
    (ROOT / "constants" / "layer" / "repository.py").write_text(repo_const)

    print(f"generated {len(SPECS)} composites")


if __name__ == "__main__":
    main()
