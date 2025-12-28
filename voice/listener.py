import sounddevice as sd
import numpy as np
import wave
import time
import io
import base64
from bytez import Bytez
from config import BYTEZ_API_KEY

sdk = Bytez(BYTEZ_API_KEY)
model = sdk.model("openai/whisper-large-v3")

def listen():
    """
    Direct-to-Memory listening using Bytez Cloud ASR (No files)
    """
    sample_rate = 16000
    threshold = 500 
    silence_limit = 0.5
    
    print("\nNova is listening...")
    
    frames = []
    recording = False
    last_voice_time = time.time()
    
    def callback(indata, frames_count, time_info, status):
        nonlocal recording, last_voice_time
        volume_norm = np.linalg.norm(indata) * 10
        
        if volume_norm > threshold:
            if not recording:
                recording = True
            frames.append(indata.copy())
            last_voice_time = time.time()
        elif recording:
            frames.append(indata.copy())
            
    with sd.InputStream(samplerate=sample_rate, channels=1, callback=callback, dtype=np.int16):
        while True:
            if recording and (time.time() - last_voice_time) > silence_limit:
                break
            time.sleep(0.02)
            
    if frames:
        buffer = io.BytesIO()
        audio_data = np.concatenate(frames, axis=0)
        with wave.open(buffer, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.tobytes())
            
        try:
            audio_bytes = buffer.getvalue()
            audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")
            
            response = model.run(audio_b64)
            
            if isinstance(response, tuple):
                output = response[0]
            else:
                output = response

            if isinstance(output, dict):
                result = output.get("text", output.get("output", ""))
            elif hasattr(output, 'text'):
                result = output.text
            else:
                result = str(output)
                
            return result.strip()
            
        except Exception as e:
            print(f"ASR Error: {e}")
            return ""
            
    return ""







