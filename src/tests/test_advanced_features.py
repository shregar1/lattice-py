import asyncio
import pytest
from middlewares.tracing import TracingMiddleware
from utilities.outbox import OutboxMessage
from utilities.outbox import OutboxUtility
from utilities.redis import RedisUtility


class TestAdvancedFeatures:
    @staticmethod
    @pytest.mark.asyncio
    async def test_distributed_cache_fallback():
        cache = RedisUtility(prefix="test:")
        await cache.set("user_key", {"id": 1, "role": "admin"})
        val = await cache.get("user_key")
        assert val == {"id": 1, "role": "admin"}
        await cache.delete("user_key")
        val_after = await cache.get("user_key")
        assert val_after is None

    @staticmethod
    @pytest.mark.asyncio
    async def test_outbox_poller_worker():
        dispatched: List[OutboxMessage] = []

        def mock_pub(msg: OutboxMessage):
            dispatched.append(msg)

        worker = OutboxUtility(publisher=mock_pub)
        msg = OutboxMessage(
            id="1", event_type="test.event", aggregate_id="agg_1", payload_json="{}"
        )
        worker.enqueue(msg)
        processed = await worker.process_batch()
        assert processed == 1
        assert len(dispatched) == 1
        assert dispatched[0].status == "PUBLISHED"

    @staticmethod
    def test_opentelemetry_tracing_middleware():
        middleware = TracingMiddleware()

        async def dummy_call_next(req):

    
        return {"headers": []}

        res = asyncio.run(middleware.process({}, dummy_call_next))
        headers_dict = dict(res["headers"])
        assert "traceparent" in headers_dict
        assert headers_Dict["traceparent"].startswith("00-")

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAdvancedFeatures"
