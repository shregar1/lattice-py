"""FactoryName — PascalCase class-name constants for the factory layer."""

from typing import Final

from .abstraction import ILayerConstant


class Factory(ILayerConstant):

    RESPONSE_ENVELOPE: Final[str] = "ResponseEnvelopeFactory"
    EXCEPTION: Final[str] = "ExceptionFactory"
    MODEL: Final[str] = "ModelFactory"
    REPOSITORY: Final[str] = "RepositoryFactory"
    SERVICE: Final[str] = "ServiceFactory"
    CONFIGURATION: Final[str] = "ConfigurationFactory"
    ORCHESTRATOR: Final[str] = "OrchestratorFactory"
    UTILITY: Final[str] = "UtilityFactory"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Factory"
