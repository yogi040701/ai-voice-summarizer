
# 🎙️ AI Voice Summarizer

An AI-powered backend application that converts audio into text using Whisper and generates a concise summary using Transformer models.

## 🚀 Features
- Upload audio files
- Speech-to-text conversion (Whisper)
- Text summarization (Transformers)
- FastAPI backend
- Docker & Docker Compose support

## 🛠️ Tech Stack
- Python
- FastAPI
- Whisper
- Transformers
- PyTorch
- Docker

## 📁 Project Structure
ai_voice_summarizer/
├── app/
│   ├── main.py
│   ├── routes/audio.py
│   └── services/
│       ├── speech_to_text.py
│       └── summarizer.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## 🐳 Run with Docker
```bash
docker-compose up --build
```

## 🌐 API Docs
http://localhost:8000/docs

## 👨‍💻 Author
Yogjeet Singh
