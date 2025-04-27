from sqlalchemy.orm import Session
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# This function is a dependency that can be used in FastAPI routes to get a database session.


