from sqlalchemy.orm import Session
from models import Event, User
from schemas import EventDTO

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


