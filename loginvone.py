# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 18:44:47 2014

@author: wyh
"""
import sys,string,sqlite3
from Tkinter import *
root = Tk()
def one_login():
    uget_name=o_entry.get()
    uget_passwd=t_entry.get()
    conn=sqlite3.connect("usrnp.db")
    conn.cursor()
    usr_name=conn.execute("select name from usrnp;")
    for eye in usr_name:
     eye= eye[0].encode('unicode_escape').decode('string_escape')     
     #print eye
     if uget_name==eye:
         #print "exist"
         password=conn.execute("select passwd from  usrnp  where name='%s';"%eye)
         password=password.fetchall()
         password=password[0][0].encode('unicode_escape').decode('string_escape')
         if uget_passwd==password:
             print "ok"
         else:
             print "wrong password"
         break
    else:
         print "no this user"
o_fun= Label(root, text="login")
o_fun.pack()
o_name= Label(root, text="name")
o_name.pack()
o_entry = Entry(root)
o_entry.pack()
t_name= Label(root, text="passwd")
t_name.pack()
t_entry = Entry(root)
t_entry.pack()
a = Button(root, text="login", command=one_login)
a.pack()
root.mainloop()