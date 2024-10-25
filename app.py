from fastapi import FastAPI
from api import job_api, video_api

app = FastAPI()

app.include_router(video_api.router)
app.include_router(job_api.router)
