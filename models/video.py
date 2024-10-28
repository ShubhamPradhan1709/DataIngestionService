from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4, UUID

class VideoCreateRequest(BaseModel):
    video_name: str
    video_format: str
    video_size: int
    video_file: bytes

class VideoResponse(BaseModel):
    video_name: str
    video_format: str
    video_size: int
    status: str

class VideoObjectStoreResponse(BaseModel):
    video_name: str
    video_format: str
    video_size: int
    video_url: str    

# class VideoTable(SQLModel, table=True):
#     video_id: UUID = Field(default= uuid4, primary_key=True)
#     video_name: str
#     video_format: str
#     video_size: int
#     # start_time: int
#     # end_time: int
#     # status: str
#     video_url: str

#     # jobs: list[JobTable] = Relationship(back_populates="jobs")

class VideoTable(SQLModel, table=True):
    video_id: UUID = Field(default_factory=uuid4, primary_key=True)
    video_name: str
    video_format: str
    video_size: int
    video_url: str

    # jobs: Optional[List["JobTable"]] = Relationship(back_populates="video")

    class Config:
        arbitrary_types_allowed = True