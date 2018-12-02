from picamera import PiCamera
from time import sleep
import cv2
import numpy as np

camera = PiCamera()

def check_cam():

	sleep(6)
	camera.capture('image_1.png')
	camera.close()

img = cv2.imread('image_4.png',0)
img = cv2.medianBlur(img,5)

circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 100, param1=50, param2=50, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
 
print(len(circles[0, :, 1]))
for i in circles[0,:]:
	# draw the outer circle
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	# draw the center of the circle
	cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


