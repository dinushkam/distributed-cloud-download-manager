from uuid import UUID

from sqlalchemy.orm import Session

from backend.manager.app.models.download import Download
from backend.manager.app.schemas.download import DownloadCreate


class DownloadRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, download: DownloadCreate) -> Download:
        db_download = Download(**download.model_dump())

        self.db.add(db_download)
        self.db.commit()
        self.db.refresh(db_download)

        return db_download

    def get_by_id(self, download_id: UUID) -> Download | None:
        return self.db.query(Download).filter(Download.id == download_id).first()

    def get_all(self) -> list[Download]:
        return self.db.query(Download).all()

    def delete(self, download_id: UUID) -> bool:
        download = self.get_by_id(download_id)

        if not download:
            return False

        self.db.delete(download)
        self.db.commit()

        return True
