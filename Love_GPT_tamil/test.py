import traceback

try:
    from app import run_lovegpt
    print("Testing CrewAI flow...")
    result = run_lovegpt("Naan oru ponna pakka poren, ava name Priya. Ava oru paattukarai. Epdi propose pandrathu?")
    print("\n--- RESULT ---")
    print(result)
except Exception as e:
    print("Encountered exception:")
    traceback.print_exc()
