from djitellopy import Tello

tello=Tello()
tello.connect()

#tello.takeoff()
#
#move
#tello.move_up(100)
#tello.move_forward(50)
#tello.rotate_clockwise(90)

#tello.move_back(50)
#tello.move_up(50)
#
#tello.land()

import cv2

panel=cv2.imread('./DroneBlocks_TT.jpg')
cv2.imshow('tello panel', panel)
while True:
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('t'):
        tello.takeoff()
    elif key==ord('l'):
        tello.land()
    elif key==ord('u'):
        tello.move('up', 50)
    elif key==ord('d'):
        tello.move('down', 50)
    elif key==ord('f'):
        tello.move('forward', 50)
    elif key==ord('b'):
        tello.move('back', 50)
    elif key==ord('c'):
        tello.rotate_clockwise(90)
    elif key==ord('w'):
        tello.rotate_counter_clockwise(90)

    

pass