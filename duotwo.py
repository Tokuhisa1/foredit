# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 00:17:21 2014

@author: wyh
"""

import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print "I was listening music %s,%s"%(func,ctime())
        sleep(1)
        
def movie(func):
    for i in range(3):
        print "I was listening movie %s,%s"%(func,ctime())
        sleep(5)
        
threads=[]
t1=threading.Thread(target=music, args=(u'maimaiaiqing',))
threads.append(t1)
t2=threading.Thread(target=movie,args=(u'moshu',))
threads.append(t2)

if __name__=='__main__':
 for t in threads:
    t.setDaemon(True)
    t.start()
    
print "all over %s"%ctime() 
        