from fastapi import APIRouter

from backend.manager.app.api.chunks import router as chunks_router
from backend.manager.app.api.downloads import router as downloads_router
from backend.manager.app.api.health import router as health_router
from backend.manager.app.api.workers import router as workers_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(workers_router)
api_router.include_router(downloads_router)
api_router.include_router(chunks_router)
