from fastapi import FastAPI
from pydantic import BaseModel

from backend.agents.idea_agent import (
    IdeaAgent
)

app = FastAPI()


class IdeaRequest(BaseModel):
    idea: str


@app.get("/")
def home():
    return {
        "message": "StartupLens AI Running"
    }


@app.post("/validate")
def validate(request: IdeaRequest):

    result = IdeaAgent.validate(
        request.idea
    )

    return {
        "analysis": result
    }