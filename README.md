# Computer-Vision-Toolkit
Real-time detection tools for faces and motion using Python &amp; OpenCV.

# 👁️ Smart Security & Face Detection Tools

A collection of Computer Vision scripts built with **Python** and **OpenCV** to perform real-time monitoring and detection tasks. These tools run locally without requiring heavy internet usage.

## 📂 Project Files

### 1. Face Detection (`face_detect.py`)
- **Description:** Real-time face detection using Haar Cascades.
- **Tech:** Uses pre-trained XML classifiers to identify frontal faces.
- **Features:** Draws bounding boxes around detected faces and labels them.

### 2. Motion Detector (`security_cam.py`)
- **Description:** A security monitoring script that detects movement.
- **Mechanism:** Compares consecutive frames to detect changes (Frame Differencing).
- **Features:** alerts "MOVEMENT DETECTED" and highlights moving objects.

### 3. Stationary Object Detector (`object_detector.py`)
- **Description:** Advanced detection for abandoned or stationary objects.
- **Mechanism:** Uses Background Subtraction (First Frame approach) to detect new objects entering the scene.
- **Features:** Calculates and displays the size (Width x Height) of detected objects.

## 🛠️ Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)

## 🚀 How to Run
Simply run the script via terminal:
```bash
python face_detect.py
