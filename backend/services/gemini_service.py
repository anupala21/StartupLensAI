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
    try:    
        response = model.generate_content(prompt)
        text = response.text
        text = text.replace("```json", "")
        text = text.replace("```", "")
        return text.strip()
    except Exception as e:

        print("GEMINI ERROR:", e)

        return """
        {
            "innovation_score": 0,
            "market_potential": 0,
            "competition_level": "Unknown",
            "success_probability": 0,
            "recommendations": [
                "AI analysis temporarily unavailable."
            ]
        }
        """

# NEW FUNCTION

def find_competitors(idea):

    prompt = f"""
    Analyze this startup idea:

    {idea}

    Return ONLY valid JSON:

    {{
        "competitors": [
            "Competitor 1",
            "Competitor 2",
            "Competitor 3"
        ],
        "market_gap": "Gap in market",
        "opportunity_level": "High"
    }}

    Return JSON only.
    """
    try:
        response = model.generate_content(prompt)
        text = response.text
        print("GEMINI RESPONSE:")
        print(text)
        text = text.replace("```json", "")
        text = text.replace("```", "")
        return text.strip()
    except Exception as e:

        print("GEMINI ERROR:", e)

        return """
        { 
            "competitors": [],
            "market_gap": "AI analysis temporarily unavailable.",
            "opportunity_level": "Unknown"
        }
        """
def find_market_research(idea):

    prompt = f"""
    Analyze this startup idea:

    {idea}

    Return ONLY valid JSON:

    {{
        "tam": "$100 Billion",
        "sam": "$10 Billion",
        "som": "$500 Million",
        "growth_rate": "15% CAGR",
        "target_audience": [
            "Audience 1",
            "Audience 2",
            "Audience 3"
        ]
    }}

    Return JSON only.
    """
    try:
        response = model.generate_content(prompt)
        text = response.text
        text = text.replace("```json", "")
        text = text.replace("```", "")
        return text.strip()
    except Exception as e:

        print("GEMINI ERROR:", e)

        return """
        {
            "tam": "N/A",
            "sam": "N/A",
            "som": "N/A",
            "growth_rate": "N/A",
            "target_audience": [
                 "AI analysis temporarily unavailable."
             ]
        }
        """
def generate_blueprint(idea):

    prompt = f"""
    Create a startup blueprint for:

    {idea}

    Return ONLY valid JSON:

    {{
        "executive_summary": "...",
        "problem_statement": "...",
        "solution": "...",
        "target_audience": "...",
        "revenue_model": "...",
        "go_to_market_strategy": "...",
        "funding_recommendation": "..."
    }}

    Return JSON only.
    """
    try:
        response = model.generate_content(prompt)
        text = response.text
        text = text.replace("```json", "")
        text = text.replace("```", "")
        return text.strip()
    except Exception as e:

        print("GEMINI ERROR:", e)

        return """
        {
            "executive_summary": "AI analysis temporarily unavailable.",
            "problem_statement": "Unavailable",
            "solution": "Unavailable",
            "target_audience": "Unavailable",
            "revenue_model": "Unavailable",
            "go_to_market_strategy": "Unavailable",
            "funding_recommendation": "Unavailable"
        }
        """