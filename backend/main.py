from fastapi import FastAPI
from pydantic import BaseModel
from backend.agents.competitor_agent import (
    CompetitorAgent
)
from backend.agents.idea_agent import (
    IdeaAgent
)
from backend.agents.market_agent import (
    MarketAgent
)
from backend.agents.blueprint_agent import (
    BlueprintAgent
)
app = FastAPI()


class IdeaRequest(BaseModel):
    idea: str


@app.get("/")
def home():
    return {
        "message": "StartupLens AI Running"
    }

import json

@app.post("/validate")
def validate(request: IdeaRequest):

    result = IdeaAgent.validate(request.idea)

    try:
        return json.loads(result)

    except Exception as e:

        print("JSON ERROR:", e)
        print(result)
        return {
            "raw_response": result
        }
@app.post("/competitors")
def competitors(request: IdeaRequest):

    result = CompetitorAgent.analyze(
        request.idea
    )

    return result
@app.post("/market-research")
def market_research(request: IdeaRequest):

    result = MarketAgent.analyze(
        request.idea
    )

    return result
@app.post("/blueprint")
def blueprint(request: IdeaRequest):

    result = BlueprintAgent.analyze(
        request.idea
    )

    return result