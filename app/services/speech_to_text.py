# from openai import OpenAI
# from dotenv import load_dotenv
# import os


# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def transcribe_audio(audio_path: str) -> str:
#     with open(audio_path, "rb") as audio:
#         transcript = client.audio.transcriptions.create(model="whisper-1", file=audio)
#     return transcript['text']


import whisper

_model = None

def get_model():
    global _model
    if _model is None:
        _model = whisper.load_model("tiny", device="cpu")  # load model tiny, base, small, medium, large
    return _model

def transcribe_audio(path: str) -> str:
    model = get_model()
    result = model.transcribe(path, fp16=False)
    return result["text"]

