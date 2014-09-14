# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 18:34:42 2014

@author: wyh
"""
#定义类
class Athlete:
    def _init_(self,word):
        print "I want say:"+word
    def hello (self,name):
        print "hello"+name
#实例化
a=Athlete()
#执行
a._init_("I Love You")
a.hello("wang")
        
