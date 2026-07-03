from uuid import UUID

from sqlalchemy.orm import Session

from backend.manager.app.repositories.chunk_repository import ChunkRepository
from backend.manager.app.schemas.chunk import (
    ChunkCreate,
    ChunkResponse,
)
from backend.manager.app.services.worker_service import WorkerService


class ChunkService:
    def __init__(self, db: Session):
        self.repository = ChunkRepository(db)
        self.worker_service = WorkerService(db)

    def create_chunk(self, chunk: ChunkCreate) -> ChunkResponse:
        return self.repository.create(chunk)

    def get_chunk(self, chunk_id: UUID):
        return self.repository.get_by_id(chunk_id)

    def get_chunks_by_download(self, download_id: UUID):
        return self.repository.get_by_download(download_id)

    def get_all_chunks(self):
        return self.repository.get_all()

    def delete_chunk(self, chunk_id: UUID) -> bool:
        chunk = self.repository.get_by_id(chunk_id)

        if chunk is None:
            return False

        self.repository.delete(chunk)
        return True
