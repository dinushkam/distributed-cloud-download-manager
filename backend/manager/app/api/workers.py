from fastapi import APIRouter

router = APIRouter(
    prefix="/workers",
    tags=["Workers"]
)

workers = {}


@router.get("/")
def get_workers():
    return workers
