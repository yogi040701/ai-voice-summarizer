from fastapi import FastAPI
from app.routes.audio import router as audio_router

app = FastAPI(title="AI Voice Summarizer")

app.include_router(audio_router)

@app.get("/")
def health():
    return {"status": "ok"}