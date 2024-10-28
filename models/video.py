from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class VideoCreateRequest(BaseModel):
    video_name: str
    video_format: str
    video_size: int
    video_file: bytes

class VideoResponse(BaseModel):
    video_id: str
    video_name: str
    video_format: str
    video_size: int
    status: str

class VideoObjectStoreResponse(BaseModel):
    video_name: str
    video_format: str
    video_size: int
    video_url: str    

class VideoTable(SQLModel, table=True):
    video_id: Optional[int] = Field(default=None, primary_key=True)
    video_name: str
    video_format: str
    video_size: int
    # start_time: int
    # end_time: int
    # status: str
    video_url: str

    # jobs: list[JobTable] = Relationship(back_populates="jobs")


