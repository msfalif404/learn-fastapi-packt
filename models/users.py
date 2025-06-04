from pydantic import BaseModel, EmailStr
from typing import Optional, List

from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": "orang1@gmail.com",
                "password": "ABCD1234",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "orang1@gmail.com",
                "password": "ABCD1234"
            }
        }