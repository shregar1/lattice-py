""" repository abstraction layer.

``ICompositeRepository`` is a mixin providing multi-entity join helpers.
Concrete composites inherit from their atomic repository **and** this mixin::

    class EnvelopeRepository(AtomicEnvelopeRepository, ICompositeRepository):
        ...
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple, TypeVar

TModel = TypeVar("TModel")


class ICompositeRepository(ABC):
    """Mixin for composite repositories that extend an atomic repository."""

    def _apply_conditions(
        self,
        query: Any,
        models: List[Any],
        conditions: Dict[str, Any],
    ) -> Any:
        """Applies filter conditions across a list of models to a query object."""
        where_clauses = []
        for col_spec, value in conditions.items():
            if isinstance(col_spec, tuple) and len(col_spec) == 2:
                model_cls, col_name = col_spec
                where_clauses.append(getattr(model_cls, col_name) == value)
            else:
                for m in models:
                    if hasattr(m, str(col_spec)):
                        where_clauses.append(getattr(m, str(col_spec)) == value)
                        break

        if where_clauses:
            combined = where_clauses[0]
            for clause in where_clauses[1:]:
                combined = combined & clause
            query = query.where(combined)

        return query

    def join(
        self,
        primary_model: Any,
        target_model: Any,
        join_left_col: str,
        join_right_col: str,
    ) -> Any:
        """JOIN primary_model to target_model and return the query object."""
        left_col = getattr(primary_model, join_left_col)
        right_col = getattr(target_model, join_right_col)
        return primary_model.find_many().join(target_model, left_col == right_col)

    def multi_join(
        self,
        primary_model: Any,
        joins: List[Tuple[Any, str, str]],
    ) -> Any:
        """Multi-table JOIN across N models; returns the query object."""
        query = primary_model.find_many()
        active_models = [primary_model]

        for target_model, left_col_name, right_col_name in joins:
            left_col = None
            for m in active_models:
                if hasattr(m, left_col_name):
                    left_col = getattr(m, left_col_name)
                    break

            if left_col is None:
                raise AttributeError(
                    f"Join left column '{left_col_name}' not found on any preceding model."
                )

            right_col = getattr(target_model, right_col_name)
            query = query.join(target_model, left_col == right_col)
            active_models.append(target_model)

        return query

    def filter_by_join(
        self,
        primary_model: type[TModel],
        target_model: Any,
        join_left_col: str,
        join_right_col: str,
        conditions: Optional[Dict[str, Any]] = None,
    ) -> List[TModel]:
        """JOIN query with conditions; returns matching records."""
        query = self.join(
            primary_model=primary_model,
            target_model=target_model,
            join_left_col=join_left_col,
            join_right_col=join_right_col,
        )
        if conditions:
            query = self._apply_conditions(query, [primary_model, target_model], conditions)

        return list(query.all())

    def filter_by_multi_join(
        self,
        primary_model: type[TModel],
        joins: List[Tuple[Any, str, str]],
        conditions: Optional[Dict[str, Any]] = None,
    ) -> List[TModel]:
        """Multi-table JOIN with conditions; returns matching records."""
        query = self.multi_join(primary_model=primary_model, joins=joins)
        if conditions:
            active_models = [primary_model] + [target for target, _, _ in joins]
            query = self._apply_conditions(query, active_models, conditions)

        return list(query.all())

    def exists_by_join(
        self,
        primary_model: Any,
        target_model: Any,
        join_left_col: str,
        join_right_col: str,
        conditions: Optional[Dict[str, Any]] = None,
    ) -> bool:
        """True when at least one JOIN row matches the conditions."""
        matches = self.filter_by_join(
            primary_model=primary_model,
            target_model=target_model,
            join_left_col=join_left_col,
            join_right_col=join_right_col,
            conditions=conditions,
        )
        return len(matches) > 0

    def exists_by_multi_join(
        self,
        primary_model: Any,
        joins: List[Tuple[Any, str, str]],
        conditions: Optional[Dict[str, Any]] = None,
    ) -> bool:
        """True when at least one multi-JOIN row matches the conditions."""
        matches = self.filter_by_multi_join(
            primary_model=primary_model,
            joins=joins,
            conditions=conditions,
        )
        return len(matches) > 0

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name that every composite repository must define."""
        pass
