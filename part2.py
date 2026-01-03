from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff()

side_length = 100
angle = 120

for _ in range(3):
    tello.move_forward(side_length)
    tello.rotate_clockwise(angle)

tello.land()