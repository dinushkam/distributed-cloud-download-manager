from pathlib import Path
import sys

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from backend.shared.config.settings import settings

print("Application :", settings.APP_NAME)
print("Database    :", settings.DATABASE_URL)
print("AWS Region  :", settings.AWS_REGION)
print("Bucket      :", settings.AWS_BUCKET)