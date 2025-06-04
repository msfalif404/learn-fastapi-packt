from fastapi import APIRouter, Depends, Body, HTTPException, status
from typing import List

from database.connection import get_session

from sqlmodel import select

from models.events import Event, EventUpdate, EventResponse

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/", response_model=EventResponse)
async def retrieve_all_events(session=Depends(get_session)) -> dict:
    statement = select(Event)
    events = session.exec(statement).all()

    return {
        "status": "success",
        "length": len(events),
        "datas": events
    }

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)

    if event:
        return event

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Event with supplied ID does not exist"
    )

@event_router.post("/")
async def create_event(event: Event, session = Depends(get_session)) -> dict:
    session.add(event)
    session.commit()
    session.refresh(event)

    return {
        "status": "success",
        "message": "Event created successfully"
    }

@event_router.put("/{id}", response_model=Event)
async def update_event(id: int, data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)

    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )

    event_data = data.dict(exclude_unset=True)

    for k, v in event_data.items():
        setattr(event, k, v)

    session.add(event)
    session.commit()
    session.refresh(event)

    return event

@event_router.delete("/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)

    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )

    session.delete(event)
    session.commit()

    return {
        "status": "success",
        "message": "Event deleted successfully"
    }