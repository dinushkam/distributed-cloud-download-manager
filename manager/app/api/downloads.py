from fastapi import APIRouter

router = APIRouter(
    prefix="/downloads",
    tags=["Downloads"]
)


@router.get("/")
def downloads():
    return {
        "message": "Download API coming soon"
    }
