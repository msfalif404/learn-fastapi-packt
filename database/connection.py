from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

DB_FILE = "planner.db"
db_connection_string = f"sqlite:///{DB_FILE}"
db_connection_args = {"check_same_thread":False}

engine_url = create_engine(db_connection_string, connect_args=db_connection_args, echo=True)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session