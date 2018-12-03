import easygopigo3 as easy
from time import sleep
import cv2
import numpy as np
import picamera as cam
import lights as l

bot = easy.EasyGoPiGo3()
servo = bot.init_servo()
camera = cam.PiCamera()


def main(index):
    take_image()
    circles = find_circles()
    
    print('main index', index)
    if circles > 2:
        for _ in range(index):
        	l.blink('red')
	for _ in range(circles):
		l.blink('blue')

    else:
        left, index = next_move(circles, index)
        move(left)
        main(index)
    

def take_image():
	sleep(5)
	camera.capture('image.png')

	pass

def find_circles():
    img = cv2.imread('image.png',0)
    img = cv2.medianBlur(img,5)

    circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 100, param1=50, param2=50, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))

    print(len(circles[0, :, 1]))
    return len(circles[0, :, 1])

def next_move(circles, index):
	if circles == 1:
		left = True
		index = index - 1

	elif circles == 2:
		left = False
		index = index + 1
	
	else:
		left = False
                for _ in range(index):
		    l.blink(red)

        print(left)
        print('loop index', index)
	return left, index

def move(left):
	l.wink('white', left)

	if left:
		bot.turn_degrees(90)
		bot.drive_inches(14.75)
		bot.turn_degrees(-90)
                bot.drive_inches(-1)

	else:
		bot.turn_degrees(-90)
		bot.drive_inches(14.75)
		bot.turn_degrees(90)
                bot.drive_inches(-1)

	pass

if __name__ == "__main__":
        index = 3;
	main(index)
