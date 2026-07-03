from uuid import UUID

from sqlalchemy.orm import Session

from backend.manager.app.models.chunk import Chunk
from backend.manager.app.schemas.chunk import ChunkCreate


class ChunkRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, chunk: ChunkCreate) -> Chunk:
        db_chunk = Chunk(**chunk.model_dump())
        self.db.add(db_chunk)
        self.db.commit()
        self.db.refresh(db_chunk)
        return db_chunk

    def get_by_id(self, chunk_id: UUID) -> Chunk | None:
        return self.db.query(Chunk).filter(Chunk.id == chunk_id).first()

    def get_by_download(self, download_id: UUID) -> list[Chunk]:
        return (
            self.db.query(Chunk)
            .filter(Chunk.download_id == download_id)
            .order_by(Chunk.chunk_index)
            .all()
        )

    def get_all(self) -> list[Chunk]:
        return self.db.query(Chunk).all()

    def delete(self, chunk: Chunk) -> None:
        self.db.delete(chunk)
        self.db.commit()
