# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 16:55:18 2014

@author: wyh
"""

import pygame,sys
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([640,480])
pygame.time.delay(1000)
pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()