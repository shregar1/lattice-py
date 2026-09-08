"""Base class for dependency-injection providers."""

from abc import ABC, abstractmethod
from rivex import Dependency
from typing import Any


class DependencyLayer(Dependency, ABC):
    """
    Base class for objects exposed via the dependency-injection container.

    Subclasses implement :meth:`resolve` to construct and return the underlying
    object (utility, repository, service, ...) given the request context.
    """

    @abstractmethod

    def resolve(self, *args: Any, **kwargs: Any) -> Any:
        """Builds and returns the injected object for the current context."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
