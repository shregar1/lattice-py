from rivex import get

from abstractions import ControllerLayer
from constants import APITag
from utilities import timer


class DBHealthController(ControllerLayer):
    path = "/health"
    tags: List[str] = [APITag.HEALTH]


    @get("/db", summary="Database connectivity probe")
    @timer("controller")
    async def health_db(self) -> Dict[str, str | int]:
        engine = get_engine()
        rows = await engine.fetch_many("SELECT 1 AS ok", [])

        return {
            "status": "ok",
            "service": project_metadata().get("name", PROJECT_NAME),
            "database": rows[0]["ok"],
        }

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "DBHealthController"
