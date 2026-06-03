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

import json

@app.post("/validate")
def validate(request: IdeaRequest):

    result = IdeaAgent.validate(request.idea)

    try:
        return json.loads(result)

    except Exception as e:

        print("JSON ERROR:", e)

        return {
            "raw_response": result
        }