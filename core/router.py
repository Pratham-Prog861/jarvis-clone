from tools.system import open_app
from tools.writer import write_text
from tools.browser import open_url, google_search
from tools.camera import capture_photo

def route(action):
    """
    Route actions to appropriate tools based on intent
    """
    try:
        intent = action.get("intent", "idle")
        parameters = action.get("parameters", {})
        
        if intent == "open_app":
            app = parameters.get("app")
            if app:
                print(f"Opening app: {app}")
                open_app(app)
            else:
                print("No app specified")
        
        elif intent == "write":
            content = parameters.get("content")
            if content:
                print(f"Writing text: {content}")
                write_text(content)
            else:
                print("No content to write")
        
        elif intent == "capture":
            print("Capturing photo...")
            capture_photo()
        
        elif intent == "browse":
            url = parameters.get("url")
            if url:
                print(f"Opening URL: {url}")
                open_url(url)
            else:
                print("No URL specified")
        
        elif intent == "search":
            query = parameters.get("query")
            if query:
                print(f"Searching for: {query}")
                google_search(query)
            else:
                print("No search query specified")
        
        elif intent == "idle":
            pass
        
        else:
            print(f"Unknown intent: {intent}")
    
    except Exception as e:
        print(f"Error in route(): {e}")

