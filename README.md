# ESP32-CAM YOLOv3 Object Detection

A real-time object detection system that combines ESP32-CAM with YOLOv3 for intelligent video analysis.

## 🚀 Features

- **Real-time Object Detection**: YOLOv3 model for fast and accurate detection
- **ESP32-CAM Integration**: Wireless camera streaming via HTTP
- **Multiple Classes**: Detects 80+ COCO dataset objects including birds, cats, persons, etc.
- **Optimized Performance**: Configurable confidence thresholds and NMS
- **Cross-Platform**: Works on Windows, Linux, and macOS

## 📋 Hardware Requirements

- ESP32-CAM module
- FTDI programmer (for flashing) or esp cam shield
- televerse cable
- WiFi network
- Python-capable computer

## 🔧 Software Requirements

- Python 3.7+
- OpenCV 4.5+
- pycharn
- NumPy
- Arduino IDE (for ESP32 programming)

## 📁 Project Structure
esp32cam-yolov3-object-detection/
├── esp32_cam/ # ESP32-CAM source code
│ └── esp32_cam.ino # Arduino sketch for camera
├── python_client/ # Python detection client
│ ├── detection.py # Main detection script
│ ├── requirements.txt # Python dependencies
│ └── yolov3.cfg # YOLO configuration file
├── models/ # Model files (add manually)
│ ├── yolov3.weights # YOLO pre-trained weights
│ └── coco.names.txt # COCO class names
├── docs/ # Documentation
└── README.md # This file
