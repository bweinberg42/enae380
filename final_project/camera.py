from picamera import PiCamera
from time import sleep

camera = PiCamera()

sleep(5)
camera.capture('/home/pi/Desktop/enae380/final_project/image.png', format='png')
camera.close()
