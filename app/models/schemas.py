from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventDTO(BaseModel):
    name: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

class UserDTO(BaseModel):
    username: str

