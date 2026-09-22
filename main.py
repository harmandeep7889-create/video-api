from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class VideoRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "Video API is Running Successfully"}

@app.post("/generate-video")
def generate_video(req: VideoRequest):
    try:
        return {
            "status": "success",
            "message": "Video generation request processed successfully!",
            "text": req.text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
