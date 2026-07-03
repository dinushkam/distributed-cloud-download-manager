from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.manager.app.db.session import get_db
from backend.manager.app.repositories.download_repository import DownloadRepository
from backend.manager.app.schemas.download import (
    DownloadCreate,
    DownloadResponse,
)
from backend.manager.app.services.download_service import DownloadService

router = APIRouter(prefix="/downloads", tags=["Downloads"])


def get_download_service(db: Session = Depends(get_db)) -> DownloadService:
    repository = DownloadRepository(db)
    return DownloadService(repository)


@router.post("/", response_model=DownloadResponse)
def create_download(
    download: DownloadCreate,
    service: DownloadService = Depends(get_download_service),
):
    return service.create_download(download)


@router.get("/", response_model=list[DownloadResponse])
def list_downloads(
    service: DownloadService = Depends(get_download_service),
):
    return service.list_downloads()


@router.get("/{download_id}", response_model=DownloadResponse)
def get_download(
    download_id: UUID,
    service: DownloadService = Depends(get_download_service),
):
    download = service.get_download(download_id)

    if download is None:
        raise HTTPException(status_code=404, detail="Download not found")

    return download


@router.delete("/{download_id}")
def delete_download(
    download_id: UUID,
    service: DownloadService = Depends(get_download_service),
):
    deleted = service.delete_download(download_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Download not found")

    return {"message": "Download deleted successfully"}
