from models.video import VideoCreateRequest, VideoObjectStoreResponse
import os
import shutil
from sqlmodel import Session
from models.job import JobTable
from models.video import VideoObjectStoreResponse, VideoTable
from models.player import PlayerTable
from models.user import UserTable
from db.dbsetup import SessionDep
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

class VideoService:
    async def save_video(self, video_details: VideoCreateRequest):

        validate_dir = "uploads/"
        
        if not os.path.exists(validate_dir):
            os.makedirs(validate_dir)
            
        file_path = os.path.join(validate_dir, video_details.video_name)
        
        with open(file_path, "wb") as buffer:
            buffer.write(video_details.video_file)
        
        return VideoObjectStoreResponse(
            video_name= video_details.video_name,
            video_format= video_details.video_format,
             video_size= video_details.video_size,
            video_url= validate_dir
           
        )




    def get_video_details(self, video_id):

        # Placeholder for video detail retrieval logic

        pass

videoService = VideoService()



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