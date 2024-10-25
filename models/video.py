from pydantic import BaseModel

class VideoCreateRequest(BaseModel):
    video_name: str
    video_format: str
    video_size: int

class VideoResponse(BaseModel):
    video_id: str
    video_name: str
    video_format: str
    video_size: int
    status: str
