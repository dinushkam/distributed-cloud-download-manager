from backend.manager.app.database.database import engine
from backend.manager.app.database.base import Base

# Import models
from backend.manager.app.models import Worker

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")