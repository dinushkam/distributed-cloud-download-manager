from sqlalchemy.orm import Session

from backend.manager.app.models.worker import Worker
from backend.manager.app.repositories.worker_repository import WorkerRepository
from backend.manager.app.schemas.worker import WorkerRegister


class WorkerService:
    def __init__(self, db: Session):
        self.repository = WorkerRepository(db)

    def register_worker(self, worker: WorkerRegister) -> Worker:
        existing = self.repository.get_by_name(worker.worker_name)

        if existing:
            raise ValueError(f"Worker '{worker.worker_name}' is already registered.")

        return self.repository.create(worker)

    def list_workers(self):
        return self.repository.list_workers()

    def get_worker(self, worker_id):
        return self.repository.get_by_id(worker_id)
