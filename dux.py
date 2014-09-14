# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 22:38:07 2014

@author: wyh
"""

from time import ctime,sleep

def music():
  for i in range(2):
      print "I am playing music,%s"%ctime()
      sleep(1)

def movie():
    for i in range(3):
        print "I am watch movie,%s"%ctime()
        sleep(5)
        
if __name__ == '__main__':
    movie()
    music()
    print "all over %s"%ctime()

    
      