import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crewai import Crew, Process

# Import from the relocated modules
from agents import (
    Love_Story_Collector_Agent, Emotion_Analyzer_Agent, Love_Plan_Strategist_Agent,
    Pickup_Line_Poet_Agent, Gift_Idea_Agent, Date_Planner_Agent,
    Rejection_Handler_Agent, Jealousy_Detector_Agent,
    Relationship_Status_Tracker_Agent, Commitment_Closer_Agent,
)
from tasks import (
    collect_story_task, analyze_emotion_task, create_love_plan_task,
    create_pickup_lines_task, suggest_gifts_task, plan_date_task,
    handle_rejection_task, detect_jealousy_task,
    track_relationship_task, close_commitment_task,
)

app = FastAPI(title="LoveGPT Tamil API")

# Setup CORS to allow the React frontend to communicate with it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For production, restrict this to the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StoryRequest(BaseModel):
    story: str

@app.post("/api/generate_love_plan")
async def generate_love_plan(request: StoryRequest):
    user_story = request.story
    if not user_story.strip():
        raise HTTPException(status_code=400, detail="Story cannot be empty.")

    try:
        LoveGPT_Tamil = Crew(
            agents=[
                Love_Story_Collector_Agent, Emotion_Analyzer_Agent, Love_Plan_Strategist_Agent,
                Pickup_Line_Poet_Agent, Gift_Idea_Agent, Date_Planner_Agent,
                Rejection_Handler_Agent, Jealousy_Detector_Agent,
                Relationship_Status_Tracker_Agent, Commitment_Closer_Agent,
            ],
            tasks=[
                collect_story_task, analyze_emotion_task, create_love_plan_task,
                create_pickup_lines_task, suggest_gifts_task, plan_date_task,
                handle_rejection_task, detect_jealousy_task,
                track_relationship_task, close_commitment_task,
            ],
            process=Process.sequential,
            verbose=True,
        )

        result = LoveGPT_Tamil.kickoff(inputs={"story": user_story})
        return {"plan": str(result.raw)}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
