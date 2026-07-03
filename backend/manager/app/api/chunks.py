from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.manager.app.db.session import get_db
from backend.manager.app.schemas.chunk import (
    ChunkCreate,
    ChunkResponse,
)
from backend.manager.app.services.chunk_service import ChunkService

router = APIRouter(
    prefix="/chunks",
    tags=["Chunks"],
)


@router.post("/", response_model=ChunkResponse)
def create_chunk(
    chunk: ChunkCreate,
    db: Session = Depends(get_db),
):
    service = ChunkService(db)
    return service.create_chunk(chunk)


@router.get("/{chunk_id}", response_model=ChunkResponse)
def get_chunk(
    chunk_id: UUID,
    db: Session = Depends(get_db),
):
    service = ChunkService(db)

    chunk = service.get_chunk(chunk_id)

    if chunk is None:
        raise HTTPException(
            status_code=404,
            detail="Chunk not found",
        )

    return chunk


@router.get("/download/{download_id}", response_model=list[ChunkResponse])
def get_chunks_by_download(
    download_id: UUID,
    db: Session = Depends(get_db),
):
    service = ChunkService(db)
    return service.get_chunks_by_download(download_id)
