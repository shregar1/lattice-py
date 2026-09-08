"""PascalCase class-name constants for the abstraction layer."""

from typing import Final, Tuple

from abstractions import ConstantLayer


class ILayerConstant(ConstantLayer):
    """Base abstraction for layer constant classes."""

    HTTP: Final[str] = "http"
    CONTROLLER: Final[str] = "controller"
    SERVICE: Final[str] = "service"
    REPOSITORY: Final[str] = "repository"
    UTILITY: Final[str] = "utility"
    MODEL: Final[str] = "model"
    MIDDLEWARE: Final[str] = "middleware"
    DEPENDENCY: Final[str] = "dependency"
    CONSTANT: Final[str] = "constant"
    ENUM: Final[str] = "enum"
    FACTORY: Final[str] = "factory"
    LAYERS: Final[Tuple[str, ...]] = (
        HTTP,
        CONTROLLER,
        SERVICE,
        REPOSITORY,
        UTILITY,
        MODEL,
        MIDDLEWARE,
        FACTORY,
    )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ILayerConstant"
