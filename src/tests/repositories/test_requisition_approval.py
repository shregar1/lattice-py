
from repositories.requisition.requisition_approval import RequisitionApprovalRepository

class TestRequisitionApprovalRepository:

    def test_repository_instantiation(self) -> None:
        repo = RequisitionApprovalRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestRequisitionApprovalRepository"

