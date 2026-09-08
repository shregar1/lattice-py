import pytest
from exceptions.http.conflict import ConflictException
from exceptions.http.not_found import NotFoundException
from exceptions.http.bad_input import BadInputException
from factories.exception import ErrorFactory
from factories.model import ModelFactory
from factories.repository import RepositoryFactory
from factories.utility import UtilityFactory
from .user.user import User
from repositories.atomic.candidate.candidate import CandidateRepository
from repositories.job.job import JobRepository
from repositories.user.user import UserRepository
from utilities.crypto import CryptoUtility
from utilities.hashing import HashingUtility
from utilities.jwt import JWTUtility
from utilities import Logger
from utilities.validation import ValidationUtility


class TestFactories:
    @staticmethod
    def test_error_factory_all_registrations() -> None:
        factory = ErrorFactory()
        assert isinstance(factory.build("not_found", resource="User"), NotFoundException)
        assert isinstance(factory.build("validation", message="Invalid field"), BadInputException)
        assert isinstance(factory.build("conflict", message="Conflict"), ConflictException)
        with pytest.raises(KeyError):
            factory.build("unknown_error_type")

    @staticmethod
    def test_model_factory_all_registrations() -> None:
        factory = ModelFactory()
        user = factory.build(
            "user", name="Alice", title="Manager", user_type_id=1, tenant_id=1, user_id=1
        )
        assert isinstance(user, User)
        with pytest.raises(KeyError):
            factory.build("unknown_model")

    @staticmethod
    def test_repository_factory_all_registrations() -> None:
        factory = RepositoryFactory()
        assert isinstance(factory.build("candidate"), CandidateRepository)
        assert isinstance(factory.build("job"), JobRepository)
        assert isinstance(factory.build("user"), UserRepository)
        with pytest.raises(KeyError):
            factory.build("unknown_repo")

    @staticmethod
    def test_utility_factory_all_registrations() -> None:
        factory = UtilityFactory()
        assert isinstance(factory.build("logger"), Logger)
        assert isinstance(factory.build("crypto"), CryptoUtility)
        assert isinstance(factory.build("hashing"), HashingUtility)
        assert isinstance(factory.build("jwt"), JWTUtility)
        assert isinstance(factory.build("validation"), ValidationUtility)
        with pytest.raises(KeyError):
            factory.build("unknown_utility")

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestFactories"
