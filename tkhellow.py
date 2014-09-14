# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 11:56:52 2014

@author: wyh
"""

from Tkinter import *

root = Tk()
def callone():
    print e.get()
def calltwo():
    print f.get()
w = Label(root, text="please login")
w.pack()
e = Entry(root)
e.pack()
f= Entry(root)
f.pack()

a = Button(root, text="one", command=callone)
a.pack()
b = Button(root, text="two", command=calltwo)
b.pack()


root.mainloop()