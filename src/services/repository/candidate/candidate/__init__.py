"""Candidate repository services package."""

from .abstraction import ICandidateRepositoryService
from .candidate.create import CreateCandidateService
from .candidate.update import UpdateCandidateService
from .candidate.delete import DeleteCandidateService
from .candidate.filter import FilterCandidateService
