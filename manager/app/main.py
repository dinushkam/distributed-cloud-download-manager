from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.workers import router as workers_router
from app.api.downloads import router as downloads_router

app = FastAPI(
    title="Distributed Download Manager",
    version="1.0.0",
    description="Manager Service"
)


@app.get("/")
def root():
    return {
        "service": "Distributed Download Manager",
        "status": "running"
    }


app.include_router(health_router)
app.include_router(workers_router)
app.include_router(downloads_router)
