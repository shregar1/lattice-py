"""Repository abstraction layer.

Concrete repositories inherit from ``IAtomicRepository`` and only set
``model_class``; the 18 base methods (filter, find_by_id, create, ...) are
implemented here against the ormx model API.
"""

import time

from abc import ABC, abstractmethod
from dataclasses import dataclass
from rivex import Dependency
from typing import Any, Optional, List, Sequence

from abstractions import RepositoryLayer
from models import IModel
from dependencies import LoggerUtilityDependency
from utilities import Logger


@dataclass(frozen=True)
class PaginationParams:
    offset: int = 0
    limit: int = 50


class IAtomicRepository(RepositoryLayer, ABC):
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
        *args: Any,
        **kwargs: Any,
    ) -> None:

        RepositoryLayer.__init__(
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

    def list_all(self) -> List[IModel]:
        start_time = time.time()

        try:

            result = list(self.model.find_many())
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for list_all",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for list_all",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter(self, column: str, value: Any) -> List[IModel]:
        start_time = time.time()

        try:

            result = list(self.model.find_many(**{column: value}))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"column": column, "value": value},
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"column": column, "value": value},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_in(self, column: str, values: Sequence[Any]) -> List[IModel]:

        if not values:
            return []
        start_time = time.time()

        try:

            col = getattr(self.model_class, column)
            result = list(self.model_class.find_many().where(col.in_(list(values))).all())
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_in",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"column": column, "values": values},
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_in",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"column": column, "values": values},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def find_by_id(self, id: int) -> Optional[IModel]:
        start_time = time.time()

        try:

            result = self.model_class.find_one(id=id)
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for find_by_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"id": id},
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for find_by_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"id": id},
                error=str(exc),
                exc=exc,
            )

            return None

    def find_by_urn(self, urn: str) -> Optional[IModel]:
        start_time = time.time()

        try:

            result = self.model_class.find_one(urn=urn)
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for find_by_urn",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"urn": urn},
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for find_by_urn",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"urn": urn},
                error=str(exc),
                exc=exc,
            )

            return None

    def get_by_id(self, id: int) -> IModel:
        start_time = time.time()

        try:

            result = self.find_by_id(id)
            if result is None:
                raise LookupError(f"{self.model_class.__name__} with id={id} not found")
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for get_by_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"id": id},
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for get_by_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"id": id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def exists(self, **kwargs: Any) -> bool:
        start_time = time.time()

        try:

            result = bool(self.model.find_many(**kwargs))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for exists",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details=kwargs,
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for exists",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details=kwargs,
                error=str(exc),
                exc=exc,
            )

            return False

    def exists_by_id(self, id: int) -> bool:
        return self.exists(id=id)

    def exists_by_urn(self, urn: str) -> bool:
        return self.exists(urn=urn)

    def count(self) -> int:
        start_time = time.time()

        try:

            result = int(self.model_class.count())
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for count",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for count",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                error=str(exc),
                exc=exc,
            )
            raise exc

    def count_filtered(self, column: str, value: Any) -> int:
        start_time = time.time()

        try:

            result = int(self.model_class.count(**{column: value}))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for count_filtered",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"column": column, "value": value},
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for count_filtered",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"column": column, "value": value},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def list_paginated(self, params: PaginationParams) -> List[IModel]:
        start_time = time.time()

        try:

            result = list(
                self.model_class.find_many().limit(params.limit).offset(params.offset).all()
            )
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for list_paginated",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"offset": params.offset, "limit": params.limit},
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for list_paginated",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"offset": params.offset, "limit": params.limit},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def create(self, model: IModel) -> IModel:
        start_time = time.time()

        try:

            result = self.model_class.create(**model.model_dump())
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for create",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for create",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                error=str(exc),
                exc=exc,
            )
            raise exc

    def update(self, model: IModel) -> IModel:
        start_time = time.time()

        try:

            result = self.model_class.update(model)
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for update",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for update",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                error=str(exc),
                exc=exc,
            )
            raise exc

    def soft_delete(self, id: int) -> None:
        start_time = time.time()

        try:

            instance = self.get_by_id(id)
            instance.is_deleted = True
            self.update(instance)
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for soft_delete",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"id": id},
            )

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for soft_delete",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"id": id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def hard_delete(self, id: int) -> None:
        start_time = time.time()

        try:

            self.model_class.delete(id=id)
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for hard_delete",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"id": id},
            )

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for hard_delete",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"id": id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def bulk_create(self, models: Sequence[IModel]) -> List[IModel]:
        start_time = time.time()

        try:

            result = self.model_class.create_many([m.model_dump() for m in models])
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for bulk_create",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"count": len(models)},
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for bulk_create",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"count": len(models)},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def bulk_soft_delete(self, ids: Sequence[int]) -> None:
        start_time = time.time()

        try:

            for id_value in ids:
                self.soft_delete(id_value)
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for bulk_soft_delete",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"ids": ids},
            )

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for bulk_soft_delete",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"ids": ids},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def upsert(self, model: IModel) -> IModel:
        start_time = time.time()

        try:

            existing = self.find_by_id(model.id) if getattr(model, "id", None) else None
            if existing is not None:
                result = self.update(model)
            else:
                result = self.create(model)
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for upsert",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
            )

            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for upsert",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                error=str(exc),
                exc=exc,
            )
            raise exc

    @abstractmethod
    @property
    def name(self) -> str:
        pass
