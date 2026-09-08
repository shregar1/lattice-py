"""MongoDB utility — connection management and document-store helpers."""

from motor.motor_asyncio import AsyncIOMotorClient

from rivex import Dependency
from typing import Any, Optional

from configurations.database.mongo import MongoConfiguration, MongoConfigurationDTO
from constants import Utility
from dependencies import MongoConfigurationDependency
from dependencies import LoggerUtilityDependency
from .abstraction import IDatabaseUtility
from utilities import Logger


class MongoDatabaseUtility(IDatabaseUtility):
    """Thin wrapper around a motor / pymongo client with safe lifecycle helpers."""

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
        mongo_configuration: MongoConfiguration = Dependency(MongoConfigurationDependency),
        logger: Logger = Dependency(LoggerUtilityDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        IDatabaseUtility.__init__(
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

        self.mongo_configuration: MongoConfigurationDTO = mongo_configuration.get_instance()
        self._client = None

    async def connect(self) -> Any:
        """Open a MongoDB client and return it (motor.AsyncIOMotorClient)."""
        try:
            self._client = AsyncIOMotorClient(self.mongo_configuration.connection_uri)
            return self._client
        except ImportError:
            if self.logger is not None:
                self.logger.warning(
                    "motor is not installed; MongoDatabaseUtility will operate in disconnected mode"
                )
            self._client = None
            return None

    async def disconnect(self) -> None:
        """Close the underlying MongoDB client."""
        if self._client is not None and hasattr(self._client, "close"):
            self._client.close()
        self._client = None

    def get_collection(self, name: str) -> Any:
        """Return a collection handle from the active client."""
        if self._client is None:
            return None
        return self._client[self.mongo_configuration.database][name]
    @property
    def client(self) -> Any:
        return self._client
    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.MONGO_DATABASE
