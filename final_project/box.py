import easygopigo3 as easy
import orient 

bot = easy.EasyGoPiGo3()
d_sensor = bot.init_distance_sensor()

orient.orient_short()

def center():
    dist = d_sensor.read_inches()
    bot.drive_inches(36 - dist)

    bot.drive_degrees(90)

    pass

for _ in range(6):
    center()
