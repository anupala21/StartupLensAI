import json

from backend.services.gemini_service import (
    generate_blueprint
)


class BlueprintAgent:

    @staticmethod
    def analyze(idea):

        result = generate_blueprint(idea)

        try:
            return json.loads(result)

        except Exception as e:

            print("Blueprint JSON Error:", e)

            return {
                "executive_summary": "Unavailable",
                "problem_statement": "Unavailable",
                "solution": "Unavailable",
                "target_audience": "Unavailable",
                "revenue_model": "Unavailable",
                "go_to_market_strategy": "Unavailable",
                "funding_recommendation": "Unavailable"
            }