from picamera import PiCamera
from time import sleep

camera = PiCamera()

sleep(6)
camera.capture('image.png')
camera.close()
