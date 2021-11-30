from djitellopy import Tello

tello=Tello()
tello.connect()

tello.streamon()
frame_read=tello.get_frame_read()

import cv2
while True:
    cv2.imshow('tello stream', frame_read.frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    
tello.streamoff()

pass