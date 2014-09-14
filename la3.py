# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 23:48:15 2014

@author: wyh
"""


import os
def make_new_file(a):
    os.mknod("%s.txt"%a)
    print "ok"

b=raw_input()
make_new_file(a)