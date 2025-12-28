import pyautogui
import pytesseract
from PIL import Image
import time

def capture_screen(path="screen.png"):
    """
    Capture current screen
    """
    screenshot = pyautogui.screenshot()
    screenshot.save(path)
    return path


def read_screen_text():
    """
    Read visible text from screen using OCR
    """
    time.sleep(0.5)
    img_path = capture_screen()
    image = Image.open(img_path)
    text = pytesseract.image_to_string(image)
    return text.strip()
