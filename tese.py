# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 22:49:21 2014

@author: wyh
"""

import socket
from time import ctime
import sys

bufsize = 1024

host = '127.0.0.1'
port = 8100
address = (host,port)

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen(1)