import uuid

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

from backend.manager.app.database.base import Base


class Worker(Base):
    __tablename__ = "workers"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    worker_name: Mapped[str] = mapped_column(String(100), unique=True)

    host: Mapped[str] = mapped_column(String(100))

    port: Mapped[int]

    status: Mapped[str] = mapped_column(
        String(20),
        default="OFFLINE"
    )

    cpu_usage: Mapped[int] = mapped_column(default=0)

    memory_usage: Mapped[int] = mapped_column(default=0)

    current_jobs: Mapped[int] = mapped_column(default=0)

    last_heartbeat: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )