from fastapi import APIRouter
from services.video_service import videoService
from models.video import VideoCreateRequest, VideoResponse

router = APIRouter()

@router.post("/videos")
async def upload_video(video_details: VideoCreateRequest):
   
    # Placeholder for uploading video to object store
    # save_video()

    # Also once the video is successfully create the metadata in video table as well as call the VideoChunkingEventQueue
    # writeVideoMetaData()
    # produce_VideoChunkingEventQueue()

    return {"message": "Video uploaded successfully"}



@router.get("/videos/{video_id}")
async def get_video_details(video_id: VideoResponse):

    # Placeholder for getting video details 

    return {"message": "Video details fetched"}