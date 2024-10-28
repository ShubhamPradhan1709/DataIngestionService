from pydantic import BaseModel, HttpUrl
from datetime import datetime
from uuid import UUID


class VideoChunkingEvent(BaseModel):
    event_id: UUID
    video_id: str
    timestamp: datetime
    video_url: HttpUrl



