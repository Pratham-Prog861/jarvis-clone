import pyautogui
import time
import os

def open_app(app):
    try:
        if os.name == 'nt':
            pyautogui.press('win')
            time.sleep(0.5)
            pyautogui.write(app, interval=0.05)
            time.sleep(0.5)
            pyautogui.press('enter')
            print(f"Searching and opening: {app}")
        else:
            import subprocess
            subprocess.Popen(app)
    except Exception as e:
        print(f"Failed to open {app}: {e}")

