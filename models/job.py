from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from models.video import VideoTable

class JobCreateRequest(BaseModel):
    video_id: str
    job_type: str

class JobTable(SQLModel, table=True):
    job_id: int = Field(default=None, primary_key=True)
    video_id: int = Field(default=None, foreign_key="VideoTable.video_id")
    start_time: int
    end_time: int
    chunk: int

    video: VideoTable = Relationship(back_populates="video")
    
    
