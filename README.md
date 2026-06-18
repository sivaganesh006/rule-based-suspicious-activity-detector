# Rule-Based Suspicious Activity Detector

## Description
This project detects suspicious activity using YOLOv8.

Rules:
- Multiple persons detected
- Mobile phone detected

If any rule is triggered, the system prints:

{"suspicious": true}

## Technologies Used
- Python
- OpenCV
- YOLOv8
- NumPy

## Run

pip install -r requirements.txt

python suspicious_detector.py