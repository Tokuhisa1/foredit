# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 23:39:30 2014

@author: wyh
"""

# server

import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()
s.bind(address)
s.listen(5)

ss, addr = s.accept()
print 'got connected from',addr

ss.send('byebye')


ss.close()
s.close()
