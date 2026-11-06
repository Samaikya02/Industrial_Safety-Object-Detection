import cv2
from ultralytics import YOLO
from detect_utils import get_violations, speak_alerts

model = YOLO("yolov8n.pt")  # or yolov8s.pt

def detect_and_alert(image):
    results = model(image)[0]
    violations = get_violations(results)
    if violations:
        print("Detected violations:", violations)
        speak_alerts(violations)

# Real-time webcam capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1020, 600))
    detect_and_alert(frame)
    cv2.imshow("Industrial Safety Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
