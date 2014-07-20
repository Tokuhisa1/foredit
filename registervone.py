# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 20:56:11 2014

@author: wyh
"""

import sys,string,sqlite3
from Tkinter import *
root = Tk()
def one_register():
    uget_name=o_entry.get()
    uget_passwd=t_entry.get()
    conn=sqlite3.connect("usrnp.db")
    conn.cursor()
    conn.execute("insert into usrnp values ('%s','%s');"%(uget_name, uget_passwd))
    conn.commit()
    print "end" 
t_fun= Label(root, text="register")
t_fun.pack()
o_name= Label(root, text="name")
o_name.pack()
o_entry = Entry(root)
o_entry.pack()
t_name= Label(root, text="passwd")
t_name.pack()
t_entry = Entry(root)
t_entry.pack()
b = Button(root, text="register", command=one_register)
b.pack()
root.mainloop()