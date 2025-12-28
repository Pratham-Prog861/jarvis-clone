import webbrowser
import pyautogui
import time

def open_url(url: str):
    """
    Open a URL in the default browser
    """
    webbrowser.open(url)


def google_search(query: str):
    """
    Perform a Google search
    """
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)


def type_in_browser(text: str):
    """
    Type text in active browser input (search bar / textbox)
    """
    time.sleep(1)
    pyautogui.write(text, interval=0.03)
    pyautogui.press("enter")
