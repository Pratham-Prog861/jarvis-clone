import cv2
import os
import time

def capture_photo():
    """
    Capture a photo from the webcam and save it
    """
    cap = None
    try:
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Could not open webcam")
            return False
        time.sleep(1)

        ret, frame = cap.read()
        
        if ret:
            if not os.path.exists("captures"):
                os.makedirs("captures")
                
            filename = f"captures/photo_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Photo saved as: {filename}")

            os.startfile(os.path.abspath(filename))
            return True
        else:
            print("Failed to capture frame")
            return False
            
    except Exception as e:
        print(f"Camera Error: {e}")
        return False
    finally:
        if cap and cap.isOpened():
            cap.release()

