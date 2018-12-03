import easygopigo3 as easy
import orient 

bot = easy.EasyGoPiGo3()
d_sensor = bot.init_distance_sensor()

def center():
    dist = d_sensor.read_inches()
    bot.drive_inches(35.5 - dist)

    bot.turn_degrees(90)

    pass

def centering():
    orient.orient_short()

    for _ in range(2):
        center()

centering()
