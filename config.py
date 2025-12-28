import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BYTEZ_API_KEY = os.getenv("BYTEZ_API_KEY")

AI_NAME = "Nova"
VOICE_RATE = 175
VOICE_GENDER = "female"
