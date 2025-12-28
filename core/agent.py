from google import genai
from config import GEMINI_API_KEY
from core.memory import get_memory
import os

client = genai.Client(api_key=GEMINI_API_KEY)

def load_system_prompt():
    """Load the Nova system prompt"""
    prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "nova_system.txt")
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"⚠️ Could not load system prompt: {e}")
        return "You are Nova, a helpful AI assistant. Always respond in valid JSON format."

SYSTEM_PROMPT = load_system_prompt()

def think(user_input, emotion):
    """
    Process user input and generate AI response
    """
    try:
        prompt = f"""{SYSTEM_PROMPT}

User emotion: {emotion}
User says: {user_input}

Respond ONLY with valid JSON. Be concise and fast.
"""
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text.strip()
    
    except Exception as e:
        print(f"❌ Error in think(): {e}")
        return '''{
    "intent": "idle",
    "tool": "none",
    "parameters": {},
    "reply": "I'm having trouble processing that right now."
}'''
