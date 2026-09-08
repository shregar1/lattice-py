"""Base abstraction for utility-validation DTOs.

Concrete DTOs in ``dtos/utilities/validation/`` extend ``IValidationUtilityDTO``, which
in turn extends ``IUtilityDTO``. The base carries no validation-specific fields
— subclasses declare their own state and provide a ``build`` factory plus a
``name`` property.
"""


from abc import abstractmethod
from typing import Any, Self

from .abstraction import IValidationUtilityDTO


class IValidationUtilityDTO(IValidationUtilityDTO):
    """
    Marker base for validation-rule DTOs.

    Concrete subclasses (``RequestValidationContext``, ``ResponseValidationContext``,
    ``RuleValidationResult``) extend this class and supply their own fields via
    Pydantic ``Field`` annotations.
    """

    @classmethod
    def build(cls, *args: Any, **kwargs: Any) -> Self:
        """Constructs a fully-validated instance from the given inputs."""
        return cls(*args, **kwargs)

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass


__all__ = ["IValidationUtilityDTO"]
