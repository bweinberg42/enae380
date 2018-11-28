import easygopigo3 as easy
import numpy as np

bot = easy.EasyGoPiGo3()
d_sensor = pig.init_distance_sensor()

distance = np.zeros([2, 6])
distance[0, :] = np.linspace(0, 360, 6)

for i in range(6):
	distance[1, i] = d_sensor.read_mm()
	bot.orbit(distance[0, i])

dist = np.argmin(distance[1, :])
angle = distance[1, dist]

bot.orbit(angle)

