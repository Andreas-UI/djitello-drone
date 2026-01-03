from djitellopy import Tello
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

tello = Tello()
tello.connect()

tello.streamon()
tello.takeoff()

frame_read = tello.get_frame_read()

found_face = False
direction = "left"

while not found_face:
    frame = frame_read.frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5
    )

    if len(faces) > 0:
        print("Face detected!")
        found_face = True
        cv2.imwrite("face_detected.jpg", frame)
        break

    if direction == "left":
        tello.move_left(30)
        direction = "right"
    else:
        tello.move_right(30)
        direction = "left"

tello.land()
tello.streamoff()
