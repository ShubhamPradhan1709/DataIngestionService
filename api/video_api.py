from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from services.video_service import videoService, video_crud
from models.video import VideoCreateRequest, VideoResponse, VideoTable
from db.dbsetup import get_session
from sqlmodel import Session

router = APIRouter()

@router.post("/videos")
async def upload_video(session: Session = Depends(get_session), file: UploadFile = File(...)):
   
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

        video_data = VideoTable(
            video_name=videoMetaData.video_name,
            video_format=videoMetaData.video_format,
            video_size=videoMetaData.video_size,
            video_url=videoMetaData.video_url
        )

        video_data = await video_crud.create(session, video_data)
        if not video_data:
            return HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error: Entry not created {str(e)}"
            )
        
        return videoMetaData

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {str(e)}"
        )
    
    # writeVideoMetaData()
    
    # Also once the video is successfully create the metadata in video table as well as call the VideoChunkingEventQueue
    # writeVideoMetaData()
    



@router.get("/videos/{video_id}")
async def get_video_details(video_id: str):

    # Placeholder for getting video details 

    return {"message": "Video details fetched"}


