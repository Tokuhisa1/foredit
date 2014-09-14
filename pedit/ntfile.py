# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 22:40:43 2014

@author: wyh
"""
import os
a=raw_input("title:")
b=raw_input("content:")
def st_one():
  #print a
  #print b
  tif= os.path.exists('%s.txt'%a)
  # True
  if tif:
      pass
  else:
      os.mknod("%s.txt"%a)
  read = open("%s.txt"%a,'w+')
  
      
def main():
  st_one()
if __name__=="__main__": 
    main()
