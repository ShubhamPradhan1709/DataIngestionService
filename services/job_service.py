from models.job import JobTable
from db.dbsetup import SessionDep

class JobService:
    def create_job(self, job_details):
        # Placeholder for job creation logic
        pass



class JobCrud:
    async def create(self, db: SessionDep, job_data: JobTable):
        job = JobTable(**job_data.model_dump())
        db.add(job)
        db.commit()
        db.refresh(job)
        return str(job.id)

    async def get(self, db: SessionDep, job_id: str = None):
        if job_id:
            response = db.get(JobTable, job_id)
            return response if response else None
        
        return db.exec(JobTable).all()

    async def update(self, db: SessionDep, job_id: str, updated_job: JobTable):
        job = db.get(JobTable, job_id)
        if job:
            for key, value in updated_job.model_dump(exclude_unset=True).items():
                setattr(job, key, value)
            db.commit()
            db.refresh(job)
            return job
        return None

    async def delete(self, db: SessionDep, job_id: str):
        job = db.get(JobTable, job_id)
        if job:
            db.delete(job)
            db.commit()
            return "Job Deleted Successfully"
        return "Job not found"

job_crud = JobCrud()
