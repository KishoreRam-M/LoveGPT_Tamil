from crewai import Task
from agents import (
    Love_Story_Collector_Agent,
    Emotion_Analyzer_Agent,
    Love_Plan_Strategist_Agent,
    Pickup_Line_Poet_Agent,
    Gift_Idea_Agent,
    Date_Planner_Agent,
    Rejection_Handler_Agent,
    Commitment_Closer_Agent,
    Jealousy_Detector_Agent,
    Relationship_Status_Tracker_Agent,
)

collect_story_task = Task(
    description=(
        "Ask the user deep emotional questions to collect their complete love story. "
        "Collect: who they love, how they met, current status, obstacles they face. "
        "Use the story input: {story}. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete love story report containing: "
        "1. Name and description of loved one "
        "2. How they met and when "
        "3. Current relationship status "
        "4. Key moments and memories "
        "5. Obstacles and challenges they face"
    ),
    agent=Love_Story_Collector_Agent,
)

analyze_emotion_task = Task(
    description=(
        "Receive the love story from collect_story_task. "
        "Apply all 13 emotion techniques to deeply analyze the story. "
        "Identify hidden feelings, emotional triggers and patterns. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete emotional profile report containing: "
        "1. Dominant emotions detected "
        "2. Emotional triggers identified "
        "3. Behavioral patterns found "
        "4. Sentiment score (positive, negative, neutral) "
        "5. Key emotional insights for planning"
    ),
    agent=Emotion_Analyzer_Agent,
    context=[collect_story_task],
)

create_love_plan_task = Task(
    description=(
        "Receive emotional profile from analyze_emotion_task. "
        "Create a personalized step-by-step love plan. "
        "Include approach strategy, conversation starters, "
        "emotional connection steps, timing and commitment tactics. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete love plan containing: "
        "1. Approach strategy "
        "2. Conversation starters "
        "3. Emotional connection steps "
        "4. Timing advice "
        "5. Commitment tactics"
    ),
    agent=Love_Plan_Strategist_Agent,
    context=[analyze_emotion_task],
)

create_pickup_lines_task = Task(
    description=(
        "Receive love plan from create_love_plan_task. "
        "Create powerful situation-based Tamil and Tanglish pickup lines. "
        "For each line give: situation, delivery style, expected reaction. "
        "Also teach the user the formula to create their own pickup lines. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete pickup line guide containing: "
        "1. 5 situation-based pickup lines "
        "2. When and how to use each line "
        "3. Expected reaction for each "
        "4. Own pickup line creation formula with example"
    ),
    agent=Pickup_Line_Poet_Agent,
    context=[create_love_plan_task],
)

suggest_gifts_task = Task(
    description=(
        "Receive love plan from create_love_plan_task and "
        "emotional profile from analyze_emotion_task. "
        "Suggest perfect romantic gifts based on her personality. "
        "Include budget options and DIY Tamil cultural gift ideas. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete gift guide containing: "
        "1. Top 5 gift suggestions with reasons "
        "2. Best occasion for each gift "
        "3. How to present each gift romantically "
        "4. Budget range for each "
        "5. DIY gift idea with Tamil cultural touch "
        "6. What NOT to gift and why"
    ),
    agent=Gift_Idea_Agent,
    context=[create_love_plan_task, analyze_emotion_task],
)

plan_date_task = Task(
    description=(
        "Receive love story from collect_story_task and "
        "love plan from create_love_plan_task. "
        "Create a perfect practical romantic date plan. "
        "Include location, timing, flow, outfit, backup plan. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete date plan containing: "
        "1. Date type and location "
        "2. Perfect timing details "
        "3. Step-by-step date flow "
        "4. What to wear, say and do "
        "5. Backup plan "
        "6. How to end the date memorably"
    ),
    agent=Date_Planner_Agent,
    context=[collect_story_task, create_love_plan_task],
)

handle_rejection_task = Task(
    description=(
        "Receive love story from collect_story_task and "
        "emotional profile from analyze_emotion_task. "
        "Identify rejection type and provide complete recovery plan. "
        "Include second chance strategy and self improvement plan. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete rejection recovery plan containing: "
        "1. Rejection type identified "
        "2. Immediate emotional first aid steps "
        "3. What NOT to do list "
        "4. Day by day recovery plan "
        "5. Second chance strategy "
        "6. Self improvement plan "
        "7. When and how to move on"
    ),
    agent=Rejection_Handler_Agent,
    context=[collect_story_task, analyze_emotion_task],
)

detect_jealousy_task = Task(
    description=(
        "Receive love story from collect_story_task and "
        "emotional profile from analyze_emotion_task. "
        "Detect jealousy type and patterns in the relationship. "
        "Show how to use healthy jealousy and avoid toxic jealousy. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete jealousy analysis report containing: "
        "1. Jealousy type identified "
        "2. Jealousy triggers detected "
        "3. Relationship impact analysis "
        "4. How to use jealousy as a love tool "
        "5. Toxic jealousy warning signs "
        "6. Jealousy management plan "
        "7. How to increase your value in her eyes"
    ),
    agent=Jealousy_Detector_Agent,
    context=[collect_story_task, analyze_emotion_task],
)

track_relationship_task = Task(
    description=(
        "Receive all reports from all previous tasks. "
        "Track and analyze current relationship status in real time. "
        "Give progress score, positive signals, warning signals. "
        "Provide overall relationship health score out of 10. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete relationship status report containing: "
        "1. Current relationship stage "
        "2. Progress score "
        "3. Positive signals she is showing "
        "4. Warning signals to watch "
        "5. Next milestone and how to reach it "
        "6. Real time advice "
        "7. Relationship health score out of 10"
    ),
    agent=Relationship_Status_Tracker_Agent,
    context=[
        collect_story_task,
        analyze_emotion_task,
        create_love_plan_task,
        plan_date_task,
        detect_jealousy_task,
    ],
)

close_commitment_task = Task(
    description=(
        "Receive relationship report from track_relationship_task and "
        "love plan from create_love_plan_task. "
        "Guide the user to get a commitment successfully. "
        "Give exact words, perfect moment, location and response handling. "
        "Respond in Tanglish or Tamil."
    ),
    expected_output=(
        "A complete commitment closing plan containing: "
        "1. Right time and moment to propose "
        "2. Exact words to say in Tamil and Tanglish "
        "3. Perfect location and setting "
        "4. How to handle yes, maybe, need time responses "
        "5. What to do if she hesitates "
        "6. Post commitment relationship plan "
        "7. Red flags that mean she is not ready"
    ),
    agent=Commitment_Closer_Agent,
    context=[track_relationship_task, create_love_plan_task],
)