import pyautogui
import time
import pyperclip

def write_text(text):
    time.sleep(0.5)

    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
