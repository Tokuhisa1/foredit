# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 15:25:55 2014

@author: wyh
"""

import string, os, sys
import StringIO

def writedata(fd, msg):
    fd.write(msg)
    
f = open('aaa.txt', 'w')

writedata(f, "123")

writedata(f, "456")
f.close()