# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 12:37:56 2014

@author: wyh
"""

from Tkinter import *

master = Tk()

def callback():
    print "click!"

b = Button(master, text="login", command=callback)
b.pack()

mainloop()