from backend.manager.app.db.base import Base
from backend.manager.app.db.session import engine

# Import models

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
