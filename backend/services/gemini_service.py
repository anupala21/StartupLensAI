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

Return ONLY valid JSON in this format:

{{
    "innovation_score": 8,
    "market_potential": 9,
    "competition_level": "Medium",
    "success_probability": 75,
    "recommendations": [
        "Recommendation 1",
        "Recommendation 2",
        "Recommendation 3"
    ]
}}

Do not include markdown.
Do not include explanations.
Return JSON only.
"""
    response = model.generate_content(prompt)

    text = response.text

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text.strip()