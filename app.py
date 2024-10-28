from fastapi import FastAPI, Depends
from db.dbsetup import get_db
from sqlmodel import SQLModel
# from api import video_api, job_api

app = FastAPI()

# app.include_router(video_api.router)
# app.include_router(job_api.router)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(bind=get_db().bind)
