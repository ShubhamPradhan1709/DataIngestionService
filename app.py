from fastapi import FastAPI, Depends, HTTPException
# from db.dbsetup import lifespan
from sqlmodel import SQLModel
from api import video_api, job_api
from db.dbsetup import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health")
async def health_check():
    return {"message": "Database connection successful!"}

app.include_router(video_api.router)
app.include_router(job_api.router)
