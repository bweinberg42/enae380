from picamera import PiCamera
from time import sleep
import cv2
import numpy as np

camera = PiCamera()

def check_cam():

	sleep(6)
	camera.capture('image.png')
	camera.close()

for i in circles[0,:]:
	# draw the outer circle
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	# draw the center of the circle
	cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

print(circles)
cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
