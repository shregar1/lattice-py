from rivex import get
from typing import Dict

from abstractions import ControllerLayer
from configs import PROJECT_NAME, PROJECT_VERSION, project_metadata
from constants import HEALTH_TAG
from utilities import timer


class LivenessHealthController(ControllerLayer):
    path = "/health"
    tags: List[str] = [HEALTH_TAG]


    @get(path=path, tags=tags, summary="Liveness probe")
    @timer("controller")
    async def health_liveness(self) -> Dict[str, str]:
        meta = project_metadata()

        return {
            "status": "ok",
            "service": meta.get("name", PROJECT_NAME),
            "version": meta.get("version", PROJECT_VERSION),
        }

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "LivenessHealthController"
