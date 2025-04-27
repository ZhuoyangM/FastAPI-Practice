from sqlalchemy.orm import Session
from models import Event, User
from schemas import EventDTO, UserDTO

def create_event(db: Session, eventdto: EventDTO) -> Event:
    new_event = Event(
        title=eventdto.name,
        description=eventdto.description,
        start_time=eventdto.start_time,
        end_time=eventdto.end_time
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def get_event(db: Session, event_id: str) -> Event:
    return db.query(Event).filter(Event.id == event_id).first()


def get_events(db: Session, skip: int = 0, limit: int = 10) -> list[Event]:
    return db.query(Event).offset(skip).limit(limit).all()


def create_user(db: Session, userdto: UserDTO) -> User:
    new_user = User(
        username=userdto.username
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: str) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()

