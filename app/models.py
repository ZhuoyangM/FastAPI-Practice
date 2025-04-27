from sqlalchemy import Column, String, DateTime,ForeignKey, Table
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DATABASE_URL = "sqlite:///./app/test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

user_event_association = Table(
    'user_event_association',
    Base.metadata,
    Column('user_id', String, ForeignKey('users.id'), primary_key=True),
    Column('event_id', String, ForeignKey('events.id'), primary_key=True)
)

class Event(Base):
    __tablename__ = "events"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    users = relationship("User", secondary=user_event_association, back_populates="events")

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    username = Column(String, nullable=False, unique=True)
    events = relationship("Event", secondary=user_event_association, back_populates="users")

