#!/usr/bin/env python3
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("❌ Error: Please provide a module name.")
        print("Example: python scripts/create_module.py Product")
        sys.exit(1)

    raw = sys.argv[1]
    pascal = raw.capitalize()
    snake = raw.lower()
    kebab = raw.lower().replace("_", "-")

    print(f"🚀 Scaffolding Lattice-Py Clean-Architecture Module for: {pascal}...\n")

    def write_file(path, content):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if os.path.exists(path):
            print(f"  ⚠️ Skipping existing file: {path}")
            return
        with open(path, "w") as f:
            f.write(content.strip() + "\n")
        print(f"  ✓ Created: {path}")

    # 1. Model
    write_file(f"src/lattice/models/{snake}.py", f"""
from datetime import datetime
from typing import Optional
from dataclasses import dataclass

@dataclass
class {pascal}Model:
    id: str
    urn: str
    name: str
    owner_id: str
    tenant_id: str
    is_deleted: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
""")

    # 2. DTO
    write_file(f"src/lattice/dto/requests/{snake}.py", f"""
from pydantic import BaseModel, Field

class Create{pascal}Request(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
""")

    write_file(f"src/lattice/dto/responses/{snake}.py", f"""
from pydantic import BaseModel

class {pascal}Response(BaseModel):
    id: str
    urn: str
    name: str
    owner_id: str
""")

    # 3. Repository
    write_file(f"src/lattice/repositories/{snake}.py", f"""
from abc import ABC, abstractmethod
from typing import Optional
from lattice.models.{snake} import {pascal}Model

class I{pascal}Repository(ABC):
    @abstractmethod
    async def find_by_id(self, id: str) -> Optional[{pascal}Model]:
        pass
""")

    # 4. Service
    write_file(f"src/lattice/services/{snake}.py", f"""
from lattice.repositories.{snake} import I{pascal}Repository
from lattice.dto.responses.{snake} import {pascal}Response

class {pascal}Service:
    def __init__(self, repo: I{pascal}Repository):
        self.repo = repo
""")

    # 5. Orchestrator
    write_file(f"src/lattice/orchestrators/{snake}.py", f"""
from lattice.services.{snake} import {pascal}Service

class {pascal}Orchestrator:
    def __init__(self, service: {pascal}Service):
        self.service = service
""")

    print(f"\n✨ Scaffolding complete for lattice-py module '{pascal}'!")

if __name__ == "__main__":
    main()
