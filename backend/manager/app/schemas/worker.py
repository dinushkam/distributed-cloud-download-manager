from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class WorkerRegister(BaseModel):
    worker_name: str
    host: str
    port: int


class WorkerHeartbeat(BaseModel):
    cpu_usage: int
    memory_usage: int
    current_jobs: int


class WorkerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    worker_name: str
    host: str
    port: int
    status: str
    cpu_usage: int
    memory_usage: int
    current_jobs: int
    last_heartbeat: datetime | None
    created_at: datetime
    updated_at: datetime
