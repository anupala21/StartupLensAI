import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_startup_idea(idea):
    prompt = f"""
    Analyze this startup idea:

    {idea}

    Return:
    1. Innovation Score (1-10)
    2. Market Potential (1-10)
    3. Competition Level
    4. Success Probability (%)
    5. Key Recommendations

    Format nicely.
    """

    response = model.generate_content(prompt)

    return response.text