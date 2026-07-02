import uuid
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.manager.app.db.base import Base


class Worker(Base):
    __tablename__ = "workers"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    worker_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    host: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    port: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="OFFLINE",
        nullable=False,
    )

    cpu_usage: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    memory_usage: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    current_jobs: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    last_heartbeat: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
