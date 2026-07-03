from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ChunkCreate(BaseModel):
    download_id: UUID
    chunk_index: int
    start_byte: int
    end_byte: int


class ChunkUpdate(BaseModel):
    worker_id: UUID | None = None
    status: str | None = None


class ChunkResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    download_id: UUID
    worker_id: UUID | None

    chunk_index: int
    start_byte: int
    end_byte: int

    status: str

    created_at: datetime
    updated_at: datetime
