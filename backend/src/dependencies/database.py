
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.settings import load_settings


setting  = load_settings()

engine = create_engine(''.join(setting.get_db_url()))

# SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()