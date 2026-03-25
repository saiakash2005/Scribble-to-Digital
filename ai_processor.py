import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def process_text_with_ai(raw_text):

    prompt = f"""
You are an AI assistant.

1. Correct grammar and spelling of the following OCR text.
2. Convert it into clear readable notes.
3. Extract tasks if present.

Text:
{raw_text}

Return response in this format:

NOTES:
(clean paragraph)

TASKS:
(task1)
(task2)
"""

    response = model.generate_content(prompt)

    result = response.text

    notes = ""
    tasks = []

    if "TASKS:" in result:
        parts = result.split("TASKS:")
        notes = parts[0].replace("NOTES:","").strip()
        tasks = [t.strip() for t in parts[1].split("\n") if t.strip()]

    else:
        notes = result

    return notes, tasks