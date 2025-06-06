from typing import Optional, List
from pydantic import BaseModel, EmailStr
from beanie import Document, Link

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]] = None

    class Config:
        schema_extra = {
            "example": {
                "email": "orang1@gmail.com",
                "password": "ABCD1234",
                "events": []
            }
        }
    
    class Settings:
        name = "users"