import os
import warnings

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
warnings.filterwarnings("ignore", category=UserWarning)

import json
import re
from voice.listener import listen
from voice.speaker import speak
from core.agent import think
from core.emotion import detect_emotion
from core.router import route
import threading

def extract_json(text):
    """
    Extract JSON from text that might contain markdown code blocks
    """
    json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    if json_match:
        return json_match.group(1)
    
    json_match = re.search(r'\{.*\}', text, re.DOTALL)
    if json_match:
        return json_match.group(0)
    
    return text

print("=" * 50)
print("Nova is online and listening...")
print("=" * 50)
print("JARVIS Mode Active:")
print("   - Just start speaking to talk to Nova")
print("   - Nova will automatically detect your voice")
print("   - Nova will respond and keep listening")
print("\n   Press Ctrl+C to exit")
print("=" * 50)

try:
    while True:
        user_text = listen()
        if not user_text:
            continue
        emotion = detect_emotion(user_text)
        
        ai_response = think(user_text, emotion)
        
        try:
            json_text = extract_json(ai_response)
            action = json.loads(json_text)
            
            if "reply" not in action:
                continue
            
            print(f"Nova: {action['reply']}")
            
            action_thread = threading.Thread(target=route, args=(action,))
            action_thread.start()
            
            speak(action["reply"])
            
            action_thread.join(timeout=1.0)
            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Response was: {ai_response}")
            speak("I'm having trouble understanding my own response. Let me try again.")
        
        except Exception as e:
            print(f"Error processing action: {e}")
            speak("Something went wrong while processing that.")

except KeyboardInterrupt:
    print("\n\nNova shutting down. Goodbye!")
    speak("Goodbye!")

except Exception as e:
    print(f"Fatal error: {e}")
    speak("A critical error occurred. Shutting down.")
