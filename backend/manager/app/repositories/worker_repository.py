from sqlalchemy.orm import Session

from backend.manager.app.models.worker import Worker
from backend.manager.app.schemas.worker import WorkerRegister


class WorkerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, worker: WorkerRegister) -> Worker:
        db_worker = Worker(
            worker_name=worker.worker_name,
            host=worker.host,
            port=worker.port,
        )

        self.db.add(db_worker)
        self.db.commit()
        self.db.refresh(db_worker)

        return db_worker

    def get_by_name(self, worker_name: str) -> Worker | None:
        return self.db.query(Worker).filter(Worker.worker_name == worker_name).first()

    def get_by_id(self, worker_id):
        return self.db.query(Worker).filter(Worker.id == worker_id).first()

    def list_workers(self):
        return self.db.query(Worker).all()

    def delete(self, worker: Worker):
        self.db.delete(worker)
        self.db.commit()
