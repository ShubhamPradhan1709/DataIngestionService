from pydantic import BaseModel

class JobCreateRequest(BaseModel):
    video_id: str
    job_type: str