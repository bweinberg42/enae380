#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:29:41 2018

@author: charlie
"""

import easygopigo3 as easy
import time

pig=easy.EasyGoPiGo3
d_sensor = pig.init_distance_sensor()
servo = pig.init_servo() #Check this init

if left==True:
    #If the first move is to turn left we are in the position S1:
    
#Orient yourself - somehow. Assuming starting after the turn left facing the first opening
    pig.drive_inches(10,blocking=True)
    pig.orbit(-90,0,blocking=True)
    pig.drive_inches(8,blocking=True)
    pig.orbit(90,0,blocking=True)
    



else: