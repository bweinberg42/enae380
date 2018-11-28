import easygopigo3 as easy
import cv2
import numpy as np
import picamera as cam
import lights as l

bot = easy.EasyGoPiGo3()
servo = bot.init_servo()
camera = PiCamera()

index = 3;
left = False

def main():
	take_image()
	circles = find_circles()
	left, index = next_move(circles, index)
	move(left)
	
def take_image():
	#https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/6
	camera.start_preview()
	sleep(5)
	camera.capture('/home/pi/Desktop/enae380/final_project/image.png')
	camera.stop_preview()

	pass

def find_circles():
	#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html
	img = cv2.imread('image.png', 0)
	img = cv2.medianBlur(img, 5)

	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

	return circles[0, -1]

def next_move(circles, index):
	if circles == 1:
		left = True
		index -= index

	elif circles == 2:
		left = False
		index += index
	
	else:
		left = False
		index * l.blink(red)

	return left, index

def move(left):
	l.wink(white, left)

	if left:
		bot.orbit(90)
		bot.drive_inches(14)
		bot.orbit(-90)

	else:
		bot.orbit(-90)
		bot.drive_inches(14)
		bot.orbit(90)

	pass

if __name__ == "__main__":
	main()