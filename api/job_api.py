from fastapi import APIRouter
from models.job import JobCreateRequest
from services.job_service import JobService

router = APIRouter()

@router.post("/jobs")
async def create_job(job_details: JobCreateRequest):
    # Placeholder for creating a job
    return {"message": "Job created successfully"}

