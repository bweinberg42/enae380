#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:29:41 2018

@author: charlie
"""

import easygopigo3 as easy
import lights
import orient


pig = easy.EasyGoPiGo3()
d_sensor = pig.init_distance_sensor()

#orient.orient_long()
pig.drive_inches(-12,blocking=True)
left = orient.orient_path()

if left:
    #If the first move is to turn left we are in the position S1:
    
    #Orient yourself - somehow. Assuming starting after the turn left facing the first opening
    #Drive forward 10 inches
    pig.drive_inches(-13,blocking=True)
    #Turn left 90 degrees
    pig.turn_degrees(-90)
    #Drive forward 8 inches
    pig.drive_inches(-12,blocking=True)
    #Turn left 90 degrees
    pig.turn_degrees(90)
    #Drive forward 10 inches
    pig.drive_inches(-12,blocking=True)
    #Turn right 90 degrees
    pig.turn_degrees(80)
    #Drive forward 8 inches
    pig.drive_inches(-13,blocking=True)
    #TUrn right 90 degrees
    pig.turn_degrees(-80)
    #Drive forward 8 inches
    pig.drive_inches(-11,blocking=True)
    #Turn left 90 degrees
    pig.turn_degrees(90)
    #Drive forward 8 inches
    pig.drive_inches(-11,blocking=True)
    #Turn right 90 degrees
    pig.turn_degrees(-90)
    #Drive forward 8 inches
    pig.drive_inches(-20,blocking=True)
    #We out the fucking maze bitches
    
    for _ in range(3):
    	lights.blink('green')

else:
    
    #Drive forward 10 inches
    pig.drive_inches(-24,blocking=True)
    #Turn right 90 degrees
    pig.turn_degrees(-90)
    #Drive forward 8 inches
    pig.drive_inches(-10,blocking=True)
    #Turn left 90 degrees
    pig.turn_degrees(-93)
    #Drive forward 10 inches
    pig.drive_inches(-36,blocking=True)
    #Turn left 90 degrees
    pig.turn_degrees(-90)
    #Drive forward 25 inches
    pig.drive_inches(-12,blocking=True)
    #TUrn left 90 degrees
    pig.turn_degrees(90)
    #Drive forward 8 inches
    pig.drive_inches(-12,blocking=True)
    #Turn right 90 degrees
    pig.turn_degrees(-90)
    #Drive forward 8 inches
    pig.drive_inches(-12,blocking=True)
    #Turn left 90 degrees
    pig.turn_degrees(90)
    #Drive forward 8 inches
    pig.drive_inches(-20,blocking=True)
    #We out the fucking maze bitches

    for _ in range(3):
    	lights.blink('green')
