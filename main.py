from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
import os

app = FastAPI()

class VideoRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "Video API is Running Successfully"}

@app.post("/generate-video")
def generate_video(req: VideoRequest):
    try:
        output_path = "output.mp4"
        
        # Simple color clip video without system font errors
        clip = ColorClip(size=(1080, 1920), color=[10, 10, 10], duration=5)
        clip.write_videofile(output_path, fps=24, codec="libx264")
        
        return FileResponse(output_path, media_type="video/mp4", filename="video.mp4")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
