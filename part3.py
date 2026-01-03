from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

tello.streamon()
tello.takeoff()

reader = tello.get_frame_read()
while True:
    frame = reader.frame
    if frame is not None and frame.mean() > 10:
        break

cv2.imwrite("tello_photo.jpg", frame)

tello.land()
tello.streamoff()