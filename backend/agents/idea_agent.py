from backend.services.gemini_service import (
    analyze_startup_idea
)


class IdeaAgent:

    @staticmethod
    def validate(idea):
        return analyze_startup_idea(idea)
    