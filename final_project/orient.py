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
    if dist < 2:
        angle = 30 * dist
 
    elif dist < 9:
        angle = 30 * dist + 5

 
    else:
        angle = 30 * dist + 10

    return angle

def orient_long():
    distance = orient()

    dist = np.argmax(distance[:])
    
    angle = find_angle(dist)
    bot.turn_degrees(angle)

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

    
