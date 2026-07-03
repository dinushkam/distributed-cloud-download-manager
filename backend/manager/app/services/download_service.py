from uuid import UUID

from backend.manager.app.repositories.chunk_repository import ChunkRepository
from backend.manager.app.repositories.download_repository import DownloadRepository
from backend.manager.app.schemas.download import DownloadCreate
from backend.manager.app.services.chunk_splitter import ChunkSplitter


class DownloadService:
    def __init__(self, repository: DownloadRepository, chunk_repo: ChunkRepository):
        self.repository = repository
        self.chunk_repo = chunk_repo

    def create_download(self, download: DownloadCreate):
        # 1. Create download record
        db_download = self.repository.create(download)

        # 2. Split file into chunks
        file_size = db_download.file_size or 0
        chunk_size = 10 * 1024 * 1024  # 10MB default

        chunks = ChunkSplitter.split(file_size, chunk_size)

        # 3. Store chunks in DB
        for start_byte, end_byte in chunks:
            self.chunk_repo.create(
                {
                    "download_id": db_download.id,
                    "start_byte": start_byte,
                    "end_byte": end_byte,
                    "status": "PENDING",
                }
            )

        return db_download

    def get_download(self, download_id: UUID):
        return self.repository.get_by_id(download_id)

    def list_downloads(self):
        return self.repository.get_all()

    def delete_download(self, download_id: UUID):
        return self.repository.delete(download_id)
