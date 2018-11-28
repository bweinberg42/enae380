import easygopigo3 as easy
import numpy as np

def orient():
    bot = easy.EasyGoPiGo3()
    d_sensor = bot.init_distance_sensor()

    distance = np.zeros(6)

    for i in range(6):
	    distance[i] = d_sensor.read_mm()
            bot.turn_degrees(60)

    dist = np.argmin(distance[:])
    angle = 60 * dist

    bot.turn_degrees(angle)

    pass

