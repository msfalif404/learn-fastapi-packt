from typing import Optional, List

from beanie import Document
from pydantic import BaseModel

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book",
                "image": "https://image.com",
                "description": "We will discussing about this book later.",
                "tags": ["python", "fastapi", "book"],
                "location": "China"
            }
        }
    
    class Settings:
        name = "Events"

class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book",
                "image": "https://image.com",
                "description": "We will discussing about this book later.",
                "tags": ["python", "fastapi", "book"],
                "location": "China"
            }
        }

class EventResponse(BaseModel):
    status: str
    length: int
    datas: List[Event]