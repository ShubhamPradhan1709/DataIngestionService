from fastapi import FastAPI, Depends
from sqlmodel import create_engine, SQLModel, Session
from db.dbconfig import config
from contextlib import asynccontextmanager
from typing import Annotated
import asyncpg

DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD
DB_HOST = config.DB_HOST
DB_PORT = config.DB_PORT
DB_NAME = config.DB_NAME
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# connect_args = {"check_same_thread": False}
engine = create_engine(DB_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Establish a connection to the database
#     connection = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD,
#                                         database=DB_NAME, host=DB_HOST, port=DB_PORT)
#     try:
#         app.state.db_connection = connection
#         create_db_and_tables(app.state.db_connection)
#         print("Database connection established successfully.")  # Success message
#         yield  # Control returned to FastAPI
#     finally:
#         await connection.close()  # Ensure the connection is closed when the app stops
#         print("Database connection closed.") 

