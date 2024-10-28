from fastapi import APIRouter, UploadFile, File, HTTPException, status
from services.video_service import videoService
from models.video import VideoCreateRequest, VideoResponse
from services.crud_service import video_crud

router = APIRouter()

@router.post("/videos")
async def upload_video(file: UploadFile = File(...)):
   
    # Placeholder for uploading video to object store

    try:
        file_content = await file.read()
        videoCreateObject = VideoCreateRequest(
            video_name=file.filename,
            video_format=file.content_type,
            video_size=len(file_content),
            video_file=file_content
        )
        
        videoMetaData =  await videoService.save_video(videoCreateObject)

        print(videoMetaData)
        return videoMetaData
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {str(e)}"
        )
    
    # writeVideoMetaData()
    
    
    return {"message": "Video uploaded successfully"}
    # Also once the video is successfully create the metadata in video table as well as call the VideoChunkingEventQueue
    # writeVideoMetaData()
    
    # produce_VideoChunkingEventQueue()

    return {"message": "Video uploaded successfully"}


# What will be the object store?
# what parameter/input are we taking from the user to upload the file
# 

@router.get("/videos/{video_id}")
async def get_video_details(video_id: str):

    # Placeholder for getting video details 

    return {"message": "Video details fetched"}


