# Driver Drowsiness Detection - CARLA Integration
# Author: Mohammed Junaith Sulthan
# I used mobile camera as webcam for face input

import cv2
import numpy as np
import carla
import pygame
import time
import random
from tensorflow.keras.models import load_model

# load my trained model
model = load_model("model/drowsiness_model.h5")

# face detector using opencv
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# connect to carla
client = carla.Client("localhost", 2000)
client.set_timeout(10.0)
world = client.get_world()

# spawn a vehicle
bp_lib = world.get_blueprint_library()
vehicle_bp = bp_lib.filter("model3")[0]
spawn_point = random.choice(world.get_map().get_spawn_points())
vehicle = world.spawn_actor(vehicle_bp, spawn_point)
vehicle.set_autopilot(True)

# attach camera to vehicle
camera_bp = bp_lib.find("sensor.camera.rgb")
camera_bp.set_attribute("image_size_x", "800")
camera_bp.set_attribute("image_size_y", "600")
camera = world.spawn_actor(
    camera_bp,
    carla.Transform(carla.Location(x=1.5, z=2.4)),
    attach_to=vehicle
)

# pygame window setup
pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drowsiness Detection")
font = pygame.font.SysFont("Arial", 30)

# store latest carla frame
latest_frame = [None]

def save_frame(image):
    arr = np.frombuffer(image.raw_data, dtype=np.uint8)
    arr = arr.reshape((image.height, image.width, 4))
    latest_frame[0] = arr[:, :, :3]

camera.listen(save_frame)

# open webcam (mobile camera connected as webcam)
cap = cv2.VideoCapture(0)

drowsy_count = 0

print("Running... press Q to stop")

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt

        # read webcam frame
        ret, frame = cap.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        status = "Alert"

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face = cv2.resize(face, (64, 64)) / 255.0
            face = np.expand_dims(face, axis=0)

            prediction = model.predict(face, verbose=0)[0][0]

            if prediction > 0.6:
                drowsy_count += 1
                status = "DROWSY!"
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            else:
                drowsy_count = max(0, drowsy_count - 1)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # show alert if drowsy for too long
        if drowsy_count >= 15:
            cv2.putText(frame, "WAKE UP!", (50, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

        cv2.putText(frame, f"Status: {status}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 0, 255) if status == "DROWSY!" else (0, 255, 0), 2)

        cv2.imshow("Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # show carla view in pygame
        if latest_frame[0] is not None:
            surface = pygame.surfarray.make_surface(latest_frame[0].swapaxes(0, 1))
            display.blit(surface, (0, 0))
            if drowsy_count >= 15:
                alert = font.render("DROWSINESS ALERT!", True, (255, 0, 0))
                display.blit(alert, (20, 20))
            pygame.display.flip()

        time.sleep(0.03)

except KeyboardInterrupt:
    pass

finally:
    cap.release()
    cv2.destroyAllWindows()
    camera.stop()
    vehicle.destroy()
    pygame.quit()
    print("Stopped.")
