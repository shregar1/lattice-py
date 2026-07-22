import json
import os

class LatticeConfigLoader:
    @staticmethod
    def load_config(config_path: str = "config/lattice.json"):
        if os.path.exists(config_path):
            with open(config_path) as f:
                return json.load(f)
        return {"serviceName": "LatticeBackend", "environment": "development"}
