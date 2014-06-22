# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 16:40:19 2014

@author: wyh
"""

import pygame

pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()