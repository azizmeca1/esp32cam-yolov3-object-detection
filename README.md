# ESP32-CAM YOLOv3 Object Detection

![Example de Détection](images/example%20of%20detection.png)
*Système de détection d'objets en temps réel avec ESP32-CAM et YOLOv3*

## Real-Time Object Detection System with ESP32-CAM and YOLOv3

A real-time object detection system using ESP32-CAM camera and YOLOv3 model with OpenCV.

### Features
- [x] Real-time object detection via ESP32-CAM  
- [x] YOLOv3 pre-trained model implementation  
- [x] Detection of 80 object classes (people, animals, vehicles, etc.)  
- [x] Bounding boxes and confidence scores display  
- [x] Live visualization interface with OpenCV  

## 📊 Demonstration

![Detection Results](images/example%20of%20detection.png)
*Live object detection with bounding boxes and confidence scores*

## 🛠️ Installation

### Requirements
- ESP32-CAM module
- Python 3.7+
- OpenCV 4.5+
- YOLOv3 weights and configuration

### Setup
```bash
git clone https://github.com/azizmecai/esp32cam-yolov3-object-detection.git
cd esp32cam-yolov3-object-detection
pip install -r requirements.txt# ESP32-CAM YOLOv3 Object Detection



![Exemple de Détection](images/example%20of%20detection.png)
*Système de détection d'objets en temps réel avec ESP32-CAM et YOLOv3*

# 📷 Real-Time Object Detection System with ESP32-CAM and YOLOv3

A real-time object detection system using ESP32-CAM camera and YOLOv3 model with OpenCV.

## 🎯 Features

- ✅ Real-time object detection via ESP32-CAM
- ✅ YOLOv3 pre-trained model implementation
- ✅ Detection of 80 object classes (people, animals, vehicles, etc.)
- ✅ Bounding boxes and confidence scores display
- ✅ Live visualization interface with OpenCV
- ✅ Smart text positioning (always visible even for partially off-frame objects)
- ✅ Adjustable window size for comfortable viewing

## 📋 Prerequisites

### Hardware
- **ESP32-CAM AI-Thinker** (with OV2640 module)
- FTDI programmer or USB-TTL cable
- WiFi network
- Computer with Python 3.7+

### Software
- Arduino IDE or PlatformIO
- Python 3.7 or higher
- Required Python libraries (see Installation)

## 🚀 Installation

### 1. ESP32-CAM Setup

#### a) Install ESP32 Board in Arduino IDE
1. Open Arduino IDE
2. Go to **File > Preferences**
3. Add this URL to "Additional Board Manager URLs":
   ```
   https://dl.espressif.com/dl/package_esp32_index.json
   ```
4. Go to **Tools > Board > Boards Manager**
5. Search for "ESP32" and install **ESP32 by Espressif Systems**

#### b) Upload Code to ESP32-CAM
1. Open the `esp32cam_server.ino` file
2. Modify WiFi credentials:
   ```cpp
   const char* WIFI_SSID = "YOUR_WIFI_NAME";
   const char* WIFI_PASS = "YOUR_PASSWORD";
   ```
3. Select board: **Tools > Board > ESP32 Arduino > AI Thinker ESP32-CAM**
4. Connect FTDI programmer:
   - FTDI 5V → ESP32 5V
   - FTDI GND → ESP32 GND
   - FTDI TX → ESP32 U0R
   - FTDI RX → ESP32 U0T
   - ESP32 IO0 → ESP32 GND (for programming mode)
5. Click **Upload**
6. After upload, disconnect IO0 from GND and press RESET

#### c) Get ESP32-CAM IP Address
1. Open Serial Monitor (115200 baud)
2. Press RESET button on ESP32-CAM
3. Note the IP address displayed (e.g., `192.168.1.16`)

### 2. Python Environment Setup

#### a) Install Python Dependencies
```bash
pip install numpy opencv-python urllib3
```

#### b) Download YOLOv3 Files

Create a project folder and download these files:

**1. COCO Classes File** (`coco.names.txt`):
```bash
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names -O coco.names.txt
```

**2. YOLOv3 Configuration** (`yolov3.cfg`):
```bash
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
```

**3. YOLOv3 Weights** (~236 MB):
```bash
wget https://pjreddie.com/media/files/yolov3.weights
```

Or manually download from:
- [YOLOv3 Weights](https://pjreddie.com/media/files/yolov3.weights)
- [YOLOv3 Config](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- [COCO Names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

### 3. Project Structure

Your project folder should look like this:
```
esp32cam_yolo_detection/
├── esp32cam_server.ino          # ESP32-CAM Arduino code
├── object_detection_yolo.py     # Python detection script
├── yolov3.cfg                   # YOLOv3 configuration
├── yolov3.weights               # YOLOv3 pre-trained weights
└── coco.names.txt               # 80 object classes names
```

## 🎮 Usage

### 1. Start ESP32-CAM
- Power on ESP32-CAM
- Wait for WiFi connection (check Serial Monitor)
- Note the IP address

### 2. Update Python Script
Edit `object_detection_yolo.py` and change the URL:
```python
url = 'http://YOUR_ESP32_IP/cam.jpg'  # Replace with your ESP32-CAM IP
```

### 3. Run Detection
```bash
python object_detection_yolo.py
```

### 4. Controls
- **Window will display live feed with detected objects**
- **Press 'Q'** to quit the application
- **Resize window** manually if too large

## ⚙️ Configuration

### Adjust Detection Parameters

In `object_detection_yolo.py`:

```python
# Detection confidence threshold (0.0 to 1.0)
confThreshold = 0.5  # Lower = more detections, more false positives

# Non-maximum suppression threshold
nmsThreshold = 0.3   # Lower = fewer overlapping boxes

# Window size adjustment
im_resized = cv2.resize(im, (0, 0), fx=0.5, fy=0.5)  # 0.5 = 50% size
```

### Change Frame Size (ESP32-CAM)

In `esp32cam_server.ino`:

```cpp
config.frame_size = FRAMESIZE_SVGA;  // Options:
// FRAMESIZE_QQVGA  (160x120)
// FRAMESIZE_QVGA   (320x240)
// FRAMESIZE_VGA    (640x480)
// FRAMESIZE_SVGA   (800x600)
// FRAMESIZE_XGA    (1024x768)
// FRAMESIZE_UXGA   (1600x1200)
```

## 🐛 Troubleshooting

### ESP32-CAM Issues

**Problem:** Camera initialization fails
```
Solution: Check all pin connections, ensure OV2640 camera is properly seated
```

**Problem:** Can't connect to WiFi
```
Solution: 
- Verify WiFi credentials
- Check if WiFi is 2.4GHz (ESP32 doesn't support 5GHz)
- Check router firewall settings
```

**Problem:** Image quality is poor
```
Solution: Adjust JPEG quality in code:
config.jpeg_quality = 10;  // Lower = better quality (10-63)
```

### Python Script Issues

**Problem:** "Connection refused" or timeout
```
Solution:
- Verify ESP32-CAM IP address
- Ping ESP32-CAM: ping 192.168.1.16
- Check firewall settings
- Ensure both devices are on same network
```

**Problem:** OpenCV window doesn't appear
```
Solution:
- On Linux: sudo apt-get install python3-opencv
- On macOS: brew install opencv
- Try: cv2.namedWindow('ESP32-CAM Detection', cv2.WINDOW_NORMAL)
```

**Problem:** "Failed to load YOLO files"
```
Solution:
- Verify all three files exist (cfg, weights, names)
- Check file names exactly match
- Re-download yolov3.weights if corrupted
```

**Problem:** Slow detection/Low FPS
```
Solution:
- Reduce frame size on ESP32-CAM
- Reduce input size: whT = 320 (or lower to 256)
- Use YOLOv3-tiny for faster detection (smaller model)
```

## 🔧 Advanced Features

### Use YOLOv3-Tiny (Faster, Less Accurate)

For faster detection on slower computers:

1. Download YOLOv3-Tiny files:
```bash
wget https://pjreddie.com/media/files/yolov3-tiny.weights
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg
```

2. Update Python script:
```python
modelConfig = 'yolov3-tiny.cfg'
modelWeights = 'yolov3-tiny.weights'
```

### Detect Specific Objects Only

Modify the `findObject` function to filter specific classes:

```python
# Only detect people and cats
allowed_classes = ['person', 'cat']

if classNames[classIds[i]] in allowed_classes:
    # Draw box and label
    cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 255), 2)
    # ... rest of the code
```

### Save Detections to Video

Add this code to save output:

```python
# Before the while loop
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Inside the loop, after findObject()
out.write(im_resized)

# After the loop
out.release()
```

## 📊 Detected Object Classes

The system can detect 80 classes from COCO dataset:
- **People:** person
- **Animals:** cat, dog, bird, horse, sheep, cow, elephant, bear, zebra, giraffe
- **Vehicles:** car, motorcycle, airplane, bus, train, truck, boat
- **Indoor:** chair, couch, bed, dining table, toilet, tv, laptop, mouse, keyboard
- **Food:** banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake
- And many more...

## 📝 Code Explanation

### ESP32-CAM Code
```cpp
handleJpg()  // Captures and streams JPEG image via HTTP
```

### Python Detection Script
```python
cv2.dnn.readNetFromDarknet()  // Loads YOLOv3 model
cv2.dnn.blobFromImage()       // Preprocesses image for YOLO
net.forward()                  // Runs object detection
cv2.dnn.NMSBoxes()            // Removes duplicate detections
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **YOLOv3:** Joseph Redmon and Ali Farhadi
- **ESP32-CAM:** Espressif Systems
- **OpenCV:** Open Source Computer Vision Library
- **COCO Dataset:** Common Objects in Context

## 📧 Contact

For questions or issues, please open an issue on GitHub.

## 🔗 Useful Links

- [YOLOv3 Paper](https://arxiv.org/abs/1804.02767)
- [ESP32-CAM Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [COCO Dataset](https://cocodataset.org/)

---

**⭐ If you find this project helpful, please give it a star!**
