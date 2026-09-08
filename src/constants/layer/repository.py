"""RepositoryName — PascalCase class-name constants for the repository layer."""

from typing import Final

from .abstraction import ILayerConstant


class Repository(ILayerConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Repository"
