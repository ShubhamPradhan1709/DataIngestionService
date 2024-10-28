from sqlmodel import Session
from models.job import JobTable
from models.video import VideoObjectStoreResponse, VideoTable
from models.player import PlayerTable
from models.user import UserTable
from db.dbsetup import SessionDep
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

class UserCrud:
    async def create(self, db: SessionDep, user_data: UserTable):
        user = UserTable(**user_data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return str(user.id)

    async def get(self, db: SessionDep, user_id: str = None):
        if user_id:
            response = db.get(UserTable, user_id)
            return response if response else None
        
        return db.exec(UserTable).all()

    async def update(self, db: SessionDep, user_id: str, updated_user: UserTable):
        user = db.get(UserTable, user_id)
        if user:
            for key, value in updated_user.model_dump(exclude_unset=True).items():
                setattr(user, key, value)
            db.commit()
            db.refresh(user)
            return user
        return None

    async def delete(self, db: SessionDep, user_id: str):
        user = db.get(UserTable, user_id)
        if user:
            db.delete(user)
            db.commit()
            return "User Deleted Successfully"
        return "User not found"

user_crud = UserCrud()

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

class PlayerCrud:
    async def create(db: SessionDep, player_data: PlayerTable):
        player = PlayerTable(**player_data.model_dump())
        db.add(player)
        db.commit()
        db.refresh(player)
        return str(player.id)

    async def get(self, db: SessionDep, player_id: str = None):
        if player_id:
            response = db.get(PlayerTable, player_id)
            return response if response else None
        
        return db.exec(PlayerTable).all()

    async def update(self, db: SessionDep, player_id: str, updated_player: PlayerTable):
        player = db.get(PlayerTable, player_id)
        if player:
            for key, value in updated_player.model_dump(exclude_unset=True).items():
                setattr(player, key, value)
            db.commit()
            db.refresh(player)
            return player
        return None

    async def delete(self, db: SessionDep, player_id: str):
        player = db.get(PlayerTable, player_id)
        if player:
            db.delete(player)
            db.commit()
            return "Player Deleted Successfully"
        return "Player not found"

player_crud = PlayerCrud()

class VideoCrud:
    async def create(self, session : SessionDep, video_data: VideoTable):
        session.add(video_data)
        session.commit()
        session.refresh(video_data)
        return video_data

    async def get(self, db: SessionDep, video_id: str = None):
        if video_id:
            response = db.get(VideoTable, video_id)
            return response if response else None
        
        return db.exec(VideoTable).all()

    async def update(self, db: SessionDep, video_id: str, updated_video: VideoTable):
        video = db.get(VideoTable, video_id)
        if video:
            for key, value in updated_video.model_dump(exclude_unset=True).items():
                setattr(video, key, value)
            db.commit()
            db.refresh(video)
            return video
        return None

    async def delete(self, db: SessionDep, video_id: str):
        video = db.get(VideoTable, video_id)
        if video:
            db.delete(video)
            db.commit()
            return "Video Deleted Successfully"
        return "Video not found"

video_crud = VideoCrud()
