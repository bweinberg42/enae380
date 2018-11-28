"""
Script to handle LED for bot
Can blink and wink
"""

import time
import easygopigo3 as easy

bot = easy.EasyGoPiGo3()


def blink(color):
	color = get_color(color)
	bot.set_eye_color(color)
	bot.open_eyes()
	time.sleep(0.5)
	bot.close_eyes()


def wink(color, left):
	color = get_color(color)

	if left:
		bot.set_eye_color(color)
		bot.open_left_eye()
		time.sleep(0.5)
		bot.close_left_eye()
	
	else:
		bot.set_eye_color(color)
		bot.open_right_eye()
		time.sleep(0.5)
		bot.close_right_eye()

def get_color(color):
	if color == 'white':
		return (255, 255, 255)

        elif color == 'red':
		return (255, 0, 0)

        elif color == 'blue':
		return (0, 0, 255)

        elif color == 'green':
		return (0, 128, 0)
