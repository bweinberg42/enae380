#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:29:41 2018

@author: charlie
"""

import easygopigo3 as easy
import lights


pig = easy.EasyGoPiGo3()
d_sensor = pig.init_distance_sensor()
servo = pig.init_servo() #Check this init

left=True

if left:
    #If the first move is to turn left we are in the position S1:
    
    #Orient yourself - somehow. Assuming starting after the turn left facing the first opening
    #Drive forward 10 inches
    pig.drive_inches(10,blocking=True)
    #Turn left 90 degrees
    pig.orbit(-90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #Turn left 90 degrees
    pig.orbit(-90,0,blocking=True)
    #Drive forward 10 inches
    pig.drive_inches(10,blocking=True)
    #Turn right 90 degrees
    pig.orbit(90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #TUrn right 90 degrees
    pig.orbit(90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #Turn left 90 degrees
    pig.orbit(-90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #Turn right 90 degrees
    pig.orbit(90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #Turn left 90 degrees
    pig.orbit(-90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(12,blocking=True)
    #We out the fucking maze bitches
    
	for _ in range(3):
    	lights.blink('green')

else:
    
    #Drive forward 10 inches
    pig.drive_inches(10,blocking=True)
    #Turn right 90 degrees
    pig.orbit(90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #Turn left 90 degrees
    pig.orbit(-90,0,blocking=True)
    #Drive forward 10 inches
    pig.drive_inches(10,blocking=True)
    #Turn left 90 degrees
    pig.orbit(-90,0,blocking=True)
    #Drive forward 25 inches
    pig.drive_inches(25,blocking=True)
    #TUrn left 90 degrees
    pig.orbit(-90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #Turn right 90 degrees
    pig.orbit(90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #Turn left 90 degrees
    pig.orbit(90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(8,blocking=True)
    #Turn right 90 degrees
    pig.orbit(90,0,blocking=True)
    #Drive forward 8 inches
    pig.drive_inches(12,blocking=True)
    #We out the fucking maze bitches
    #Blaire's edits
<<<<<<< Updated upstream
 
	for _ in range(3):
    	lights.blink('green')
=======
    
    lights.blink('green')
    lights.blink('green')
    lights.blink('green')
    
>>>>>>> Stashed changes
