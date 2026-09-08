"""CandidateLocation repository services package."""

from .abstraction import ICandidateLocationRepositoryService
from .candidate_location.create import CreateCandidateLocationService
from .candidate_location.update import UpdateCandidateLocationService
from .candidate_location.delete import DeleteCandidateLocationService
from .candidate_location.filter import FilterCandidateLocationService
