"""
Created on Mon Nov 26 15:29:41 2018

@author: charlie
"""

import easygopigo3 as easy
import lights
import orient

pig = easy.EasyGoPiGo3()
d_sensor = pig.init_distance_sensor()

def main():
	orient.orient_long()
	pig.drive_inches(-12,blocking=True)
	left = orient.orient_path()
	maize(left)
	end()

def maize(left):
	if left:
		drive(-13, -90)
		drive(-12, 90)
		drive(-12, -80)
		drive(-13, -80)
		drive(-11, 90)
		drive(-11, -90)
		drive(-20, 0)
    	
	else:
		drive(-10, -93)
		drive(-36, -90)
		drive(-12, 90)
		drive(-12, -90)
		drive(-13, 90)
		drive(-20, 0)

def end():
    for _ in range(3):
    	lights.blink('green')

def drive(dist, angle):
    pig.drive_inches(dist,blocking=True)
    pig.turn_degrees(angle)

if __name__ == "__main__":
	main()
