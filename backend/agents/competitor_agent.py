import json

from backend.services.gemini_service import (
    find_competitors
)


class CompetitorAgent:

    @staticmethod
    def analyze(idea):

        result = find_competitors(idea)

        try:
            return json.loads(result)

        except Exception as e:

            print("Competitor JSON Error:", e)

            return {
                "competitors": [],
                "market_gap": "Unable to analyze",
                "opportunity_level": "Unknown"
            }