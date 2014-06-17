# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 19:17:17 2014

@author: wyh
"""

def make_new_file(a):
    a=raw_input()
    os.mknod("%s.txt",a)
    print "ok"

make_new_file()
    