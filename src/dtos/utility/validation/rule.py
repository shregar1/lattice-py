"""Rule-validation result DTO."""


from typing import Optional, Self

from .abstraction import IValidationUtilityDTO


class RuleValidationResult(IValidationUtilityDTO):
    """Outcome of a single validation rule."""

    passed: bool
    rule_id: str
    error_message: Optional[str] = None
    error_code: Optional[str] = None

    @classmethod
    def build(
        cls,
        passed: bool,
        rule_id: str,
        error_message: Optional[str] = None,
        error_code: Optional[str] = None,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            passed=passed,
            rule_id=rule_id,
            error_message=error_message,
            error_code=error_code,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RuleValidationResult"
