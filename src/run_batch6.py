import os, glob

def create_dto_package(domain_name, model_dto_class_name, fields_def, build_args, build_kwargs, list_param_name):
    pkg_dir = os.path.join('dtos/service/repository', domain_name)
    input_dir = os.path.join(pkg_dir, 'input')
    input_filter_dir = os.path.join(input_dir, 'filter')
    output_dir = os.path.join(pkg_dir, 'output')
    output_filter_dir = os.path.join(output_dir, 'filter')

    os.makedirs(input_filter_dir, exist_ok=True)
    os.makedirs(output_filter_dir, exist_ok=True)

    class_prefix = ''.join(x.title() for x in domain_name.split('_'))
    dto_marker_base = f'I{class_prefix}RepositoryServiceDTO'

    # Clean old root files
    for f_name in glob.glob(os.path.join(pkg_dir, '*.py')):
        if not f_name.endswith('__init__.py') and not f_name.endswith('abstraction.py'):
            os.remove(f_name)

    # 1. Root abstraction
    with open(os.path.join(pkg_dir, 'abstraction.py'), 'w') as f:
        f.write(f'''"""{class_prefix} repository service DTO abstractions."""

from dtos.abstraction import IDTO


class {dto_marker_base}(IDTO):
    """Marker base for {domain_name} repository service DTOs."""
    pass


__all__ = [
    "{dto_marker_base}",
]
''')

    # 2. Input abstraction
    with open(os.path.join(input_dir, 'abstraction.py'), 'w') as f:
        f.write(f'''"""Input {domain_name} repository service DTO abstractions."""

from ..abstraction import {dto_marker_base}

__all__ = [
    "{dto_marker_base}",
]
''')

    # 3. Input create.py
    with open(os.path.join(input_dir, 'create.py'), 'w') as f:
        f.write(f'''"""Create {domain_name} service DTO."""

from datetime import datetime
from decimal import Decimal
from pydantic import Field
from typing import Optional, Self

from .abstraction import {dto_marker_base}


class Create{class_prefix}InputDTO({dto_marker_base}):
    """DTO carrying parameters for creating a {domain_name} record."""

    urn: Optional[str] = Field(default=None, description="Optional record URN")
    user_id: Optional[int] = Field(default=None, description="User ID executing operation")
    tenant_id: Optional[int] = Field(default=None, description="Tenant ID executing operation")
{fields_def['create_input']}

    is_deleted: Optional[bool] = Field(default=None, description="Optional is_deleted status")
    is_active: Optional[bool] = Field(default=None, description="Optional is_active status")
    created_at: Optional[datetime] = Field(default=None, description="Optional created_at timestamp")
    created_by: Optional[int] = Field(default=None, description="Optional created_by user ID")

    @classmethod
    def build(
        cls,
{build_args['create_input']}
    ) -> Self:
        """Builds a new Create{class_prefix}InputDTO instance."""
        return cls(
{build_kwargs['create_input']}
        )

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "Create{class_prefix}InputDTO"
''')

    # 4. Input update.py
    with open(os.path.join(input_dir, 'update.py'), 'w') as f:
        f.write(f'''"""Update {domain_name} service DTO."""

from datetime import datetime
from decimal import Decimal
from pydantic import Field
from typing import Optional, Self

from .abstraction import {dto_marker_base}


class Update{class_prefix}InputDTO({dto_marker_base}):
    """DTO carrying parameters for updating a {domain_name} record."""

    id: Optional[int] = Field(default=None, description="Optional record ID")
    urn: Optional[str] = Field(default=None, description="Optional record URN")
    user_id: Optional[int] = Field(default=None, description="User ID executing operation")
    tenant_id: Optional[int] = Field(default=None, description="Tenant ID executing operation")
{fields_def['update_input']}

    is_deleted: Optional[bool] = Field(default=None, description="Optional updated is_deleted status")
    is_active: Optional[bool] = Field(default=None, description="Optional updated is_active status")
    updated_at: Optional[datetime] = Field(default=None, description="Optional updated_at timestamp")
    updated_by: Optional[int] = Field(default=None, description="Optional updated_by user ID")

    @classmethod
    def build(
        cls,
{build_args['update_input']}
    ) -> Self:
        """Builds a new Update{class_prefix}InputDTO instance."""
        return cls(
{build_kwargs['update_input']}
        )

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "Update{class_prefix}InputDTO"
''')

    # 5. Input delete.py
    with open(os.path.join(input_dir, 'delete.py'), 'w') as f:
        f.write(f'''"""Delete {domain_name} service DTO."""

from datetime import datetime
from pydantic import Field
from typing import Optional, Self

from .abstraction import {dto_marker_base}


class Delete{class_prefix}InputDTO({dto_marker_base}):
    """DTO carrying parameters for deleting a {domain_name} record."""

    id: Optional[int] = Field(default=None, description="Optional record ID")
    urn: Optional[str] = Field(default=None, description="Optional record URN")
    user_id: Optional[int] = Field(default=None, description="User ID executing operation")
    tenant_id: Optional[int] = Field(default=None, description="Tenant ID executing operation")
    is_hard_delete: bool = Field(default=False, description="Whether to perform hard deletion")

    @classmethod
    def build(
        cls,
        id: Optional[int] = None,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        tenant_id: Optional[int] = None,
        is_hard_delete: bool = False,
    ) -> Self:
        """Builds a new Delete{class_prefix}InputDTO instance."""
        return cls(
            id=id,
            urn=urn,
            user_id=user_id,
            tenant_id=tenant_id,
            is_hard_delete=is_hard_delete,
        )

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "Delete{class_prefix}InputDTO"
''')

    # 6. Input filter/abstraction.py
    with open(os.path.join(input_filter_dir, 'abstraction.py'), 'w') as f:
        f.write(f'''"""Abstraction module for filter {domain_name} input DTOs."""

from ...abstraction import {dto_marker_base}


class IFilter{class_prefix}InputDTO({dto_marker_base}):
    """Base abstraction for filter {domain_name} input DTOs."""
    pass
''')

    # 7. Input filter/by_all.py
    with open(os.path.join(input_filter_dir, 'by_all.py'), 'w') as f:
        f.write(f'''"""Filter {domain_name} service DTO."""

from decimal import Decimal
from pydantic import Field
from typing import Optional, Self

from .abstraction import IFilter{class_prefix}InputDTO


class Filter{class_prefix}InputDTO(IFilter{class_prefix}InputDTO):
    """DTO carrying optional parameters for filtering {domain_name} records."""

    id: Optional[int] = Field(default=None, description="Optional id filter parameter")
    urn: Optional[str] = Field(default=None, description="Optional urn filter parameter")
    user_id: Optional[int] = Field(default=None, description="User ID executing operation")
    tenant_id: Optional[int] = Field(default=None, description="Tenant ID executing operation")
{fields_def['filter_input']}

    @classmethod
    def build(
        cls,
{build_args['filter_input']}
    ) -> Self:
        """Builds a new Filter{class_prefix}InputDTO instance."""
        return cls(
{build_kwargs['filter_input']}
        )

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "Filter{class_prefix}InputDTO"
''')

    # 8. Input filter/__init__.py
    with open(os.path.join(input_filter_dir, '__init__.py'), 'w') as f:
        f.write(f'''"""Filter input DTOs for {domain_name} service."""

from .abstraction import IFilter{class_prefix}InputDTO
from .by_all import Filter{class_prefix}InputDTO

__all__ = [
    "Filter{class_prefix}InputDTO",
    "IFilter{class_prefix}InputDTO",
]
''')

    # 9. Input __init__.py
    with open(os.path.join(input_dir, '__init__.py'), 'w') as f:
        f.write(f'''"""Input DTOs for {domain_name} service."""

from .abstraction import {dto_marker_base}
from .create import Create{class_prefix}InputDTO
from .delete import Delete{class_prefix}InputDTO
from .filter import (
    Filter{class_prefix}InputDTO,
    IFilter{class_prefix}InputDTO,
)
from .update import Update{class_prefix}InputDTO

__all__ = [
    "Create{class_prefix}InputDTO",
    "Delete{class_prefix}InputDTO",
    "Filter{class_prefix}InputDTO",
    "{dto_marker_base}",
    "IFilter{class_prefix}InputDTO",
    "Update{class_prefix}InputDTO",
]
''')

    # 10. Output abstraction.py
    with open(os.path.join(output_dir, 'abstraction.py'), 'w') as f:
        f.write(f'''"""Output {domain_name} repository service DTO abstractions."""

from datetime import datetime
from decimal import Decimal
from pydantic import Field
from typing import Optional, Self

from dtos.abstraction import IDTO
from ..abstraction import {dto_marker_base}


class {model_dto_class_name}(IDTO):
    """{model_dto_class_name} entity DTO using URNs and lookup codes instead of raw internal IDs."""

    urn: Optional[str] = Field(default=None, description="{domain_name} URN")
{fields_def['entity_output']}

    @classmethod
    def build(
        cls,
{build_args['entity_output']}
    ) -> Self:
        """Builds a new {model_dto_class_name} instance."""
        return cls(
{build_kwargs['entity_output']}
        )

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "{model_dto_class_name}"


__all__ = [
    "{model_dto_class_name}",
    "{dto_marker_base}",
]
''')

    # 11. Output create.py
    with open(os.path.join(output_dir, 'create.py'), 'w') as f:
        f.write(f'''"""Create {domain_name} output DTO."""

from datetime import datetime
from decimal import Decimal
from pydantic import Field
from typing import Optional, Self

from .abstraction import {model_dto_class_name}, {dto_marker_base}


class Create{class_prefix}OutputDTO({model_dto_class_name}, {dto_marker_base}):
    """Output DTO for create {domain_name} service."""

    created_at: Optional[datetime] = Field(default=None, description="Timestamp when record was created")

    @classmethod
    def build(
        cls,
{build_args['create_output']}
    ) -> Self:
        """Builds a new Create{class_prefix}OutputDTO instance."""
        return cls(
{build_kwargs['create_output']}
        )

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "Create{class_prefix}OutputDTO"
''')

    # 12. Output update.py
    with open(os.path.join(output_dir, 'update.py'), 'w') as f:
        f.write(f'''"""Update {domain_name} output DTO."""

from datetime import datetime
from decimal import Decimal
from pydantic import Field
from typing import Optional, Self

from .abstraction import {model_dto_class_name}, {dto_marker_base}


class Update{class_prefix}OutputDTO({model_dto_class_name}, {dto_marker_base}):
    """Output DTO for update {domain_name} service."""

    updated_at: Optional[datetime] = Field(default=None, description="Timestamp when record was updated")

    @classmethod
    def build(
        cls,
{build_args['update_output']}
    ) -> Self:
        """Builds a new Update{class_prefix}OutputDTO instance."""
        return cls(
{build_kwargs['update_output']}
        )

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "Update{class_prefix}OutputDTO"
''')

    # 13. Output delete.py
    with open(os.path.join(output_dir, 'delete.py'), 'w') as f:
        f.write(f'''"""Delete {domain_name} output DTO."""

from datetime import datetime
from pydantic import Field
from typing import Optional, Self

from .abstraction import {dto_marker_base}


class Delete{class_prefix}OutputDTO({dto_marker_base}):
    """Output DTO for delete {domain_name} service."""

    urn: Optional[str] = Field(default=None, description="{domain_name} URN")
    deleted_at: Optional[datetime] = Field(default=None, description="Timestamp when record was deleted")
    success: bool = Field(default=True, description="Indicates if deletion was successful")

    @classmethod
    def build(
        cls,
        urn: Optional[str] = None,
        deleted_at: Optional[datetime] = None,
        success: bool = True,
    ) -> Self:
        """Builds a new Delete{class_prefix}OutputDTO instance."""
        return cls(
            urn=urn,
            deleted_at=deleted_at,
            success=success,
        )

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "Delete{class_prefix}OutputDTO"
''')

    # 14. Output filter/abstraction.py
    with open(os.path.join(output_filter_dir, 'abstraction.py'), 'w') as f:
        f.write(f'''"""Abstraction module for filter {domain_name} output DTOs."""

from pydantic import Field
from typing import List

from ...abstraction import (
    {model_dto_class_name},
    {dto_marker_base},
)


class IFilter{class_prefix}OutputDTO({dto_marker_base}):
    """Base abstraction for filter {domain_name} output DTOs carrying a list of {model_dto_class_name} records."""

    {list_param_name}: List[{model_dto_class_name}] = Field(default_factory=list, description="Filtered {domain_name} records")
''')

    # 15. Output filter/by_all.py
    with open(os.path.join(output_filter_dir, 'by_all.py'), 'w') as f:
        f.write(f'''"""Filter {domain_name} service response DTO."""

from pydantic import Field
from typing import List, Self

from .abstraction import {model_dto_class_name}, IFilter{class_prefix}OutputDTO


class Filter{class_prefix}OutputDTO(IFilter{class_prefix}OutputDTO):
    """DTO carrying the response data for filter operation on {domain_name} repository."""

    @classmethod
    def build(cls, {list_param_name}: List[{model_dto_class_name}]) -> Self:
        """Builds a new Filter{class_prefix}OutputDTO instance."""
        return cls({list_param_name}={list_param_name})

    @property
    def name(self) -> str:
        """Returns the DTO name."""
        return "Filter{class_prefix}OutputDTO"
''')

    # 16. Output filter/__init__.py
    with open(os.path.join(output_filter_dir, '__init__.py'), 'w') as f:
        f.write(f'''"""Filter output DTOs for {domain_name} service."""

from .abstraction import (
    {model_dto_class_name},
    {dto_marker_base},
    IFilter{class_prefix}OutputDTO,
)
from .by_all import Filter{class_prefix}OutputDTO

__all__ = [
    "{model_dto_class_name}",
    "Filter{class_prefix}OutputDTO",
    "{dto_marker_base}",
    "IFilter{class_prefix}OutputDTO",
]
''')

    # 17. Output __init__.py
    with open(os.path.join(output_dir, '__init__.py'), 'w') as f:
        f.write(f'''"""Output DTOs for {domain_name} service."""

from .abstraction import (
    {model_dto_class_name},
    {dto_marker_base},
)
from .create import Create{class_prefix}OutputDTO
from .delete import Delete{class_prefix}OutputDTO
from .filter import (
    Filter{class_prefix}OutputDTO,
    IFilter{class_prefix}OutputDTO,
)
from .update import Update{class_prefix}OutputDTO

__all__ = [
    "{model_dto_class_name}",
    "Create{class_prefix}OutputDTO",
    "Delete{class_prefix}OutputDTO",
    "Filter{class_prefix}OutputDTO",
    "{dto_marker_base}",
    "IFilter{class_prefix}OutputDTO",
    "Update{class_prefix}OutputDTO",
]
''')

    # 18. Root __init__.py
    with open(os.path.join(pkg_dir, '__init__.py'), 'w') as f:
        f.write(f'''"""{class_prefix} repository service DTOs package."""

from .abstraction import {dto_marker_base}
from .input import (
    Create{class_prefix}InputDTO,
    Delete{class_prefix}InputDTO,
    Filter{class_prefix}InputDTO,
    IFilter{class_prefix}InputDTO,
    Update{class_prefix}InputDTO,
)
from .output import (
    {model_dto_class_name},
    Create{class_prefix}OutputDTO,
    Delete{class_prefix}OutputDTO,
    Filter{class_prefix}OutputDTO,
    IFilter{class_prefix}OutputDTO,
    Update{class_prefix}OutputDTO,
)

__all__ = [
    "{model_dto_class_name}",
    "Create{class_prefix}InputDTO",
    "Create{class_prefix}OutputDTO",
    "Delete{class_prefix}InputDTO",
    "Delete{class_prefix}OutputDTO",
    "Filter{class_prefix}InputDTO",
    "Filter{class_prefix}OutputDTO",
    "{dto_marker_base}",
    "IFilter{class_prefix}InputDTO",
    "IFilter{class_prefix}OutputDTO",
    "Update{class_prefix}InputDTO",
    "Update{class_prefix}OutputDTO",
]
''')

    print(f'Successfully generated DTO package for {domain_name}!')

def gen_lookup_entity(domain, model_dto, list_name):
    c_fields = '''    code: str = Field(..., description="code parameter")
    label: str = Field(..., description="label parameter")
    description: str = Field(..., description="description parameter")'''
    u_fields = '''    code: Optional[str] = Field(default=None, description="Optional code parameter")
    label: Optional[str] = Field(default=None, description="Optional label parameter")
    description: Optional[str] = Field(default=None, description="Optional description parameter")'''
    f_fields = '''    code: Optional[str] = Field(default=None, description="Optional code parameter")
    label: Optional[str] = Field(default=None, description="Optional label parameter")'''
    e_fields = '''    code: str = Field(..., description="code parameter")
    label: str = Field(..., description="label parameter")
    description: str = Field(..., description="description parameter")'''

    b_args = {
        'create_input': '''        code: str,
        label: str,
        description: str,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        tenant_id: Optional[int] = None,
        is_deleted: Optional[bool] = None,
        is_active: Optional[bool] = None,
        created_at: Optional[datetime] = None,
        created_by: Optional[int] = None,''',
        'create_input_kw': '''            urn=urn,
            user_id=user_id,
            tenant_id=tenant_id,
            code=code,
            label=label,
            description=description,
            is_deleted=is_deleted,
            is_active=is_active,
            created_at=created_at,
            created_by=created_by,''',
        'update_input': '''        id: Optional[int] = None,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        tenant_id: Optional[int] = None,
        code: Optional[str] = None,
        label: Optional[str] = None,
        description: Optional[str] = None,
        is_deleted: Optional[bool] = None,
        is_active: Optional[bool] = None,
        updated_at: Optional[datetime] = None,
        updated_by: Optional[int] = None,''',
        'update_input_kw': '''            id=id,
            urn=urn,
            user_id=user_id,
            tenant_id=tenant_id,
            code=code,
            label=label,
            description=description,
            is_deleted=is_deleted,
            is_active=is_active,
            updated_at=updated_at,
            updated_by=updated_by,''',
        'filter_input': '''        id: Optional[int] = None,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        tenant_id: Optional[int] = None,
        code: Optional[str] = None,
        label: Optional[str] = None,''',
        'filter_input_kw': '''            id=id,
            urn=urn,
            user_id=user_id,
            tenant_id=tenant_id,
            code=code,
            label=label,''',
        'entity_output': '''        code: str,
        label: str,
        description: str,
        urn: Optional[str] = None,''',
        'entity_output_kw': '''            urn=urn,
            code=code,
            label=label,
            description=description,''',
        'create_output': '''        code: str,
        label: str,
        description: str,
        urn: Optional[str] = None,
        created_at: Optional[datetime] = None,''',
        'create_output_kw': '''            urn=urn,
            code=code,
            label=label,
            description=description,
            created_at=created_at,''',
        'update_output': '''        code: str,
        label: str,
        description: str,
        urn: Optional[str] = None,
        updated_at: Optional[datetime] = None,''',
        'update_output_kw': '''            urn=urn,
            code=code,
            label=label,
            description=description,
            updated_at=updated_at,''',
    }

    create_dto_package(
        domain,
        model_dto,
        {
            'create_input': c_fields,
            'update_input': u_fields,
            'filter_input': f_fields,
            'entity_output': e_fields,
        },
        b_args,
        {
            'create_input': b_args['create_input_kw'],
            'update_input': b_args['update_input_kw'],
            'filter_input': b_args['filter_input_kw'],
            'entity_output': b_args['entity_output_kw'],
            'create_output': b_args['create_output_kw'],
            'update_output': b_args['update_output_kw'],
        },
        list_name,
    )

# 1. country_lk and currency_lk
gen_lookup_entity('country_lk', 'CountryLKDTO', 'countries')
gen_lookup_entity('currency_lk', 'CurrencyLKDTO', 'currencies')

# 2. company
c_comp_fields = '''    name: str = Field(..., description="name parameter")
    domain: Optional[str] = Field(default=None, description="domain parameter")