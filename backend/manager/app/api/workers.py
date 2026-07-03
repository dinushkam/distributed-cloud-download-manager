from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.manager.app.db.session import get_db
from backend.manager.app.schemas.worker import (
    WorkerRegister,
    WorkerResponse,
)
from backend.manager.app.services.worker_service import WorkerService

router = APIRouter(
    prefix="/workers",
    tags=["Workers"],
)


@router.post(
    "/register",
    response_model=WorkerResponse,
    status_code=201,
)
def register_worker(
    worker: WorkerRegister,
    db: Session = Depends(get_db),
):
    service = WorkerService(db)

    try:
        return service.register_worker(worker)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
