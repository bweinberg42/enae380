import easygopigo3 as easy
import numpy as np

bot = easy.EasyGoPiGo3()
d_sensor = bot.init_distance_sensor()
    
def orient_long():

    distance = np.zeros(6)

    for i in range(6):
	    distance[i] = d_sensor.read_mm()
            bot.turn_degrees(60)

    dist = np.argmax(distance[:])
    angle = 60 * dist

    bot.turn_degrees(angle)

    pass

def orient_short():

    distance = np.zeros(6)

    for i in range(6):
	    distance[i] = d_sensor.read_mm()
            bot.turn_degrees(60)

    dist = np.argmin(distance[:])
    angle = 60 * dist

    bot.turn_degrees(angle)

    pass

def orient_path():
    
    bot.turn_degrees(90)
    if d_sensor.read_mm < 50.8:
        bot.turn_degrees(180)
        left=True
    
    return left

    