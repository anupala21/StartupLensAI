import json

from backend.services.gemini_service import (
    find_market_research
)


class MarketAgent:

    @staticmethod
    def analyze(idea):

        result = find_market_research(idea)

        try:
            return json.loads(result)

        except Exception as e:

            print("Market JSON Error:", e)

            return {
                "tam": "Unknown",
                "sam": "Unknown",
                "som": "Unknown",
                "growth_rate": "Unknown",
                "target_audience": []
            }