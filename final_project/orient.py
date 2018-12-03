import easygopigo3 as easy
from time import sleep
import numpy as np

bot = easy.EasyGoPiGo3()
d_sensor = bot.init_distance_sensor()

def orient():
	distance = np.zeros(12)

	for i in range(12):
		sleep(0.5)
		distance[i] = d_sensor.read_mm()
		bot.turn_degrees(30)

	return distance

def find_angle(dist):
    angle = 32 * dist

    return angle

def orient_long():
	distance = orient()

	dist = np.argmax(distance[:]) + 1

	angle = find_angle(dist)
	bot.turn_degrees(angle)


	distance = d_sensor.read_mm()
        print(distance)

        if distance < 80:
	    bot.turn_degrees(-90)

        if distance > 340:
                bot.turn_degrees(-15)

	pass

def orient_short():
	distance = orient()

	dist = np.argmin(distance[:])

	angle = find_angle(dist)
	bot.turn_degrees(angle)

	pass

def orient_path():
	left = True 

	bot.turn_degrees(-90)
	dist = d_sensor.read_mm()

	if dist < 100:
		bot.turn_degrees(180)
		left = False

	return left


