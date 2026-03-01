import json
from vision_agents import YoloDetector

def check_privacy(image_path):
    """
    Simple vision agent to detect faces and trigger privacy actions.
    """
    detector = YoloDetector()
    detections = detector.detect(image_path)
    
    # Check if any face is detected (assuming detector returns labels)
    # This is a simplified logic for the hackathon demo
    face_detected = any(d.label == 'face' for d in detections)
    
    if face_detected:
        return json.dumps({
            "privacy": "BREACH",
            "action": "BLUR"
        })
    else:
        return json.dumps({
            "privacy": "SECURE",
            "action": "NONE"
        })

if __name__ == "__main__":
    # Example usage
    print(check_privacy("test_frame.jpg"))
