# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 13:16:48 2014

@author: wyh
"""

print "you enter a dark room with two doors.Do you go through door #1 or #2?"
door=raw_input(">")

if door=="1":
    print "There is a bear here eating a cake. What do you do?"
    print "1,take the cake"
    print "2,scream at the bear"
    
    bear=raw_input(">")
    
    if bear=="1":
        print "the bear eats your face off,good job"
    elif bear=="2":
        print "the bear eats your logs off,good job"
    else:
        print "well,doing %s is probably better.bear runs away"%bear
        
elif door=="2":
    print "you stare into the endless abyss"
    print "1,blueberries"
    print "2,yellow jacket"
    print "3,understand revolvers"
    
    insanity=raw_input(">")
    
    if insanity=="1"or insanity=="2":
        print "you survives"
    else:
        print "the yellow mod"
else:
    print "you die"