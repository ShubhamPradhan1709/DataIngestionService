from models.video import VideoCreateRequest, VideoObjectStoreResponse
import os
import shutil

class VideoService:
    async def save_video(self, video_details: VideoCreateRequest):

        validate_dir = "uploads/"
        
        if not os.path.exists(validate_dir):
            os.makedirs(validate_dir)
            
        file_path = os.path.join(validate_dir, video_details.video_name)
        
        with open(file_path, "wb") as buffer:
            buffer.write(video_details.video_file)
        
        return VideoObjectStoreResponse(
            video_name=video_details.video_name, 
            video_format=video_details.video_format, 
            video_size=video_details.video_size, 
            video_url=validate_dir
            )




    def get_video_details(self, video_id):

        # Placeholder for video detail retrieval logic

        pass

videoService = VideoService()