# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 18:52:02 2014

@author: wyh
"""

import os
from Tkinter import *
root = Tk()
root.title('ppedit')
def one_save():
    tit=o_entry.get()
    con=t_entry.get("1.0",END)
    os.mknod("%s.txt"%tit)
    fp = open("%s.txt"%tit,'w') 
    fp.writelines(con)
    fp.close()
o_title= Label(root, text="title")
o_title.pack()
o_entry = Entry(root)
o_entry.pack()
t_content= Label(root, text="content")
t_content.pack()
var = StringVar()
t_entry =Text(root,height=40,width=30)
t_entry.pack()
a = Button(root, text="save",width=10,height=1,command=one_save)
a.pack()

root.mainloop()