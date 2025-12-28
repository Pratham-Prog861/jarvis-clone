import os
import warnings
import asyncio
import edge_tts
import pygame
import io

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
warnings.filterwarnings("ignore", category=UserWarning)

pygame.mixer.init()

def speak(text):
    """
    Speak text using Edge TTS directly from RAM (No files)
    """
    asyncio.run(_async_speak(text))

async def _async_speak(text):
    try:
        is_hindi = any('\u0900' <= char <= '\u097f' for char in text)
        voice = "hi-IN-SwaraNeural" if is_hindi else "en-US-AvaNeural"
        
        communicate = edge_tts.Communicate(text, voice)
        
        buffer = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                buffer.write(chunk["data"])
        
        buffer.seek(0)

        pygame.mixer.music.load(buffer, "mp3")
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.05)
            
        pygame.mixer.music.unload()
        
    except Exception as e:
        print(f"Voice Error: {e}")



