# Driver Drowsiness Detection using CARLA Simulator

![Demo](demo.gif)

## About the Project

This project is a real-time Driver Drowsiness Detection System developed using Python, TensorFlow, OpenCV, and the CARLA Simulator.

The system detects driver drowsiness using a CNN model and shows the output during a live driving simulation in CARLA.

For webcam input, I connected my mobile camera to my laptop and used it for real-time face monitoring. The model processes the captured frames and detects whether the driver is alert or drowsy. When drowsiness is detected continuously, an alert is displayed in the simulation window.

---

## Features

- Real-time drowsiness detection
- Mobile camera used as webcam input
- Face detection using OpenCV
- CNN-based prediction model
- CARLA simulator integration
- Live alert display
- Pygame simulation window

---

## Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- CARLA Simulator
- Pygame
- NumPy

---

## Workflow

```text
Mobile Camera Input
        ↓
Face Detection
        ↓
Image Preprocessing
        ↓
CNN Prediction
        ↓
Drowsiness Detection
        ↓
Alert Display in CARLA Simulator
```

---

## Project Structure

```bash
drowsiness-detection-carla/
│
├── model/
├── screenshots/
├── demo.gif
├── project.py
├── requirements.txt
├── model_train.ipynb
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/junaith1704/drowsiness-detection-carla.git
cd drowsiness-detection-carla
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Start the CARLA simulator and run:

```bash
python project.py
```

---

## Future Improvements

- Audio alert system
- Eye blink detection
- Better face tracking
- Improved CNN model accuracy
- Lane detection integration

---

## Author

Mohammed Junaith Sulthan
