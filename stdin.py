# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 00:00:00 2014

@author: wyh
"""
#cho "hellow world"|python stdin.py
import sys
for one in sys.stdin:
    a=one.split()
    for b in range(len(a)):
     print a[b]