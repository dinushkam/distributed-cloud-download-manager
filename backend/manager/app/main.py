from fastapi import FastAPI

from backend.manager.app.api.router import api_router
from backend.manager.app.core.logging import logger
from backend.shared.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Distributed Cloud Download Manager API",
)


@app.on_event("startup")
async def startup():
    logger.info("Manager API started")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Manager API stopped")


app.include_router(api_router)
