#!/usr/bin/env python3
"""Generate SignFlow atomic and composite repositories."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATOMIC = ROOT / "repositories" / "atomic"
COMPOSITE = ROOT / "repositories" / "composite"

LOOKUP_MODELS = [
    "EventTypeLK",
    "MimeTypeLK",
    "EnvelopeStatusLK",
    "RecipientStatusLK",
    "TeamMemberStatusLK",
    "WebhookDeliveryStatusLK",
]

CORE_LOOKUP_MODELS = [
    "UserTypeLK",
    "AuthTypeLK",
    "MFATypeLK",
    "OtpTypeLK",
]

TENANT_SCOPED = {
    "AuditEvent": ["envelope_id"],
    "CompanyProfile": [],
    "Contact": ["email"],
    "Envelope": ["status_id", "template_id", "external_id"],
    "ExportRecord": ["envelope_id", "kind"],
    "TeamMember": ["email", "status_id", "role"],
    "Template": ["template_name", "shared"],
    "WebhookDelivery": ["endpoint_id", "envelope_id", "event_type_id"],
    "WebhookEndpoint": ["active"],
}

NESTED_SCOPED = {
    "Recipient": ("envelope_id", "Envelope", "tenant_id"),
    "TemplateRole": ("template_id", "Template", "tenant_id"),
    "Field": ("envelope_id", "Envelope", "tenant_id"),
}

STANDALONE = {
    "Company": {
        "filters": ["user_id", "tenant_id", "user_type_id"],
        "composite_models": ["Tenant", "User", "UserTypeLK"],
        "idor": ("id", "user_id", "tenant_id"),
    },
    "Tenant": {
        "filters": ["subdomain"],
        "composite_models": ["User"],
        "idor_expr": "return self.tenant_model.exists(id=entity_id)",
    },
    "TenantProfile": {
        "filters": ["tenant_id", "name"],
        "composite_models": ["Tenant", "User"],
        "idor_expr": "return self.tenant_profile_model.exists(id=entity_id, tenant_id=tenant_id)",
    },
    "User": {
        "filters": ["email", "auth_type_id", "is_mfa_enabled"],
        "composite_models": ["AuthTypeLK", "MFATypeLK", "Tenant"],
        "idor_expr": "return self.user_model.exists(id=entity_id)",
    },
    "UserOtp": {
        "filters": ["user_id", "otp_type_id"],
        "composite_models": ["User", "OtpTypeLK"],
        "idor_expr": "return self.user_otp_model.exists(id=entity_id, user_id=user_id)",
    },
    "UserRecoveryCode": {
        "filters": ["user_id", "is_used"],
        "composite_models": ["User"],
        "idor_expr": "return self.user_recovery_code_model.exists(id=entity_id, user_id=user_id)",
    },
}


CONST_KEYS = {
    "AuditEvent": "AUDIT_EVENT",
    "AuthTypeLK": "AUTH_TYPE_LK",
    "Company": "COMPANY",
    "CompanyProfile": "COMPANY_PROFILE",
    "Contact": "CONTACT",
    "Envelope": "ENVELOPE",
    "EnvelopeStatusLK": "ENVELOPE_STATUS_LK",
    "EventTypeLK": "EVENT_TYPE_LK",
    "ExportRecord": "EXPORT",
    "Field": "FIELD",
    "MFATypeLK": "MFA_TYPE_LK",
    "MimeTypeLK": "MIME_TYPE_LK",
    "OtpTypeLK": "OTP_TYPE_LK",
    "Recipient": "RECIPIENT",
    "RecipientStatusLK": "RECIPIENT_STATUS_LK",
    "TeamMember": "TEAM_MEMBER",
    "TeamMemberStatusLK": "TEAM_MEMBER_STATUS_LK",
    "Template": "TEMPLATE",
    "TemplateRole": "TEMPLATE_ROLE",
    "Tenant": "TENANT",
    "TenantProfile": "TENANT_PROFILE",
    "User": "USER",
    "UserOtp": "USER_OTP",
    "UserRecoveryCode": "USER_RECOVERY_CODE",
    "UserTypeLK": "USER_TYPE_LK",
    "WebhookDelivery": "WEBHOOK_DELIVERY",
    "WebhookDeliveryStatusLK": "WEBHOOK_DELIVERY_STATUS_LK",
    "WebhookEndpoint": "WEBHOOK_ENDPOINT",
}


def snake(name: str) -> str:
    import re

    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    return s.lower()


def const_key(model: str) -> str:
    return CONST_KEYS[model]


def model_var(model: str) -> str:
    if model == "ExportRecord":
        return "export_model"
    return f"{snake(model)}_model"


def repo_name(model: str) -> str:
    if model == "ExportRecord":
        return "ExportRepository"
    return f"{model}Repository"


def composite_repo_name(model: str) -> str:
    if model == "ExportRecord":
        return "CompositeExportRepository"
    return f"{model}Repository"


LOOKUP_ABSTRACTION = '''"""Lookup repository abstraction layer."""

from abc import ABC
from typing import Any, Dict, List, Optional, Sequence

from rivex import Dependency

from dependencies import LoggerUtilityDependency
from models import IModel
from utilities import Logger

from .abstraction import IAtomicRepository


class ILookupRepository(IAtomicRepository[IModel, int], ABC):
    """Base class for lookup (reference/type table) repositories."""

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
        model: IModel = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        IAtomicRepository.__init__(
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
            *args,
            **kwargs,
        )
        self.model = model
        self.model_class = model

    def find_by_code(self, code: str) -> Optional[IModel]:
        """Find a lookup record by its unique code."""
        results = self.filter("code", code)
        return results[0] if results else None

    def find_by_codes(self, codes: Sequence[str]) -> List[IModel]:
        """Find lookup records matching a list of codes."""
        if not codes:
            return []
        return self.filter_in("code", codes)

    def exists_by_code(self, code: str) -> bool:
        """Check if a lookup record exists with the given code."""
        return self.find_by_code(code) is not None

    def get_code_map(self) -> Dict[str, IModel]:
        """Returns a dictionary mapping lookup code -> model instance."""
        return {
            getattr(item, "code"): item
            for item in self.list_all()
            if hasattr(item, "code")
        }

    def get_id_by_code(self, code: str) -> Optional[int]:
        """Resolves the primary key ID for a given lookup code."""
        item = self.find_by_code(code)
        return getattr(item, "id", None) if item is not None else None
'''


def atomic_lookup(model: str) -> str:
    repo = repo_name(model)
    return f'''"""Repository for {model} persistence and domain queries."""

from typing import Any, Optional

from rivex import Dependency

from dependencies import LoggerUtilityDependency
from models import {model}
from utilities import Logger

from .lookup_abstraction import ILookupRepository


class {repo}(ILookupRepository[{model}, int]):
    """Atomic repository for {model}."""

    def __init__(
        self,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        model: {model} = {model},
        *args: Any,
        **kwargs: Any,
    ) -> None:
        if model is None:
            logger.error("No model found")
            raise ModuleNotFoundError("No model found")

        ILookupRepository.__init__(
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
            **kwargs,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "{repo}"
'''


def atomic_standard(model: str, extra_methods: str = "") -> str:
    repo = repo_name(model)
    return f'''"""Repository for {model} persistence and domain queries."""

from typing import Any, Optional

from rivex import Dependency

from dependencies import LoggerUtilityDependency
from models import {model}
from utilities import Logger

from .abstraction import IAtomicRepository


class {repo}(IAtomicRepository[{model}, int]):
    """Atomic repository for {model}."""

    def __init__(
        self,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        model: {model} = {model},
        *args: Any,
        **kwargs: Any,
    ) -> None:
        if model is None:
            logger.error("No model found")
            raise ModuleNotFoundError("No model found")

        IAtomicRepository.__init__(
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
            **kwargs,
        )
        self.model = model
        self.model_class = model
{extra_methods}
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "{repo}"
'''


def tenant_idor_method(model: str, id_field: str = "id") -> str:
    var = model_var(model)
    return f'''
    def exists_by_id_user_and_tenant(self, entity_id: int, user_id: int, tenant_id: int) -> bool:
        """Verifies tenant-scoped record existence (IDOR guard)."""
        return self.model.exists({id_field}=entity_id, tenant_id=tenant_id)
'''


def composite_lookup(model: str) -> str:
    repo = composite_repo_name(model)
    var = model_var(model)
    return f'''""" repository implementation for {model}."""

from typing import Any, List, Optional

from rivex import Dependency

from dependencies import LoggerUtilityDependency
from models import {model}, Tenant, User
from utilities import Logger

from .abstraction import ICompositeRepository


class {repo}(ICompositeRepository):
    """ repository orchestrating multi-entity operations for {model}."""

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
        logger: Logger = Dependency(LoggerUtilityDependency),
        lookup_model: {model} = {model},
        tenant_model: Tenant = Tenant,
        user_model: User = User,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        ICompositeRepository.__init__(
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
            *args,
            **kwargs,
        )
        self.lookup_model = lookup_model
        self.tenant_model = tenant_model
        self.user_model = user_model

    def exists_by_id_user_and_tenant(
        self,
        lookup_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Verifies lookup entity existence."""
        return self.lookup_model.exists(id=lookup_id)

    def filter_by_code(self, code: str) -> List[Any]:
        """Filter lookup records by code."""
        return list(self.lookup_model.find_many(code=code))

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "{repo}"
'''


def composite_tenant(model: str, filters: list[str]) -> str:
    repo = composite_repo_name(model)
    var = model_var(model)
    filter_methods = ""
    for f in filters:
        filter_methods += f'''
    def filter_by_{f}(self, {f}: Any) -> List[Any]:
        """Filter {model} records by {f}."""
        return list(self.{var}.find_many({f}={f}))
'''
    return f'''""" repository implementation for {model}."""

from typing import Any, List, Optional

from rivex import Dependency

from dependencies import LoggerUtilityDependency
from models import {model}, Tenant, User
from utilities import Logger

from .abstraction import ICompositeRepository


class {repo}(ICompositeRepository):
    """ repository orchestrating multi-entity operations for {model}."""

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
        logger: Logger = Dependency(LoggerUtilityDependency),
        {var}: {model} = {model},
        tenant_model: Tenant = Tenant,
        user_model: User = User,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        ICompositeRepository.__init__(
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
            *args,
            **kwargs,
        )
        self.{var} = {var}
        self.tenant_model = tenant_model
        self.user_model = user_model

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Prevents IDOR by verifying tenant ownership."""
        return self.{var}.exists(id=entity_id, tenant_id=tenant_id)

    def filter_by_tenant(self, tenant_id: int) -> List[Any]:
        """Filter {model} records by tenant_id."""
        return list(self.{var}.find_many(tenant_id=tenant_id))
{filter_methods}
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "{repo}"
'''


def composite_standalone(model: str, cfg: dict) -> str:
    repo = composite_repo_name(model)
    var = model_var(model)
    extra_models = cfg.get("composite_models", [])
    model_imports = ", ".join([model] + extra_models)
    init_lines = [f"        self.{var} = {var}"]
    for m in extra_models:
        init_lines.append(f"        self.{snake(m)}_model = {snake(m)}_model")
    init_block = "\n".join(init_lines)

    params = [f"{var}: {model} = {model}"]
    for m in extra_models:
        params.append(f"{snake(m)}_model: {m} = {m}")

    filter_methods = ""
    for f in cfg.get("filters", []):
        filter_methods += f'''
    def filter_by_{f}(self, {f}: Any) -> List[Any]:
        """Filter {model} records by {f}."""
        return list(self.{var}.find_many({f}={f}))
'''

    idor = cfg.get("idor", ("id", "user_id", "tenant_id"))
    idor_expr = cfg.get("idor_expr")
    if idor_expr:
        idor_body = idor_expr
    else:
        id_field, user_field, tenant_field = idor
        if tenant_field == "tenant_id" and user_field == "user_id":
            idor_body = f"return self.{var}.exists({id_field}=entity_id, {user_field}=user_id, tenant_id=tenant_id)"
        elif user_field == "id" and tenant_field == "tenant_id":
            idor_body = f"return self.{var}.exists({id_field}=entity_id)"
        elif user_field == "user_id" and tenant_field == "user_id":
            idor_body = f"return self.{var}.exists({id_field}=entity_id, user_id=user_id)"
        else:
            idor_body = f"return self.{var}.exists({id_field}=entity_id, tenant_id=tenant_id)"

    return f'''""" repository implementation for {model}."""

from typing import Any, List, Optional

from rivex import Dependency

from dependencies import LoggerUtilityDependency
from models import {model_imports}
from utilities import Logger

from .abstraction import ICompositeRepository


class {repo}(ICompositeRepository):
    """ repository orchestrating multi-entity operations for {model}."""

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
        logger: Logger = Dependency(LoggerUtilityDependency),
        {", ".join(params)},
        *args: Any,
        **kwargs: Any,
    ) -> None:
        ICompositeRepository.__init__(
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
            *args,
            **kwargs,
        )
{init_block}

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Prevents IDOR by verifying record ownership."""
        {idor_body}

{filter_methods}
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "{repo}"
'''


def composite_nested(model: str, fk: str, parent: str, tenant_via: str) -> str:
    repo = composite_repo_name(model)
    var = model_var(model)
    parent_var = model_var(parent)
    return f'''""" repository implementation for {model}."""

from typing import Any, List, Optional

from rivex import Dependency

from dependencies import LoggerUtilityDependency
from models import {model}, {parent}, Tenant, User
from utilities import Logger

from .abstraction import ICompositeRepository


class {repo}(ICompositeRepository):
    """ repository orchestrating multi-entity operations for {model}."""

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
        logger: Logger = Dependency(LoggerUtilityDependency),
        {var}: {model} = {model},
        {parent_var}: {parent} = {parent},
        tenant_model: Tenant = Tenant,
        user_model: User = User,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        ICompositeRepository.__init__(
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
            *args,
            **kwargs,
        )
        self.{var} = {var}
        self.{parent_var} = {parent_var}
        self.tenant_model = tenant_model
        self.user_model = user_model

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Prevents IDOR by verifying parent tenant ownership."""
        record = self.{var}.find_one(id=entity_id)
        if record is None:
            return False
        parent = self.{parent_var}.find_one(id=getattr(record, "{fk}"))
        return parent is not None and getattr(parent, "{tenant_via}") == tenant_id

    def filter_by_{fk}(self, {fk}: int) -> List[Any]:
        """Filter {model} records by {fk}."""
        return list(self.{var}.find_many({fk}={fk}))

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "{repo}"
'''


def main() -> None:
    (ATOMIC / "lookup_abstraction.py").write_text(LOOKUP_ABSTRACTION)

    all_models: list[str] = []
    atomic_exports: list[str] = []
    composite_exports: list[str] = []

    for model in LOOKUP_MODELS + CORE_LOOKUP_MODELS:
        all_models.append(model)
        fname = snake(model) + ".py"
        (ATOMIC / fname).write_text(atomic_lookup(model))
        atomic_exports.append(repo_name(model))

    composite_models: list[str] = []

    for model, filters in TENANT_SCOPED.items():
        all_models.append(model)
        composite_models.append(model)
        fname = snake(model) + ".py"
        extra = tenant_idor_method(model)
        (ATOMIC / fname).write_text(atomic_standard(model, extra))
        (COMPOSITE / fname).write_text(composite_tenant(model, filters))
        atomic_exports.append(repo_name(model))
        composite_exports.append(composite_repo_name(model))

    for model, spec in NESTED_SCOPED.items():
        all_models.append(model)
        composite_models.append(model)
        fname = snake(model) + ".py"
        (ATOMIC / fname).write_text(atomic_standard(model))
        (COMPOSITE / fname).write_text(composite_nested(model, *spec))
        atomic_exports.append(repo_name(model))
        composite_exports.append(composite_repo_name(model))

    for model, cfg in STANDALONE.items():
        all_models.append(model)
        composite_models.append(model)
        fname = snake(model) + ".py"
        extra = ""
        if model == "Company":
            extra = tenant_idor_method("Company")
        (ATOMIC / fname).write_text(atomic_standard(model, extra))
        (COMPOSITE / fname).write_text(composite_standalone(model, cfg))
        atomic_exports.append(repo_name(model))
        composite_exports.append(composite_repo_name(model))

    atomic_init = '"""SignFlow atomic repositories."""\n\n'
    for model in sorted(set(all_models), key=lambda m: snake(m)):
        mod = snake(model)
        atomic_init += f"from .{mod} import {repo_name(model)}\n"
    atomic_init += "\n__all__ = [\n"
    for name in sorted(atomic_exports):
        atomic_init += f'    "{name}",\n'
    atomic_init += "]\n"
    (ATOMIC / "__init__.py").write_text(atomic_init)

    composite_init = '"""SignFlow composite repositories."""\n\n'
    for model in sorted(set(composite_models), key=lambda m: snake(m)):
        mod = snake(model)
        composite_init += f"from .{mod} import {composite_repo_name(model)}\n"
    composite_init += "\n__all__ = [\n"
    for name in sorted(composite_exports):
        composite_init += f'    "{name}",\n'
    composite_init += "]\n"
    (COMPOSITE / "__init__.py").write_text(composite_init)

    repo_init = '"""Repositories package top-level exports."""\n\n'
    repo_init += "from repositories.atomic import (\n"
    for name in sorted(atomic_exports):
        repo_init += f"    {name},\n"
    repo_init += ")\n\n"
    repo_init += "from repositories.composite import (\n"
    for name in sorted(composite_exports):
        repo_init += f"    {name},\n"
    repo_init += ")\n\n"
    repo_init += "__all__ = [\n"
    for name in sorted(composite_exports):
        repo_init += f'    "{name}",\n'
    for name in sorted(atomic_exports):
        repo_init += f'    "{name}",\n'
    repo_init += "]\n"
    (ROOT / "repositories" / "__init__.py").write_text(repo_init)

    repo_constants = '''"""RepositoryName — PascalCase class-name constants for the repository layer."""

from typing import Final

from .abstraction import ILayerConstant


class Repository(ILayerConstant):
'''
    dep_constants = '''"""Repository dependency layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class RepositoryDependency(ILayerConstant):
'''
    for model in sorted(set(all_models), key=lambda m: snake(m)):
        key = const_key(model)
        repo_constants += f'\n    {key}: Final[str] = "{repo_name(model)}"'
        dep_constants += f'\n    {key}: Final[str] = "{repo_name(model)}Dependency"'
        if model not in LOOKUP_MODELS and model not in CORE_LOOKUP_MODELS:
            dep_constants += f'\n    COMPOSITE_{key}: Final[str] = "{composite_repo_name(model)}Dependency"'

    repo_constants += '''

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Repository"
'''
    dep_constants += '''

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RepositoryDependency"
'''
    (ROOT / "constants" / "layer" / "repository.py").write_text(repo_constants)
    (ROOT / "constants" / "layer" / "dependency" / "repository.py").write_text(dep_constants)

    print(f"Generated {len(all_models)} atomic + {len(all_models)} composite repositories")


if __name__ == "__main__":
    main()
