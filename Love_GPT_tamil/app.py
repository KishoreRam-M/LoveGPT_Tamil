import os
import gradio as gr
from dotenv import load_dotenv
from crewai import Crew, Process, LLM

from agents import (
    Love_Story_Collector_Agent,
    Emotion_Analyzer_Agent,
    Love_Plan_Strategist_Agent,
    Pickup_Line_Poet_Agent,
    Gift_Idea_Agent,
    Date_Planner_Agent,
    Rejection_Handler_Agent,
    Jealousy_Detector_Agent,
    Relationship_Status_Tracker_Agent,
    Commitment_Closer_Agent,
)
from tasks import (
    collect_story_task,
    analyze_emotion_task,
    create_love_plan_task,
    create_pickup_lines_task,
    suggest_gifts_task,
    plan_date_task,
    handle_rejection_task,
    detect_jealousy_task,
    track_relationship_task,
    close_commitment_task,
)

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key="AIzaSyBgzArzLPeeinip1YI6Va37F5257rfFH2U",
)

Love_Story_Collector_Agent.llm        = gemini_llm
Emotion_Analyzer_Agent.llm            = gemini_llm
Love_Plan_Strategist_Agent.llm        = gemini_llm
Pickup_Line_Poet_Agent.llm            = gemini_llm
Gift_Idea_Agent.llm                   = gemini_llm
Date_Planner_Agent.llm                = gemini_llm
Rejection_Handler_Agent.llm           = gemini_llm
Jealousy_Detector_Agent.llm           = gemini_llm
Relationship_Status_Tracker_Agent.llm = gemini_llm
Commitment_Closer_Agent.llm           = gemini_llm

def run_lovegpt(user_story):
    if not user_story.strip():
        return "⚠️ Ungala love story sollunga! Empty-a irukku."

    LoveGPT_Tamil = Crew(
        agents=[
            Love_Story_Collector_Agent,
            Emotion_Analyzer_Agent,
            Love_Plan_Strategist_Agent,
            Pickup_Line_Poet_Agent,
            Gift_Idea_Agent,
            Date_Planner_Agent,
            Rejection_Handler_Agent,
            Jealousy_Detector_Agent,
            Relationship_Status_Tracker_Agent,
            Commitment_Closer_Agent,
        ],
        tasks=[
            collect_story_task,
            analyze_emotion_task,
            create_love_plan_task,
            create_pickup_lines_task,
            suggest_gifts_task,
            plan_date_task,
            handle_rejection_task,
            detect_jealousy_task,
            track_relationship_task,
            close_commitment_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    result = LoveGPT_Tamil.kickoff(inputs={"story": user_story})
    return str(result)

with gr.Blocks(theme=gr.themes.Soft(), title="LoveGPT Tamil") as app:

    gr.Markdown("""
    # 💕 LoveGPT Tamil
    ### Ungala love story sollunga — perfect plan ready pannuvom 🌹
    """)

    with gr.Row():
        with gr.Column(scale=1):
            story_input = gr.Textbox(
                label="💬 Ungala Love Story",
                placeholder="Example: Naan oru ponnaiya college-la paarthen, ava per Priya, aana pesave mudiyala...",
                lines=6,
            )
            submit_btn = gr.Button("🚀 Love Plan Uruvaakku", variant="primary")
            clear_btn  = gr.Button("🔄 Clear", variant="secondary")

        with gr.Column(scale=2):
            with gr.Tabs():
                with gr.Tab("📋 Full Plan"):
                    output_box = gr.Textbox(
                        label="LoveGPT Tamil Result",
                        lines=25,
                        interactive=False,
                    )

    with gr.Row():
        gr.Markdown("#### 💡 Tips")
        gr.Markdown("- Ungala story detailed-a sollunga — better result kidaikkum")
        gr.Markdown("- Ava peyar, place, situation ellame include pannunga")
        gr.Markdown("- Tamil or English — rendu language-layum solலலாம்")

    submit_btn.click(
        fn=run_lovegpt,
        inputs=story_input,
        outputs=output_box,
    )

    clear_btn.click(
        fn=lambda: (gr.update(value=""), gr.update(value="")),
        inputs=None,
        outputs=[story_input, output_box],
    )

# ─── Launch ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.launch(
        share=True,
        debug=True,
    )