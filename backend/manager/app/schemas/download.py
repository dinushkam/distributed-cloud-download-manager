from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from backend.manager.app.models.download import DownloadStatus


class DownloadCreate(BaseModel):
    url: str
    file_name: str
    file_size: int = 0
    total_chunks: int = 0
    downloaded_chunks: int = 0
    status: DownloadStatus = DownloadStatus.PENDING


class DownloadUpdate(BaseModel):
    downloaded_chunks: int | None = None
    status: DownloadStatus | None = None


class DownloadResponse(BaseModel):
    id: UUID
    url: str
    file_name: str
    file_size: int
    total_chunks: int
    downloaded_chunks: int
    status: DownloadStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
