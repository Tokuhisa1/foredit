import os
import sys
os.mknod("test1.txt")
file=open('test1.txt','w')
file.write("hellow world")
file.close()