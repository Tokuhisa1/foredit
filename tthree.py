# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 11:38:30 2014

@author: wyh
"""

import Tkinter
from Tkinter import *
root=Tk()

widget=Label(root)
widget.config(text='myfirst')
widget.pack(side=TOP,expand=YES,fill=BOTH)
root.mainloop()