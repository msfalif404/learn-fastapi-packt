from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional

class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

class TodoItem(BaseModel):
    item: str

class TodoItemResponse(BaseModel):
    todos: List[TodoItem]