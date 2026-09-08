from exceptions import BadInputException
"""Update notification repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateNotificationServiceDTO
from dependencies import NotificationRepositoryDependency
from repositories import NotificationRepository
from models import Notification
from .abstraction import INotificationRepositoryService


class UpdateNotificationService(INotificationRepositoryService):
    """Application service for update operation on notification repository."""

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
        notification_repository: NotificationRepository = Dependency(NotificationRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        super().__init__(
            urn=urn,
            user_urn=user_urn,
            user_id=user_id,
            tenant_urn=tenant_urn,
            tenant_id=tenant_id,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            *args,
            **kwargs,
        )
        self.notification_repository = notification_repository

    async def run(self, request: UpdateNotificationServiceDTO) -> DTOLayer:
        """Executes update business logic for notification."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            notification: Notification = Notification.build(
            title=request.title,
            body=request.body,
            at=request.at,
            is_read=request.is_read,
            link=request.link,
            kind_id=request.kind_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.notification_repository.update(model=notification)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_NOTIFICATION_SERVICE
