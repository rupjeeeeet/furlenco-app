# rag/llm.py
from dotenv import load_dotenv
load_dotenv()

import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing in environment variables.")

def llm_answer(query: str, context: str) -> str:
    prompt = f"""
You are a helpful e-commerce product recommendation assistant.

User Query:
{query}

Relevant Product Information (from vector search):
{context}

Your tasks:
1. Understand the customer's intent.
2. Recommend the BEST matching products using ONLY the context above.
3. Provide a helpful explanation for each recommended product.
4. If the context seems insufficient, ask a simple clarifying question.

Output:
- Natural helpful text
- No JSON
- No markdown
"""

    url = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        res = requests.post(url, json=payload)
        data = res.json()

        if res.status_code != 200:
            return f"Gemini error: {data.get('error', {}).get('message', 'Unknown error')}"

        text = data["candidates"][0]["content"]["parts"][0]["text"]
        return text.strip()

    except Exception as e:
        return f"Error communicating with Gemini: {e}"
