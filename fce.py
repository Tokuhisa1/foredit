# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 21:24:44 2014

@author: wyh
"""

import socket
port=8081
host='localhost'
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b'hello,this is a test info !',(host,port))