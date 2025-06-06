from typing import List
from fastapi import APIRouter, Depends, Body, HTTPException, status
from beanie import PydanticObjectId

from database.connection import Database

from models.events import Event, EventUpdate, EventResponse

from auth.authenticate import authenticate

event_router = APIRouter(
    tags=["Events"]
)

event_database = Database(Event)

@event_router.get("/", response_model=EventResponse)
async def retrieve_all_events() -> dict:
    events = await event_database.get_all()

    return {
        "status": "success",
        "length": len(events),
        "datas": events
    }

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)

    if event:
        return event

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Event with supplied ID does not exist"
    )

@event_router.post("/")
async def create_event(event: Event, user: str = Depends(authenticate)) -> dict:
    event.creator = user

    await event_database.save(event)

    return {
        "status": "success",
        "message": "Event created successfully"
    }

@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, data: EventUpdate, user: str = Depends(authenticate)) -> Event:
    event = await event_database.get(id)
    if event.creator != user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Operation not allowed"
        )

    updated_event = await event_database.update(id, data)

    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )

    return updated_event

@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    event = await event_database.get(id)
    if event.creator != user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Operation not allowed"
        )
        
    event = await event_database.delete(id)

    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )


    return {
        "status": "success",
        "message": "Event deleted successfully"
    }