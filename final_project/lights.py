"""
Script to handle LED for bot
Can blink and wink
"""

import time
import easygopigo3 as easy

bot = easy.EasyGoPiGo3()


def blink(color):
	bot.set_eye_color(color)
	bot.open_eyes()
	time.sleep(0.5)
	bot.close_eyes()


def wink(color, left):
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


