import pytest
from utilities.outbox import DomainEvent, OutboxMessage, UnitOfWorkUtility


class TestOutbox:
    @staticmethod
    @pytest.mark.asyncio
    async def test_unit_of_work_outbox_commit():
        published: List[OutboxMessage] = []

        async def mock_publisher(msg: OutboxMessage):
            published.append(msg)

        async with UnitOfWorkUtility(message_publisher=mock_publisher) as uow:
            event = DomainEvent(
                event_type="candidate.created",
                aggregate_id="cand_123",
                payload={"email": "test@example.com"},
            )
            uow.record_event(event)
        assert len(published) == 1
        assert published[0].event_type == "candidate.created"
        assert published[0].aggregate_id == "cand_123"
        assert published[0].status == "PUBLISHED"

    @staticmethod
    @pytest.mark.asyncio
    async def test_unit_of_work_outbox_rollback():
        published: List[OutboxMessage] = []

        async def mock_publisher(msg: OutboxMessage):
            published.append(msg)

        with pytest.raises(RuntimeError):
            async with UnitOfWorkUtility(message_publisher=mock_publisher) as uow:
                event = DomainEvent(event_type="job.deleted", aggregate_id="job_999", payload={})
                uow.record_event(event)
                raise RuntimeError("Simulated transaction failure")
        assert len(published) == 0

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestOutbox"
