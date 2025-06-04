from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
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