from sqlmodel import JSON, SQLModel, Field, Column
from typing import List, Optional
from pydantic import BaseModel

class Event(SQLModel, table=True):
    id: int = Field(default = None, primary_key = True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
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

class EventUpdate(SQLModel):
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