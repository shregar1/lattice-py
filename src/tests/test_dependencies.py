from abstractions import DependencyLayer
from dependencies import (
    CandidateRepositoryDependency,
    CryptoUtilityDependency,
    EmailUtilityDependency,
    HashingUtilityDependency,
    JobRepositoryDependency,
    JWTUtilityDependency,
    URNUtilityDependency,
    SMSUtilityDependency,
    UserRepositoryDependency,
    ValidationUtilityDependency,
)
from repositories import CandidateRepository, JobRepository, UserRepository
from utilities.crypto import CryptoUtility
from utilities.email import EmailUtility
from utilities.hashing import HashingUtility
from utilities.jwt import JWTUtility
from utilities.urn import URNUtility
from utilities.sms import SMSUtility
from utilities.validation import ValidationUtility


class TestDependencies:
    @staticmethod
    def test_repository_dependencies_resolve():
        cand_dep = CandidateRepositoryDependency()
        assert isinstance(cand_dep, DependencyLayer)
        cand_repo = cand_dep.resolve()
        assert isinstance(cand_repo, CandidateRepository)
        job_dep = JobRepositoryDependency()
        assert isinstance(job_dep, DependencyLayer)
        job_repo = job_dep.resolve()
        assert isinstance(job_repo, JobRepository)
        user_dep = UserRepositoryDependency()
        assert isinstance(user_dep, DependencyLayer)
        user_repo = user_dep.resolve()
        assert isinstance(user_repo, UserRepository)

    @staticmethod
    def test_utility_dependencies_resolve():
        email_dep = EmailUtilityDependency()
        assert isinstance(email_dep, DependencyLayer)
        assert isinstance(email_dep.resolve(), EmailUtility)
        sms_dep = SMSUtilityDependency()
        assert isinstance(sms_dep, DependencyLayer)
        assert isinstance(sms_dep.resolve(), SMSUtility)
        jwt_dep = JWTUtilityDependency()
        assert isinstance(jwt_dep, DependencyLayer)
        assert isinstance(jwt_dep.resolve(), JWTUtility)
        crypto_dep = CryptoUtilityDependency()
        assert isinstance(crypto_dep, DependencyLayer)
        assert isinstance(crypto_dep.resolve(), CryptoUtility)
        hashing_dep = HashingUtilityDependency()
        assert isinstance(hashing_dep, DependencyLayer)
        assert isinstance(hashing_dep.resolve(), HashingUtility)
        validation_dep = ValidationUtilityDependency()
        assert isinstance(validation_dep, DependencyLayer)
        assert isinstance(validation_dep.resolve(), ValidationUtility)
        urn_dep = URNUtilityDependency()
        assert isinstance(urn_dep, DependencyLayer)
        assert urn_dep.resolve() is URNUtility.parse_public_urn

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestDependencies"
