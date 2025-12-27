# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def summarize_text(text: str) -> str:
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "user",
#                 "content": f"""
# Extract:
# 1. Key points
# 2. Action items

# Text:
# {text}
# """
#             }
#         ],
#         temperature=0.3
#     )
#     return response.choices[0].message.content


from transformers import pipeline

_summarizer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=-1  # CPU
        )
    return _summarizer


def summarize_text(text: str) -> str:
    summarizer = get_summarizer()

    result = summarizer(
        text,
        max_new_tokens=256,
        do_sample=False
    )

    return result[0]["summary_text"]