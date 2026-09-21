from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from moviepy.editor import TextClip
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
        
        # Create text clip without watermark
        clip = TextClip(req.text, fontsize=70, color='white', size=(1080, 1920), bg_color='black', method='caption')
        clip = clip.set_duration(5)
        
        # Write output video
        clip.write_videofile(output_path, fps=24, codec="libx264")
        
        return FileResponse(output_path, media_type="video/mp4", filename="video.mp4")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
