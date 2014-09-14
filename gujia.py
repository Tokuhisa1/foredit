# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 18:04:37 2014

@author: wyh
"""

import pygame.mixer
from time import sleep
pygame.mixer.init()
track = pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()