import google.generativeai as genai

from config import (
    GOOGLE_API_KEY,
    GEMINI_MODEL
)

genai.configure(
    api_key=GOOGLE_API_KEY
)

model = genai.GenerativeModel(
    GEMINI_MODEL
)

def get_ai_response(prompt):
    """
    Generate a response using Gemini.
    """

    response = model.generate_content(prompt)

    return response.text