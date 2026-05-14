# Driver Drowsiness Detection using CARLA Simulator

This is my project where I built a drowsiness detection system and tested it inside the CARLA driving simulator.

I used my mobile camera as a webcam to capture my face in real time. The system detects if the driver is alert or drowsy using a CNN model I trained. If drowsiness is detected for multiple frames continuously, an alert shows up in the CARLA simulation window.

---

## Demo

![Demo](demo.gif)

---

## What it does

- Detects drowsiness in real time using webcam (mobile camera)
- Uses OpenCV to detect face
- CNN model predicts alert or drowsy
- If drowsy for too long, alert shows in CARLA window
- Vehicle runs on autopilot in CARLA while detection happens

---

## Technologies I used

- Python
- TensorFlow and Keras
- OpenCV
- CARLA Simulator
- Pygame
- NumPy

---

## How to run

Clone the repo:
```
git clone https://github.com/junaith1704/drowsiness-detection-carla.git
cd drowsiness-detection-carla
```

Install libraries:
```
pip install -r requirements.txt
```

Start CARLA simulator first, then run:
```
python project.py
```

---

## Project files

```
drowsiness-detection-carla/
├── project.py           - main detection script
├── model_train.ipynb    - how I trained the CNN model
├── requirements.txt     - libraries needed
└── README.md
```

---

## What I learned

- How to integrate a deep learning model with a simulator
- Real time face detection using OpenCV
- Training a CNN from scratch for binary classification
- Using CARLA Python API to spawn and control vehicles

---

## Future ideas

- Add audio alert
- Try eye blink detection instead of full face
- Test in different lighting conditions

---

**Mohammed Junaith Sulthan**  
B.E CSE (AI & ML) - Sathyabama University  
junaith2006@gmail.com
