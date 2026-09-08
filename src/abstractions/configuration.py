import json
import threading

from abc import ABC, abstractmethod
from typing import Any, ClassVar, Dict, Optional, Self

from .abstraction import ILayer


class ConfigurationLayer(ILayer, ABC):
    """
    Root configuration interface.

    Concrete singletons live in ``configurations/``. Every subclass is held
    in a class-level ``_instances`` cache so repeated access returns the same
    object. ``load()`` is responsible for constructing, hydrating, and validating
    the singleton on first access; ``get_instance()`` is the public entry point.

    Attributes:
        _instances: Cache of constructed configuration singletons keyed by subclass.
        _lock: Lock guarding concurrent first-access construction.
    """

    _instances: ClassVar[Dict[type, Any]] = {}
    _lock: ClassVar[threading.Lock] = threading.Lock()

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
        logger: Optional[Any] = None,
        config_path: Optional[str] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Stores the request-scoped context fields and the configuration path."""

        self.urn = urn
        self.tenant_id = tenant_id
        self.tenant_urn = tenant_urn
        self.user_id = user_id
        self.user_urn = user_urn
        self.api_name = api_name
        self.ip_address = ip_address
        self.user_agent = user_agent
        self.logger = logger
        self.CONFIG_PATH = config_path
        self.config = self.load()

    def load(self) -> Self:
        """
        Construct, hydrate and return the singleton instance for ``cls``.

        The default implementation constructs an empty instance with default
        arguments and delegates validation to :meth:`validate`. Subclasses may
        override to perform environment/file loading before validation.
        """
        with open(self.CONFIG_PATH, "r", encoding="utf-8") as file:
            config = json.loads(file)
        self.validate(config)
        return config

    @abstractmethod
    def validate(self, config: Dict[str, Any]) -> None:
        """Fail-fast validation before the server accepts traffic."""
        pass

    @classmethod
    def get_instance(cls) -> Self:
        """

        return the singleton instance, constructing it on first access.

        Concurrent first-access is serialised by ``_lock`` so callers always
        observe a fully-constructed singleton.
        """
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = cls()
        return cls._instances[cls]

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
