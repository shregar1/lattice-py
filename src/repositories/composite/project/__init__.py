"""project composite repositories."""

from .project import ProjectRepository
from .project_template import ProjectTemplateRepository

__all__ = [
    "ProjectRepository",
    "ProjectTemplateRepository",
]
