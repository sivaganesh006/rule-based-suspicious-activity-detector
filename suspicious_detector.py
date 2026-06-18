from ultralytics import YOLO
import cv2
import time
import json
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

face_missing_start = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    person_count = 0
    phone_detected = False

    for box in results[0].boxes:
        cls = int(box.cls[0])

        if cls == 0:  # person
            person_count += 1

        if cls == 67:  # cell phone
            phone_detected = True

    suspicious = False

    # Rule 1: Multiple persons
    if person_count > 1:
        suspicious = True

    # Rule 2: Phone detected
    if phone_detected:
        suspicious = True

    if suspicious:
        print(json.dumps({"suspicious": True}))
    else:
        print(json.dumps({"suspicious": False}))

    annotated_frame = results[0].plot()

    cv2.imshow("Suspicious Activity Detector", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()