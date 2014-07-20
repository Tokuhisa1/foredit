# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 23:39:52 2014

@author: wyh
"""

# client

import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

data = s.recv(512)
print 'the data received is',data

s.close()
