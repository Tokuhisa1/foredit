# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 16:27:31 2014

@author: wyh
"""

import pygame.mixer
sounds=pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

s=sounds.Sound("1.mp3")
wait_finish(s.play())
