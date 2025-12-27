# from fastapi import APIRouter, UploadFile, File
# import shutil

# router = APIRouter(prefix="/audio")

# @router.post("/upload")
# async def upload_audio(file: UploadFile = File(...)):
#     path = f"uploads/{file.filename}"
#     with open(path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {"message": "Audio uploaded", "path": path}



from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.services.speech_to_text import transcribe_audio
from app.services.summarizer import summarize_text

router = APIRouter(prefix="/audio")

@router.post("/process")
async def process_audio(file: UploadFile = File(...)):
    # 1️⃣ Save uploaded file
    path = f"uploads/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2️⃣ Speech → Text
    transcript = transcribe_audio(path)

    # 3️⃣ Text → Summary
    summary = summarize_text(transcript)

    return {
        "transcript": transcript,
        "summary": summary
    }
